#!/bin/python

import sys
from bisect import bisect

n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.insert(bisect(a,a_t),a_t)
    
    if a_i %2 == 0: #odd num
        print float(a[a_i/2])
    else:
        print (float(a[a_i/2])+a[a_i/2 +1])/2