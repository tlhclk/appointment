all_rhs=[]
file=open('denem.txt')
for a in file:
    b,c=a.strip().split('\t')
    all_rhs.append((b,c))
rh_dict={}
for i in range(0,1440):
    rh_dict[i]=0
for x in all_rhs:
    y=int(x[0].split(':')[0])*60+int(x[0].split(':')[1])
    z=int(x[1].split(':')[0])*60+int(x[1].split(':')[1])
    for k in range(y,z):
        rh_dict[k]+=1
"""
to hour
"""
rh_list=[]
file2=open('denem2.txt','w')
for a in rh_dict:
    h=int(a/60)
    m=a%60
    rh_list.append((str(h)+':'+str(m)+':0',rh_dict[a]))
    file2.write(str(h)+':'+str(m)+':0\t'+str(rh_dict[a])+'\n')
print(rh_list)
file2.close()
file.close()