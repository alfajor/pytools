import hashlib
import argparse

# POC MD5 Hash cracker. Generate sample md5 hash and run against sample wordlist 
def usage():
    parser = argparse.ArgumentParser(description='MD5 hash cracker')
    parser.add_argument('-md5', dest='hash', help='MD5 hash', required=True)
    parser.add_argument('-f', dest='wordlist', help='wordlist file path', required=True)

    parsed_args = parser.parse_args()
    return parsed_args

def md5_crack():
    arg = usage()
    cracked_hash = ''

    with open(arg.wordlist) as file:
        for word in file:
            word = word.strip()

            if hashlib.md5(bytes(word, 'utf-8')).hexdigest() == arg.hash:
                cracked_hash = word
                print(f'Success! Hash has been cracked: {cracked_hash}')
    
    if cracked_hash == '':
        print('Unable to crack hash. Consider expanding wordlist.')

md5_crack()