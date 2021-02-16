# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:20:29 2021

@author: RIPLECS
"""

from laba1 import cleaning
from collections import Counter
import math
import pandas as pd

cipher_text=open('катерина.txt', 'r', encoding='UTF-8')
textt=''
for line in cipher_text:
    textt=textt+line
    

text=cleaning(textt.lower())
print(text)

a=ord('а')
alph=''.join(chr(i) for i in range(a, a+32))
#alph='абвгдежзийклмнопрстуфхцчшщъыьэюя'
m=len(alph)

def numerate(string):
    chars=[]
    for i in string:
        chars.append(alph.index(i))
    return chars

def convert(string):
    res=[]
    for i in string:
        res.append(alph[int(i)])
    return ''.join(res)
        

def parcer(obj, n):
    args = [iter(obj)] * n
    return zip(*args)

def Vigenere(r, text):
    if len(text)%len(r)==0:
        for i in range(0, len(text), len(r)):
            mas=[''.join(j) for j in parcer(text, len(r))]
    else: 
        mas=[''.join(j) for j in parcer(text, len(r))]
        mas.append(text[(len(text)-len(text)%len(r)):])
    res=[]
    for i in mas: res.append(numerate(i))
    for j in res:
        k=0
        while k<len(j):
            j[k]=(j[k]+(numerate(r))[k])%m
            k=k+1
    fin=[]
    for i in range(len(res)):
        fin=fin+res[i]
    return fin


def conformity(text):
    n=len(text)
    res=0
    for i in range(len(alph)):
        res=res+text.count(alph[i])*(text.count(alph[i])-1)
    return res/(n*(n-1))

r2='ад'
#print(f'r = {r2}\n', convert(Vigenere(r2, text)))
r3='рай'
#print(f'r = {r3}\n', convert(Vigenere(r3, text)))
r4='свет'
#print(f'r = {r4}\n', convert(Vigenere(r4, text)))
r5='жизнь'
print(f'r = {r5}\n', convert(Vigenere(r5, text)))
r13='темноецарство'
#print(f'r = {r13}\n', convert(Vigenere(r13, text)))
r24='лучиксветавтемномцарстве'
#print(f'r = {r24}\n', convert(Vigenere(r24, text)))


#print('I_r2 = ', conformity(convert(Vigenere(r2, text))))
#print('I_r3 = ', conformity(convert(Vigenere(r3, text))))
#print('I_r4 = ', conformity(convert(Vigenere(r4, text))))
#print('I_r5 = ', conformity(convert(Vigenere(r5, text))))
#print('I_r13 = ', conformity(convert(Vigenere(r13, text))))
#print('I_r24 = ', conformity(convert(Vigenere(r24, text))))


##################################################################
def Kronecker(a, b):
    if a==b: return 1
    else: return 0
    
def statistics(text):
    d=[0, 0]
    r=2
    while r<30:
        el=0
        for j in range(1, len(text)-r):
            el=el+Kronecker(text[j], text[j+r])
        d.append(el)
        r=r+1
    res=[]
    print(d)
    for i in sorted(d)[-2:]:
        res.append(d.index(i))
    return res 

def split_text(text, key):
    res=key*[0]
    for i in range(key):
        res[i]=[''.join(j for j in text[i:len(text):key])]
    return res
    

def max_count(mas):
    res=[]
    for i in mas:
        res.append(Counter(''.join(i)).most_common(1).pop(0)[0])
    return res

print(max_count(split_text(text, 13)))
x='т'
def find_key(length, mas):
    res=[]
    for i in mas:
        res.append((alph.index(i)+alph.index(x))%m)
    return res
