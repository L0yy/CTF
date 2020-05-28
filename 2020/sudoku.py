
import numpy as np
sum = 0
outstr = ""

def scanf():
    S = []
    dusoku = "006000900010602030400050008070000080004000300080000090700010063030408010009000800"
    for i in range(len(dusoku)):
        S = S+list(dusoku[i])
    for i in S:
        d = S.index(i)
        S[d] = int(i)
    print('=== Orignal ===\n',np.array(S).reshape(9,9))
    return S


class blank:
    def __init__(self,row,column,block,rangelist):
        self.row = row              # 行（0-8）
        self.column = column        # 列（0-8）
        self.block = block          # 宫（0-8）
        self.rangelist = rangelist  # 该空白区取值范围


def S_orignal(S):
    R = [[],[],[],[],[],[],[],[],[]]
    C = [[],[],[],[],[],[],[],[],[]]
    B = [[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        for j in range(9):
            if S[i,j]!= 0:
                R[i].append(S[i,j])
                C[j].append(S[i,j])
                if i<3 and j<3:
                    B[0].append(S[i,j])
                elif i<3 and j<6:
                    B[1].append(S[i,j])
                elif i<3 and j>=6:
                    B[2].append(S[i,j])
                elif i<6 and j<3:
                    B[3].append(S[i,j])
                elif i<6 and j<6:
                    B[4].append(S[i,j])
                elif i<6 and j>=6:
                    B[5].append(S[i,j])
                elif i>=6 and j<3:
                    B[6].append(S[i,j])
                elif i>=6 and j<6:
                    B[7].append(S[i,j])
                else:
                    B[8].append(S[i,j])
    return R,C,B


def Blank_orignal(S,R,C,B):                   # 获取空白区域初始化信息
    BLANK = []
    for i in range(9):
        for j in range(9):
            if S[i,j]== 0:
                if i<3 and j<3:
                    b=0
                elif i<3 and j<6:
                    b=1
                elif i<3 and j>=6:
                    b=2
                elif i<6 and j<3:
                    b=3
                elif i<6 and j<6:
                    b=4
                elif i<6 and j>=6:
                    b=5
                elif i>=6 and j<3:
                    b=6
                elif i>=6 and j<6:
                    b=7
                else:
                    b=8
                rd = [1,2,3,4,5,6,7,8,9]
                for k in R[i]:
                    if k in rd:
                        rd.remove(k)
                for k in C[j]:
                    if k in rd:
                        rd.remove(k)
                for k in B[b]:
                    if k in rd:
                        rd.remove(k)
                b0 = blank(i,j,b,rd)
                BLANK.append(b0)
    BLANK.sort(key = lambda l : len(l.rangelist))
    return BLANK

def check(S,R,C,B,BLANK):         # 检查是否有错误填充值
    for i in R:
        if len(set(i))!=len(i):
            return 3
    for i in C:
        if len(set(i))!=len(i):
            return 5
    for i in B:
        if len(set(i))!=len(i):
            return 7
    for i in BLANK:
        if len(i.rangelist)==0:
            return 9
    return 1


def start(S):
    
    global sum,outstr
    R,C,B = S_orignal(np.array(S).reshape(9,9))
    BLANK = Blank_orignal(np.array(S).reshape(9,9),R,C,B)
    if check(S,R,C,B,BLANK) != 1:
        return 0
    if BLANK == []:
        sum+=1
        b = str(S).replace(", ","")[1:-1]
        outstr += b
        outstr += "\n"
        
        #print(np.array(S).reshape(9,9))
        return 0
    else:
        b = BLANK[0]
        if len(b.rangelist) == 1:
            S[(9*b.row)+b.column] = b.rangelist[0]
            
            return start(S)
        elif len(b.rangelist) > 1:
            S1 = list(S)
            for j in b.rangelist: 
                S[(9*b.row)+b.column] = j
                
                if start(S) == 0:
                    S = S1
            return 0


S = scanf()
R,C,B = S_orignal(np.array(S).reshape(9,9))
BLANK = Blank_orignal(np.array(S).reshape(9,9),R,C,B)
if check(S,R,C,B,BLANK) == 1:
    start(S)
    f = open ("solver.csv","w") 
    f.write(outstr)
    f.close()
    print("已将结果放入solver.csv中\n解法:",sum)
else:
    print('=== No Solution! ===')

