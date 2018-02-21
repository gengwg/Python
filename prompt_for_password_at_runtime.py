import getpass

def svc_login(user,passwd):
    return (user, passwd) == ('gengwg', 'lol')

# uses login name according to shell env
# or local system password database
user = getpass.getuser()

# explicitly prompt the user for username
# user = input('Enter your username: ')

passwd = getpass.getpass()

if svc_login(user,passwd):
    print('yay!')
else:
    print('boo!')
