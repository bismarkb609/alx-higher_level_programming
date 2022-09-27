#!/usr/bin/python3
""" take a url, sends a requet to the url """

if __name__ == "__main__":

    import requests
    import sys

    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
