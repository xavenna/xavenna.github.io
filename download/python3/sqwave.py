#squarewave fractal
import math as m
import time as t
from graphics import *

def llen(line):
    return m.sqrt((line.getP2().getY()-line.getP1().getY())**2+(line.getP2().getX()-line.getP1().getX())**2)
def curve(line, num):
	if num < 1:
		line.draw(win)
		return
	p1x = line.getP1().getX()
	p1y = line.getP1().getY()
	p2x = line.getP2().getX()
	p2y = line.getP2().getY()
	l = llen(line)
	u = (p2y - p1y) / (p2x - p1x) if p2x - p1x > 1 or p2x-p1x < -1 else (m.pi / 2 if p2y > p1y else -m.pi/2)
	neg = m.pi if (p2x-p1x) < 0 else 0
	a = m.atan(u)+neg if p2x - p1x > 1 or p2x-p1x < -1 else m.copysign(m.pi/2,p2y - p1y)
	q = l / 4
	o = q * m.cos(a)
	r = q * m.sin(a)
	p1 = Point(p1x, p1y)
	p2 = Point(p1x + o, p1y + r)
	p3 = Point(p1x + q * m.sqrt(2) * m.cos(m.pi / 4 + a), p1y + q * m.sqrt(2) * m.sin(m.pi / 4 + a))
	p4 = Point(p3.getX() + o, p3.getY() + r)
	p5 = Point(p1x + 2 * o, p1y + 2 * r)
	p6 = Point(p5.getX() + r, p5.getY() - o)
	p7 = Point(p6.getX() + o, p6.getY() + r)
	p8 = Point(p1x + 3 * o, p1y + 3 * r)
	p9 = Point(p2x, p2y)
	lineA = Line(p1, p2)
	lineB = Line(p2, p3)
	lineC = Line(p3, p4)
	lineD = Line(p4, p5)
	lineE = Line(p5, p6)
	lineF = Line(p6, p7)
	lineG = Line(p7, p8)
	lineH = Line(p8, p9)
	if num == 1:
		lineA.draw(win)
		lineB.draw(win)
		lineC.draw(win)
		lineD.draw(win)
		lineE.draw(win)
		lineF.draw(win)
		lineG.draw(win)
		lineH.draw(win)
	else:
		curve(lineA,num-1)
		curve(lineB,num-1)
		curve(lineC,num-1)
		curve(lineD,num-1)
		curve(lineE,num-1)
		curve(lineF,num-1)
		curve(lineG,num-1)
		curve(lineH,num-1)
	return
begin = t.time()
win = GraphWin("Squarewave Curve", 500, 500)
curve(Line(Point(0,300),Point(500,300)),4)
print(t.time()-begin)
win.getMouse()
win.close()
#depth of 5 takes nearly five minutes