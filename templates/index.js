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

function insertAfter(newElement,targetElement) {
    var parent = targetElement.parentNode;
    if (parent.lastChild === targetElement){
        parent.appendChild(newElement);
    }else{
        parent.insertBefore(newElement,targetElement.nextSibling);
    }

}

function moveElement(elementID,final_x,final_y,interval) {
    var elem = document.getElementById("message");
    if (elem.movement){
        clearTimeout(elem.movement);
    }
    if (!elem.style.left){
        elem.style.left = "0px";
    }
    if (!elem.style.top){
        elem.style.top = "0px";
    }
    var xpos = parseInt(elem.style.left);
    var ypos = parseInt(elem.style.top);
    if (xpos === final_x && ypos === final_y) return true;
    if (xpos<final_x){
        var dist = Math.ceil((final_x - xpos)/10)
        xpos = xpos+dist;
    }
    if (xpos>final_x){
        var dist = Math.ceil((final_x - xpos)/10)
        xpos = xpos-dist;
    }
    if (ypos<final_y){
        var dist = Math.ceil((final_y - ypos)/10)
        ypos = ypos+dist;
    }
    if (ypos>final_y){
        var dist = Math.ceil((final_y - ypos)/10)
        ypos = ypos-dist;
    }
    elem.style.left = xpos+"px";
    elem.style.top = ypos+"px";
    var repeat = "moveElement('"+elementID+"','"+final_x+"','"+final_y+"','"+interval+"')";
    elem.movement = setTimeout(repeat,interval)
}

function prepareSlidshow() {  //book DOM
    var intro = document.getElementById("intro");
}


var fetchAndCache = function () {
    var pages = document.getElementsByClassName("page");
    for (var i = 0;i <pages.length; i++){
        var pageLinks = page[i].getElementsByTagName("a");
        for (var j = 0;j<pageLinks; j++){
            var link = pageLinks[j];
            if (link.hasAttribute("href") && !(/[\#]/g).test() && (link.className.indexOf("fetch") >= 0)){
                var ai = new ajax(link,function (text,url) {
                   insertPages(text,url);
                });
                ai.doGet();
            }
        }
    }
}

function insertPages (text, originalLink) {

    var frame = getFrame();
    frame.write(text);

    //now we have a DOM to work with
    var incomingPages = frame.getElementsByClassName('page');

    var i;
    var pageCount = incomingPages.length;
    //helper for onlcick below
    var onclickHelper = function (e) {
        return function (f) {
            slidfast.ui.slideTo(e);
        };
    };

    for (i = 0; i < pageCount; i += 1) {
        //the new page will always be at index 0 because
        //the last one just got popped off the stack with appendChild (below)
        //todo - handle better
        var newPage = incomingPages[0];
        //stage the new pages to the left by default
        //(todo check for predefined stage class)
        newPage.className = 'page stage-left';

        //find out where to insert
        var location = newPage.parentNode.id === 'back' ? 'back' : 'front';

        try {
            //mobile safari will not allow nodes to be transferred from one DOM to another so
            //we must use adoptNode()
            document.getElementById(location).appendChild(document.adoptNode(newPage));
        } catch (e) {
            //todo graceful degradation?
        }
        //this is where prefetching multiple "mobile" pages embedded in a single html page gets tricky.
        //we may have N embedded pages, so how do we know which node/page this should link/slide to?
        //for now we'll assume the first *-page in the "front" node is where this links to.
        if (originalLink.onclick === null) {
            //todo set the href for ajax bookmark (override back button)
            originalLink.setAttribute('href', '#');
            //set the original link for transition
            originalLink.onclick = onclickHelper(newPage.id);
        }
    }
}

