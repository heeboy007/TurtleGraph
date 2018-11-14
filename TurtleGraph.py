import turtle
import math
from tkinter import *

class MyTurtle:

    def __init__(self):
        self.windowSizeX = 850
        self.windowSizeY = 850
        self.degree = 270
        turtle.setup(self.windowSizeX,self.windowSizeY, 30, 30)
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

        self.disp_window = Tk()
        self.listen = ButtonListeners(self)
        
        self.disp_window.title("Cordinates")
        self.disp_window.geometry("+%d+%d"%(self.windowSizeX + 50, 100))
        self.display_init(self.disp_window, self.listen)

    def display_init(self, window, listener):
        label_x = Label(window, text="X:")
        label_y = Label(window, text="Y:")

        entry_x = Entry(window)
        entry_y = Entry(window)
        entry_code = Entry(window)

        btn_draw_point = Button(window, text="점찍기", command=listener.point)
        btn_func_draw = Button(window, text="함수 그리기", command=listener.draw)

        self.gadget_list = [
            [label_x, label_y],
            [entry_x, entry_y],
            [btn_draw_point],
            [entry_code, btn_func_draw]
            ]

        for i in range(len(self.gadget_list)):
            for j in range(len(self.gadget_list[i])):
                self.gadget_list[i][j].grid(row=i, column=j)

    def setTurtle(self,setTurtle):
        self.turtle = setTurtle;

    def getTurtle(self):
        return self.turtle

    def drawUserFunction(self):
        exec(self.listen.code)

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
        self.turtle.penup()
        self.turtle.forward(self.gridSize/2+10)
        self.turtle.write(text)
        self.turtle.backward(self.gridSize/2+10)
        self.turtle.pendown()
        self.degrees(0)

    def drawTextAtLeftBottom(self,text):
        self.degrees(45)
        self.turtle.penup()
        self.turtle.forward(self.gridSize/2+10)
        self.turtle.write(text)
        self.turtle.backward(self.gridSize/2+10)
        self.turtle.pendown()
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
                    self.listen.cord_info(pixx/self.gridSize, nomy)
                    self.gotoRel(pixx,pixy)
                    t.pendown()
                else:
                    t.penup()
            t.penup()

            if(func.lambda_func == False):
                func.cur_query = func.cur_query + 1
            else:
                break;
            

    """def drawFunctionX(self,func):
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
        t.penup()"""
            
    def drawGrid(self,num):
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

class ButtonListeners:

    def __init__(self, access):
        self.t = access

    def set_tm(self, access):
        self.tm = access

    def point(self):
        lab_x = self.t.gadget_list[1][0]
        lab_y = self.t.gadget_list[1][1]
        x = float(lab_x.get())
        y = float(lab_y.get())
        self.t.getTurtle().dot()
        self.t.drawTextAtLeftBottom("(%.2f, %.2f)"%(x, y))

    def cord_info(self, x, y):
        lab_x = self.t.gadget_list[1][0]
        lab_y = self.t.gadget_list[1][1]
        lab_x.delete(0, END)
        lab_y.delete(0, END)
        lab_x.insert(0, "%.2f"%(x))
        lab_y.insert(0, "%.2f"%(y))

    def draw(self):
        inst_code = """
        local lmabda_func = lambda x : """
        inst_code_back = """
        self.tm.lambda_func = lmabda_func
        self.t.drawFunctionY(self.tm)
        """
        ent_c = self.t.gadget_list[3][0]
        inst_code += ent_c.get()
        inst_code += inst_code_back
        exec(inst_code)

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

    """def fx(self,y):
        try:
            self.x = (y - 6)**2 + 5
        except ZeroDivisionError as e:
            print(str(e))
            return 0;
        return self.x"""

myt = MyTurtle()
tm = TurtleMathFunc()
t = myt.getTurtle()

myt.listen.set_tm(tm)

t.ht()
myt.drawGrid(myt.gridNormalSize)

myt.drawFunctionY(tm)

lmabda_func = lambda x : 5/(x+2)-6

tm.lambda_func = lmabda_func

myt.drawFunctionY(tm)
