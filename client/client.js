const Ice = require('ice').Ice;
const Soup = require('./Soup').Soup;

async function main() {
    let communicator;
    try {
        communicator = Ice.initialize(process.argv);
        const base = communicator.stringToProxy('MusicLibrary:default -p 10000');
        const musicLibrary = await Soup.MusicLibraryPrx.checkedCast(base);
        if (!musicLibrary) {
            throw new Error('Invalid proxy');
        }

        // Utilisez musicLibrary pour appeler les méthodes sur le serveur
        const songs = await musicLibrary.searchByTitle('Zeus');
        console.log(songs);
    } catch (ex) {
        console.error(ex.toString());
        process.exitCode = 1;
    } finally {
        if (communicator) {
            await communicator.destroy();
        }
    }
}

main();