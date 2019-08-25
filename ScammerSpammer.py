from sys import argv
from requests import session
from random import choice
from string import digits
from json import loads
from threading import Thread

session = session()
session.proxies = {'http':  'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'} # run the requests through tor

names = loads(open("names.json").read())
url = 'http://the-url-here-cause-im-too-lazy-to-add-argument-support-which-would-only-take-10-seconds.com'

def rangeOf10():
    return ''.join(choice(digits) for i in range(choice([1,2,3,4,5,6,7,8,9])))

def send(user, pwd):
    session.post(url, allow_redirects=False, data={'username': user, 'password': pwd})

for name in names:
    user = name.lower()

    a = choice([0,1])
    if(a == 0): # disgusting but okay
        user = user + choice(names)
    else:
        user = user + choice(names).lower()
    user = user + rangeOf10()

    pwd = None
    b = choice([0, 1])
    if(b == 0): # also disgusting but okay
        pwd = choice(names)
    else:
        pwd = choice(names).lower()
    pwd = pwd + rangeOf10()

    print("sending %s : %s" % (user, pwd))
    Thread(target=send, args=[name, pwd]).start()
