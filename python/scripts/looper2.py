import time
from datetime import datetime

def hello(i):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    print("hello %s" % (i))
    
temp = []
full = False
first = True
array = [1, 2, 3]
old_value = 1
while True:       
    
    
    print("first", array)
    for i in array:
        time.sleep(2)
        
        if first == True:
            first = False
            continue 
        else:
            first = False
            
        hello(i)
            
            
            

