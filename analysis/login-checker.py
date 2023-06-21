# read test login file & create counter to track attempts
log_directory = '../sample-logs'

with open(log_directory + '/logins.txt', 'r') as file:
    contents = file.read()
all_logins = contents.split()

# could extend to limit by timestamp / login range
def login_check(logins, current_user):
    counter = 0
    for attempt in logins:
        if attempt == current_user:
            # count attempts
            counter = counter + 1
    if counter >= 3:
        print('Too many login attempts')
    else: 
        print(f'Welcome {current_user}')
    
login_check(all_logins, 'someone')