'''import numpy as np
def osd(data=[]):
    
    m= np.mean(data)
    vr=np.var(data)
    st= np.std(data)
    r= 0

    for i in data:
        if i>=m-st and i<=m+st:
            r+=1
    print(r)
    #return r 

data = [180,172,178,185,190,192,200,210,190]
#osd = np.frompyfun(osd,1)
osd(data)'''

def osd(data=[]):
    mean = sum(data)/len(data)
    stdvar = (sum((v-mean)**2 for v in data)/len(data))**0.5

    low, high = mean-stdvar,mean+stdvar

    count = len([v for v in data if low < v < high])

    print(count)

#data = [180,172,178,185,190,192,200,210,190]
#osd(data)