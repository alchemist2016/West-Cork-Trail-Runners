function myFunction() {
  var inpObj = document.getElementById("length");
  if (!inpObj.checkValidity()) {
    document.getElementById("verify").innerHTML = inpObj.validationMessage;
  }
}