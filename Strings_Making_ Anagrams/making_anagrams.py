def number_needed(a, b):
    count = 0
    a = list(a)
    b = list(b)
    l = len(a) + len(b)
    #print a,b
    for i in a:
        if i in b:
            b.remove(i);
            count+=2
    #print len(a), len(b) , count
    count = l - count
    print count
            
    

a = raw_input().strip()
b = raw_input().strip()

number_needed(a, b)