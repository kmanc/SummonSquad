$(document).ready(function(){
    $("#s1").mouseenter(function(){
   		$('#s1').css({
			'border-color': '#40a0a5',
			'border-radius': 1,
			'border-right-width': 0,
			'border-left-width': 0,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#s1').mouseleave(function(){
    	$('#s1').css({
			'border-color': 'rgba(20, 91, 95, .5)',
			'border-radius': 1,
			'border-right-width': '2',
			'border-left-width': '2',
			'border-top-width': '2',
			'border-bottom-width': '2',
		});
    });
    $("#s2").mouseenter(function(){
   		$('#s2').css({
			'border-color': '#40a0a5',
			'border-radius': 1,
			'border-right-width': 0,
			'border-left-width': 0,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#s2').mouseleave(function(){
    	$('#s2').css({
			'border-color': 'rgba(20, 91, 95, .5)',
			'border-radius': 1,
			'border-right-width': '2',
			'border-left-width': '2',
			'border-top-width': '2',
			'border-bottom-width': '2',
		});
    });
    $("#s3").mouseenter(function(){
   		$('#s3').css({
			'border-color': '#40a0a5',
			'border-radius': 1,
			'border-right-width': 0,
			'border-left-width': 0,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#s3').mouseleave(function(){
    	$('#s3').css({
			'border-color': 'rgba(20, 91, 95, .5)',
			'border-radius': 1,
			'border-right-width': '2',
			'border-left-width': '2',
			'border-top-width': '2',
			'border-bottom-width': '2',
		});
    });
    $("#s4").mouseenter(function(){
   		$('#s4').css({
			'border-color': '#40a0a5',
			'border-radius': 1,
			'border-right-width': 0,
			'border-left-width': 0,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#s4').mouseleave(function(){
    	$('#s4').css({
			'border-color': 'rgba(20, 91, 95, .5)',
			'border-radius': 1,
			'border-right-width': '2',
			'border-left-width': '2',
			'border-top-width': '2',
			'border-bottom-width': '2',
		});
    });
    $("#s5").mouseenter(function(){
   		$('#s5').css({
			'border-color': '#40a0a5',
			'border-radius': 1,
			'border-right-width': 0,
			'border-left-width': 0,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#s5').mouseleave(function(){
    	$('#s5').css({
			'border-color': 'rgba(20, 91, 95, .5)',
			'border-radius': 1,
			'border-right-width': '2',
			'border-left-width': '2',
			'border-top-width': '2',
			'border-bottom-width': '2',
		});
    });

/*	    $('div#summ1').hover(function(){
   		$('html').css({
			'background' : 'url(../imgs/teemo.jpg) no-repeat center center fixed',
			'-webkit-background-size' : 'cover',
			'-moz-background-size' : 'cover',
			'-o-background-size' : 'cover',
			'background-size' : 'cover',
			'transition-duration': '.3s' 
	    });
	}); 
*/
    $('div#summ2').hover(function(){
   		$('html').css({
			'background' : 'url(../imgs/aatrox.jpg) no-repeat center center fixed',
			'-webkit-background-size' : 'cover',
			'-moz-background-size' : 'cover',
			'-o-background-size' : 'cover',
			'background-size' : 'cover',
			'transition-duration': '.3s' 
	    });
	}); 
    $('div#summ3').hover(function(){
   		$('html').css({
			'background' : 'url(../imgs/leesin.jpg) no-repeat center center fixed',
			'-webkit-background-size' : 'cover',
			'-moz-background-size' : 'cover',
			'-o-background-size' : 'cover',
			'background-size' : 'cover',
			'transition-duration': '.3s' 
	    });
	}); 
    $('div#summ4').hover(function(){
   		$('html').css({
			'background' : 'url(../imgs/taric.jpg) no-repeat center center fixed',
			'-webkit-background-size' : 'cover',
			'-moz-background-size' : 'cover',
			'-o-background-size' : 'cover',
			'background-size' : 'cover',
			'transition-duration': '.3s' 
	    });
	}); 
    $('div#summ5').hover(function(){
   		$('html').css({
			'background' : 'url(../imgs/graves.jpg) no-repeat center center fixed',
			'-webkit-background-size' : 'cover',
			'-moz-background-size' : 'cover',
			'-o-background-size' : 'cover',
			'background-size' : 'cover',
			'transition-duration': '.3s' 
	    });
	});
	// input box pretty stuff

	$('input:text').one('focus', function(){
	    this.value = '';
	}); 

	$('input:text').one('focus blur', function() {
	    $(this).toggleClass('glow');
	});
});


