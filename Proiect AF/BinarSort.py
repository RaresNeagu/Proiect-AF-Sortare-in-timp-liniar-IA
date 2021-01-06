import time




def BinarSort(data,drawData,left,right,Bit,timeTick):
    if Bit>32 or left+1>right:
        return 
    
    low=left
    high=right

    while low<high+1:
        currentBit=data[low]<<Bit & 0x80000000
        
        
        if  currentBit==0:
            low=low+1
            
            
        else:
            drawData(data, ColorArray(len(data),left,right,low,high,currentBit,True),32-Bit)
            time.sleep(timeTick)
            data[low],data[high]=data[high],data[low]
            drawData(data, ColorArray(len(data),left,right,low,high,currentBit,True),32-Bit)
            time.sleep(timeTick)
            
            high=high-1
            
            

    if low==right+1:
         BinarSort(data,drawData,left,right,Bit+1,timeTick)
    else:
         BinarSort(data,drawData,left,low-1,Bit+1,timeTick)
         BinarSort(data,drawData,low,right,Bit+1,timeTick)

def ColorArray(dataLen,left,right,low,high,currentBit,isSwap=False):
    colorArray=[]
    for i in range(dataLen):
        if i>=low and i <=high:
            colorArray.append("gray")
        else:
            colorArray.append("white")

        if i==left:
            colorArray[i]=='orange'
        elif i==right:
            colorArray[i]=='red'
        elif i==currentBit:
            colorArray[i]=='yellow'

        if isSwap:
            if i==low or i==high:
                colorArray[i]='green'
            
    return colorArray




