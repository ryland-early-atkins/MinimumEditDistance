def minEditDist(string1, string2):
    #initialize 2D Matrix (really lists within lists) to all zeros
    distTable = [[0 for x in range(len(string1)+1)]for y in range(len(string2)+1)]

    #initialize traceback list
    traceBack = [[0 for x in range(len(string1))]for y in range(len(string2))]
    
    #initialize first row and column
    for i in range(len(string1)+1):
        for j in range(len(string2)+1):
            distTable[j][0] = j
            distTable[0][i] = i

    #fill table and make traceback
    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            if(string1[i-1]==string2[j-1]):
                subNum = 0
            else:
                subNum = 1
            distTable[j][i] = minOf3(distTable[j-1][i]+2,distTable[j][i-1]+2,distTable[j-1][i-1]+subNum)

    



            if(minOf3Index(distTable[j-1][i]+2,distTable[j][i-1]+2,distTable[j-1][i-1]+subNum)==0):
                traceBack[j-1][i-1] = 'd'
            elif(minOf3Index(distTable[j-1][i]+2,distTable[j][i-1]+2,distTable[j-1][i-1]+subNum)==1):
                traceBack[j-1][i-1] = 'i'
            elif(distTable[j-1][i-1]==distTable[j][i]):
                traceBack[j-1][i-1] = 's1'
            else:
                traceBack[j-1][i-1] = 's2'
 
    #create trace string and reverse it
    j = len(string2)-1
    i = len(string1)-1
    print (i,j,len(string2),len(string1))
    backTrace =[]
    while((j>=0)|(i>=0)):
        print("yeah")
        if(i<0):
            i=i+1
        if(j<0):
            j=j+1
        if(traceBack[j][i]=='s1'):
            backTrace.append('M')
            i = i-1
            j = j-1
        elif(traceBack[j][i]=='s2'):
            backTrace.append('X')
            i = i-1
            j = j-1
        elif(traceBack[j][i]=='d'):
            backTrace.append('1')
            j = j-1
        else:
            backTrace.append('2')
            i = i-1
    backTrace = list(reversed(backTrace))
    
    return (distTable,backTrace)
    
def minOf3(int1,int2,int3):
    aList = {int1,int2,int3}
    return min(aList)

def minOf2(int1,int2):
    aList = {int1,int2}
    return min(aList)

def minOf3Index(int1,int2,int3):
    aList = {int1,int2,int3}
    if(int1==min(aList)):
        return 0
    elif(int2==min(aList)):
        return 1
    else:
        return 2

def traceAlign(table,str1,str2,trace):
    j = 0
    i = 0
    if(len(str1)<len(str2)):
        for k in trace:
            if(i==len(str1)):
                i=i-1
            if(j==len(str2)):
                j=j-1
            if(k=='s1'):
                print (str1[i],'|',str2[j],'|',0)
                j=j+1
                i=i+1
            elif(k=='s2'):
                print ('_','|',str2[j],'|',1)
                j=j+1
            elif(k=='i'):
                print (str1[i],'|','_','|',2)
                i=i+1
            elif(k=='d'):
                print ('_','|',str2[j],'|',2)
                j=j+1

                
def minDistTrace(table,str1,str2):
    i = len(str1)-1
    j = len(str2)-1
    order = []
    dist = 0
    while ((i!=0)|(j!=0)):
        if(((table[j][i]==table[j-1][i-1]+1)&(table[j][i]==table[j][i-1]+2)) | ((table[j][i]==table[j-1][i-1])&(table[j][i]==table[j][i-1]+2))):
            
            dist1,trash = minDistTrace(table[0:j][0:i-1],str1[0:i-1],str2)
            trash,order1 = minDistTrace(table[0:j][0:i-1],str1[0:i-1],str2)

            dist2,trash = minDistTrace(table[0:j-1][0:i-1],str1[0:i-1],str2[0:j-1])
            trash,order2 = minDistTrace(table[0:j-1][0:i-1],str1[0:i-1],str2[0:j-1])

            if(dist1<dist2):
                dist = dist+dist1
                for k in order1:
                    order.append(k)
            else:
                dist = dist+dist2
                for k in order2:
                    order.append(k)
         if(((table[j][i]==table[j-1][i-1]+1)&(table[j][i]==table[j-1][i]+2))|((table[j][i]==table[j-1][i-1])&(table[j][i]==table[j-1][i]+2))):
            
            dist1,trash = minDistTrace(table[0:j-1][0:i],str1,str2[0:j-1])
            trash,order1 = minDistTrace(table[0:j-1][0:i],str1,str2[0:j-1])

            dist2,trash = minDistTrace(table[0:j-1][0:i-1],str1[0:i-1],str2[0:j-1])
            trash,order2 = minDistTrace(table[0:j-1][0:i-1],str1[0:i-1],str2[0:j-1])

            if(dist1<dist2):
                dist = dist+dist1
                for k in order1:
                    order.append(k)
            else:
                dist = dist+dist2
                for k in order2:
                    order.append(k)    









        switch(val):
            
        if(table[j][i]==table[j][i-1]+2):
            order.append('2')    
        elif(table[j][i]==table[j-1][i]+2):
            order.append('1')
        elif(table[j][i]==table[j-1][i-1]+1):
            order.append('X')
        elif(table[j][j]==table[j-1][i-1]):
            order.append('M')

def main():
    str1 = "ANTARCTICA"
    str2 = "ARCTIC"
    table,trace = minEditDist(str1,str2)
    for i in range(len(str2)+1):
        print (table[i])
    print('\n')
    print(trace)

    traceAlign(table,str1,str2,trace)

main()
    
