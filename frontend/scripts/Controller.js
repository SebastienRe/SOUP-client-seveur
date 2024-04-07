function envoyerMp3() {
  const titre = $("#inputTitre")[0].value;
  const auteur = $("#inputAuteur")[0].value;
  const inputFile = $("#inputMp3")[0];

  if (!titre || !auteur || !inputFile) {
    error("Veuillez remplir tous les champs");
    return;
  }
  if (titre.includes("-") || auteur.includes("-")) {
    error("Les champs ne peuvent pas contenir le caractère '-'");
    return;
  }

  const file = inputFile.files[0];
  const reader = new FileReader();
  reader.onload = async function (event) {
    const data = new Uint8Array(event.target.result);
    try {
      player.addSong("dqs", "Unknown", "mp3", data);
    } catch (e) {
      error(e, "Ajout de mp3 échoué");
    }
  };
  reader.readAsArrayBuffer(file);
}
