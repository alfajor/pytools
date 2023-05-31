from bs4 import BeautifulSoup
import requests
from colorama import init, Fore
init()

# scrape any and all email addresses and export to a file. 
def mail_scraper():
    try:
        # url = input(Fore.GREEN + 'Enter a URL: ')
        url = 'http://example.com'
        response = requests.get(str(url))
    except requests.exceptions.RequestException as err:
        print('There was an error in the supplied URL: {}'.format(err))
        raise SystemExit(err)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    mail_list = []
    emails = soup.select('a[href^=mailto]')
    for mail in emails:
        addy = mail['href'].split(':', 1)[1]
        if mail != None:
            mail_list.append(addy)
   
    print('{} Emails found {}'.format(len(mail_list), mail_list))

    try:
        answer = str(input(Fore.YELLOW + '[*] Would you like to export the email addresses? (y/n): '))
    except ValueError:
        print('[*] Please enter yes or no.')
            
    if answer.lower() in ['y', 'yes']:
        # write emails to a file
        try:
            with open('contacts.txt', 'w') as f:
                for item in mail_list:
                    print(item, file=f)
                    print(Fore.YELLOW + '[*] Success! Emails have been saved to the current working directory')
                    break
        except:
             print('Unable to write data to file.')
            
    elif answer.lower() in ['n', 'no']:
        print('goodbye')    

mail_scraper()