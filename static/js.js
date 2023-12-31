
function validatereg(){
    var username = document.forms["registrationform"]["username"].value;
    var password = document.forms["registrationform"]["password"].value;
    var fullname = document.forms["registrationform"]["fullname"].value;
    var email = document.forms["registrationform"]["email"].value;
    var telephone = document.forms["registrationform"]["telephone"].value;

    if(username == ""){
        document.getElementById("wrong").innerHTML = "Username must be filled out";
        return false;
    }

    if(password == ""){
        document.getElementById("wrong").innerHTML = "Password must be filled out";
        return false;
    }

    if(fullname == ""){
        document.getElementById("wrong").innerHTML = "Fullname must be filled out";
        return false;
    }

    if(email == ""){
        document.getElementById("wrong").innerHTML = "Email must be filled out";
        return false;
    }

    if(telephone == ""){
        document.getElementById("wrong").innerHTML = "Telephone must be filled out";
        return false;
    }

    //password should include at least one upper case letter, one lower case letter, one digit and one of these symbols [+, !, *, -] and its length should be at least ten.
    var upperCaseLetters = /[A-Z]/g;
    if(!password.match(upperCaseLetters)){
        document.getElementById("wrong").innerHTML = "Password should include at least one upper case letter";
        return false;
    }

    var lowerCaseLetters = /[a-z]/g;
    if(!password.match(lowerCaseLetters)){
        document.getElementById("wrong").innerHTML = "Password should include at least one lower case letter";
        return false;
    }

    var numbers = /[0-9]/g;
    if(!password.match(numbers)){
        document.getElementById("wrong").innerHTML = "Password should include at least one digit";
        return false;
    }

    var symbols = /[+!*\-]/g;
    if(!password.match(symbols)){
        document.getElementById("wrong").innerHTML = "Password should include at least one of these symbols [+, !, *, -]";
        return false;
    }

    if(password.length < 10){
        document.getElementById("wrong").innerHTML = "Password should be at least 10 characters";
        return false;
    }

}

function validateAdForm() {
    var title = document.forms["advertisementcreate"]["title"].value;
    var description = document.forms["advertisementcreate"]["description"].value;
    var category = document.forms["advertisementcreate"]["category"].value;

    document.getElementById("formerror").innerHTML = "";

    if (title == "") {
        document.getElementById("formerror").innerHTML = "Title must be filled out";
        return false;
    }

    if (description == "") {
        document.getElementById("formerror").innerHTML = "Description must be filled out";
        return false;
    }

    if (category == "") {
        document.getElementById("formerror").innerHTML = "Category must be selected";
        return false;
    }

    return true;
}

function validateLogin(){
    var username = document.forms["loginform"]["username"].value;
    var password = document.forms["loginform"]["password"].value;

    if(username == ""){
        document.getElementById("wrong").innerHTML = "Username must be filled out";
        return false;
    }

    if(password == ""){
        document.getElementById("wrong").innerHTML = "Password must be filled out";
        return false;
    }
}
