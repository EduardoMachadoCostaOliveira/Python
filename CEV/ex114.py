# Crie um codigo em Python que teste se o site Pudim
# está acessivel pelo computador usado

import urllib
import urllib.request
try:
    s = urllib.request.urlopen('http://www.pudim.com.br')
except (urllib.error.URLError):
    print('O site Pudim não esta acessivel.')
else:
    print('Consegui acessar o site Pudim com sucesso!')

# s = urllib.request.urlopen('http://www.pudim.com.br')
# print(s)