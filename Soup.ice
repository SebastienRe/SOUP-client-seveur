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
        int addSong(string title, string author, string extension); // returns the id of the song
        void addSongData(Song song, songdatas data, bool finish); // returns the id of the song
        void updateSong(Song song, bool reset);
        void removeSong(Song song);
        Songs searchWithText(string text);

        int playSong(Song song); //returns the port number
        void stopSong(int port); //stops the song playing on the port
        void playPauseSong(int port); //pauses or play the song playing on the port 
    }
}