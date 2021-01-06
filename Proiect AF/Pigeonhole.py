import time

def pigeonhole_sort(a,drawData,drawCounting,timeTick): 
    
    my_min = min(a) 
    my_max = max(a) 
    size = my_max - my_min + 1
  
    
    holes = [0] * 32
    
     
    for x in range(len(a)): 
        
        holes[a[x] - my_min] += 1
        drawCounting(a,holes,['green' if j==a[x]-my_min else 'white' for j in range(0,32)])
        drawData(a,['green' if b==x else "#A90042" for b in range(len(a))],0)
        time.sleep(timeTick)
     
    i = 0
    for count in range(size): 
        while holes[count] > 0: 
            holes[count] -= 1
            a[i] = count + my_min 
            i += 1
            drawData(a,['green' if x==i else "#A90042" for x in range(len(a)+1)],count+my_min)
            drawCounting(a,holes,['green' if j==count else 'white' for j in range(0,32)])
            time.sleep(timeTick)

