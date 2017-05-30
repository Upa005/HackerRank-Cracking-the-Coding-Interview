from bisect import *
n = int(raw_input().strip())
a = []

for i in xrange(n):
    op, contact = raw_input().strip().split(' ')
    
    if op == 'add':
        a.insert(bisect(a,contact),contact)
        #print a

       
    elif op =='find':
        count = 0
        l = len(contact)
        p = bisect_left(a,contact)
        while p<len(a):
            if a[p][:l] == contact:
                count+=1
                p+=1
            else:
                break
        print count