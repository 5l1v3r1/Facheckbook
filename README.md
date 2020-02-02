# Mass Facebook Account Checker
<pre>
Usage : python3 fb.py [list.txt] [proxy:port]

list.txt file contains:
        $email|$password
        Example : jhonykecil@gmail.com|s3cr3tp4ssw0rd

Use Tor Proxies : 
        first, start tor service by using command "tor"
        then execute:
        python3 fb.py list.txt "socks5://127.0.0.1:9050"
        
Use free proxy from https://free-proxy-list.net/ :
        find your proxy in https://free-proxy-list.net/
        execute:
        python3 fb.py list.txt "$ip:$port"

By FilthyRoot 
(c) 2020 Jogjakarta Hacker Link
