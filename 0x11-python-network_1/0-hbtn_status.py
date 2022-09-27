#!/usr/bin/python3
#Fetches https://intranet.hbtn.io/statu

if __name__ == "__main__":
    import urllib.request 

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()

        print("Body response:$")
        print(f"\t- type: {type(html)}$")
        print(f"\t- content: {format(html)}$")
        print(f"\t- utf8 content: {format(html.decode('utf-8', 'replace'))}$")



