import os
import MailboxValidator
from datetime import date
from pathlib import Path
from termcolor import colored

# make directory
today = date.today()
d4 = today.strftime("%b-%d-%Y")
dat = str(d4)
os.makedirs(dat)

# input file
l = input("input list file : ")
a = open('api.txt', 'r').read().splitlines()
b = open('list.txt', 'r').read().splitlines()
c = int(input("how many check on 1 api : "))
ba = open(l, 'r').read().splitlines()
ac = len(ba)
ad = str(ba)
lo = ac // c
li = lo+1

#split list
for i in range(1, li+1):
    n = i * c
    n2 = n - c
    ap = open(os.path.join(dat, f'list{i}.txt'), 'a+')
    for line in ba[n2:n]:
        ap.write(line + '\n')

# execute the list
for i in range(0, len(a)):
    mbv = MailboxValidator.EmailValidation(a[0+i])
    data_folder = Path(dat)
    lb = data_folder / f'list{i+1}.txt'
    fu = open(lb).read().splitlines()
    for j in range(0, len(fu)):
            results = mbv.validate_email(fu[0+j])
            if results is None:
                print("Error connecting to API.\n")
            elif results['error_code'] == '':
                ase = float(results['mailboxvalidator_score'])
                if (ase > 0.7):
                    print(colored(results['email_address'] + ' - score: ' + str(results['mailboxvalidator_score']), 'green'))
                    ar = open('result.txt', 'a+')
                    ar.write(fu[0+j] + '\n')
                    ar.close()
                else:
                    print(colored(results['email_address'] + ' - score: ' + str(results['mailboxvalidator_score']), 'red'))
            else:
                print('error_code = ' + results['error_code'] + "\n")
            

