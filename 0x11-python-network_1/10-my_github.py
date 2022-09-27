#!/usr/bin/python3
""" takes a github credentials """

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))
