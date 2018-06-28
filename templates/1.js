// var request = new XMLHttpRequest()

function addLoadEvent(func) {
    var oldonload = window.onload;
    if(typeof window.onload !== "function"){
        window.onload = func;

    }else{
        window.onload = function () {
            oldonload();
            func();
        }
    }
}

function getHTTPObject() {
    if (typeof XMLHttpRequest == "undefind") {

        XMLHttpRequest = function () {
            try {
                return new ActiveXObject("Msxml2.XMLHTTP.6.0");
            } catch (e) {
            }
            try {
                return new ActiveXObject("Msxml2.XMLHTTP.3.0");
            } catch (e) {
            }

            try {
                return new ActiveXObject("Msxml2.XMLHTTP");
            } catch (e) {
            }
            return false;
        }
        return new XMLHttpRequest();
    }
}

function getNewContent() {
    // var request = new getHTTPObject();
    var request = new XMLHttpRequest();

    // request.setRequestHeader('Access-Control-Allow-Origin', '*');
    if (request){

        request.open("GET","1.txt",true);
        // alert("5")
        request.onreadystatechange = function () {
            // alert("4")
            if (request.readyState == 4){
                // alert("3")
                var  para = document.createElement("p");
                var txt = document.createTextNode(request.responseText);
                para.appendChild(txt);
                document.getElementById("new").appendChild(para);
            }
        };
        request.send(null);
    }else {
        alert(("sorry,your browser doesn't support XMLHTTPRequest"))
    }

}
addLoadEvent(getNewContent);

