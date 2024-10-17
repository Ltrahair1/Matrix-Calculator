# Author: Linus Trahair
# Date: 12th December 2021
# This creates the gui for the application

import tkinter as tk
import matrix 

#the window variable
window=tk.Tk()
canvas=tk.Canvas(window,bg="white",width=220,height=100)


Cmatrix=False
CmatrixH=0
CmatrixW=0

#the current operation that the calculator is doing.
currentOperation=""

#the current number and the number that it is operating on
presult=None
result=None

#checks if the = key has been pressed
finishOperation=False

#these variables are used to find the width and height 
htext=tk.StringVar()
wtext=tk.StringVar()

# a list that will be used to create a matrix
makewindow=0

#sets the current operation and clears
def setOperation(op):
    #using variables from higher in the code
    global currentOperation
    global result
    global presult

    #sets the operation that will be used
    currentOperation=op

    #if the result exists
    if result != None:
        presult=result
        result=None
    #prints which operation is in effect
    canvas.create_text(210,90,text=op)

#when the equal key is pressed, calculate the result
def calculate():
    #using variables higher in the code
    global result
    global presult
    global finishOperation

    #checks if there is a value to be calculated
    if result!=None and presult!=None:

        #if addition is the operation
        if currentOperation == "+":
            #checks if the type is the same and if the result actually exists
            if type(result)==type(presult) and result+presult!=None:

                #gets rid of any previous drawings
                canvas.delete('all')

                #if the type is a number, print a number, if it is a matrix print a matrix.
                #also set finishOperation to true to signify that an operation has been done
                if type(result)==int:
                    PrintNum(result+presult)
                    finishOperation=True
                else:
                    PrintMatrix(result+presult)
                    finishOperation=True
                result=result+presult
            else:
                #if the operation doesn't work, print this
                canvas.delete('all')
                canvas.create_text(30,30,text="nope")
                result=None
                presult=None

        #if subtraction is the operation
        elif currentOperation == "-":
            
            #checks if the type is the same and if the result actually exists
            if type(result)==type(presult) and presult-result!=None:

                #gets rid of any previous drawings
                canvas.delete('all')

                #if the type is a number, print a number, if it is a matrix print a matrix.
                #also set finishOperation to true to signify that an operation has been done
                if type(result)==int:
                    PrintNum(result-presult)
                    finishOperation=True
                else:
                    PrintMatrix(result-presult)
                    finishOperation=True
                result=result-presult
            else:
                #if the operation doesn't work, print this
                canvas.delete('all')
                canvas.create_text(20,20,text="nope")
                result=None
                presult=None

        
        #if multiplication is the operation
        elif currentOperation == "*":

            #checks if the result actually exists
            if result!=None and presult!=None:

                #gest rid of everything else from the screen
                canvas.delete('all')

                #if both are integers, print an integer
                #and set finishOperation to true
                if type(result)==int and type(presult)==int:
                    PrintNum(result*presult)
                    result=result*presult
                    finishOperation=True
                    
                #if only one of them is an int, do the multByNum method to multiply the matrix by an integer.
                elif type(result)==int:
                    PrintMatrix(presult.multByNum(result))
                    result=presult.multByNum(result)
                    finishOperation=True
                elif type(presult)==int:     
                    PrintMatrix(result.multByNum(presult))
                    result=result.multByNum(presult)
                    finishOperation=True
                #if both are matrices, then multiply them and print the matrix
                else:
                    PrintMatrix(presult*result)
                    result=result*presult
                    finishOperation=True
            
            else:
            #if the operation doesn't work, then display this and get rid of both values
                canvas.delete('all')
                canvas.create_text(10,10,text="nope")
                result=None
                presult=None

#displays the number and adds to it if it exists.                
def addtoNum(num):

    #gets these variables from higher up in the program
    global finishOperation
    global result
    
    #gets rid of anything on the screen
    canvas.delete('all')

    #if first variable doesn't exist then make it exist as 0
    if result==None:
        result=0
    #if an operation has just finished, then replace the number
    if finishOperation==True:
        result=num
        finishOperation=False
    #otherwise, multiply the number by 10 and add the number to the end
    else:
        result*=10
        result+=num

    #show the number
    canvas.create_text(30,30,text=str(result))

#creates a window to get the dimensions of a matrix
def popWindow():
    #makes the window the top level window
    makewindow=tk.Toplevel(window)

    #entry for the matrix height
    Hlabel=tk.Label(makewindow,text="Height")
    Hentry=tk.Entry(makewindow,textvariable=htext)

    #entry forthe matrix length
    Wlabel=tk.Label(makewindow,text="Width")
    Wentry=tk.Entry(makewindow,textvariable=wtext)

    #put everything into a grid formation
    Hlabel.grid(row=0,column=0)
    Hentry.grid(row=0,column=1)
    
    Wlabel.grid(row=1,column=0)
    Wentry.grid(row=1,column=1)

    
    #create and organize enter button
    SubmitButton=tk.Button(makewindow,text="Enter",command=lambda:enterStats(makewindow))
    SubmitButton.grid(row=2,column=0)

    #start the window
    makewindow.mainloop()

#makes the matrix list of which will contain all stringvars and then closes the old window
#and makes a new one
def enterStats(toplevel):
    #list for all of the stringvars
    matrixlist=[]

    #destroys the current top bar
    toplevel.destroy()
    inputList=[]
    newlevel=tk.Toplevel(window) 

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
    _matrix=matrix.Matrix(int(htext.get()),int(wtext.get()))
    #adds all the values to the correct places
    for i in range(len(matrixlist)):
        for j in range(len(matrixlist[i])):
            _matrix.setCell(i,j,int(matrixlist[i][j].get()))
    #prints the matrix
    PrintMatrix(_matrix)

    #sets the result to the matrix
    result=_matrix
    #destroy the matrix creation window
    toplevel.destroy()


            
#clears values and screen
def clear():
    #gets values from higher in the program
    global result
    global finishOperation
    global presult

    #deletes both variables, canvas elements and makes sure that finishOperation is false
    canvas.delete('all')
    result=None
    presult=None
    finishOperation=False
    

            

#initializes the window           
def init():
    #creates all the numbers
    button1=tk.Button(window,text="1",width=6,command=lambda:addtoNum(1))
    button2=tk.Button(window,text="2",width=6,command=lambda:addtoNum(2))
    button3=tk.Button(window,text="3",width=6,command=lambda:addtoNum(3))
    button4=tk.Button(window,text="4",width=6,command=lambda:addtoNum(4))
    button5=tk.Button(window,text="5",width=6,command=lambda:addtoNum(5))
    button6=tk.Button(window,text="6",width=6,command=lambda:addtoNum(6))
    button7=tk.Button(window,text="7",width=6,command=lambda:addtoNum(7))
    button8=tk.Button(window,text="8",width=6,command=lambda:addtoNum(8))
    button9=tk.Button(window,text="9",width=6,command=lambda:addtoNum(9))
    button0=tk.Button(window,text="0",width=6,command=lambda:addtoNum(0))

    #creates all the operation buttons
    buttonplus=tk.Button(window,text="+",width=6, command=lambda: setOperation("+"))
    buttonsubtract=tk.Button(window,text="-",width=6, command=lambda: setOperation("-"))
    buttonmultiply=tk.Button(window,text="x",width=6,command=lambda:setOperation("*"))
    buttonequal=tk.Button(window,text="=",width=6, command=lambda: calculate())

    #creates the matrix initialization button
    buttonmatrix=tk.Button(window,text="[ ]",command=popWindow,width=6)

    #clears the values
    buttonclear=tk.Button(window,text="C", command=clear,width=6)

    #packing all of the elements
    canvas.grid(row=0,column=0,columnspan=4)
    button1.grid(row=1,column=0)
    button2.grid(row=1,column=1)
    button3.grid(row=1,column=2)
    button4.grid(row=2,column=0)
    button5.grid(row=2,column=1)
    button6.grid(row=2,column=2)
    button7.grid(row=3,column=0)
    button8.grid(row=3,column=1)
    button9.grid(row=3,column=2)
    button0.grid(row=4,column=1)
    buttonplus.grid(row=1,column=3)
    buttonsubtract.grid(row=2,column=3)
    buttonmultiply.grid(row=3,column=3)
    buttonequal.grid(row=4,column=3)
    buttonclear.grid(row=4,column=2)
    buttonmatrix.grid(row=4,column=0)

    #makes the window unresizable
    window.resizable(False,False)


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
window.mainloop()

