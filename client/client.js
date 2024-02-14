const Ice = require('ice').Ice;
const Soup = require('./Soup').Soup;

(async function() {
    let communicator;
    try {
        communicator = Ice.initialize(process.argv);
        const base = communicator.stringToProxy('MusicLibrary:default -p 10000');
        const musicLibrary = await Soup.MusicLibraryPrx.checkedCast(base);
        if (!musicLibrary) {
            throw new Error('Invalid proxy');
        }

        // Utilisez musicLibrary pour appeler les méthodes sur le serveur
        // Par exemple, pour ajouter une chanson :
        const song = new Soup.Song('Titre', 'Auteur', 'mp3', Ice.ByteSeq.fromArray(Buffer.from('données de la chanson', 'utf-8')));
        await musicLibrary.addSong(song);
    } catch (ex) {
        console.error(ex.toString());
        process.exitCode = 1;
    } finally {
        if (communicator) {
            await communicator.destroy();
        }
    }
}());