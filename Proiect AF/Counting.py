import time

def CountingSort(array,drawCounting,timeTick,drawData):
    size = len(array)
    output = [0] * size

    
    count = [0] * 32

    
    for i in range(0, size):
        count[array[i]] += 1
        drawCounting(array,count,['green' if x==array[i] else 'white' for x in range(0,31)])
        drawData(array,['green' if x==i else "#A90042" for x in range(size)],0)
        time.sleep(timeTick)
        
        
    count2=[0]*32
    for i in range(1,32):
        count2[i]=count[i]

    
    for i in range(1,32):
        count[i] += count[i - 1]
        

    
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        drawData(output,['green' if output[count[array[i]] - 1] == array[i] else "#A90042" for x in range(size)],0)
        
        time.sleep(timeTick)
        count[array[i]] -= 1
        i -= 1
       
        
       

    
    for i in range(0, size):
        array[i] = output[i]
    
    drawCounting(array,count2,['white' if count2[i]==0 else 'green' for x in range(1,32)])
    



