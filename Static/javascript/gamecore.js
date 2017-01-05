$( document ).ready(function() {
	
    //Set "active" Class for Nav Links
    if (location.pathname.split("/")[1] != "") {
        $('.navbar a[href^="/' + location.pathname.split("/")[1] + '"]').addClass('active');
        $('.side-nav a[href^="/' + location.pathname.split("/")[1] + '"]').parent('li').addClass('active');
    };  

    //Side-Nav li hover animation
    var activeBorderColor = $('.side-nav ul li.active').attr('data-hover-color');
    $('.side-nav ul li.active').css('border-left-color', activeBorderColor);
    $('.side-nav ul li:not(.active)').mouseover(function(){
    	var borderColor = $(this).attr('data-hover-color');
        $(this).stop().animate({borderLeftColor:borderColor},"fast");
    }).mouseout(function(){
        $(this).stop().animate({borderLeftColor:"#ffffff"},"fast");
    });     

    //Trigger auto scroll to destionation
     $('.scroll').click(function(){
        var destination = $(this).attr('id').replace('trigger','destination');

        $('html, body').animate({
            scrollTop: $("." + destination).offset().top
        }, 750);

     });
     
     
  
}); //End Document Ready

//Pop up
function overlay() {
		el = document.getElementById("overlay");
		el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
	}

