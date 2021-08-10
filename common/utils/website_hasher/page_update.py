import hashlib
import os
import sys

def hash_comparer(response, save_folder, print_output):
    try:
        cur_hash = hashlib.md5(response.text.encode('utf-8')).hexdigest()
    except AttributeError:
        print(" [!] page_update recieved the response as \"response.text\". (hash_comparer)")
        cur_hash = hashlib.md5(response.encode('utf-8')).hexdigest()

    with open(save_folder + 'hash.txt','r') as hash:
        old_hash = hash.read()

        if cur_hash == old_hash:
            if print_output:
                print("Page hasn't changed since last check")
            return False
        elif cur_hash != old_hash:
            if print_output:
                print("Page has updated.")
            with open(save_folder + 'hash.txt','w') as output:
                output.write(cur_hash)
            output.close()
            return True

def page_hasher(response, save_folder):
    try:
        hash = hashlib.md5(response.text.encode('utf-8')).hexdigest()
    except AttributeError:
        print(" [!] page_update recieved the response as \"response.text\". (page_hasher)")
        hash = hashlib.md5(response.encode('utf-8')).hexdigest()

    with open(save_folder + 'hash.txt', 'w') as output:
        output.write(hash)
    output.close()

def page_update(response, save_folder="./", loop=False, print_output=True):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    # Checks if the script has been run before.
    # If it has, it will use the hash_comparer function to compare the current and old hash.
    if os.path.isfile(save_folder + "hash.txt") and os.stat(save_folder + "hash.txt").st_size != 0:
        if hash_comparer(response, save_folder, print_output) == False:
            if not loop: # Needs to be checked because it would otherwise not work in a loop
                sys.exit()
            else:
                return False # Pass this to the write checker.
        else: # If the hash is different
            if loop:
                return True
            pass
    # If the script has never been run, it will generate the hash and store it for the next run.
    else:
        page_hasher(response, save_folder)
        print("   [*] page_update found no hash file. First time?")
        return True
