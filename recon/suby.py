import sys
import requests

# simple subdomain enumerator
def usage():
    if len(sys.argv) < 3:
        print('Usage: <url> <subdomain wordlist> Enter a URL and path to subdomain wordlist.')
        sys.exit(1)
usage()

def suby():
    subdomain_list = sys.argv[2]
    wordlist_file = open(subdomain_list).read()
    subdomains = wordlist_file.splitlines()

    #check for valid subdomains 
    for sub in subdomains:
        target_url = f'http://{sub}.{sys.argv[1]}'

    try:
        requests.get(target_url)

    except requests.ConnectionError:
        print('There was a problem connecting to the URL. Trying again..')
        pass

    # TODO: prompt and write to export file
    print('Valid subdomain found:', target_url)

suby()