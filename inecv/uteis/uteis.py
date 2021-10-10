import pandas as pd
import numpy as np


def leiaint(msg):
    while True:
        try:
            ano = int (input (msg))
        except(ValueError, TypeError):
            print ('ERRO: digite um numero inteiro válido')
            continue
        except KeyboardInterrupt:
            print ('\nInterrompido.')
            return 0
        else:
            return ano


def leiafloat(msg):
    while True:
        try:
            preco = float (input (msg))
        except(ValueError, TypeError):
            print ('ERRO: digite um numero inteiro ou decimal')
            continue
        except KeyboardInterrupt:
            print ('\nInterrompido.')
            return 0
        else:
            return preco


c = ('\033[m',  # 0 - Sem cor
     '\033[30m',  # 1 - Branco
     '\033[31m',  # 2 - Vermelho
     '\033[32m',  # 3 - Verde
     '\033[33m',  # 4 - Amarelo
     '\033[34m',  # 5 - Azul
     '\033[35m',  # 6 - Roxo
     '\033[36m',  # 7 - Magenta
     '\033[37m')  # 8 - Cinza


def linha(tam=0, cor=0):
    print (c[cor], '-' * tam)


def titulo(cor=0, msg=''):
    tam = len (msg)
    linha (tam, 5)
    print (c[cor], msg)
    linha (tam, 5, )
    print ('\033[m')


def dados():
    # Importa o excel com o ano e a taxa de inflação anual
    df = pd.read_excel ('inecv/taxacv.xlsx', engine='openpyxl')

    # Altera o nome das 2 colunas
    df.rename (columns={'ano': 'Ano', 'taxa': 'Taxa'}, inplace=True)

    # Calcula e cria uma coluna 'Fator Conv.' (Fator de Conversão)
    df['Fator Conv.'] = 1 + df['Taxa'] / 100

    df = df.set_index ('Ano')

    df = df.loc[leiaint ('\033[036mDigite o ano de referência do preço [1990/2016]:\033[m '):]

    # Regista numa variável o valor a calcular e valida a operação
    preco = leiafloat ('\033[036mDigite o valor inteiro ou decimal a calcular:\033[m ')
    print ('')

    # Cria uma coluna 'Novo Valor' com valores nulos
    df['Novo Valor'] = np.nan

    # Anexa o Valor solicitado
    df['Novo Valor'] = preco

    pd.set_option ('display.precision', 2)
    # Calcula e anexa o Novo Valor
    df['Novo Valor'] = df['Novo Valor'] * df['Fator Conv.'].cumprod ()

    # Substitui os valores nulos pelo Novo Valor
    df['Novo Valor'] = df['Novo Valor'].ffill ()

    return df
