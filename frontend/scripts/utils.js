function error(e, ...str) {
  console.error(e);
  $("#notifContent").html("<h1>Error</h1><p>" + e + "</p><p>" + str + "</p>");
  $("#notif").removeClass("w3-hide");
}

function info(str) {
  console.log(str);
  $("#notifContent").html("<h1>Info</h1><p>" + str + "</p>");
  $("#notif").removeClass("w3-hide");
}

function disable_error() {
  $("#notif").addClass("w3-hide");
}

function afficherInfos() {
  if ($("#infos").hasClass("w3-hide")) $("#infos").removeClass("w3-hide");
  else $("#infos").addClass("w3-hide");
}
