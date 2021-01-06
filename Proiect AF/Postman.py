import time



def ordona(pi,pf,data,data2,drawData,timeTick,baza):
    for i in range(pi,pf-1):
        for j in range(i+1,pf):
            if data2[i]>data2[j]:
                drawData(data2,['green' if x==i or x==j else 'red' for x in range(len(data))],0)
                time.sleep(timeTick)
                data2[i],data2[j]=data2[j],data2[i]
                drawData(data2,['green' if x==i or x==j else 'red' for x in range(len(data))],0)
                time.sleep(timeTick)
                aux=data[i]%10
                data[i]=data[j]%10
                data[j]=aux
                
                

   

def PostmanSort(data,drawData,timeTick):
    data2=[0]*len(data)
    for i in range(len(data)):
         data2[i]=data[i]
    maxidigits=0
    nrdigit=0
    for i in range(0,len(data)):
        t=data[i]
        while t>0:
            nrdigit=nrdigit+1
            t=t/10
        if nrdigit>maxidigits:
            maxidigits=nrdigit
        nrdigit=0
    baza=1
    for i in range(0,maxidigits-1):
        baza=baza*10
    
    for i in range(0,len(data)):
        maxi=data[i]/baza
        pmaxi=i
        for j in range(i+1,len(data)):
            if maxi>(data[j]/baza):
                maxi=data[j]/baza
                pmaxi=j
                
        drawData(data2,['yellow' if x==maxi else 'red' for x in range(len(data))],0)
        time.sleep(timeTick)
        drawData(data2,['green' if x==i or x==pmaxi else 'red' for x in range(len(data))],0)
        time.sleep(timeTick)
        
        data2[pmaxi],data2[i]=data2[i],data2[pmaxi]
        data[i],data[pmaxi]=data[pmaxi],data[i]
        drawData(data2,['green' if x==i or x==pmaxi else 'red' for x in range(len(data))],0)
        time.sleep(timeTick)
    i=0
    while baza>=1:

        while i<len(data):

            nr=data[i]/baza
            for j in range(i+1,len(data)+1):

                ordona(i,j,data,data2,drawData,timeTick,0)
                
            i=i+1
        baza=baza//10
    drawData(data2,['green' for x in range(len(data))],0)



