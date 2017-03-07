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
		<h4>

			<?php

				//make sure input to python script is formatted correctly

				for ($i = 1; $i <= 5; $i += 1) {
					$sani[$i] = str_replace(' ','',$_POST["sum$i"]);
				}


				$path = '/var/www/html/Main.py';
				$python = '/usr/bin/python3.4';
				$script = $python . " " . $path . " -s " . $sani[1] . " " . $sani[2] . " " . $sani[3] . " " . $sani[4] . " " . $sani[5] . " -r " . $_POST["region"] . " -c " . $_POST["champnum"];
				$command = escapeshellcmd($script);
				$results = exec($command, $my_output, $status);
				$data_array = explode(",", $results);

				//get the properly formatted bgs for the champions

				$j = 1;
				for ($i = 1; $i <= 13; $i += 3) {
					$champ[$j] = str_replace(array('"', ' '), '' , $data_array[$i]);
					$j++;
				}

				//temp fix to get rid of double quotes around KogMaw's name (rito pls)
				// KEVIN COMMENT
				// why are we iterating $data_array here, and not $champ?
				// gonna try to change this to see if that fixes things
				// END
				
				#$k = 1;
				#for ($i = 1; $i <= 13; $i += 1) {
				for ($i = 1; $i <= 5; $i += 1) {
					$pattern = "/\"/"; 
					$replace = ""; 
					//$fix_quote[$k] = preg_replace($pattern,$replace,$data_array[$i]);
					$fix_quote[$i] = preg_replace($pattern,$replace,$champ[$i]);
					$k++;
				}

				//standardize role names, e.g. DUO_CARRY turns to Carry, JUNGLE turns to Jungle

				$m = 1;
				for ($i = 2; $i <= 14; $i += 3){
					$role[$m] = ucfirst(strtolower(preg_replace('/DUO_/', '', $data_array[$i])));
					$m++;
				}

				$c = 1;
				for ($i = 15; $i <= 19; $i++){
					$champID[$c] = $data_array[$i];
					$c++;
				}

				?>
			 </h4>
			<h2 class="error"><?php 
				if ($status != 0) {
					echo '$script output' . $script;
					echo 'Status error:' . $status . '. Something went wrong.<br> Make sure all of your summoner names are spelled correctly.<br> Press the back button or click <a href="../index.html"><button class="buttonAdd">   Here   </button></a> to go back';
				}
//				else {
//					echo '<button class="buttonAdd" onClick="exec($summonerList, $summoners, $lockedList, $banList">Recalculate</button>'
//				}
				?>
			</h2>
			<div class="summoners">
				<div class="player1">
					<p class="p1">
						<?php echo strip_tags($_POST['sum1']); ?>
					</p>
				</div><div class="player2">
					<p class="p2">
						<?php echo strip_tags($_POST['sum2']); ?>
					</p>
				</div><div class="player3">
					<p class="p3">
						<?php echo strip_tags($_POST['sum3']); ?>
					</p>
				</div><div class="player4">
					<p class="p4">
						<?php echo strip_tags($_POST['sum4']); ?>
					</p>
				</div><div class="player5">
					<p class="p5">
						<?php echo strip_tags($_POST['sum5']); ?>
					</p>
				</div>
			</div>
				<div class="readText">
					<div id="summ1">
							<?php
								echo '<p class="bot_text">';
								echo $_POST['sum1'];
								echo '<br>' . $fix_quote[1] . ' ' . '<input type="button" class="champButton" id="pick1" value="&#10004;"> <input type="button" class="champButton" id="banned1" value="&#10006;">';
								echo '<br>' . $role[1];
								echo '</p>';
							?>
					</div><div id="summ2">
							<?php
								echo '<p class="bot_text">';
								echo $_POST['sum2'];
								echo '<br>' . $fix_quote[2] . ' ' . '<input type="button" class="champButton" id="pick2" value="&#10004;"> <input type="button" class="champButton" id="banned2" value="&#10006;">';
								echo '<br>' . $role[2];
								echo '</p>';
							?>
					</div><div id="summ3">
							<?php
								echo '<p class="bot_text">';
								echo $_POST['sum3'];
								echo '<br>' . $fix_quote[3] . ' ' . '<input type="button" class="champButton" id="pick3" value="&#10004;"> <input type="button" class="champButton" id="banned3" value="&#10006;">';
								echo '<br>' . $role[3];
								echo '</p>';
							?>
					</div><div id="summ4">
							<?php
								echo '<p class="bot_text">';
								echo $_POST['sum4'];
								echo '<br>' . $fix_quote[4] . ' ' . '<input type="button" class="champButton" id="pick4" value="&#10004;"> <input type="button" class="champButton" id="banned4" value="&#10006;">';
								echo '<br>' . $role[4];
								echo '</p>';
							?>
					</div><div id="summ5">
							<?php
								echo '<p class="bot_text">';
								echo $_POST['sum5'];
								echo '<br>' . $fix_quote[5] . ' ' . '<input type="button" class="champButton" id="pick5" value="&#10004;"> <input type="button" class="champButton" id="banned5" value="&#10006;">';
								echo '<br>' . $role[5];
								echo '</p>';
							?>
					</div>
				</div>
			</div>
<script>
	var picked = new Array();
	var banned = new Array();
	//jquery for changing the background on hover for champions
	$(document).ready(function(){
	    $('div#summ1').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ[1]; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	    $('div#summ1').mouseenter(function(){
	   		$('p.p1').css({
	   			'color' : 'rgba(230,230,230,1)',
				'transition-duration': '.4s', 
		    });
		    $('div.player1').css({
		    	'background-color' : 'rgba(0,0,0,.4)',
		    })
		}); 
	    $('div#summ1').mouseleave(function(){
	    	$('p.p1').css({
	    		'color' : 'rgba(0,0,0,0)',
				'transition-duration': '.4s', 
			});
		    $('div.player1').css({
		    	'background-color' : 'rgba(0,0,0,0)',
		    })
	    });

	    $('div#summ2').mouseenter(function(){
	   		$('p.p2').css({
	   			'color' : 'rgba(230,230,230,1)',
				'transition-duration': '.4s', 
		    });
		    $('div.player2').css({
		    	'background-color' : 'rgba(0,0,0,.4)',
		    })
		}); 
	    $('div#summ2').mouseleave(function(){
	    	$('p.p2').css({
	    		'color' : 'rgba(0,0,0,0)',
				'transition-duration': '.4s', 
			});
		    $('div.player2').css({
		    	'background-color' : 'rgba(0,0,0,0)',
		    })
	    });
	    $('div#summ3').mouseenter(function(){
	   		$('p.p3').css({
	   			'color' : 'rgba(230,230,230,1)',
				'transition-duration': '.4s', 
		    });
		    $('div.player3').css({
		    	'background-color' : 'rgba(0,0,0,.4)',
		    })
		}); 
	    $('div#summ3').mouseleave(function(){
	    	$('p.p3').css({
	    		'color' : 'rgba(0,0,0,0)',
				'transition-duration': '.4s', 
			});
		    $('div.player3').css({
		    	'background-color' : 'rgba(0,0,0,0)',
		    })
	    });
	    $('div#summ4').mouseenter(function(){
	   		$('p.p4').css({
	   			'color' : 'rgba(230,230,230,1)',
				'transition-duration': '.4s', 
		    });
		    $('div.player4').css({
		    	'background-color' : 'rgba(0,0,0,.4)',
		    })
		}); 
	    $('div#summ4').mouseleave(function(){
	    	$('p.p4').css({
	    		'color' : 'rgba(0,0,0,0)',
				'transition-duration': '.4s', 
			});
		    $('div.player4').css({
		    	'background-color' : 'rgba(0,0,0,0)',
		    })
	    });
	    $('div#summ5').mouseenter(function(){
	   		$('p.p5').css({
	   			'color' : 'rgba(230,230,230,1)',
				'transition-duration': '.4s', 
		    });
		    $('div.player5').css({
		    	'background-color' : 'rgba(0,0,0,.4)',
		    })
		}); 
	    $('div#summ5').mouseleave(function(){
	    	$('p.p5').css({
	    		'color' : 'rgba(0,0,0,0)',
				'transition-duration': '.4s',  
			});
		    $('div.player5').css({
		    	'background-color' : 'rgba(0,0,0,0)',
		    })
	    });
	    $('div#summ2').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ[2]; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	    $('div#summ3').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ[3]; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	    $('div#summ4').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ[4]; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	    $('div#summ5').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ[5]; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	});
	$('input#pick1').click(function(){
	   		$('input#pick1').css({
				'color' : '#3CB371',
				'transition-duration' : '.3s' 
		    });
		    picked.push("<?php echo $champID[1]; ?>");
		}); 
	$('input#banned1').click(function(){
	   		$('input#banned1').css({
				'color' : '#EA4C44',
				'transition-duration' : '.3s' 
		    });
		    banned.push("<?php echo $champID[1]; ?>");
		}); 
	$('input#pick2').click(function(){
	   		$('input#pick2').css({
				'color' : '#3CB371',
				'transition-duration' : '.3s' 
		    });
		    picked.push("<?php echo $champID[2]; ?>");
		}); 
	$('input#banned2').click(function(){
	   		$('input#banned2').css({
				'color' : '#EA4C44',
				'transition-duration' : '.3s' 
		    });
		    banned.push("<?php echo $champID[2]; ?>");
		}); 
	$('input#pick3').click(function(){
	   		$('input#pick3').css({
				'color' : '#3CB371',
				'transition-duration' : '.3s' 
		    });
		    picked.push("<?php echo $champID[3]; ?>");
		}); 
	$('input#banned3').click(function(){
	   		$('input#banned3').css({
				'color' : '#EA4C44',
				'transition-duration' : '.3s' 
		    });
		    banned.push("<?php echo $champID[3]; ?>");
		}); 
	$('input#pick4').click(function(){
	   		$('input#pick4').css({
				'color' : '#3CB371',
				'transition-duration' : '.3s' 
		    });
		    picked.push("<?php echo $champID[4]; ?>");
		}); 
	$('input#banned4').click(function(){
	   		$('input#banned4').css({
				'color' : '#EA4C44',
				'transition-duration' : '.3s' 
		    });
		    banned.push("<?php echo $champID[4]; ?>");
		}); 
	$('input#pick5').click(function(){
	   		$('input#pick5').css({
				'color' : '#3CB371',
				'transition-duration' : '.3s' 
		    });
		    picked.push("<?php echo $champID[5]; ?>");
		}); 
	$('input#banned5').click(function(){
	   		$('input#banned5').css({
				'color' : '#EA4C44',
				'transition-duration' : '.3s' 
		    });
		    banned.push("<?php echo $champID[5]; ?>");
		}); 
	$(window).load(function(){
   		$('html').css({
			'background' : 'url(../bg/<?php echo $champ[1]; ?>.jpg) no-repeat center center fixed',
			'background-position' : '50% 10%',
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
