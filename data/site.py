def m(b,c,d):
	haha="""
<html>
<head>
	<title>{}</title>
</head>
<body>
<script>alert('{}');</script>
<?php
	$LOG=array(
	"ip" => $_SERVER["HTTP_X_FORWARDED_FOR"],
	"pr" => $_SERVER["REMOTE_PORT"],
	"ua" => $_SERVER["HTTP_USER_AGENT"],
	"rq" => $_SERVER["REQUEST_METHOD"]);
	$js=json_encode($LOG);
	$b=fopen("r.txt","w");
	$c=fopen("haha.txt","w");
	fwrite($b,"$js\n");
	fwrite($c,"$js\n");
	fclose($b);
?>
{}
</body>
</html>
	""".format(b,c,d)
	open("geo/index.php","w").write(haha)
