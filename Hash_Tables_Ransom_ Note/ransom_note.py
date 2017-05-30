def ransom_note(a, b,m,n):
    a.sort()
    b.sort()
    for i in b:
        if i in a:
            a.remove(i)
        else:
            return False

    return True;
    
    
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom,m,n)
if(answer):
    print "Yes"
else:
    print "No"