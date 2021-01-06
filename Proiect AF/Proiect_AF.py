from tkinter import *
from tkinter import ttk
import random
from Postman import PostmanSort
from BinarSort import BinarSort
from Counting import CountingSort
from Pigeonhole import pigeonhole_sort
root=Tk()
root.title('Proiect')
root.geometry('900x700+200+80')
root.config(bg='#082A46')
data=[]


def drawData(data,color,Bit):
    canvas.delete("all")
    canvas_height=450
    canvas_width=870
    x_width=canvas_width/(len(data)+1)
    offset=10
    spacing_bet_rect=10

    normalised_data=[i/max(data) for i in data]
   
    for i,height in enumerate(normalised_data):
        x0=i*x_width+offset+spacing_bet_rect
        y0=canvas_height-height*400
        x1=(i+1)*x_width
        y1=canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=color[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),font=("UT Sans",15,"italic bold"), fill="blue")
       
        if algo_menu.get()=='Postman Sort': 
            canvasCounting.delete("all")
            
            
            
        if algo_menu.get()=='Binar Sort': 
            canvasCounting.delete("all")
            canvas.create_text(x0+2,y0-20,anchor=SW,text=str(bin(data[i])[2:]),font=("UT Sans",11,"italic bold"), fill="green")
            
            canvasCounting.create_text(25,30,anchor=SW,text="Algoritmul considera bitul: "+str(Bit)+" de la dreapta la stanga",font=("UT Sans",14,"italic"),fill="white")
            
        
    root.update_idletasks()   


def drawCounting(data,count,color):
    canvasCounting.delete("all")
    
    
    j=0
    for i in range(0,31):
        
        canvasCounting.create_rectangle(j+25,30,25,10,outline="white")
        canvasCounting.create_text(j+27,30,anchor=SW,text=str(i),font=("UT Sancs",11,"italic bold"),fill="white")
        canvasCounting.create_rectangle(j+25,60,25,40,outline="white")
        canvasCounting.create_text(j+27,60,anchor=SW,text=str(count[i]),font=("UT Sancs",11,"italic bold"),fill=color[i])
        j=j+25
    
    canvasCounting.create_rectangle(j+25,30,25,10,outline="white")
    canvasCounting.create_rectangle(j+25,60,25,40,outline="white")
    root.update_idletasks()


def Sort():
    global data
    if algo_menu.get()=='Postman Sort':


        PostmanSort(data,drawData,speedscale.get())
    elif algo_menu.get()=='Binar Sort':
        
        BinarSort(data,drawData,0,len(data)-1,0,speedscale.get())
        drawData(data,['green' for x in range(len(data))],0)
        
        
    elif algo_menu.get()=='Counting Sort':
        CountingSort(data,drawCounting,speedscale.get(),drawData)
        drawData(data,['green' for x in range(len(data))],0)
    else:
        pigeonhole_sort(data,drawData,drawCounting,speedscale.get())
        drawData(data,['green' for x in range(len(data))],0)
        

    
    

def Generate():
    global data
    print('selected algorithm: '+selected_algorithm.get())
    
    
    minivalue=int(minvalue.get())
    maxivalue=int(maxvalue.get())
    sizeevalue=int(sizevalue.get())
    data=[]
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue,maxivalue+1))

   

    drawData(data,['red' for x in range(len(data))],0)



selected_algorithm=StringVar()
mainlabel=Label(root,text="algoritm=", font=("UT Sans",16,"italic bold"),bg="#05897A", width=10, fg="black",relief=GROOVE,bd=5)

mainlabel.place(x=0,y=0)

algo_menu=ttk.Combobox(root,width=15,font=("UT Sans",19,"italic bold"), textvariable=selected_algorithm,values=['Postman Sort','Binar Sort','Counting Sort','Pigeonhole Sort'])
algo_menu.place(x=145,y=0)
algo_menu.current(0)

random_generate=Button(root,text="Generate",bg="#2DAE9A",font=("UT Sans",12,"italic bold"),relief=SUNKEN,activebackground="#05945B",activeforeground="white",bd=5,width=10,command=Generate)
random_generate.place(x=750,y=60)

sizevaluelabel=Label(root,text="Size: ",font=("UT Sans",12,"italic bold"),bg="#0E6DA5",width=10,fg="black",height=2,relief=GROOVE,bd=5)
sizevaluelabel.place(x=0,y=60)

sizevalue=Scale(root,from_=0,to=30,resolution=1,orient=HORIZONTAL,font=("UT Sans",14,"italic bold"),relief=GROOVE,bd=2,width=10)
sizevalue.place(x=120,y=60)

minvaluelabel=Label(root,text="Min value: ",font=("UT Sans",12,"italic bold"), bg="#0E6DA5",width=10,fg="black",height=2,relief=GROOVE,bd=5)
minvaluelabel.place(x=250,y=60)

minvalue=Scale(root,from_=0,to=30,resolution=1,orient=HORIZONTAL,font=("UT Sans",14,"italic bold"),relief=GROOVE,bd=2,width=10)

minvalue.place(x=370,y=60)

maxvaluelabel=Label(root,text="Max value: ",font=("UT Sans",12,"italic bold"), bg="#0E6DA5",width=10,fg="black",height=2,relief=GROOVE,bd=5)
maxvaluelabel.place(x=500,y=60)

maxvalue=Scale(root,from_=0,to=30,resolution=1,orient=HORIZONTAL,font=("UT Sans",14,"italic bold"),relief=GROOVE,bd=2,width=10)
maxvalue.place(x=620,y=60)

start=Button(root,text="Sort",bg="#C45B09",font=("UT Sans",12,"italic bold"),relief=SUNKEN,activebackground="#05945B",activeforeground="white",bd=5,width=10,command=Sort)
start.place(x=750,y=0)

speedlabel=Label(root,text="Speed: ",font=("UT Sans",12,"italic bold"), bg="#0E6DA5",width=10,fg="black",height=2,relief=GROOVE,bd=5)
speedlabel.place(x=400,y=0)

speedscale=Scale(root,from_=0.1,to=5.0,resolution=0.2, length=200 ,digits=2,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
speedscale.place(x=520.0,y=0)

canvas=Canvas(root,width=870,height=450,bg="black")
canvas.place(x=10,y=130)

canvasCounting=Canvas(root,width=870,height=100,bg="black")
canvasCounting.pack(side=BOTTOM)




root.mainloop();





