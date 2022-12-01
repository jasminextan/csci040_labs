'''
Instructions:

Download whitehouse_secrets.zip.
The SecLists github repo contains lots of security related datasets, including the passwords of the Ashley-Madison leak. These passwords are located at Passwords/Leaked-Databases/Ashley-Madison.txt. Download this file.
Create a program password_cracker.py that finds the password of the zip file. Your program should:
Open then file Ashley-Madison.txt, and create a list called passwords that contains all of the passwords.
    For each password in passwords, try opening whitehouse_secrets.zip with that password. If it successfully opens, then print out the password.
    HINT: You should use a try/except clause to determine whether the zip file opened, and perform different operations based on whether the file opened or not.
    Once the file is successfully decrypted, you should have a new file whitehouse_secrets/secrets.txt that contains President Obama's secrets.
    (Optional, but recommended) Change your passwords so that you're not using the same password for everything. I personally like to memorize all my passwords, but other people prefer using password managers to store the passwords. Firefox has an excellent one built-in.
According to Snowden, the NSA is capable of guessing up to 1 trillion passwords per second, and jack the ripper is a famous open source tool that's capable of guessing millions of passwords per second on an ordinary computer. (Your python program is probably capable of guessing between 10,000-100,000 passwords per second, which is a lot slower than jack the ripper.) So using strong passwords that are hard to guess is important. The XKCD comic has a great technique for generating easy-to-remember passwords that not even the NSA can crack.
'''

from zipfile import ZipFile

passextract = open('password_cracking_lab/Ashley-Madison.txt').read()
passwords = passextract.split()

for i in passwords:
    try:
        with ZipFile('password_cracking_lab/whitehouse_secrets.zip') as zf:
            zf.extractall(pwd=i.encode('ascii'))
            print("The password is" + i)
        break
    except:
        pass