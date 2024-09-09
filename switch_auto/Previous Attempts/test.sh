#!/bin/bash

# Authentication and capturing H_P_SSID coockie
COOKIE=$(echo -e "POST /logon.cgi HTTP/1.1\r\nHost: 192.168.1.43\r\nContent-Length: 56\r\nCache-Control: max-age=0\r\nAccept-Language: en-US\r\nUpgrade-Insecure-Requests: 1\r\nOrigin: http://192.168.1.43\r\nContent-Type: application/x-www-form-urlencoded\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\nReferer: http://192.168.1.43/\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\n\r\nusername=admin&password={   }&cpassword=&logon=Login" | nc 192.168.1.43 80 | grep 'Cookie' | grep -o 'H_P_SSID=[^;]*')

#echo $COOKIE

# VLAN configuration
#echo -e "GET /qvlanSet.cgi?vid=20&vname=General&selType_1=0&selType_2=0&selType_3=2&selType_4=2&selType_5=0&qvlan_add=Add%2FModify HTTP/1.1\r\nHost: 192.168.1.43\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nReferer: http://192.168.1.43/qvlanSet.cgi?vid=1&vname=Default&selType_1=0&selType_2=0&selType_3=0&selType_4=0&selType_5=0&qvlan_add=Add%2FModify\r\nCookie: $COOKIE\r\nUpgrade-Insecure-Requests: 1\r\nPriority: u=4\r\n\r\n" | nc 192.168.1.43 80
