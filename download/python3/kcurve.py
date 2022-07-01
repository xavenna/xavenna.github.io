#koch curve
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
	u = (p2y - p1y) / (p2x - p1x)
	neg = m.pi if (p2x-p1x) < 0 else 0
	a = m.atan(u)+neg
	o = m.cos(a)*l/3
	q = l / 3
	p1 = Point(p1x, p1y)
	p2 = Point(p1x + o, p1y + q * m.sin(a))
	p3 = Point(p1x + o + q * m.sin(m.pi/6 - a), p1y + q * m.sin(a) + q * m.cos(m.pi/6 - a))
	p4 = Point(p1x + 2 * o, p1y + 2 * q * m.sin(a))
	p5 = Point(p2x, p2y)
	lineA = Line(p1, p2)
	lineB = Line(p2, p3)
	lineC = Line(p3, p4)
	lineD = Line(p4, p5)
	if num == 1:
		lineA.draw(win)
		lineB.draw(win)
		lineC.draw(win)
		lineD.draw(win)
	else:
		curve(lineA,num-1)
		curve(lineB,num-1)
		curve(lineC,num-1)
		curve(lineD,num-1)
	return
begin = t.time()
win = GraphWin("Koch Curve", 500, 500)
curve(Line(Point(0,100),Point(500,100)),6)
print(t.time()-begin)
win.getMouse()
win.close()
#depth of 7 takes around 2 minutes