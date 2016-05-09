$(document).ready(function(){
    $('#s1').mouseenter(function(){
   		$('#s1').css({
			'border-color': '#40a0a5',			
			'border-right-width': 3,
			'border-left-width': 3,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#s1').mouseleave(function(){
    	$('#s1').css({
			'border-color': 'rgba(20, 91, 95, .5)',			
			'border-right-width': 10,
			'border-left-width': 10,
			'border-top-width': 0,
			'border-bottom-width': 0,
		});
    });
    $('#s2').mouseenter(function(){
   		$('#s2').css({
			'border-color': '#40a0a5',			
			'border-right-width': 3,
			'border-left-width': 3,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#s2').mouseleave(function(){
    	$('#s2').css({
			'border-color': 'rgba(20, 91, 95, .5)',			
			'border-right-width': 10,
			'border-left-width': 10,
			'border-top-width': 0,
			'border-bottom-width': 0,
		});
    });
    $('#s3').mouseenter(function(){
   		$('#s3').css({
			'border-color': '#40a0a5',			
			'border-right-width': 3,
			'border-left-width': 3,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#s3').mouseleave(function(){
    	$('#s3').css({
			'border-color': 'rgba(20, 91, 95, .5)',			
			'border-right-width': 10,
			'border-left-width': 10,
			'border-top-width': 0,
			'border-bottom-width': 0,
		});
    });
    $('#s4').mouseenter(function(){
   		$('#s4').css({
			'border-color': '#40a0a5',			
			'border-right-width': 3,
			'border-left-width': 3,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#s4').mouseleave(function(){
    	$('#s4').css({
			'border-color': 'rgba(20, 91, 95, .5)',			
			'border-right-width': 10,
			'border-left-width': 10,
			'border-top-width': 0,
			'border-bottom-width': 0,
		});
    });
    $('#s5').mouseenter(function(){
   		$('#s5').css({
			'border-color': '#40a0a5',			
			'border-right-width': 3,
			'border-left-width': 3,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#s5').mouseleave(function(){
    	$('#s5').css({
			'border-color': 'rgba(20, 91, 95, .5)',	
			'border-right-width': 10,
			'border-left-width': 10,
			'border-top-width': 0,
			'border-bottom-width': 0,
		});
    });
    $('#champnum').mouseenter(function(){
   		$('#champnum').css({
			'border-color': '#40a0a5',			
			'border-right-width': 3,
			'border-left-width': 3,
			'border-top-width': 1,
			'border-bottom-width': 1,
	    });
	}); 
    $('#champnum').mouseleave(function(){
    	$('#champnum').css({
			'border-color': 'rgba(20, 91, 95, .5)',	
			'border-right-width': 10,
			'border-left-width': 10,
			'border-top-width': 0,
			'border-bottom-width': 0,
		});
    });
	// input box pretty stuff

	$('input:text').one('focus', function(){
	    this.value = '';
	}); 

	$('input:text').one('focus blur', function() {
	    $(this).toggleClass('glow');
	    $(this).css({
			'border-right-width': 10,
			'border-left-width': 10,
			'border-top-width': 0,
			'border-bottom-width': 0,
	    })
	});
});