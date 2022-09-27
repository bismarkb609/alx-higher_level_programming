#!/bin/bash
#sends a request to a url, display only status code
curl -sI -w '%{response_code}' "$1" -o /dev/null
