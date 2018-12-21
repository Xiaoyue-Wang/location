
#感知定位
p=[1./5]*5 # 网格均匀分布,先验概率
Measurements=['green','green'] #度量
world=['red','red','green','green','red'] #外部环境
pHit=0.6
pMiss=0.3


#得到后验概率

def sense_single(p,Z):
    q=[]
    for i in range(len(p)):
        t=(world[i]==Z)
        q.append(p[i]*pHit*t+p[i]*pMiss*(1-t))

    S=sum(q)
    for i in range(len(q)):
        q[i]=q[i]/S

    return q

def sense_continue(p,measurements):
    for i in range(len(measurements)):
        p=sense_single(p,measurements[i])
    return p


print(sense_continue(p,Measurements))
print(sum(sense_continue(p,Measurements)))