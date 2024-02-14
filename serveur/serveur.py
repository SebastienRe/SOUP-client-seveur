import Ice
import Soup
from serveur.Soup_ice import Song
import os

class GererFichiersMusiques():
    def __init__(self):
        pass
    
    def ajouterMusique(self, titre, auteur, donnees):
        if os.path.exists(f"musiques/{titre}-{auteur}.mp3"):
            raise Soup.FileAlreadyExists()
        with open(f"musiques/{titre}-{auteur}.mp3", "wb") as f:
            f.write(donnees)
            
    def supprimerMusique(self, titre, auteur):
        if not os.path.exists(f"musiques/{titre}-{auteur}.mp3"):
            raise Soup.FileNotFound()
        os.remove(f"musiques/{titre}-{auteur}.mp3")
        
    def modifierMusique(self, titre, auteur, donnees):
        if not os.path.exists(f"musiques/{titre}-{auteur}.mp3"):
            raise Soup.FileNotFound()
        with open(f"musiques/{titre}-{auteur}.mp3", "wb") as f:
            f.write(donnees)

    def getAllMusiques(self) -> dict[str, Song]:
        """
        Renvoie la liste des musiques sous forme de dictionnaire
        {titre: Song}
        """
        dossier = "musiques"
        fichiers = os.listdir(dossier) # liste des fichiers dans le dossier
        
        #recuperation des musiques dans le dossier musiques et transformation en objet Song que j'ai défini dans mon ice
        # le nom du fichier ressebmle à "titre-auteur.mp3"
        dict = {}
        for fichier in fichiers:
            titre, auteur_and_ext = fichier.split("-")
            auteur, extension = auteur_and_ext.split(".")
            
            # lecture des données binaires du fichier
            donnees = None
            with open(f"{dossier}/{fichier}", "rb") as f:
                donnees = f.read()
            #donnees est de type bytes
            
            dict[titre] = Song(titre, auteur, extension, donnees)
            
        return dict         
    

class MusicLibraryI(Soup.MusicLibrary):
    def __init__(self):
        
    def addSong(self, song : Soup, current=None):
        self.library[song.title] = song

    def removeSong(self, title, current=None):
        if title in self.library:
            del self.library[title]

    def updateSong(self, title, newSong : Soup, current=None):
        if title in self.library:
            self.library[title] = newSong

    def searchByTitle(self, title, current=None):
        return self.library.get(title, None)

    def searchByAuthor(self, author, current=None):
        for song in self.library.values():
            if song.author == author:
                return song
        return None

with Ice.initialize() as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("MusicLibraryAdapter", "default -p 10000") # Création de l'adaptateur qui sert à communiquer avec le client
    object = MusicLibraryI() # Création de l'objet servant
    adapter.add(object, communicator.stringToIdentity("MusicLibrary")) # Ajout de l'objet servant à l'adaptateur
    adapter.activate() # Activation de l'adaptateur
    communicator.waitForShutdown() # Attente de la fin du programme