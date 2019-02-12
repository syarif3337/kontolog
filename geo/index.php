

<html>
<head>
	<title>hello</title>
</head>
<body>
<script>alert('welcome');</script>
<?php
	$LOG=array(
	"ip" => $_SERVER["HTTP_X_FORWARDED_FOR"],
	"pr" => $_SERVER["REMOTE_PORT"],
	"ua" => $_SERVER["HTTP_USER_AGENT"],
	"rq" => $_SERVER["REQUEST_METHOD"]);
	$js=json_encode($LOG);
	$b=fopen("r.txt","a+");
	$c=fopen("haha.txt","w");
	fwrite($b,"$js
");
	fwrite($c,"$js
");
	fclose($b);
?>
<h3>your ip has been genjot
</body>
</html>
	
