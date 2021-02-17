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


def frequency(a, text):
    return text.count(a)/len(text)


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


def entropy(n, text):
    res=0
    if n==1:
        for i in range(len(alp)):
            res=res-freq_l[i]*math.log2(freq_l[i])
    else:
        for i in range(len(bi_in)):
            res=res-freq_b[i]*math.log2(freq_b[i])
        res=res/n
    return res 


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
    
    print('Частоти літер: ')
    freq_l=[]
    for i in range(len(alp)):
        freq_l.append(frequency(alp[i], cipher_text))
    df=pd.DataFrame({'Літера': [i for i in alp] ,'Частота': [i for i in freq_l]})
    df.to_csv('frequency.csv', encoding='UTF-8', index=False)
    print(df.sort_values(by='Частота', ignore_index=True, ascending=False).set_index('Літера'))
    
    print('Частоти усіх біграм: ')
    freq_b=[]
    for i in range(len(bi_in)):
        freq_b.append(frequency(bi_in[i], cipher_text))
    df=pd.DataFrame({'Біграма': [i for i in bi_in], 'Частота': [i for i in freq_b]})
    df.to_csv('frequency_cross_bigramms.csv', encoding='UTF-8', index=False)
    print(df.sort_values(by='Частота', ignore_index=True, ascending=False).set_index('Біграма'))


    print('Частоти біграм, що не перетинаются: ')
    freq_b_n=[]
    for i in range(len(bi_not_in)):
        freq_b_n.append(frequency(bi_not_in[i], cipher_text))
    df=pd.DataFrame({'Біграма': [i for i in bi_not_in], 'Частота': [i for i in freq_b_n]})
    df.to_csv('frequency_noncross_bigramms.csv', encoding='UTF-8', index=False)
    print(df.sort_values(by='Частота', ignore_index=True, ascending=False).set_index('Біграма'))
    

    print(f'Питома ентропія на символ: ', entropy(1, cipher_text))
    print(f'Питома ентропія на символ біграми:  ', entropy(2, cipher_text))
        H_0=math.log2(len(alp))
    H_10=(1.9571012893219+2.68527943900685)/2
    H_20=(1.28396862434949+1.98664532347824)/2
    H_30=(1.24794818862794+1.76056922372768)/2
    print('Надлишковість російської мови R(H_10) = ', 1-H_10/H_0)
    print('Надлишковість російської мови R(H_20) = ', 1-H_20/H_0)
    print('Надлишковість російської мови R(H_30) = ', 1-H_30/H_0)
