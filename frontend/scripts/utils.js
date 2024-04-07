let errors = [];

function error(e, ...str) {
  errors.push({ error: e, str: str });
  html = "<h1>Error</h1>";
  for (let i = 0; i < errors.length; i++) {
    console.error(errors[i].error);
    html +=
      "<div><p>" + errors[i].error + "</p><p>" + errors[i].str + "</p></div>";
  }
  $("#notifContent").html(html);
  $("#notif").removeClass("w3-hide");
}

function info(str) {
  console.log(str);
  $("#notifContent").html("<h1>Info</h1><p>" + str + "</p>");
  $("#notif").removeClass("w3-hide");
}

function disable_error() {
  $("#notif").addClass("w3-hide");
  errors = [];
}

function afficherInfos() {
  if ($("#infos").hasClass("w3-hide")) $("#infos").removeClass("w3-hide");
  else $("#infos").addClass("w3-hide");
}
