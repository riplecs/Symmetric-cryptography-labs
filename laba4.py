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

L1=(0, 2)
L2=(0, 1, 3, 4)
L3=(0, 3)

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
    for state in lfsr(x0, L1, math.inf):
        x=int(state, base=2)
    for state in lfsr(y0, L2, math.inf):
        y=int(state, base=2)
    for state in lfsr(s0, L3, math.inf):
        s=int(state, base=2)
    z=(x&s)^(y& (~s))
    return bin(z)


p1=0.25
p2=0.5
t_λ=2.326347874
#β=1/2**25
t_β=5.41998
#C=N*p1+t_λ*math.sqrt(N*p1*(1-p1))
#t_β=(N*p2-C)/math.sqrt(N*p2*(1-p2))


x, y = symbols('x, y')
eq1=Eq(x*p1+t_λ*sqrt(x*p1*(1-p1))-y, 0.001)
eq2=Eq((x*p2-y)/sqrt(x*p2*(1-p2))-t_β, 0.001)
N1, C1 = solve([eq1, eq2], [x, y])[1]
print(N1, C1)

β=1/2**26
t_β=5.54259
eq1=Eq(x*p1+t_λ*sqrt(x*p1*(1-p1))-y, 0.001)
eq2=Eq((x*p2-y)/sqrt(x*p2*(1-p2))-t_β, 0.001)
N2, C2 = solve([eq1, eq2], [x, y])[1]
print(N2, C2)


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

v=10*'0'+'1'
N=int(N1)
for state in lfsr(v, L1, math.inf):
    state0=state
check=R(state0, math.floor(C1))
candidates1=[]
for i in range(len(state0)-N):
    check=R(state0[i:N+i], math.floor(C1))
    if check is True:
        candidates1.append(state0[i:N+i][:11])
print(candidates1)

v=8*'0'+'1'
N=int(N2)
for state in lfsr(v, L2, math.inf):
    state0=state
check=R(state0, math.floor(C2))
candidates2=[]
for i in range(len(state0)-N):
    check=R(state0[i:N+i], math.floor(C2))
    if check is True:
        candidates2.append(state0[i:N+i][:9])
print(candidates2)

vectors = bin_array(10)

check=R(Giffi(candidates1[1], candidates2[0], 9*'0'+'1')[2:], 1)
i=0
for v in vectors:
    v=str(v)
    G=Giffi(candidates1[1], candidates2[0], v[1:len(v)-1:2])
    print(f'{i}) ', G[:20])
    i+=1
    check=R(G[2:], 1)
    if check is True:
        print(v[1:len(v)-1:2])
        print('---------------------------------------')


