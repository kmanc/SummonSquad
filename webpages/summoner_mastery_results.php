<html>
<head>
  <meta charset="utf-8">
  <link href='https://fonts.googleapis.com/css?family=Gentium+Basic:400,700italic' rel='stylesheet' type='text/css'>
  <link href='riot.css' rel='stylesheet' type='text/css'>
  <title>SummonSquad</title>
	<script src="../scripts/jquery.js"></script>
</head>
<body>
		<h1>SummonSquad</h1>
		<h4><?php
				$sum1sani = str_replace(' ','',$_POST['sum1']);
				$sum2sani = str_replace(' ','',$_POST['sum2']);
				$sum3sani = str_replace(' ','',$_POST['sum3']);
				$sum4sani = str_replace(' ','',$_POST['sum4']);
				$sum5sani = str_replace(' ','',$_POST['sum5']);
				$python = '/usr/bin/python3.4 ';
				$path = '/var/www/html/scripts/Main.py ';
				$script = "/usr/bin/python3.4 /var/www/html/scripts/Main.py " . $sum1sani . " " . $sum2sani . " " . $sum3sani . " " . $sum4sani . " " . $sum5sani;
				//kmancxc, apajunky, raker, ashtreelee, iamjerbear
				$command = escapeshellcmd($script);
				$results = exec($command, $my_output, $status);
				$data_array = explode(",", $results);
				$champ1 = str_replace(array('"', ' '), '' , $data_array[1]);
				$champ2 = str_replace(array('"', ' '), '' , $data_array[4]);
				$champ3 = str_replace(array('"', ' '), '' , $data_array[7]);
				$champ4 = str_replace(array('"', ' '), '' , $data_array[10]);	
				$champ5 = str_replace(array('"', ' '), '' , $data_array[13]);

				$role1 = ucfirst(strtolower(preg_replace('/DUO_/', '', $data_array[2])));
				$role2 = ucfirst(strtolower(preg_replace('/DUO_/', '', $data_array[5])));
				$role3 = ucfirst(strtolower(preg_replace('/DUO_/', '', $data_array[8])));
				$role4 = ucfirst(strtolower(preg_replace('/DUO_/', '', $data_array[11])));
				$role5 = ucfirst(strtolower(preg_replace('/DUO_/', '', $data_array[14])));
				?>
			 </h4>
			<div class="summoners">
				<div class="readText">
					<div id="summ1">
						<span style="position: absolute; bottom: 0;">
							<?php
								echo $_POST['sum1'];
								echo '<br>' . $data_array[1];
								echo '<br>' . $role1;
							?>
						</span>
					</div><div id="summ2">
						<span style="position: absolute; bottom: 0;">
							<?php
								echo $_POST['sum2'];
								echo '<br>' . $data_array[4];
								echo '<br>' . $role2;
							?>
						</span>
					</div><div id="summ3">
						<span style="position: absolute; bottom: 0;">
							<?php
								echo $_POST['sum3'];
								echo '<br>' . $data_array[7];
								echo '<br>' . $role3;
							?>
						</span>
					</div><div id="summ4">
						<span style="position: absolute; bottom: 0;">
							<?php
								echo $_POST['sum4'];
								echo '<br>' . $data_array[10];
								echo '<br>' . $role4;
							?>
						</span>
					</div><div id="summ5">
						<span style="position: absolute; bottom: 0;">
							<?php
								echo $_POST['sum5'];
								echo '<br>' . $data_array[13];
								echo '<br>' . $role5;
							?>
						</span>
					</div>
				</div>
			</div>

<script>
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

	    $('div#summ1').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ1; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 90%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 

	    $('div#summ2').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ2; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 70%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	    $('div#summ3').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ3; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 50%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	    $('div#summ4').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ4; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 30%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	    $('div#summ5').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ5; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	});
	$(window).load(function(){
   		$('html').css({
			'background' : 'url(../bg/<?php echo $champ1; ?>.jpg) no-repeat center center fixed',
			'background-position' : '50% 90%',
			'-webkit-background-size' : 'cover',
			'-moz-background-size' : 'cover',
			'-o-background-size' : 'cover',
			'background-size' : 'cover',
			'transition-duration': '.3s' 
	    });
	}); 


</script>
</body>
</html>