var signUp = document.getElementById("reg-container")
var logIn = document.getElementById("login-container")
var signUpButton = document.getElementById("sign-up-button")
var logInButton = document.getElementById("log-in-button")
var facebookLogIn = document.getElementById("facebook-login")
var signUpSubmit = document.getElementById("sign-up-submit")
var logInSubmit = document.getElementById("log-in-submit")
var body = document.getElementsByTagName("body")[0];

var openNav = function () {
    document.getElementById("mySideNav").style.width = "350px";
    document.getElementById("main").style.marginLeft = "350px";
}

var closeNav = function () {
    document.getElementById("mySideNav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
}

var sendToServer = function () {
	var request = new XMLHttpRequest();
	request.onreadystatechange = function () {
		if (request.readyState == XMLHttpRequest.DONE) {
			if (request.status >= 200 && request.status < 400) {
				console.log("200 OK. Request has gone through.");
        $.sweetModal({
        content: "Registration successful!",
        icon: $.sweetModal.ICON_SUCCESS,

        buttons: [
          {
            label: "Thanks!",
            classes: "greenB"
          }
        ]
      });


			getFromServer();
      var sideBarOpen = document.getElementById("navOpen")
      sideBarOpen.style.display = "";
      var sideBar = document.getElementById("mySideNav")
      sideBar.remove()

			} else {
				console.error("Something has gone wrong.");
        $.sweetModal({
        content: "An account with this e-mail already exists!",
        icon: $.sweetModal.ICON_ERROR,

        buttons: [
          {
            label: "Oops...",
            classes: "redB"
          }
        ]
      });

        signUp.style.display = "none";
        logIn.style.display = "block";


		}

	}
	};

  var firstName = document.getElementById("fname");
  fname = firstName.value;
  var lastName = document.getElementById("lname")
  lname = lastName.value;
  var eMail = document.getElementById("email")
  email = eMail.value;
  var passWord = document.getElementById("password")
  password = passWord.value
  var data = "fname=" + encodeURIComponent(fname) + "&lname=" + encodeURIComponent(lname) + "&email=" + encodeURIComponent(email) + "&password=" + encodeURIComponent(password);

  request.open("POST","https://circa.herokuapp.com/users");
	request.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
  request.withCredentials = true;
	request.send(data);

}

// // page loads
//
// 1. get resrouce data
//   if 200:
//     show data
//   elif 401:
//     show login form
//       if 200:
//         get resource data
//       elif 401:
//         :(

var getFromServer = function () {


  var request = new XMLHttpRequest();
  	request.onreadystatechange = function () {
  		if (request.readyState == XMLHttpRequest.DONE) {
  			if (request.status == 200) {


          signUp.parentNode.removeChild(signUp);
          logIn.parentNode.removeChild(logIn);
          signUpButton.parentNode.removeChild(signUpButton);
          logInButton.parentNode.removeChild(logInButton);
          facebookLogIn.parentNode.removeChild(facebookLogIn);
          contacts = JSON.parse(request.responseText)
					var contacts_table = document.createElement("table");
					contacts_table.setAttribute("id","contactsTable");
					var sidebar_div = document.createElement("div");
					sidebar_div.setAttribute("id","mySideNav");
					sidebar_div.setAttribute("class","sidenav");
          var sideBarOpen = document.getElementById("navOpen")
          sideBarOpen.style.display = "";
					var aTag = document.createElement('a');
					aTag.setAttribute("href","javascript:void(0)")
					aTag.setAttribute("class","closebtn")
					aTag.setAttribute("onclick","closeNav()")
					aTag.innerHTML = "&times;"
  				$.sweetModal("Welcome back!");
  				for (var i=0; i < contacts.length; i++){

					var id = contacts[i]["id"]
					var name = contacts[i]["name"]
					phones = JSON.parse(request.responseText)
					var phone = phones[i]["phone"]
					ethnicities = JSON.parse(request.responseText)
					var ethnicity = ethnicities[i]["ethnicity"]
					froms = JSON.parse(request.responseText)
					var she_from = froms[i]["she_from"]
					bodies = JSON.parse(request.responseText)
					var body_type = bodies[i]["body_type"]
					doing = JSON.parse(request.responseText)
					var does = doing[i]["does"]

					var row = contacts_table.insertRow(-1);
					row.id = 'r' + id;
					var cell1 = row.insertCell(0);
					var cell2 = row.insertCell(1);
					var cell3 = row.insertCell(2);
					var cell4 = row.insertCell(3);
					var cell5 = row.insertCell(4);
					var cell6 = row.insertCell(5);
				  var cell7 = row.insertCell(6);
				  cell1.innerHTML = id;
				  cell2.innerHTML = name;
				  cell3.innerHTML = phone;
				  cell4.innerHTML = ethnicity;
				  cell5.innerHTML = she_from;
				  cell6.innerHTML = body_type;
				  cell7.innerHTML = does;
					body.appendChild(sidebar_div);
					sidebar_div.appendChild(contacts_table);
					sidebar_div.appendChild(aTag);
					contacts_table.style.display = "block";
				}

				console.log(contacts_table)

        } else {

          if (request.status == 401) {
						$.sweetModal({
						content: "Sorry, you are not authorized for this process.",
						icon: $.sweetModal.ICON_ERROR,

						buttons: [
							{
								label: "Darn it!",
								classes: "redB"
							}
						]

						});

            var sideBarOpen = document.getElementById("navOpen")
            sideBarOpen.style.display = "none";

            if (request.status >= 200 && request.status < 400) {


              contacts = JSON.parse(request.responseText)
    					var contacts_table = document.createElement("table");
    					contacts_table.setAttribute("id","contactsTable");
    					var sidebar_div = document.createElement("div");
    					sidebar_div.setAttribute("id","mySideNav");
    					sidebar_div.setAttribute("class","sidenav");
              var sideBarOpen = document.getElementById("navOpen")
              sideBarOpen.style.display = "";
    					var aTag = document.createElement('a');
    					aTag.setAttribute("href","javascript:void(0)")
    					aTag.setAttribute("class","closebtn")
    					aTag.setAttribute("onclick","closeNav()")
    					aTag.innerHTML = "&times;"
      				$.sweetModal("Welcome back!");
							for (var i=0; i < users.length; i++){

                var id = contacts[i]["id"]
      					var name = contacts[i]["name"]
      					phones = JSON.parse(request.responseText)
      					var phone = phones[i]["phone"]
      					ethnicities = JSON.parse(request.responseText)
      					var ethnicity = ethnicities[i]["ethnicity"]
      					froms = JSON.parse(request.responseText)
      					var she_from = froms[i]["she_from"]
      					bodies = JSON.parse(request.responseText)
      					var body_type = bodies[i]["body_type"]
      					doing = JSON.parse(request.responseText)
      					var does = doing[i]["does"]

      					var row = contacts_table.insertRow(-1);
      					row.id = 'r' + id;
      					var cell1 = row.insertCell(0);
      					var cell2 = row.insertCell(1);
      					var cell3 = row.insertCell(2);
      					var cell4 = row.insertCell(3);
      					var cell5 = row.insertCell(4);
      					var cell6 = row.insertCell(5);
      				  var cell7 = row.insertCell(6);
      				  cell1.innerHTML = id;
      				  cell2.innerHTML = name;
      				  cell3.innerHTML = phone;
      				  cell4.innerHTML = ethnicity;
      				  cell5.innerHTML = she_from;
      				  cell6.innerHTML = body_type;
      				  cell7.innerHTML = does;
      					body.appendChild(sidebar_div);
      					sidebar_div.appendChild(contacts_table);
      					sidebar_div.appendChild(aTag);
      					contacts_table.style.display = "block";

						}

            console.log(contacts_table)

							}
					}

            else {

							$.sweetModal({
								content: 'Please login before continuing.',
								icon: $.sweetModal.ICON_WARNING
							});
              var sidebar_div = document.createElement("div");
              sidebar_div.setAttribute("id","mySideNav");
              sidebar_div.setAttribute("class","sidenav");
              body.appendChild(sidebar_div);
              var sideBarOpen = document.getElementById("navOpen")
	  					logIn.style.display = "block";
	  					signUp.style.display = "none";
              sideBarOpen.style.display = "none";


            }

          }

        }

}
request.open("GET","https://circa.herokuapp.com/contacts");
request.withCredentials = true;
request.send();
}

// get resource
//	display it
// 401:
// 	log in
//		201:
//			get resource

var loginToServer = function (email) {
	var request = new XMLHttpRequest();
	request.onreadystatechange = function () {
		if (request.readyState == XMLHttpRequest.DONE) {
			if (request.status >= 200 && request.status < 400) {
				console.log("USER AUTHORIZED.");
        $.sweetModal({
        content: "Log-in successful!",
        icon: $.sweetModal.ICON_SUCCESS,

        buttons: [
          {
            label: "Sweet!",
            classes: "greenB"
          }
        ]
      });

			getFromServer();
      var sideBarOpen = document.getElementById("navOpen")
      sideBarOpen.style.display = "";
      var sideBar = document.getElementById("mySideNav")
      sideBar.remove()

			} else {
          if (request.status == 401 || request.status == 404){
            console.error("USER NOT AUTHORIZED.");
            $.sweetModal({
            content: "E-mail or password is wrong. Please try again.",
            icon: $.sweetModal.ICON_ERROR,

            buttons: [
              {
                label: "Okay.",
                classes: "redB"
              }
            ]
          });
  				}
		}

	}
	};

  var in_eMail = document.getElementById("in-email")
  authemail = in_eMail.value;
  var in_passWord = document.getElementById("in-password")
  authpw = in_passWord.value
  var data = "in-email=" + encodeURIComponent(authemail) + "&in-password=" + encodeURIComponent(authpw);

  request.open("POST","https://circa.herokuapp.com/sessions");
  request.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
  request.withCredentials = true;
  request.send(data);

}

signUpButton.onclick = function () {
  signUp.style.display = "block";
  logIn.style.display = "none";
}

logInButton.onclick = function() {
  logIn.style.display = "block";
  signUp.style.display = "none";
}

signUpSubmit.onclick = function () {
  sendToServer();

}

logInSubmit.onclick = function () {
  loginToServer();
}

window.onload = function() {

	getFromServer();
}

// Random Background Hero on Page Load and Refresh
// http://stackoverflow.com/questions/19369426/random-background-image-on-refresh

function randomBackground() {
    var backGrounds = ["assets/bgs/salara.jpg","assets/bgs/venice.jpg",
    "assets/bgs/france.jpg", "assets/bgs/dubai.jpg",
    "assets/bgs/greece.jpg", "assets/bgs/espana.jpg"];

    $("body").css({
        "background" : "url("+ backGrounds[Math.floor(Math.random() * backGrounds.length)] + ") no-repeat",
        "background-size" : "110%"
    });
}

// Show Random Image on Page Load
randomBackground();
