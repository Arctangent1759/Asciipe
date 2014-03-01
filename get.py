#!/usr/bin/python

# this is the api for the client, use it to request stuff from the remote
from argparse import ArgumentParser
import urllib2

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('request', metavar='REQUEST', help='api request in /get/* or init')
    parser.add_argument('-ip', metavar="IP", help="remote ip")
    return parser.parse_args()

def main():
    get = parse_arguments()
    api_request = "/get/"+get.request+"/"
    if (get.request == "init"):
        api_request = "/"
    try:
        response = urllib2.urlopen(get.ip + api_request)
    except URLError:
        exit(4) #Exit 4 is short for 404
    print response.read()

if __name__ == "__main__":
    main()
