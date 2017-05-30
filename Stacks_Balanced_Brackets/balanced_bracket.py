def is_matched(e):
    l = len(e);
    if l%2 == 1:
        return False
    #l = l/2
    #e = list(e)
    a = []
    b = ['{', '(', '[']
    
    val = ['}', ')', ']']
    for i in range(l):
        #print 'hi'
        #print a, e[i]
        if e[i] in b:
            a.append(e[i])
        elif e[i] in val:
            #print a
            ind = val.index(e[i])
            #print a[-1], e[ind]
            if  a and a[-1] == b[ind]:                
                a.pop()
                #print 'pop a',a
            else:
                #print '2nd exit'
                return False
        else:
            return False
        
        
        #print a   
            
    if a:
        #print '3 exit', a
        return False
    else:
        return True
    

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
    #print '='*50