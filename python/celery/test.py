
from collections import deque

de = deque()

'''
de.append({1:'test'})
de.append({2:'tests'})

cc = de.copy()
for c in range(len(de)):
    print(de.pop())
print(de)
print(cc)
'''

from tasks3 import *


for i in range(20):
    results = reverse.delay()
    de.append({'id': i, 'result': results})
    
for i in range(len(de)):
    tt = de.pop()
    print(type(tt))
    print(tt.get('id'))
    print(tt.get('result'))
    #print(dir(tt.get('result')))
    print(tt.get('result').get())
    #print(tt.id)
#while True:
    #de.pop()
#print(results.status)
