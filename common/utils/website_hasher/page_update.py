import hashlib
import os
import sys

def hash_comparer(response):
    cur_hash = hashlib.md5(response.text.encode('utf-8')).hexdigest()
    with open('hash.txt','r') as hash:
        old_hash = hash.read()

        if cur_hash == old_hash:
            print("Page hasn't changed since last check")
            return False
        elif cur_hash != old_hash:
            print("Page has updated.")
            with open('hash.txt','w') as output:
                output.write(cur_hash)
            output.close()
            return True

def page_hasher(response):
    hash = hashlib.md5(response.text.encode('utf-8')).hexdigest()
    with open('hash.txt', 'w') as output:
        output.write(hash)
    output.close()

def page_update(response):
    # Basically checks if the script has been run before.
    # If it has, it will use the hash_comparer function to compare the current and old hash.
    if os.path.isfile("hash.txt") and os.stat("hash.txt").st_size != 0:
        if hash_comparer(response) == False:
            sys.exit()
        else:
            pass
    # If the script has never been run, it will generate the hash and store it for the next run.
    else:
        page_hasher(response)
        print("First time?")
