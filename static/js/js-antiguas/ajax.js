function getAjaxContent(url,divId)
{
		url="http://devcontrib.ieee.org/ieee/about/index.htm"    ;
			//submitting to following servlet
		 var req = initRequest(url);
		//alert("test");
	        req.onreadystatechange = function() {
			//alert(req.readyState );
			//alert(req.status );
	            if (req.readyState == 4) {

	                if (req.status == 200) {
				alert('200');
	                    populateDiv(req,divId);

	                } else if (req.status == 204){

	                }

	            }

	        };

	        req.open("GET", url, true);

	        req.send(null);
	        alert(req.status);

}
function populateDiv(req,divId)
 {
    var myDiv = document.getElementsByName(divId)[0];
    
    //alert(req.responseText);
    myDiv.innerHTML=req.responseText;;
    myDiv.style.display='';
    
 }
function initRequest(url) {
	    
		/* Check for running connections */ 
		// if (requester != null && requester.readyState != 0 && requester.readyState != 4) 
		 //{ 
		   //requester.abort(); 
		 //} 
		 alert(window.XMLHttpRequest) ;

	    if (window.XMLHttpRequest) {
 	        return new XMLHttpRequest(url);
	    } else if (window.ActiveXObject) {
	        isIE = true;
	        return new ActiveXObject("Microsoft.XMLHTTP");
	    }
	  }	

