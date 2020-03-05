function myFunction() {
  var inpObj = document.getElementById("length");
  if (!inpObj.checkValidity()) {
    document.getElementById("verify").innerHTML = inpObj.validationMessage;
  }
}

function myFunction() {
  var inpObj = document.getElementById("date_joined");
  if (!inpObj.checkValidity()) {
    document.getElementById("verify").innerHTML = inpObj.validationMessage;
  }
}