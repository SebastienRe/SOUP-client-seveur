function envoyerMp3(event) {
  event.preventDefault();
  const titre = $("#inputTitre")[0].value;
  const auteur = $("#inputAuteur")[0].value;
  const type = $("#inputType")[0].value;
  const inputFile = $("#inputMp3")[0];

  if (!titre || !auteur) {
    error("Veuillez remplir tous les champs");
    return;
  }
  if (titre.includes("-") || auteur.includes("-")) {
    error("Les champs ne peuvent pas contenir le caractère '-'");
    return;
  }

  const file = inputFile.files[0];

  if (!file) {
    error("Veuillez sélectionner un fichier");
    return;
  }
  const extension = file.name.split(".")[1];
  const reader = new FileReader();
  reader.onload = async function (event) {
    const data = new Uint8Array(event.target.result);
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

    try {
      players[index].addSong(titre, auteur, extension).then((response) => {
        event.preventDefault();
        console.log("response", response);
      });
    } catch (error) {
      console.error("Error calling addSong:", error);
    }
  };
  reader.readAsArrayBuffer(file);
}
