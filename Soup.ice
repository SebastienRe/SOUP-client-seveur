module Soup
{
    sequence<byte> songdatas;
    
    struct Song{
        int id;
        string title;
        string author;
        string extension;
        songdatas songData;
    }

    sequence<Song> Songs;

    interface MusicLibrary
    {
        void addSong(Song song);
        void removeSong(Song song);
        void updateSong(Song song);
        Songs searchByTitle(string title);
        Songs searchByAuthor(string author);
    }
}