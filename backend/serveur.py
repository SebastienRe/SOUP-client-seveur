import Ice
import Soup
from Soup import Song
import os

class SongFiles():
    def __init__(self):
        nom_dossier = "musiques"
        self.dossier_musiques = os.path.join(os.path.dirname(__file__), nom_dossier)
    
    def get_new_id(self) -> int:
        """
        Renvoie un id unique pour une musique
        """
        fichiers = os.listdir(self.dossier_musiques)
        return len(fichiers) + 1
    
    def ajouterMusique(self, song: Song, data: bytearray):
        """
        Ajoute une musique dans le dossier musiques
        """
        # création du fichier
        with open(f"{self.dossier_musiques}/{song.id}-{song.titre}-{song.auteur}.{song.extension}", "wb") as f:
            f.write(data)
    
    def ajouterMusique(self, title : str, author : str, extension : str, data: bytearray):
        """
        Ajoute une musique dans le dossier musiques
        """
        # création du fichier
        
        id = self.get_new_id()
        song = Song(id, title, author, extension)
        self.ajouterMusique(song, data)
            
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
    
    def modifierMusique(self, song: Song, data: bytearray):
        """
        Modifie une musique du dossier musiques
        """
        self.supprimerMusique(song.id)
        self.ajouterMusique(song, data)

    def getAlldossier_musiques(self) -> dict[int, Song]:
        """
        Renvoie la liste des musiques sous forme de dictionnaire
        {titre: Song}
        """
        fichiers = os.listdir(self.dossier_musiques) # liste des fichiers dans le dossier
        
        #recuperation des musiques dans le dossier musiques et transformation en objet Song que j'ai défini dans mon ice
        # le nom du fichier ressebmle à "titre-auteur.mp3"
        dict = {}
        for fichier in fichiers:
            id, titre, auteur_and_ext = fichier.split("-")
            auteur, extension = auteur_and_ext.split(".")
            dict[titre] = Song(int(id), titre, auteur, extension)
            
        return dict         
    

class MusicLibraryI(Soup.MusicLibrary):
    def __init__(self):
        self.songfiles = SongFiles()
        
    def addSong(self, title : str, author : str, extension : str, data: bytearray, current=None):
        print("Ajout de la musique")
        self.songfiles.ajouterMusique(title, author, extension, data)
        
    def removeSong(self, song : Song, current=None):
        print("Suppression de la musique")
        self.songfiles.supprimerMusique(song)

    def updateSong(self, song : Soup, data: bytearray, current=None):
        print("Modification de la musique")
        self.songfiles.modifierMusique(song, data)

    def searchByTitle(self, title, current=None)->list[Song]:
        print("Recherche par titre")
        songs = self.songfiles.getAlldossier_musiques()
        print(songs)
        return [song for song in songs.values() if song.title == title]

    def searchByAuthor(self, author, current=None)->list[Song]:
        print("Recherche par auteur")
        songs = self.songfiles.getAlldossier_musiques()
        print(songs)
        return [song for song in songs.values() if song.author == author]

with Ice.initialize() as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("MusicLibraryAdapter", "ws -p 10000") # Création de l'adaptateur qui sert à communiquer avec le client
    object = MusicLibraryI() # Création de l'objet servant
    adapter.add(object, communicator.stringToIdentity("MusicLibrary")) # Ajout de l'objet servant à l'adaptateur
    adapter.activate() # Activation de l'adaptateur
    communicator.waitForShutdown() # Attente de la fin du programme