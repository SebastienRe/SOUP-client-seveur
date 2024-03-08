import Ice
import Soup
from Soup import Song
import os

class SongFiles():
    def __init__(self):
        nom_dossier = "musiques"
        self.dossier_musiques = os.path.join(os.path.dirname(__file__), nom_dossier)
    
    def ajouterMusique(self, song: Song):
        """
        Ajoute une musique dans le dossier musiques
        """
        # création du fichier
        with open(f"{self.dossier_musiques}/{song.id}-{song.titre}-{song.auteur}.{song.extension}", "wb") as f:
            f.write(song.donnees)
            
    def supprimerMusique(self, song: Song):
        """
        Supprime une musique du dossier musiques
        """
        fichiers = os.listdir(self.dossier_musiques) # liste des fichiers dans le dossier
        for fichier in fichiers:
            id_fichier, titre, auteur_and_ext = fichier.split("-")
            if int(id_fichier) == song.id:
                os.remove(f"{self.dossier}/{fichier}")
                return
    
    def modifierMusique(self, song: Song):
        """
        Modifie une musique du dossier musiques
        """
        self.supprimerMusique(song.id)
        self.ajouterMusique(song)

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
            
            # lecture des données binaires du fichier
            donnees = None
            with open(f"{self.dossier_musiques}/{fichier}", "rb") as f:
                donnees = f.read()
            #donnees est de type bytes
            
            dict[titre] = Song(int(id), titre, auteur, extension, donnees)
            
        return dict         
    

class MusicLibraryI(Soup.MusicLibrary):
    def __init__(self):
        self.songfiles = SongFiles()
        self.musiques : dict[int, Song] = self.songfiles.getAlldossier_musiques()
        
    def addSong(self, song : Song, current=None):
        self.songfiles.ajouterMusique(song)
        self.musiques[song.id] = song
        
    def removeSong(self, song : Song, current=None):
        self.songfiles.supprimerMusique(song)
        del self.musiques[song.id]

    def updateSong(self, song : Soup, current=None):
        self.songfiles.modifierMusique(song)
        self.musiques[song.id] = song

    def searchByTitle(self, title, current=None)->list[Song]:
        print(self.musiques)
        return [song for song in self.musiques.values() if song.title == title]

    def searchByAuthor(self, author, current=None)->list[Song]:
        return [song for song in self.musiques.values() if song.author == author]

with Ice.initialize() as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("MusicLibraryAdapter", "default -p 10000") # Création de l'adaptateur qui sert à communiquer avec le client
    object = MusicLibraryI() # Création de l'objet servant
    adapter.add(object, communicator.stringToIdentity("MusicLibrary")) # Ajout de l'objet servant à l'adaptateur
    adapter.activate() # Activation de l'adaptateur
    communicator.waitForShutdown() # Attente de la fin du programme