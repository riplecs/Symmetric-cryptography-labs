# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:34:14 2021

@author: RIPLECS
"""


from laba1 import bigrams_not_intersect, frequency, cleaning
import pandas as pd

def Evklid(a, n):
    if n==0: return a, 1, 0
    else: d, u, v = inverted(n, a%n)
    return  d, v, u -int(a/n)*v

def inverted(a, n):
    r=Evklid(a, n)
    return r[1]%n

def congruence(a, b, n):
    d=inverted(a, n)[0]
    if d==1:
        return (inverted(a, n)*b)%n
    elif b%d!=0:
        return None
    else:
        a=a/d
        b=b/d
        n=n/d
        x=(b*inverted(a, n))%n
        res=[]
        for i in range(d):
            res.append(x+i*n)
        return res

def convert_bigram(bi):
    return (alph.index(bi[0])*m+alph.index(bi[1]))%(m**2)

def convert_text(txt):
    res=[]
    for i in range(0, len(txt)-1, 2):
        res.append(convert_bigram(txt[i]+txt[i+1]))
    return res

def deconvert_bigram(num):
    x1=int(num//m)
    x2=int(num%m)
    return ''.join(i for i in [alph[x1], alph[x2]])

def deconvert_text(mas):
    res=[]
    for i in range(len(mas)):
        res.append(deconvert_bigram(mas[i]))
    return ''.join(i for i in res)


'''
forbiden=['аь', 'оь', 'уь', 'кь', 'хь', 'оы', 'еь', 'ьы']

def check_text(t):
    c=0
    for i in forbiden:
        if t.find(i)==-1:
            c=c+1
    if c==len(forbiden): 
        if t.count('ф')/len(t)<0.0025:
            return True
        else:
            return False 
    else:
        return False
'''

def check_text(t):
    n=len(t)
    if t.count('ф')/n<0.004:
        return True
    else:
        return False 
def affin_bigramms():
    result=open('result.txt', 'w')
    keys=[]
    triger=False
    for i in range(0, 5):
        for j in range(0, 5):
            for k in range(0, 5):
                for l in range(0, 5):
                    if i==k or j==l:
                        continue
                    if triger is True:
                        break
                    x1=convert_bigram(dfr['Біграма'][i])
                    y1=convert_bigram(df['Біграма'][j])
                    x2=convert_bigram(dfr['Біграма'][k])
                    y2=convert_bigram(df['Біграма'][l])
                    a=congruence(x1-x2, y1-y2, m**2)
                    if a is None: 
                        continue
                    elif isinstance(a, list) is True: 
                        for el in a:
                            if el==0: 
                                continue
                            b=(y1-el*x1)%(m**2)
                            if (el, b) not in keys: 
                                keys.append((el, b))
                                res=[]
                                for t in ciphertext:
                                    res.append((inverted(el, m**2)*(t-b))%(m**2))
                                text=deconvert_text(res)
                                if check_text(text) is True:
                                    result.write(f'({el}, {b})\n'+deconvert_text(res))
                                    triger=True
                                    break
                    else:
                        if a==0: 
                            continue
                        b=(y1-a*x1)%(m**2)
                        if (a, b) not in keys: 
                            keys.append((a, b))
                            res=[]
                            for t in ciphertext:
                                res.append((inverted(a, m**2)*(t-b))%(m**2))
                            text=deconvert_text(res)
                            if check_text(text) is True: 
                                result.write(f'({a}, {b})\n'+ deconvert_text(res))
                                triger=True
                                break
                        
    result.close()
    file=open('result.txt', 'r')
    for line in file:
        print(line)
    file.close()
    
if __name__=='__main__':
    
    file=open('09.txt', 'r', encoding='UTF-8')
    ciphertext=cleaning(''.join(line for line in file)).replace(' ', '')
    bigrams=bigrams_not_intersect(ciphertext)
    
    freqs=[]
    for i in bigrams:
        freqs.append(frequency(i, len(ciphertext)/2, ciphertext))  
       
    df=pd.DataFrame({'Біграма' :[i for i in bigrams_not_intersect(ciphertext)], 
                     'Частота': [j for j in freqs]})
    df=df.sort_values(by='Частота', ascending = False, ignore_index=True)
    dfr=pd.DataFrame({'Біграма': ['ст', 'но', 'то', 'на', 'ен']})
    
    alph='абвгдежзийклмнопрстуфхцчшщьыэюя'
    m=len(alph) 
    ciphertext=convert_text(ciphertext)  
    affin_bigramms()

    
    
    
    
    
    
    
    
    
    
