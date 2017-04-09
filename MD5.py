import hashlib
import time
from random import randint
salt= randint(0,99999999)
#print(salt)
loop=3
while loop==3:
    key_string = raw_input( "Key to turn into an MD5 password? " )

    print hashlib.md5( key_string ).hexdigest()
    time.sleep(1.5)

    option= raw_input("Would you like to salt it? (Y/N)").lower()
    if option == 'y':
        hash = hashlib.md5( str(salt) + key_string ).hexdigest()
        print "%s:%s" % (salt, hash) # Store these
        time.sleep(1)

        options=raw_input("Would you like to encrypt another hash? (Y/N)").lower()
        if options=='y':
            loop=3
        if options=='n':
            loop=0
            
    if option == 'n':
        options=raw_input("Would you like to encrypt another hash? (Y/N)").lower()
        if options=='y':
            loop=3
        if options=='n':
            loop=0
if loop==0:
    print "Ok,bye!"
    print "--Made by Gabr--"
    time.sleep(2)
    exit
