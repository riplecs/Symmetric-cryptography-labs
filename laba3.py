# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:34:14 2021

@author: RIPLECS
"""


from laba1 import bigrams_not_intersect, frequency, cleaning
import pandas as pd

def inverted(a, n):
    if n==0: return a, 1, 0
    else: d, u, v = inverted(n, a%n)
    return  d, v, u -int(a/n)*v

def congruence(a, b, n):
    d=inverted(a, n)[0]
    if d==1:
        return ((inverted(a, n)[1]%n)*b)%n
    elif b%d!=0:
        return None
    else:
        a=a/d
        b=b/d
        n=n/d
        x=(b*(inverted(a, n)[1]%n))%n
        res=[]
        for i in range(d):
            res.append(x+i*n)
        return res


file=open('V9.txt', 'r', encoding='UTF-8')
ciphertext=''
ciphertext=cleaning(''.join(line for line in file))
bigrams=bigrams_not_intersect(ciphertext)
freqs=[]
for i in bigrams:
    freqs.append(frequency(i, len(ciphertext)/2, ciphertext))
    
print('Біграми шифротексту: ')
df=pd.DataFrame({'Біграма' :[i for i in bigrams_not_intersect(ciphertext)], 'Частота': [j for j in freqs]})
print(df.sort_values(by='Частота', ascending = False, ignore_index=True)[0:5].set_index('Біграма'))
print('Біграми російскьої мови: ')
dfr=pd.read_csv('frequencynoncrossbigramms.csv', delimiter=',', encoding='UTF-8')
print(dfr[0:5]. set_index('Біграма'))
alph='абвгдежзийклмнопрстуфхцчшщыьэюя'
m=len(alph)
 
def convert_bigram(bi):
    return (alph.index(bi[0])*m+alph.index(bi[1]))%(m**2)

def deconvert_bigram(num):
    x1=int(num//m)
    x2=int(num%m)
    return ''.join(i for i in [alph[x1], alph[x2]])

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
