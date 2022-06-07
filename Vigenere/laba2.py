# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:20:29 2021

@author: RIPLECS
"""

from laba1 import cleaning
from collections import Counter
import pandas as pd

def numerate(string):
    chars = []
    for i in string:
        chars.append(alph.index(i))
    return chars

def convert(string):
    res = []
    for i in string:
        res.append(alph[int(i)])
    return ''.join(res)

def parcer(obj, n):
    args = [iter(obj)]*n
    return zip(*args)

def Vigenere(r, text):
    if len(text)%len(r) == 0:
        for i in range(0, len(text), len(r)):
            mas = [''.join(j) for j in parcer(text, len(r))]
    else: 
        mas = [''.join(j) for j in parcer(text, len(r))]
        mas.append(text[(len(text)-len(text)%len(r)):])
    res = []
    for i in mas: 
        res.append(numerate(i))
    for j in res:
        k = 0
        while k < len(j):
            j[k] = (j[k]+numerate(r)[k])%m
            k += 1
    fin = []
    for i in range(len(res)):
        fin += res[i]
    return fin


def conformity(text):
    n = len(text)
    res = 0
    for i in range(len(alph)):
        res += text.count(alph[i])*(text.count(alph[i]) - 1)
    return res/(n*(n - 1))


def Kronecker(a, b):
    if a == b: 
        return 1
    return 0
    
def statistics(text):
    d = [0, 0]
    for r in range(2, 40):
        el = 0
        for j in range(1, len(text) - r):
            el += Kronecker(text[j], text[j + r])
        d.append(el)
    df = pd.DataFrame({'Ключ': [i for i in range(2, 40)],
                     'Статистика збігів': [j for j in d[2:]]})
    print(df.set_index('Ключ'))
    fig, ax = plt.subplots()
    ax.plot([i for i in range(2, 40)], d[2:])
    ax.set_xlabel('Ключ')
    ax.set_ylabel('Статистика збігів')
    plt.show()
    res = []
    for i in sorted(d)[-3:]:
        res.append(d.index(i))
    for i in range(len(res)):
        k = len(res)
        if np.gcd(res[i], res[(i + 1)%k]) == np.gcd(res[i], res[(i+2)%k]) == 1:
            del res[i]
        else: 
            return np.min(res)
    return np.min(res)

def split_text(text, key):
    res = key*[0]
    for i in range(key):
        res[i] = [''.join(j for j in text[i:len(text):key])]
    return res

def max_count(mas):
    res = []
    for i in mas:
        res.append(Counter(''.join(i)).most_common(1).pop(0)[0])
    return res

x = 'о'
def find_key(mas):
    res = []
    for i in mas:
        res.append((alph.index(i) - alph.index(x))%m)
    return res

def find_key_1(text):
    res = []
    for i in range(len(text)):
        txt = ''.join(text[i])
        g = 0
        while g < m:
            el = 0
            for t in range(0, m):
                l = convert([(t+g)%m])
                fr = float(df[df['Літера'] == f'{convert([t])}']['Частота'])
                el += txt.count(l)*fr
            g += 1
            res.append([i, g, el])
    result = [res[i:i+m] for i in range(0, len(res), m)]
    res = []
    for i in result:
        res.append(max(i[k][2] for k in range(m)))
    fin = []
    for i in result:
        for k in range(m):
            if i[k][2] in res:
                fin.append(convert([i[k][1] - 1]))
    return ''.join(fin)

def deVigenere(r, text):
    if len(text)%len(r) == 0:
        for i in range(0, len(text), len(r)):
            mas = [''.join(j) for j in parcer(text, len(r))]
    else: 
        mas = [''.join(j) for j in parcer(text, len(r))]
        mas.append(text[(len(text)-len(text)%len(r)):])
    res = []
    for i in mas: 
        res.append(numerate(i))
    for j in res:
        k = 0
        while k < len(j):
            j[k] = (j[k] - (numerate(r))[k])%m
            k += 1
    fin = []
    for i in range(len(res)): 
        fin += res[i]
    return fin

if __name__=='__main__':
    
    cipher_text = open('катерина.txt', 'r', encoding='UTF-8')
    textt = ''
    for line in cipher_text:
        textt += line
    
    text = cleaning(textt.lower())
    print(text)

    a = ord('а')
    alph = ''.join(chr(i) for i in range(a, a + 32))
    #alph='абвгдежзийклмнопрстуфхцчшщъыьэюя'
    m = len(alph)

    r2 = 'ад'
    print(f'r = {r2}\n', convert(Vigenere(r2, text)))
    r3 = 'рай'
    print(f'r = {r3}\n', convert(Vigenere(r3, text)))
    r4 = 'свет'
    print(f'r = {r4}\n', convert(Vigenere(r4, text)))
    r5 = 'жизнь'
    print(f'r = {r5}\n', convert(Vigenere(r5, text)))
    r13 = 'темноецарство'
    print(f'r = {r13}\n', convert(Vigenere(r13, text)))
    r24 = 'лучиксветавтемномцарстве'
    print(f'r = {r24}\n', convert(Vigenere(r24, text)))
    file = open('катерина_шифр.txt', 'w', encoding='UTF-8')

    keys = [r2, r3, r4, r5, r13, r24]
    for r in keys:
        file.write(r + '\n' + convert(Vigenere(r, text)) + '\n')
    file.close() 

    print('I_r2 = ', conformity(convert(Vigenere(r2, text))))
    print('I_r3 = ', conformity(convert(Vigenere(r3, text))))
    print('I_r4 = ', conformity(convert(Vigenere(r4, text))))
    print('I_r5 = ', conformity(convert(Vigenere(r5, text))))
    print('I_r13 = ', conformity(convert(Vigenere(r13, text))))
    print('I_r24 = ', conformity(convert(Vigenere(r24, text))))
    
    X = [len(i) for i in keys]
    Y = [conformity(convert(Vigenere(j, text))) for j in keys]
    fig, ax = plt.subplots()
    ax.plot(X, Y, marker='o')
    fig.size=(8, 4)
    ax.set_xlabel('Ключ')
    ax.set_ylabel('Індекс відповідності')
    ax.grid(True)
    plt.show()
    
    df = pd.DataFrame({'Ключ':[i for i in X],
                'Індекс відповідності':[j for j in Y]})
    print(df.set_index('Ключ'))
    
    decipher_text = open('вар9.txt', 'r', encoding = 'UTF-8')
    text = ''
    for line in decipher_text:
        text += line
    text = cleaning(text)
    print(text)
    
    length = statistics(text)
    k = length
    
    r = convert(find_key(max_count(split_text(text, k))))
    print('key = ', r)

    df = pd.read_csv('frequency_letters.csv', delimiter = ',', encoding = 'UTF-8')
    
    key = find_key_1(split_text(text, k))
    print('key = ', key)
    
    print(convert(deVigenere(key, text)))
    f = open('вар9_дешифр.txt', 'w', encoding = 'UTF-8')
    f.write(key + '\n' + convert(deVigenere(key, text)))
    f.close()

