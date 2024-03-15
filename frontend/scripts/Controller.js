var url = "http://" + window.location.hostname + ":12345/";
var communicator;
var proxy;
var player;

function error(e, ...str) {
  console.log(e);
  $("#notifContent").html("<h1>Error</h1><p>" + e + "</p><p>" + str + "</p>");
  $("#notif").removeClass("w3-hide");
}

function disable_error() {
  $("#notif").addClass("w3-hide");
}

async function initIce() {
  try {
    communicator = Ice.initialize();
    proxy = communicator.stringToProxy(
      "MusicLibrary:ws -p 10000 -h " + window.location.hostname
    );
    player = await Soup.MusicLibraryPrx.checkedCast(proxy);
    console.log("Connexion au serveur réussie");
    console.log(player);
    disable_error();
  } catch (e) {
    error(e, "Connexion au serveur échouée");
    setTimeout(initIce, 5000);
  }
}
initIce();

function envoyerMp3() {
  // <input id="inputMp3" type="file" accept="audio/mp3" multiple="false" />
  const input = document.getElementById("inputMp3");
  const file = input.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (event) {
      const data = new Uint8Array(event.target.result);
      console.log(data);
      console.log(player);
    };
    reader.readAsArrayBuffer(file);
  }
}
