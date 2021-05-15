# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:38:02 2021

@author: RIPLECS
"""
import numpy as np
import math
from sympy import symbols, solve, Eq, sqrt
    
f=open('z.txt', 'r')
z=f.read()

L1=(0, 3)
L2=(0, 1, 2, 6)
L3=(0, 1, 2, 5)

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

def Giffi(x0, y0, s0):
    res=''
    for state in lfsr(x0, L1, math.inf):
        x=state
    for state in lfsr(y0, L2, math.inf):
        y=state
    for state in lfsr(s0, L3, math.inf):
        s=state
    for i in range(min(len(x), len(y), len(s))):
        res=res+(x[i] if s[i]=='1' else y[i])
    return res[:len(z)]


p1=0.25
p2=0.5
t_λ=2.326347874
x, y = symbols('x, y')
#C=N*p1+t_λ*math.sqrt(N*p1*(1-p1))
#t_β=(N*p2-C)/math.sqrt(N*p2*(1-p2))


t_β=5.419983175
eq1=Eq(x*p1+t_λ*sqrt(x*p1*(1-p1))-y, 0.001)
eq2=Eq((x*p2-y)/sqrt(x*p2*(1-p2))-t_β, 0.001)
N1, C1 = solve([eq1, eq2], [x, y])[1]

t_β=5.542594058
eq1=Eq(x*p1+t_λ*sqrt(x*p1*(1-p1))-y, 0.001)
eq2=Eq((x*p2-y)/sqrt(x*p2*(1-p2))-t_β, 0.001)
N2, C2 = solve([eq1, eq2], [x, y])[1]


def R(vec, c):
    res=0
    for i in range(min(len(vec), len(z))):
        res+=(int(vec[i])+int(z[i]))%2
    if res>c:
        return False
    else:
        return True
 
def bin_array(N):
    return (np.arange(1<<N)[:, None] >> np.arange(N)[::-1]) & 0b1

def find_states(n, N, C, L):
    v=(n-1)*'0'+'1'
    for state in lfsr(v, L, math.inf):
        state0=state
    check=R(state0, C)
    candidates=[]
    for i in range(len(state0)-int(N)):
        check=R(state0[i:int(N)+i], C)
        if check is True:
            candidates.append(state0[i:int(N)+i][:n])
    return candidates

candidates1=find_states(25, N1, C1, L1)
candidates2=find_states(26, N2, C2, L2)

def find_l3(n, l1, l2):
    vectors = bin_array(n)
    for i in l1:
        for j in l2:
            for v in vectors[1:]:
                v=str(v)
                G=Giffi(i, j, v[1:len(v)-1:2])
                check=R(G[:len(z)], 1)
                if check is True:
                    return i, j, v[1:len(v)-1:2]
                
print(find_l3(27, candidates1, candidates2))

