# Author: Linus Trahair
# Date: 12th December 2021
# This creates the gui for the application

import tkinter as tk
import matrix 

#the window variable
win=tk.Tk()
canvas=tk.Canvas(win,bg="white",width=220,height=100)


Cmatrix=False
CmatrixH=0
CmatrixW=0

#the current operation that the calculator is doing.
currentOp=""

#the current number and the number that it is operating on
presult=None
result=None

#checks if the = key has been pressed
finishOp=False

#these variables are used to find the 
htext=tk.StringVar()
wtext=tk.StringVar()

# a list that will be used to create a matrix
makewin=0

#sets the current operation and clears
def setOp(op):
    #using variables from higher in the code
    global currentOp
    global result
    global presult

    #sets the operation that will be used
    currentOp=op

    #if the result exists
    if result != None:
        presult=result
        result=None
    #prints which operation is in effect
    canvas.create_text(210,90,text=op)

#when the equal key is pressed, calculate the result
def calc():
    #using variables higher in the code
    global result
    global presult
    global finishOp

    #checks if there is a value to be calculated
    if result!=None and presult!=None:

        #if addition is the operation
        if currentOp == "+":
            #checks if the type is the same and if the result actually exists
            if type(result)==type(presult) and result+presult!=None:

                #gets rid of any previous drawings
                canvas.delete('all')

                #if the type is a number, print a number, if it is a matrix print a matrix.
                #also set finishOp to true to signify that an operation has been done
                if type(result)==int:
                    PrintNum(result+presult)
                    finishOp=True
                else:
                    PrintMatrix(result+presult)
                    finishOp=True
                result=result+presult
            else:
                #if the operation doesn't work, print this
                canvas.delete('all')
                canvas.create_text(30,30,text="nope")
                result=None
                presult=None

        #if subtraction is the operation
        elif currentOp == "-":
            
            #checks if the type is the same and if the result actually exists
            if type(result)==type(presult) and presult-result!=None:

                #gets rid of any previous drawings
                canvas.delete('all')

                #if the type is a number, print a number, if it is a matrix print a matrix.
                #also set finishOp to true to signify that an operation has been done
                if type(result)==int:
                    PrintNum(result-presult)
                    finishOp=True
                else:
                    PrintMatrix(result-presult)
                    finishOp=True
                result=result-presult
            else:
                #if the operation doesn't work, print this
                canvas.delete('all')
                canvas.create_text(20,20,text="nope")
                result=None
                presult=None

        
        #if multiplication is the operation
        elif currentOp == "*":

            #checks if the result actually exists
            if result!=None and presult!=None:

                #gest rid of everything else from the screen
                canvas.delete('all')

                #if both are integers, print an integer
                #and set finishOp to true
                if type(result)==int and type(presult)==int:
                    PrintNum(result*presult)
                    result=result*presult
                    finishOp=True
                    
                #if only one of them is an int, do the multByNum method to multiply the matrix by an integer.
                elif type(result)==int:
                    PrintMatrix(presult.multByNum(result))
                    result=presult.multByNum(result)
                    finishOp=True
                elif type(presult)==int:     
                    PrintMatrix(result.multByNum(presult))
                    result=result.multByNum(presult)
                    finishOp=True
                #if both are matrices, then multiply them and print the matrix
                else:
                    PrintMatrix(presult*result)
                    result=result*presult
                    finishOp=True
            
            else:
            #if the operation doesn't work, then display this and get rid of both values
                canvas.delete('all')
                canvas.create_text(10,10,text="nope")
                result=None
                presult=None

#displays the number and adds to it if it exists.                
def addtoNum(num):

    #gets these variables from higher up in the program
    global finishOp
    global result
    
    #gets rid of anything on the screen
    canvas.delete('all')

    #if first variable doesn't exist then make it exist as 0
    if result==None:
        result=0
    #if an operation has just finished, then replace the number
    if finishOp==True:
        result=num
        finishOp=False
    #otherwise, multiply the number by 10 and add the number to the end
    else:
        result*=10
        result+=num

    #show the number
    canvas.create_text(30,30,text=str(result))

#creates a window to get the dimensions of a matrix
def newWin():
    #makes the window the top level window
    makewin=tk.Toplevel(win)

    #entry for the matrix height
    Hlabel=tk.Label(makewin,text="Height")
    Hentry=tk.Entry(makewin,textvariable=htext)

    #entry forthe matrix length
    Wlabel=tk.Label(makewin,text="Width")
    Wentry=tk.Entry(makewin,textvariable=wtext)

    #put everything into a grid formation
    Hlabel.grid(row=0,column=0)
    Hentry.grid(row=0,column=1)
    
    Wlabel.grid(row=1,column=0)
    Wentry.grid(row=1,column=1)

    
    #create and organize enter button
    SubmitButton=tk.Button(makewin,text="Enter",command=lambda:entstats(makewin))
    SubmitButton.grid(row=2,column=0)

    #start the window
    makewin.mainloop()

#makes the matrix list of which will contain all stringvars and then closes the old window
#and makes a new one
def entstats(toplevel):
    #list for all of the stringvars
    matrixlist=[]

    #destroys the current top bar
    toplevel.destroy()
    inputList=[]
    newlevel=tk.Toplevel(win) 

    #makes a matrix of inputs that will be tethered to the output matrix's values
    for i in range(int(htext.get())):
        matrixlist.append([])
        inputList.append([])
        
        #for each point in the row, add a stringvar and pair it with an entry
        for j in range(int(wtext.get())):
            matrixlist[i].append(tk.StringVar())
            inputList.append(tk.Entry(newlevel,textvariable=matrixlist[i][j]).grid(row=i,column=j))
    #add a submission button
    subBut=tk.Button(newlevel,text="Enter",command= lambda:toMatrix(newlevel,matrixlist)).grid(row=int(htext.get()))

    #creates the window
    newlevel.mainloop()

#creates a matrix from all the data
def toMatrix(toplevel,matrixlist):
    #gets the variable from higher up in the code
    global result
    #creates a matrix with the width and height of the new matrix
    m=matrix.Matrix(int(htext.get()),int(wtext.get()))
    #adds all the values to the correct places
    for i in range(len(matrixlist)):
        for j in range(len(matrixlist[i])):
            m.setCell(i,j,int(matrixlist[i][j].get()))
    #prints the matrix
    PrintMatrix(m)

    #sets the result to the matrix
    result=m
    #destroy the matrix creation window
    toplevel.destroy()


            
#clears values and screen
def clear():
    #gets values from higher in the program
    global result
    global finishOp
    global presult

    #deletes both variables, canvas elements and makes sure that finishOp is false
    canvas.delete('all')
    result=None
    presult=None
    finishOp=False
    

            

#initializes the window           
def init():
    #creates all the numbers
    b1=tk.Button(win,text="1",width=6,command=lambda:addtoNum(1))
    b2=tk.Button(win,text="2",width=6,command=lambda:addtoNum(2))
    b3=tk.Button(win,text="3",width=6,command=lambda:addtoNum(3))
    b4=tk.Button(win,text="4",width=6,command=lambda:addtoNum(4))
    b5=tk.Button(win,text="5",width=6,command=lambda:addtoNum(5))
    b6=tk.Button(win,text="6",width=6,command=lambda:addtoNum(6))
    b7=tk.Button(win,text="7",width=6,command=lambda:addtoNum(7))
    b8=tk.Button(win,text="8",width=6,command=lambda:addtoNum(8))
    b9=tk.Button(win,text="9",width=6,command=lambda:addtoNum(9))
    b0=tk.Button(win,text="0",width=6,command=lambda:addtoNum(0))

    #creates all the operation buttons
    bpls=tk.Button(win,text="+",width=6, command=lambda: setOp("+"))
    bsub=tk.Button(win,text="-",width=6, command=lambda: setOp("-"))
    bmlt=tk.Button(win,text="x",width=6,command=lambda:setOp("*"))
    beql=tk.Button(win,text="=",width=6, command=lambda: calc())

    #creates the matrix initialization button
    bmtx=tk.Button(win,text="[ ]",command=newWin,width=6)

    #clears the values
    bclr=tk.Button(win,text="C", command=clear,width=6)

    #packing all of the elements
    canvas.grid(row=0,column=0,columnspan=4)
    b1.grid(row=1,column=0)
    b2.grid(row=1,column=1)
    b3.grid(row=1,column=2)
    b4.grid(row=2,column=0)
    b5.grid(row=2,column=1)
    b6.grid(row=2,column=2)
    b7.grid(row=3,column=0)
    b8.grid(row=3,column=1)
    b9.grid(row=3,column=2)
    b0.grid(row=4,column=1)
    bpls.grid(row=1,column=3)
    bsub.grid(row=2,column=3)
    bmlt.grid(row=3,column=3)
    beql.grid(row=4,column=3)
    bclr.grid(row=4,column=2)
    bmtx.grid(row=4,column=0)

    #makes the window unresizable
    win.resizable(False,False)


#creates the brackets that are around a matrix when displayed
def createBracket(height,xpos,side):

    #checks which side is to be created and makes it relative to the position
    if side==True:
        canvas.create_line(20+(xpos*20),20,20+(xpos*20),40+((height-1)*20),fill="black",width=1)
        canvas.create_line(20+(xpos*20),20,25+(xpos*20),20,fill="black",width=1)
        canvas.create_line(20+(xpos*20),40+((height-1)*20),25+(xpos*20),40+((height-1)*20),fill="black",width=1)
    else:
        canvas.create_line(40+(xpos*15),20,40+(xpos*15),40+((height-1)*20),fill="black",width=1)
        canvas.create_line(35+(xpos*15),20,40+(xpos*15),20,fill="black",width=1)
        canvas.create_line(35+(xpos*15),40+((height-1)*20),40+(xpos*15),40+((height-1)*20),fill="black",width=1)

#prints the matrix
def PrintMatrix(in_matrix):
    #delete everything else
    canvas.delete('all')
    #creates both of the matrices
    createBracket(in_matrix.h,0,True)
    createBracket(in_matrix.h,in_matrix.w-1,False)

    #prints the values
    for h in range(in_matrix.h):
        for w in range(in_matrix.w):
                canvas.create_text(30+(15*w),30+(20*h),text=in_matrix.getCell(h,w))
            
#prints a number
def PrintNum(num):
    canvas.delete('all')
    canvas.create_text(30,30,text=num)
#initializes the stuff
init()

#start the application
win.mainloop()

