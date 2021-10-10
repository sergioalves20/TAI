import pandas as pd
import numpy as np
from uteis import uteis


uteis.titulo (2, 'CÁLCULO DO VALOR ACRESCIDO DA TAXA ANUAL DE INFLAÇÃO')
print ('\033[33mDADOS DISPONÍVEIS\033[m: ENTRE O ANO 2000 E 2016')
print ('\033[33mFONTE\033[m: Instituto Nacional de Estatística de Cabo Verde (INEcv)\033[m')
print ('')

while True:
    print (uteis.dados ())
    resp = ' '
    while resp not in 'SN':
        resp = str (input ('\033[31mDeseja continuar? [s/n]\033[m')).strip ().upper ()[0]
    if resp == 'N':
        print ('\033[35mFIM DA CONSULTA!\033[m')
        break
