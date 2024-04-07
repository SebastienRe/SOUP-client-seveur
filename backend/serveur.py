import socket
import Ice
import Soup as Soup
from Soup import Song
import os
import argparse
import vlc

# Créer un parseur d'arguments
parser = argparse.ArgumentParser(description="Lance le serveur avec un numéro de port spécifique et un sous-dossier spécifique dans 'dossier_musiques'.")

# Ajouter les arguments
parser.add_argument('port', type=int, help='Le numéro du port du serveur')
parser.add_argument('sous_dossier', type=str, help="Le sous-dossier dans 'dossier_musiques' qui correspond au type de musique")

# Analyser les arguments
args = parser.parse_args()

# Utiliser les arguments
port = args.port
sous_dossier = args.sous_dossier

class SongFiles():
    def __init__(self):
        self.dossier_musiques = os.path.join(os.path.dirname(__file__), "musiques", sous_dossier)
        self.file_data = {}
    
    def get_new_id(self) -> int:
        """
        Renvoie un id unique pour une musique
        """
        fichiers = os.listdir(self.dossier_musiques)
        return len(fichiers) + 1
    
    def ajouterMusiqueS(self, song: Song):
        """
        Ajoute une musique dans le dossier musiques
        """
        # création du fichier
        with open(f"{self.dossier_musiques}/{song.id}-{song.title}-{song.author}.{song.extension}", "wb") as f:
            f.write(bytearray())
    
    def ajouterMusique(self, title : str, author : str, extension : str):
        """
        Ajoute une musique dans le dossier musiques
        """
        # création du fichier
        
        id = self.get_new_id()
        song = Song(id, title, author, extension, 0)
        self.ajouterMusiqueS(song)
        return song
    
    def editionDonneesMusique(self, id : int, data: bytearray):
        """
        Modifie les données d'une musique
        """
        with open(f"{self.dossier_musiques}/{id}.mp3", "wb") as f:
            f.write(data)
    
    def addDonneesMusique(self, id : int, data: bytearray, finish: bool, resetMusic: bool):
        """
        Ajoute des données à une musique
        """
        if resetMusic:
            self.file_data[id] = bytearray()
        else :
            self.file_data[id] += data
            
        if finish:
            self.editionDonneesMusique(id, self.file_data[id])
            del self.file_data[id]
        
            
    def supprimerMusique(self, song: Song):
        """
        Supprime une musique du dossier musiques
        """
        fichiers = os.listdir(self.dossier_musiques) # liste des fichiers dans le dossier
        for fichier in fichiers:
            id_fichier, titre, auteur_and_ext = fichier.split("-")
            if int(id_fichier) == song.id:
                os.remove(os.path.join(self.dossier_musiques, fichier))
                return
    
    def modifierMusique(self, song: Song, reset: bool):
        """
        Modifie une musique du dossier musiques
        """
        fichiers = os.listdir(self.dossier_musiques)
        for fichier in fichiers:
            id_fichier, titre, auteur_and_ext = fichier.split("-")
            if int(id_fichier) == song.id:
                os.rename(os.path.join(self.dossier_musiques, fichier), os.path.join(self.dossier_musiques, f"{song.id}-{song.titre}-{song.auteur}.{song.extension}"))
                break
            
        if reset:
            self.editionDonneesMusique(song.id, bytearray())

    def getAlldossier_musiques(self) -> list[int, Song]:
        """
        Renvoie la liste des musiques sous forme de dictionnaire
        {titre: Song}
        """
        fichiers = os.listdir(self.dossier_musiques) # liste des fichiers dans le dossier
        
        #recuperation des musiques dans le dossier musiques et transformation en objet Song que j'ai défini dans mon ice
        # le nom du fichier ressebmle à "titre-auteur.extension"
        list = []
        for fichier in fichiers:
            id, titre, auteur_and_ext = fichier.split("-")
            auteur, extension = auteur_and_ext.split(".")
            list.append(Song(int(id), titre, auteur, extension, 0))
            
        return list       
    

class MusicLibraryI(Soup.MusicLibrary):
    def __init__(self):
        self.songfiles = SongFiles()
        self.ports_stream = []
        
    def addSong(self, title : str, author : str, extension : str, current=None):
        print("Ajout de la musique")
        print(title, author, extension)
        return self.songfiles.ajouterMusique(title, author, extension)

    def addSongData(self, song : Song, data: bytearray, finish : bool): #// adds the song data to the song
        print("Ajout des données de la musique")
        self.songfiles.addDonneesMusique(song.id, data, finish, False)

    def updateSong(self, song : Soup, resetMusic:bool, reset:bool, current=None):
        print("Modification de la musique")
        self.songfiles.modifierMusique(song, resetMusic, reset)
        
    def removeSong(self, song : Song, current=None):
        print("Suppression de la musique")
        self.songfiles.supprimerMusique(song)
    
    def searchWithText(self, text, current=None) -> list[Song]:
        print("Recherche par texte")
        songs = self.songfiles.getAlldossier_musiques()
        for song in songs:
            title_match = text in song.title
            author_match = text in song.author
            if title_match or author_match:
                # Calculate the percentage of precision
                title_precision = len(text) / len(song.title)
                author_precision = len(text) / len(song.author)
                song.accuracy = max(title_precision, author_precision)
        print(songs)
        return songs

    def playSong(self, song : Song, current=None):
        def generate_available_port(base = 12345):
            """
            Génère un port disponible
            """
            port = base
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.bind(('', port))
                    s.close()
                    return port
                except OSError:
                    port += 1
                    
        print("Lecture de la musique")
        instance = vlc.Instance() # Créer une instance VLC
        player = instance.media_player_new() # Créer un nouveau lecteur média
        #generer un port qui est disponible
        port = generate_available_port()
        output = 'sout=#transcode{vcodec=none,acodec='+ song.extension +',ab=128,channels=2,samplerate=44100}:http{mux=raw,dst=:' + str(port) + '/}'
        song_name_file = f'{song.id}-{song.title}-{song.author}.{song.extension}'
        media = instance.media_new(f'musiques/${sous_dossier}/${song_name_file}', output)
        player.set_media(media)
        player.play()
        self.ports_stream.append({port : player})
        return port
    
    def stopSong(self, port, current=None):
        print("Arret de la musique")
        if self.ports_stream[port]: # Si le port existe
            self.ports_stream[port].stop() # Arreter la musique
            self.ports_stream[port].release() # Libérer le port
            del self.ports_stream[port] # Supprimer le port
        return
    
    def playPauseSong(self, port, current=None):
        print("Pause de la musique")
        if self.ports_stream[port]:
            if self.ports_stream[port].is_playing():
                self.ports_stream[port].pause()
            else:
                self.ports_stream[port].play()
        return

with Ice.initialize() as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("MusicLibraryAdapter", "ws -p " + str(port)) # Création de l'adaptateur qui sert à communiquer avec le client
    object = MusicLibraryI() # Création de l'objet servant
    adapter.add(object, communicator.stringToIdentity("MusicLibrary")) # Ajout de l'objet servant à l'adaptateur
    adapter.activate() # Activation de l'adaptateur
    communicator.waitForShutdown() # Attente de la fin du programme
    
#\cmd>python serveur.py 10000 rock
#\cmd>python serveur.py 10001 epic