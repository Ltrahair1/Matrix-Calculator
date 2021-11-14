class Matrix:
    
    
    #initializes the matrix
    def __init__(self, h, w):
        self.h=h
        self.w=w
        self.matrix=[]
        list=[]
        for i in range(h):
            for j in range(w):
                list.append(0)
            self.matrix.append(list)
            list=[]
    
    #adds two matrices together
    def __add__(self, added):

        #checks that both variables are matrices
        if isinstance(added,Matrix):

            #checks if the dimensions are the same
            if added.h==self.h and added.w==self.w:

                #creates a new matrix for the return value
                res=Matrix(self.h,self.w)

                #adds each variable together
                for row in range(len(self.matrix)):
                    for var in range(len(self.matrix[0])):
                        res.matrix[row][var]=self.matrix[row][var]+added.matrix[row][var]
                return res

            else:
                return None
        else:
            return None

    #subtracts matrices    
    def __sub__(self,subs):
        
        #checks that both variables are matrices
        if isinstance(subs,Matrix):

            #checks if the dimensions are the same
            if subs.h==self.h and subs.w==self.w:

                #creates a new matrix for the return value
                res=Matrix(self.h,self.w)

                #subtracts each variable 
                for row in range(len(self.matrix)):
                    for var in range(len(self.matrix[0])):
                        res.matrix[row][var]=self.matrix[row][var]-subs.matrix[row][var]
                return res

            else:
                return None
        else:
            return None

    def __mul__(self,mult):
        if isinstance(mult,Matrix):
            if self.w==self.h:
                res=Matrix(self.h,mult.w)
                for i in range(res.h):
                    for s in range(res.w):
                        for w in range(self.w):
                            res.matrix[i][s]+=self.matrix[i][w]*mult.matrix[w][s]
                return res
            else:
                return None
        else:
            return None

    def multByNum(self,num):
        res=Matrix(self.h,self.w)
        for i in range(res.h):
            for s in range(res.w):
                res.matrix[i][s]=self.matrix[i][s]*num
        return res

                    



            
    #prints the matrix
    def printM(self):

        #string for printing the output
        string=''

        #loops through the matrix and adds values to the string
        for row in self.matrix:
            string+='|'
            for s in row:
                string+=' '+str(s)
            string+='|'
            string+='\n'

        #prints the string
        print(string)

    #gets and sets cells of the matrix
    def setCell(self,h,w,num):
        self.matrix[h-1][w-1]=num

        
    def getCell(self,h,w):
        return self.matrix[h-1][w-1];
    

