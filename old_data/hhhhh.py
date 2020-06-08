import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
import codecs

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

with codecs.open('/Users/liyingqi/Desktop/wzh/v1.txt','r') as f:
    leader1_x= f.readlines()
    leader1_x= [float(item.strip()) for item in leader1_x]

with codecs.open('/Users/liyingqi/Desktop/wzh/v2.txt', 'r') as f:
    leader1_y = f.readlines()
    leader1_y = [float(item.strip()) for item in leader1_y]

with codecs.open('/Users/liyingqi/Desktop/wzh/vt1.txt', 'r') as f:
    leader1_t = f.readlines()
    leader1_t = [float(item.strip()) for item in leader1_t]

###2
with codecs.open('/Users/liyingqi/Desktop/wzh/vv1.txt','r') as f:
    leader2_x= f.readlines()
    leader2_x= [float(item.strip()) for item in leader2_x]

with codecs.open('/Users/liyingqi/Desktop/wzh/vv2.txt', 'r') as f:
    leader2_y = f.readlines()
    leader2_y = [float(item.strip()) for item in leader2_y]

with codecs.open('/Users/liyingqi/Desktop/wzh/vvt1.txt', 'r') as f:
    leader2_t = f.readlines()
    leader2_t = [float(item.strip()) for item in leader2_t]

###3
with codecs.open('/Users/liyingqi/Desktop/wzh/vvv1.txt','r') as f:
    leader3_x= f.readlines()
    leader3_x= [float(item.strip()) for item in leader3_x]

with codecs.open('/Users/liyingqi/Desktop/wzh/vvv2.txt', 'r') as f:
    leader3_y = f.readlines()
    leader3_y = [float(item.strip()) for item in leader3_y]

with codecs.open('/Users/liyingqi/Desktop/wzh/vvvt1.txt', 'r') as f:
    leader3_t = f.readlines()
    leader3_t = [float(item.strip()) for item in leader3_t]


###f1
with codecs.open('/Users/liyingqi/Desktop/wzh/x1.txt','r') as f:
    flower1_x= f.readlines()
    flower1_x= [float(item.strip()) for item in flower1_x]

with codecs.open('/Users/liyingqi/Desktop/wzh/x2.txt', 'r') as f:
    flower1_y = f.readlines()
    flower1_y = [float(item.strip()) for item in flower1_y]

with codecs.open('/Users/liyingqi/Desktop/wzh/1xt1.txt', 'r') as f:
    flower1_t = f.readlines()
    flower1_t = [float(item.strip()) for item in flower1_t]

###f2
with codecs.open('/Users/liyingqi/Desktop/wzh/x3.txt','r') as f:
    flower2_x= f.readlines()
    flower2_x= [float(item.strip()) for item in flower2_x]

with codecs.open('/Users/liyingqi/Desktop/wzh/x4.txt', 'r') as f:
    flower2_y = f.readlines()
    flower2_y = [float(item.strip()) for item in flower2_y]

with codecs.open('/Users/liyingqi/Desktop/wzh/2xt1.txt', 'r') as f:
    flower2_t = f.readlines()
    flower2_t = [float(item.strip()) for item in flower2_t]

###f3
with codecs.open('/Users/liyingqi/Desktop/wzh/x5.txt','r') as f:
    flower3_x= f.readlines()
    flower3_x= [float(item.strip()) for item in flower3_x]

with codecs.open('/Users/liyingqi/Desktop/wzh/x6.txt', 'r') as f:
    flower3_y = f.readlines()
    flower3_y = [float(item.strip()) for item in flower3_y]

with codecs.open('/Users/liyingqi/Desktop/wzh/3xt1.txt', 'r') as f:
    flower3_t = f.readlines()
    flower3_t = [float(item.strip()) for item in flower3_t]

###f4
with codecs.open('/Users/liyingqi/Desktop/wzh/x7.txt','r') as f:
    flower4_x= f.readlines()
    flower4_x= [float(item.strip()) for item in flower4_x]

with codecs.open('/Users/liyingqi/Desktop/wzh/x8.txt', 'r') as f:
    flower4_y = f.readlines()
    flower4_y = [float(item.strip()) for item in flower4_y]

with codecs.open('/Users/liyingqi/Desktop/wzh/4xt1.txt', 'r') as f:
    flower4_t = f.readlines()
    flower4_t = [float(item.strip()) for item in flower4_t]

middle = int(len(leader1_x)/2)
fig = plt.figure()

plt.rcParams['axes.facecolor']='white'
plt.grid()
ax = Axes3D(fig)
leader_1, = ax.plot(leader1_x,leader1_y,leader1_t,linewidth=0.2)
leader_2, = ax.plot(leader2_x,leader2_y,leader2_t,color='r',linewidth=0.2)
leader_3, = ax.plot(leader3_x,leader3_y,leader3_t,color='g',linewidth=0.2)


ax.scatter(leader1_x[0],leader1_y[0],leader1_t[0],marker='^')
ax.scatter(leader2_x[0],leader2_y[0],leader2_t[0],marker='^',color='r')
ax.scatter(leader3_x[0],leader3_y[0],leader3_t[0],marker='^',color='g')

ax.scatter(leader1_x[middle],leader1_y[middle],leader1_t[middle],marker='^')
ax.scatter(leader2_x[middle],leader2_y[middle],leader2_t[middle],marker='^',color='r')
ax.scatter(leader3_x[middle],leader3_y[middle],leader3_t[middle],marker='^',color='g')

ax.scatter(leader1_x[-1],leader1_y[-1],leader1_t[-1],marker='^')
ax.scatter(leader2_x[-1],leader2_y[-1],leader2_t[-1],marker='^',color='r')
ax.scatter(leader3_x[-1],leader3_y[-1],leader3_t[-1],marker='^',color='g')


leader12_x=[leader1_x[0],leader2_x[0]]
leader12_y=[leader1_y[0],leader2_y[0]]
leader12_t=[leader1_t[0],leader2_t[0]]
ax.plot(leader12_x,leader12_y,leader12_t,color='b')

leader13_x=[leader1_x[0],leader3_x[0]]
leader13_y=[leader1_y[0],leader3_y[0]]
leader13_t=[leader1_t[0],leader3_t[0]]
ax.plot(leader13_x,leader13_y,leader13_t,color='b')

leader23_x=[leader2_x[0],leader3_x[0]]
leader23_y=[leader2_y[0],leader3_y[0]]
leader23_t=[leader2_t[0],leader3_t[0]]
ax.plot(leader23_x,leader23_y,leader23_t,color='b')

##end
leader12_x=[leader1_x[-1],leader2_x[-1]]
leader12_y=[leader1_y[-1],leader2_y[-1]]
leader12_t=[leader1_t[-1],leader2_t[-1]]
ax.plot(leader12_x,leader12_y,leader12_t,color='b')

leader13_x=[leader1_x[-1],leader3_x[-1]]
leader13_y=[leader1_y[-1],leader3_y[-1]]
leader13_t=[leader1_t[-1],leader3_t[-1]]
ax.plot(leader13_x,leader13_y,leader13_t,color='b')

leader23_x=[leader2_x[-1],leader3_x[-1]]
leader23_y=[leader2_y[-1],leader3_y[-1]]
leader23_t=[leader2_t[-1],leader3_t[-1]]
ax.plot(leader23_x,leader23_y,leader23_t,color='b')


##middle
leader12_x=[leader1_x[middle],leader2_x[middle]]
leader12_y=[leader1_y[middle],leader2_y[middle]]
leader12_t=[leader1_t[middle],leader2_t[middle]]
ax.plot(leader12_x,leader12_y,leader12_t,color='b')

leader13_x=[leader1_x[middle],leader3_x[middle]]
leader13_y=[leader1_y[middle],leader3_y[middle]]
leader13_t=[leader1_t[middle],leader3_t[middle]]
ax.plot(leader13_x,leader13_y,leader13_t,color='b')

leader23_x=[leader2_x[middle],leader3_x[middle]]
leader23_y=[leader2_y[middle],leader3_y[middle]]
leader23_t=[leader2_t[middle],leader3_t[middle]]
ax.plot(leader23_x,leader23_y,leader23_t,color='b')


f_1, =ax.plot(flower1_x,flower1_y,flower1_t,color='b',linewidth=0.2)
f_2, =ax.plot(flower2_x,flower2_y,flower2_t,color='c',linewidth=0.2)
f_3, =ax.plot(flower3_x,flower3_y,flower3_t,color='salmon',linewidth=0.2)
f_4, =ax.plot(flower4_x,flower4_y,flower4_t,color='cadetblue',linewidth=0.2)
ax.legend([leader_1, leader_2, leader_3, f_1, f_2, f_3,f_4], ['领航者1','领航者2','领航者3','跟随者1','跟随者2','跟随者3','跟随者4'], bbox_to_anchor=(0.71, 0.8))


ax.scatter(flower1_x[0],flower1_y[0],flower1_t[0],color='b',marker='x')
ax.scatter(flower2_x[0],flower2_y[0],flower2_t[0],color='c',marker='x')
ax.scatter(flower3_x[0],flower3_y[0],flower3_t[0],color='salmon',marker='x')
ax.scatter(flower4_x[0],flower4_y[0],flower4_t[0],color='cadetblue',marker='x')

ax.scatter(flower1_x[middle],flower1_y[middle],flower1_t[middle],color='b',marker='x')
ax.scatter(flower2_x[middle],flower2_y[middle],flower2_t[middle],color='c',marker='x')
ax.scatter(flower3_x[middle],flower3_y[middle],flower3_t[middle],color='salmon',marker='x')
ax.scatter(flower4_x[middle],flower4_y[middle],flower4_t[middle],color='cadetblue',marker='x')

ax.scatter(flower1_x[-1],flower1_y[-1],flower1_t[-1],color='b',marker='x')
ax.scatter(flower2_x[-1],flower2_y[-1],flower2_t[-1],color='c',marker='x')
ax.scatter(flower3_x[-1],flower3_y[-1],flower3_t[-1],color='salmon',marker='x')
ax.scatter(flower4_x[-1],flower4_y[-1],flower4_t[-1],color='cadetblue',marker='x')

ax.set_xlabel('$q_{ix}$')
ax.set_ylabel('$q_{iy}$')
ax.set_zlabel('$q_{iz}$',)

ax.view_init(elev=30., azim=40)

# plt.show()
plt.savefig('./31d.pdf')