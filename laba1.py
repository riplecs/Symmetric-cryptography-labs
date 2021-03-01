# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 21:18:08 2021

@author: RIPLECS
"""

import math
import pandas as pd


pd.set_option('display.max_rows', 100)


def cleaning(text):
    sign=" .,&!?/\|#@-—()[]–{};:…%«»\n'1234567890jvi"
    for i in sign:
        if i in text:
            text=text.replace(i, '')
    return text.replace('"', '')


def alphabet(text):
    abc=[]
    for i in range(len(text)):
        if text[i] not in abc:
            abc.append(text[i])
    return abc

def count_cros_bi(text, f):
    i = 0
    count = 0
    while i != -1:
        i = text.find(f)
        if i >= 0: count = count + 1
        text = text[i+1:]
    return count

def count_noncros_bi(text, f):
    c=0
    k=len(text)
    for i in range(0, k-1, 2):
        if text[i]+text[(i+1)]==f:
            c=c+1
    return c

def frequency(a, n, text):
    if n==len(text): return text.count(a)/n
    if n==len(text)/2: return count_noncros_bi(text, a)/n
    else: return count_cros_bi(text, a)/n


def bigrams_intersect(text):
    res=[]
    for i in range(len(text)-1):
        if text[i]+text[i+1] not in res:
            res.append(text[i]+text[i+1])
    return res

def bigrams_not_intersect(text):
    res=[]
    i=0
    while i < len(text)-1:
        if text[i]+text[i+1] not in res:
            res.append(text[i]+text[i+1])
        i=i+2
    return res

def entropy(n, frq, mas):
    res=0
    for i in range(len(mas)):
        res=res-frq[i]*math.log2(frq[i])
    return res/n


if __name__=='__main__':
    
    cipher_text_0=open('textee.txt', 'r', encoding='UTF-8')
    cipher_text=''
    for line in cipher_text_0:
        cipher_text=cipher_text+line
    cipher_text=cipher_text.lower()
    cipher_text=cleaning(cipher_text)
    
    alp=alphabet(cipher_text)
    
    bi_in=bigrams_intersect(cipher_text)
    bi_not_in=bigrams_not_intersect(cipher_text)
    n=len(cipher_text)
    print('Частоти літер: ')
    freq_l=[]
    for i in range(len(alp)):
        freq_l.append(frequency(alp[i], n, cipher_text))
    df=pd.DataFrame({'Літера': [i for i in alp] ,
                     'Частота': [i for i in freq_l]})
    df=df.sort_values(by='Частота', ignore_index=True, ascending=False)
    df.to_csv('frequency_letters.csv', encoding='UTF-8', index=False)
    print(df.set_index('Літера'))
    
    print('Частоти усіх біграм: ')
    freq_b=[]
    for i in range(len(bi_in)):
        freq_b.append(frequency(bi_in[i], n-1, cipher_text))
    df=pd.DataFrame({'Біграма': [i for i in bi_in], 
                     'Частота': [i for i in freq_b]})
    df=df.sort_values(by='Частота', ignore_index=True, ascending=False)
    df.to_csv('frequency_cross_bigramms.csv', encoding='UTF-8', index=False)
    print(df.set_index('Біграма'))

    print('Частоти біграм, що не перетинаются: ')
    freq_b_n=[]
    for i in range(len(bi_not_in)):
        freq_b_n.append(frequency(bi_not_in[i], n/2, cipher_text))
    df=pd.DataFrame({'Біграма': [i for i in bi_not_in], 
                     'Частота': [i for i in freq_b_n]})
    df=df.sort_values(by='Частота', ignore_index=True, ascending=False)
    df.to_csv('frequency_noncross_bigramms.csv', encoding='UTF-8', index=False)
    print(df.set_index('Біграма'))

    print(f'Питома ентропія на символ: ', entropy(1, freq_l, alp))
    print(f'Питома ентропія на символ біграми:  ', entropy(2, freq_b, bi_in))
    print(f'Питома ентропія на символ біграми, що не перетиняються:  ', entropy(2, freq_b_n, bi_not_in))
    H_0=math.log2(len(alp))
    H_10=(1.9571012893219+2.68527943900685)/2
    H_20=(1.28396862434949+1.98664532347824)/2
    H_30=(1.24794818862794+1.76056922372768)/2
    print('Надлишковість російської мови R(H_10) = ', 1-H_10/H_0)
    print('Надлишковість російської мови R(H_20) = ', 1-H_20/H_0)
    print('Надлишковість російської мови R(H_30) = ', 1-H_30/H_0)
