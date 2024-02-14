module Soup
{
    struct Song {
        string title;
        string author;
        sequence<byte> data;
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
