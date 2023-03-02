# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:10:07 2023

@author: Manoel
"""

'''Problema 2
'''


def fibonacci(n):    #Função que calcula o n-ésimo valor da sequência de Fibonacci e retorna uma lista com a sequência até o n-ésimo valor
    
    fib = []
    if n == 0 : fib.append(0)
    if n == 1 : 
        fib.append(0)
        fib.append(1)
    anterior = 0
    atual = 1
    if n > 1:
        fib.append(anterior)
        fib.append(atual)
    
    for i in range(1,n):
        prox = atual + anterior
        fib.append(prox)
        anterior = atual
        atual = prox
        
    return fib

def prob2(m):     #Função que verifica se um dado número m está ou não na sequência de Fibonacci
    
    if m <= 5:
        fib = fibonacci(5)
        if m in fib:
            valor = True
        else: valor = False
        
    else:
        fib = fibonacci(m)
        if m in fib:
            valor = True
        else:
            valor = False
    
    if valor == True : print("O número",m,"está na sequência de Fibonacci.")
    else : print("O número",m,"não está na sequência de Fibonacci.")
        
'''Problema 3
'''

import json

def prob3():

    d = open('dados.json')
    
    dados = json.load(d) 
    
    menor = dados[0].get('valor')
    maior = dados[0].get('valor')
    dias = []
    total = 0
    cont = 0
        
    for i in range(0,len(dados)):
        if dados[i].get('valor') != 0:
    
            total += dados[i].get('valor')
            cont += 1
            
            if dados[i].get('valor') < menor:
                menor = dados[i].get('valor')
            
            if dados[i].get('valor') >  maior:
                maior = dados[i].get('valor')
    
    media = total/cont
    
    for j in range(0,len(dados)):
        if dados[j].get('valor') > media:
            dias.append(dados[j].get('dia'))
            
    return menor, maior, dias
    
def prob4(dados):      #Função que calcula os percentuais do faturamento mensal dados pelo problema
    
    sp = dados['São Paulo']
    rj = dados['Rio de Janeiro']
    mg = dados['Minas Gerais']
    es = dados['Espírito Santo']
    out = dados['Outros']
    
    total = sp + rj + mg + es + out
    
    sao = sp/total * 100
    rio = rj/total * 100
    minas = mg/total * 100
    esp = es/total * 100
    outs = out/total * 100
    
    print("Os percentuais de São Paulo, Rio de Janeiro, Minas Gerais, Espírito Santo e Outros são,respectivamente,",sao,",",rio,",",minas,",",esp,",",outs,".")
    

def prob5(strn):    #Inverte os caracteres da palavra dada "strn"
    
    a = len(strn)
    nova = ""
    while a > 0:
        nova += strn[a-1]
        a = a-1
        
    return nova
    
    

    
def main():
    
    #Transformei os valores dos estados em um dicionário para ser possível uma mudança nos valores dos faturamentos dos estados e a função continuar funcionando
    
    estados = {'São Paulo': 67836.43, 'Rio de Janeiro' : 36678.66, 'Minas Gerais' : 29229.88,
               'Espírito Santo' : 27165.48, 'Outros' : 19849.53}
    
    prob2(int(input("Insira um número natural ")))
    
    a,b,c = prob3()
    print("\nO menor valor de faturamento no mês foi",a,"\nO maior valor de faturamento no mês foi",b)
    print("Os dias em que o faturamento foi superior à média mensal foram",c,"\n")

    prob4(estados)

    palavra = prob5(input("Digite uma ou mais palavras "))
    print(palavra)



    
main()
