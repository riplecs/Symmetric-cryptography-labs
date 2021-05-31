# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:38:02 2021

@author: RIPLECS
"""

from sympy import symbols, solve, Eq, sqrt
import numpy as np

p1=0.25
p2=0.5

t_λ=2.326347874

f=open('z.txt', 'r')
z=[int(i) for i in f.read()]

L1=[0, 3]
L2=[0, 1, 2, 6]
L3=[0, 1, 2, 5]
n1=25
n2=26
n3=27
t_β1=5.419983175
t_β2=5.542594058
t_β3=5.662697617


def lfsr(state, taps, n):
    it=0
    res=[]
    state0=state
    while it<n:
        res+=[state[0]]
        state=state[1:]+[sum(state[i] for i in taps)%2]
        if state==state0:
            break
        it+=1
    return res


def Geffe(x0, y0, s0, k1, k2, k3):
    res=[]
    x=lfsr(x0, L1, k1)
    y=lfsr(y0, L2, k2)
    s=lfsr(s0, L3, k3)
    for i in range(min(k1, k2, k3)):
        res=res+[x[i] if s[i]==1 else y[i]]
    return res


def Statistic_R(vec, c):
    res=0
    for i in range(len(vec)):
        res+=(vec[i]+z[i])%2
    if res>c:
        return False
    else:
        return True
    
    
def find_states(n, N, C, L):
    v=(n-1)*[0]+[1]
    state0=lfsr(v, L, 2**n-1)
    candidates=[]
    for i in range(len(state0)-N):
        s=state0[i:N+i]
        if Statistic_R(s, C) is True:
            candidates.append(s[:n])
    return candidates


def Next_Vector(vect):
    n=len(vect)
    if vect[-1]==0:
        return vect[:n-1]+[1]
    else:
        i, k=-1, 0
        while vect[i]!=0:
            i-=1
            k+=1
        return vect[:n-k-1]+[1]+k*[0]
    
    
def find_l3(n, l1, l2):
    #v=[0]*(n-1)+[1]
    v=[0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0]
    while True:
        if v[1]!=1 or v[7]!=1 or v[8]!=1 or v[10]!=1 or v[17]!=1 or v[24]!=1 or v[25]!=1:
            v=Next_Vector(v)
        for i in l1:
            for j in l2:
                if Statistic_R(Geffe(i, j, v, n1, n2, n3), 0) is True:
                    if Statistic_R(Geffe(i, j, v, N1, N2, N3), 0) is True:
                        return i, j, v
                        break
        v=Next_Vector(v)
        
        
def calculation(t_β):
    x, y = symbols('x, y')
    eq1=Eq(x*p1+t_λ*sqrt(x*p1*(1-p1))-y, 0.001)
    eq2=Eq((x*p2-y)/sqrt(x*p2*(1-p2))-t_β, 0.001)
    return solve([eq1, eq2], [x, y])[1]


N1, C1 = (int(i) for i in calculation(t_β1))
N2, C2 = (int(i) for i in calculation(t_β2))
N3, C3 = (int(i) for i in calculation(t_β3))
'''
candidates1=[[1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
             [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
             [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
             [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
             [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
             [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]]

candidates2=[[0,1,0,0,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,1]]
'''

candidates1=find_states(n1, N1, C1, L1)
candidates2=find_states(n2, N2, C2, L2)
print(find_l3(n3, candidates1, candidates2))

