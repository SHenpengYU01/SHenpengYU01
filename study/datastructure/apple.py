# import math
def distance(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])
def move(pos,app):
    dy=-app[0]+pos[0]
    dx=app[1]-pos[1]
    # print(dx,dy)
    if(dy>0):
        for _ in range(dy):
            print("1",end="")
    if(dx>0):
        for _ in range(dx):
            print("2",end="")
    if dy<0:
        for _ in range(-dy):
            print("3",end="")
    if dx<0:
        for _ in range(-dx):
            print("4",end="")
    print("0",end="")


def movecost(pos, app):
    dy=-app[0]+pos[0]
    dx=app[1]-pos[1]
    cost=0
    if(dy>0):
        cost+=dy
    elif dy<0:
        cost+=-3*dy
    if(dx>0):
        cost+=2*dx
    elif dx<0:
        cost+=-4*dx
    # print(cost)
    return cost

num=int(input())
apple=[]

for k in range(num):
    line=input()
    for i in range(num):
        if line[i]=="1":
            apple.append((k,i))
        elif line[i]=="2":
            pos=(k,i)

minappset=[]
while(apple):
    mindis=9999999999
    for app in apple:
        dis=distance(pos,app)
        if dis<mindis:
            mindis=dis
            minappset=[]
            minappset.append(app)
        elif dis==mindis:
            minappset.append(app)
    # print(minappset)
    mincost=999999999
    for minapp in minappset:
        cost=movecost(pos,minapp)
        if cost<mincost:
            mincost=cost
            record=minapp
    apple.remove(record)
    move(pos,record)
    pos=record
    print(apple)