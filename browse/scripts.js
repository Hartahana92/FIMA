/*!
* Start Bootstrap - Bare v5.0.7 (https://startbootstrap.com/template/bare)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function onURLChange(urlAddress)
    {
    var addressID = urlAddress.value;
    var pos = addressID.indexOf('=');
        if(pos)addressID = addressID.slice(pos + 1);

    createPlayer(addressID);
    }

 function resize(){

document.querySelector('#subtitlesarea').style.height=
 document.getElementById('videoarea').style.height + 'px';
}
