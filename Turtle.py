import turtle
import math

class MyTurtle:

    def __init__(self):
        self.windowSizeX = 850
        self.windowSizeY = 850
        self.degree = 270
        turtle.setup(self.windowSizeX,self.windowSizeY)
        self.turtle = turtle.Turtle()
        #self.turtle.screensize(windowSizeX,windowSizeY)
        self.gridSize = 25
        self.gridNormalSize = 15
        # ---------- 일단 원점설정을 50픽셀 쯤 왼쪽 아래에서 띄워 잡을때.
        #self.gridOrg = 50
        #self.releOrgX = -(self.windowSizeX/2) + self.gridOrg
        #self.releOrgY = -(self.windowSizeY/2) + self.gridOrg
        self.releOrgX = 0 
        self.releOrgY = 0 
        print("initX : %d\ninitY : %d"%(self.releOrgX,self.releOrgY))
        self.turtle.reset()
        self.turtle.penup()
        self.turtle.speed(0)

    def setTurtle(self,setTurtle):
        self.turtle = setTurtle;

    def getTurtle(self):
        return self.turtle

    def drawLine(self, fromdotX, fromdotY, todotX, todotY, OrgCal):
        if OrgCal:
            self.turtle.goto(fromdotX+self.releOrgX, fromdotY+self.releOrgY)
            self.turtle.pendown()
            self.turtle.goto(todotX+self.releOrgX, todotY+self.releOrgY)
            self.turtle.penup()
        else:
            self.turtle.goto(fromdotX, fromdotY)
            self.turtle.pendown()
            self.turtle.goto(todotX, todotY)
            self.turtle.penup()
            self.turtle.home()

    def drawgoto(self, fromdotX, fromdotY):
        self.turtle.pendown()
        self.turtle.goto(fromdotX+self.gridOrgX, fromdotY+self.gridOrgY)
        self.turtle.penup()

    def gotoRel(self,relX,relY):
        self.turtle.goto(self.releOrgX + relX,self.releOrgY + relY)

    def gotoOrg(self):
        self.turtle.goto(self.releOrgX,self.releOrgY)

    def degrees(self,move):
        if move >= 360:
            move %= 360
        if move < self.degree:
            self.turtle.right((360 - self.degree) + move)
        else:
            self.turtle.right(move - self.degree)
        self.degree = move

    def drawTextAtLeftBottomRel(self,relX,relY,text):
        self.gotoRel(relX,relY)
        self.degrees(45)
        self.turtle.forward(self.gridSize/2+10)
        self.turtle.write(text)
        self.turtle.backward(self.gridSize/2+10)
        self.degrees(0)

    def drawTextAtLeftBottom(self,text):
        self.degrees(45)
        self.turtle.forward(self.gridSize/2+10)
        self.turtle.write(text)
        self.turtle.backward(self.gridSize/2+10)
        self.degrees(0)

    def drawFunctionY(self,func):
        for qur in range(0, func.end_query):
            t.penup()
            for pixx in range(-self.gridSize * self.gridNormalSize, self.gridSize * self.gridNormalSize):
                nomy = func.fy(pixx/self.gridSize)

                if nomy == "complex":
                    t.penup()
                    continue;
                
                pixy = nomy * self.gridSize
                if pixy < self.gridSize * self.gridNormalSize:
                    myt.gotoRel(pixx,pixy)
                    t.pendown()
                else:
                    t.penup()
            t.penup()
            func.cur_query = func.cur_query + 1

    def drawFunctionX(self,func):
        t.penup()
        for pixy in range(-self.gridSize * self.gridNormalSize,self.gridSize * self.gridNormalSize):
            nomx = func.fx(pixy/self.gridSize)

            if nomx == "complex":
                t.penup()
                continue;
            
            pixx = nomx * self.gridSize
            if pixx < self.gridSize * self.gridNormalSize:
                myt.gotoRel(pixx,pixy)
                t.pendown()
            else:
                t.penup()
        t.penup()
            
    def drawGrid(self,num):
        """ # 제 1사분면만 그리는 코드
        self.turtle.goto(self.releOrgX,self.releOrgY)
        for i in range(0,num):
            self.gotoRel(0,i*self.gridSize)
            self.drawTextAtLeftBottom(i)
            self.drawLine(0,i*self.gridSize,num*self.gridSize,i*self.gridSize,True)
            if i==0:
                self.degrees(270)
                self.turtle.stamp()
        for i in range(0,num):
            self.gotoRel(i*self.gridSize,0)
            self.drawTextAtLeftBottom(i)
            self.drawLine(i*self.gridSize,0,i*self.gridSize,num*self.gridSize,True)
            if i==0:
                self.degrees(180)
                self.turtle.stamp()
        """
        self.turtle.goto(self.releOrgX,self.releOrgY)
        for i in range(-num+1,num):
            self.gotoRel(-num*self.gridSize,i*self.gridSize)
            self.drawTextAtLeftBottom(i)
            self.drawLine(-num*self.gridSize,i*self.gridSize,num*self.gridSize,i*self.gridSize,True)
            if i==0:
                self.degrees(270)
                self.turtle.stamp()
        for i in range(-num+1,num):
            self.gotoRel(i*self.gridSize,-num*self.gridSize)
            self.drawTextAtLeftBottom(i)
            self.drawLine(i*self.gridSize,-num*self.gridSize,i*self.gridSize,num*self.gridSize,True)
            if i==0:
                self.degrees(180)
                self.turtle.stamp()
        self.gotoOrg()
        self.drawTextAtLeftBottomRel(0,0,"O")

class TurtleMathFunc:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.end_query = 2
        self.cur_query = 1
        self.lambda_func = False;

    def queryValue(self, query):
        self.query = query

    def fy(self,x):
        try:
            #원의 방정식 샘플.

            if self.lambda_func == False:
                if self.cur_query == 1:
                    self.y = (-(x**2) + 25)**(0.5)
                elif self.cur_query == 2:
                    self.y = -(-(x**2) + 25)**(0.5)
            else:
                self.y = self.lambda_func(x)
                
            
            #self.y = (x - 6)**2 + 5
            #self.y = math.log(x)
        except ValueError as e:
            print(str(e))
            return 0;
        except ZeroDivisionError as e:
            print(str(e))
            return 0;

        #허수
        if self.y.__class__.__name__ == "complex":
            return "complex"
        
        return self.y

    def fx(self,y):
        try:
            self.x = (y - 6)**2 + 5
        except ZeroDivisionError as e:
            print(str(e))
            return 0;
        return self.x

myt = MyTurtle()
tm = TurtleMathFunc()
t = myt.getTurtle()

t.ht()
myt.drawGrid(myt.gridNormalSize)

#myt.drawFunctionX(tm)

myt.drawFunctionY(tm)

#tm.queryValue("second")

lmabda_func = lambda x : -(-(x**2) + 25)**(0.5)

tm.lambda_func = lmabda_func

myt.drawFunctionY(tm)

