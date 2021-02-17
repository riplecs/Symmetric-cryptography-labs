# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:20:29 2021

@author: RIPLECS
"""

from laba1 import cleaning
from collections import Counter
import pandas as pd

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
    for i in sorted(d)[-2:]:
        res.append(d.index(i))
    return res 

def split_text(text, key):
    res=key*[0]
    for i in range(key):
        res[i]=[''.join(j for j in text[i:len(text):key])]
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

def find_key_1(text):
    res=[]
    for i in range(len(text)):
        txt=''.join(text[i])
        g=0
        while g<m:
            el=0
            for t in range(0, m):
                el=el+txt.count(convert([(t+g)%m]))*float(df[df['Літера']==f'{convert([t])}']['Частота'])
            g=g+1
            res.append([i, g, el])
    result=[res[i:i+m] for i in range(0, len(res), m)]
    res=[]
    for i in result:
        res.append(max(i[k][2] for k in range(m)))
    fin=[]
    for i in result:
        for k in range(m):
            if i[k][2] in res:
                fin.append(convert([i[k][1]-1]))
    return ''.join(fin)

def deVigenere(r, text):
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
            j[k]=(j[k]-(numerate(r))[k])%m
            k=k+1
    fin=[]
    for i in range(len(res)): fin=fin+res[i]
    return fin

if __name__=='__main__':
    
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

    r2='ад'
    print(f'r = {r2}\n', convert(Vigenere(r2, text)))
    r3='рай'
    print(f'r = {r3}\n', convert(Vigenere(r3, text)))
    r4='свет'
    print(f'r = {r4}\n', convert(Vigenere(r4, text)))
    r5='жизнь'
    print(f'r = {r5}\n', convert(Vigenere(r5, text)))
    r13='темноецарство'
    print(f'r = {r13}\n', convert(Vigenere(r13, text)))
    r24='лучиксветавтемномцарстве'
    print(f'r = {r24}\n', convert(Vigenere(r24, text)))
    file=open('катерина_шифр.txt', 'w', encoding='UTF-8')

    keys=[r2, r3, r4, r5, r13, r24]
    for r in keys:
        file.write(r + '\n' + convert(Vigenere(r, text)) + '\n')
    file.close() 

    print('I_r2 = ', conformity(convert(Vigenere(r2, text))))
    print('I_r3 = ', conformity(convert(Vigenere(r3, text))))
    print('I_r4 = ', conformity(convert(Vigenere(r4, text))))
    print('I_r5 = ', conformity(convert(Vigenere(r5, text))))
    print('I_r13 = ', conformity(convert(Vigenere(r13, text))))
    print('I_r24 = ', conformity(convert(Vigenere(r24, text))))

    decipher_text=open('вар9.txt', 'r', encoding='UTF-8')
    text=''
    for line in decipher_text:
        text=text+line
    text=cleaning(text)
    print(text)
    
    length=statistics(text)
    print(length)
    k=length[1]
    
    r=convert(find_key(max_count(split_text(text, k))))
    print('key = ', r)

    df=pd.read_csv('frequency_letters.csv', delimiter=',', encoding='UTF-8')
    
    key=find_key_1(split_text(text, k))
    print('key = ', key)
    
    print(convert(deVigenere(key, text)))
    f=open('вар9_дешифр.txt', 'w', encoding='UTF-8')
    f.write(key + '\n' + convert(deVigenere(key, text)))
    f.close()

