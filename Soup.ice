module Soup
{
    sequence<byte> songdatas;
    
    struct Song{
        int id;
        string title;
        string author;
        string extension;
    }

    sequence<Song> Songs;

    interface MusicLibrary
    {
        void addSong(string title, string author, string extension, songdatas data);
        void removeSong(Song song);
        void updateSong(Song song, songdatas data);
        Songs searchByTitle(string title);
        Songs searchByAuthor(string author);
    }
}