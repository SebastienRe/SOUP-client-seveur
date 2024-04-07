function envoyerMp3() {
  const titre = $("#inputTitre")[0].value;
  const auteur = $("#inputAuteur")[0].value;
  const type = $("#inputType")[0].value;
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
  const extension = file.name.split(".")[1];
  const reader = new FileReader();
  reader.onload = async function (event) {
    const data = new Uint8Array(event.target.result);
    try {
      //recuperer l'index du serveur qui a le même type que le name
      let index = -1;
      for (let i = 0; i < serveurs.length; i++) {
        if (serveurs[i].name === type) {
          index = i;
          break;
        }
      }
      if (index === -1) {
        error("Type de serveur inconnu");
        return;
      }
      console.log(titre, auteur, type, extension, index, data);
      console.log(players[index]);
      players[index].addSong(titre, auteur, extension, data);
    } catch (e) {
      error(e, "Ajout de mp3 échoué");
    }
  };
  reader.readAsArrayBuffer(file);
}
