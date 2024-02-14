module Soup
{
    sequence<byte> songdatas;
    
    struct Song{
        string title;
        string author;
        string extension;
        songdatas songData;
    }

    interface MusicLibrary
    {
        void addSong(Song song);
        void removeSong(string title);
        void updateSong(string title, Song newSong);
        Song searchByTitle(string title);
        Song searchByAuthor(string author);
    }
}