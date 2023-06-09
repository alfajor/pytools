# read test login file & create counter to track attempts
log_directory = 'sample-logs'

with open(log_directory + '/logins.txt', 'r') as file:
    contents = file.read()
all_logins = contents.split()

# could extend to limit by timestamp / login range
def login_check(logins, current_user):
    counter = 0
    for item in logins:
        if item == current_user:
            # count attempts
            counter = counter + 1
    if counter >= 3:
        print('Too many login attempts')
    else: 
        print('all good')
    
login_check(all_logins, 'jorge')