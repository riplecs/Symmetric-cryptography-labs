# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:20:29 2021

@author: RIPLECS
"""

cipher_text=open('2.txt', 'r', encoding='UTF-8')
textt=''
for line in cipher_text:
    textt=textt+line
    
def cleaning(text):
    sign=" .,&!?/\|#@-—()[]–{};:…%«»\n'1234567890jvi"
    for i in sign:
        if i in text:
            text=text.replace(i, '')
    return text.replace('"', '')

text=cleaning(textt.lower())
print(textt)
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

r=input('Введите ключ: ')
print(convert(Vigenere(r, text)))
