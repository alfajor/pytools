import requests
import sys
import json
import socket

def usage():
    if len(sys.argv) < 2:
        print('Usage: {} <url>. Please supply a URL'.format(sys.argv[0]))
        sys.exit(1)
usage()

def get_host_data():
    target = str(sys.argv[1])
    try:
        # headers
        req = requests.get('https://{}'.format(target))
        print('\n' + 'Headers: ' + str(req.headers))

        # hostname
        get_hostname = socket.gethostbyname(target)
        print('\n' + 'IP of {} is: {}'.format(target, get_hostname))

        # geo location - ipinfo.io
        geo_info = requests.get('https://ipinfo.io/{}/json'.format(get_hostname))
        res = json.loads(geo_info.text)
        city = 'City: ' + res['city']
        region = 'Region: ' + res['region']
        country = 'Country: ' + res['country']
        loc = 'Location: ' + res['loc']

        print('Geo Info: \n {} \n {} \n {} \n {}'.format(city, region, country, loc))

    except Exception as err:
        print('There was a problem: ', err)

get_host_data()