/*
  //string title, string author, string extension, songdatas data
  const data = Uint8Array.from([1, 2, 3, 4, 5]);
  await musicLibrary.addSong("titre", "Author", "mp3", data);
*/

/**
 * Sets up the ICE communication and executes the provided function.
 * @param {Function} fonction_a_executer - The function to execute.
 * @param {...any} args - The arguments to pass to the function.
 */
async function IceExecute(fonction_a_executer, ...args) {
  try {
    let communicator = Ice.initialize(process.argv);
    const base = communicator.stringToProxy("MusicLibrary:ws -p 10000");
    const player = await Soup.MusicLibraryPrx.checkedCast(base);
    if (!player) {
      throw new Error("Invalid proxy");
    }
    fonction_a_executer(player, ...args);
  } catch (ex) {
    console.error(ex.toString());
    process.exitCode = 1;
  } finally {
    if (communicator) {
      await communicator.destroy();
    }
  }
}
