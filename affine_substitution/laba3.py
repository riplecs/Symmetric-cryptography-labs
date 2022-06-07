# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:34:14 2021

@author: RIPLECS
"""


from laba1 import bigrams_not_intersect, frequency, cleaning
import pandas as pd
import matplotlib.pyplot as plt

def Evklid(a, n):
    u0, u1 = 1, 0
    v0, v1 = 0, 1
    while n! = 0:
        q = a//n
        a, n = n, a%n
        u0, u1 = u1, u0 - q*u1
        v0, v1 = v1, v0 - q*v1
    return (a, u0, v0)

def inverted(a, n):
    r = Evklid(a, n)
    return r[1]%n

def congruence(a, b, n):
    d = inverted(a, n)[0]
    if d == 1:
        return (inverted(a, n)*b)%n
    elif b%d! = 0:
        return None
    else:
        a /= d
        b /= d
        n /= d
        x = (b*inverted(a, n))%n
        res = []
        for i in range(d):
            res.append(x + i*n)
        return res

def convert_bigram(bi):
    return (alph.index(bi[0])*m + alph.index(bi[1]))%(m**2)

def convert_text(txt):
    res = []
    for i in range(0, len(txt) - 1, 2):
        res.append(convert_bigram(txt[i] + txt[i + 1]))
    return res

def deconvert_bigram(num):
    x1 = int(num//m)
    x2 = int(num%m)
    return ''.join(i for i in [alph[x1], alph[x2]])

def deconvert_text(mas):
    res = []
    for i in range(len(mas)):
        res.append(deconvert_bigram(mas[i]))
    return ''.join(i for i in res)

def check_text(t):
    n = len(t)
    return frequency('ф', n, t) < 0.003 and frequency('щ', n, t) < 0.005;

    
def decipher(text, x, y):
    inv = inverted(x, m**2)
    result = []
    for t in text:
        result.append(inv*(t - y)%m**2))
    return deconvert_text(result)

def frequencies(mas):
    res = []
    for i in mas:
        res.append(frequency(i, len(ciphertext)/2, ciphertext))  
    return res

def print_bigrams(x, y, z, w):
    print(f'{deconvert_bigram(x)}->{deconvert_bigram(y)}')
    print(f'{deconvert_bigram(z)}->{deconvert_bigram(w)}')
    
def affin_bigramms(namefile):
    result = open(f'{namefile}.txt', 'w')
    keys, f, ch = [], [], []
    triger = False
    for i in range(0, 5):
        for j in range(0, 5):
            for k in range(0, 5):
                for l in range(0, 5):
                    if i == k or j == l:
                        continue
                    if triger:
                        break
                    x1 = convert_bigram(dfr['Біграма'][i])
                    y1 = convert_bigram(df['Біграма'][j])
                    x2 = convert_bigram(dfr['Біграма'][k])
                    y2 = convert_bigram(df['Біграма'][l])
                    a = congruence(x1-x2, y1-y2, m**2)
                    if a is None: 
                        continue
                    if not isinstance(a, list): 
                        a = list([a])
                    for el in a:
                        if el == 0:  
                            continue
                        b=(y1 - el*x1)%(m**2)
                        if (el, b) not in keys: 
                            keys.append((el, b))
                            text = decipher(ciphertext, el, b)
                            f.append(frequency('ф', len(text), text))
                            ch.append(frequency('щ', len(text), text))
                            if check_text(text):
                                print_bigrams(x1, y1, x2, y2)
                                result.write(f'({el}, {b})\n'+text)
                                triger = True
                                break    
    result.close()
    file = open('result.txt', 'r')
    for line in file:
        print(line)
    file.close()
    X = [i for i in range((max(len(f), len(ch))))]
    Y = [i for i in f]
    Z = [i for i in ch]
    fig, ax = plt.subplots()
    ax.plot(X, Y, Z)
    plt.show()
    
if __name__=='__main__':
    
    file = open('09.txt', 'r', encoding='UTF-8')
    ciphertext = cleaning(''.join(line for line in file)).replace(' ', '')
    bigrams = bigrams_not_intersect(ciphertext)
    freqs = frequencies(bigrams)
       
    df = pd.DataFrame({'Біграма' :[i for i in bigrams_not_intersect(ciphertext)], 
                     'Частота': [j for j in freqs]})
    df = df.sort_values(by = 'Частота', ascending = False, ignore_index = True)
    #print(df.set_index('Біграма')[:5])
    dfr = pd.DataFrame({'Біграма': ['ст', 'но', 'то', 'на', 'ен']})
    
    alph = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
    m = len(alph) 
    ciphertext = convert_text(ciphertext)  
    affin_bigramms('result')

    
    
    
    
    
    
    
    
    
    
