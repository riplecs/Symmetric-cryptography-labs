# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:38:02 2021

@author: RIPLECS
"""

from sympy import symbols, solve, Eq, sqrt
import time 
import math

    
p1=0.25
p2=0.5

t_λ=2.326347874

'''
f=open('z.txt', 'r')
z=f.read()
L1=(0, 3)
L2=(0, 1, 2, 6)
L3=(0, 1, 2, 5)
n1=25
n2=26
n3=27
t_β1=5.419983175
t_β2=5.542594058
t_β3=5.662697617
'''


z='01011101000101001000000010100000010001100011111111011110010001011000111000100101100111100011010001100101110001101100110010110110100010001101000101000010110101100001110101111011110000010001101111000110111100100101101100001011010011110010101111111100100100111100000000011110100000000011011011111101000010101011000110001110111011001011100100011000100110111111000101101000000111100001010011100011010110100011101111100001100011011000010011101100101000011111110010000001000111010000100000111001000101111101'
L1=(0, 2)
L2=(0, 1, 3, 4)
L3=(0, 3)
n1=11
n2=9
n3=10
t_β1=3.297193346
t_β2=2.885634912
t_β3=3.097269078


def lfsr(state, taps, n):
    it=1
    res=''
    inter=state
    while True:
        res+=inter[0]
        tail=0
        for i in taps:
            tail+=int(inter[i]) 
        inter=inter[1:]+str(tail%2)
        if inter==state:
            break
        it+=1
        if it>n: 
            break
    yield res

    
def Geffe(x0, y0, s0):
    res=''
    for state in lfsr(x0, L1, N1):
        x=state
    for state in lfsr(y0, L2, N2):
        y=state
    for state in lfsr(s0, L3, N3):
        s=state
    for i in range(min(len(x), len(y), len(s))):
        res=res+(x[i] if s[i]=='1' else y[i])
    return res[:len(z)]


def calculation(t_β):
    x, y = symbols('x, y')
    eq1=Eq(x*p1+t_λ*sqrt(x*p1*(1-p1))-y, 0.001)
    eq2=Eq((x*p2-y)/sqrt(x*p2*(1-p2))-t_β, 0.001)
    return solve([eq1, eq2], [x, y])[1]


def R(vec, c):
    res=0
    for i in range(min(len(vec), len(z))):
        res+=(int(vec[i])+int(z[i]))%2
    if res>c:
        return False
    else:
        return True
 

def find_states(n, N, C, L):
    v=(n-1)*'0'+'1'
    for state in lfsr(v, L, math.inf):
        state0=state
    candidates=[]
    for i in range(len(state0)-int(N)):
        s=state0[i:int(N)+i]
        check=R(s, C)
        if check is True:
            candidates.append(s[:n])
    return candidates


def Next_Vector(vect):
    n=len(vect)
    if vect.count('0')==0:
        return n*'0'
    elif vect[-1]=='0':
        return vect[:n-1]+'1'
    else:
        i, k=-1, 0
        while vect[i]!='0':
            i-=1
            k+=1
        return vect[:n-k-1]+'1'+'0'*k
    

def find_l3(n, l1, l2):
    v='0'*(n-1)+'1'
    check=False
    while check is False:
        for i in l1:
            for j in l2:
                G=Geffe(i, j, v)
                check=R(G, 1)
                if check is True:
                    return i, j, v
                    break
        v=Next_Vector(v)
                
            
start_time = time.time() 


N1, C1 = calculation(t_β1)
N2, C2 = calculation(t_β2)
N3, C3 = calculation(t_β3)


candidates1=find_states(n1, N1, C1, L1)
candidates2=find_states(n2, N2, C2, L2)


       
print(find_l3(n3, candidates1, candidates2))
print("--- %s seconds ---" % (time.time() - start_time))

