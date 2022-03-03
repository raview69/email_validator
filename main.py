import MailboxValidator

l = input("input list file : ")
a = open('api.txt', 'r').read().splitlines()
c = int(input("how many check 1 api : "))
ba = open(l, 'r').read().splitlines()
ac = len(ba)
ad = str(ba)
lo = ac // c
li = lo+1

for i in range(1, li+1):
    n = i * c
    n2 = n - c
    ap = open(f'list{i}.txt', 'a+')
    for line in ba[n2:n]:
        ap.write(line + '\n')
    


