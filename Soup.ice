module Soup
{
    sequence<byte> songdatas;
    
    struct Song{
        int id;
        string title;
        string author;
        string extension;
        float accuracy;
    }

    sequence<Song> Songs;

    interface MusicLibrary
    {
        void addSong(string title, string author, string extension, songdatas data);
        void removeSong(Song song);
        void updateSong(Song song, songdatas data);
        Songs searchWithText(string text);

        int playSong(Song song); //returns the port number
        void stopSong(int port); //stops the song playing on the port
        void playPauseSong(int port); //pauses or play the song playing on the port 
    }
}