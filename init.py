# Script Criad Por Cyber Root | Cyber Intelligence 
from __future__ import with_statement   
import codecs
url=input("Digite o Nome de Dominio: "); url.upper
ext=input("Digite a Extensão, por Exemplo '.com.br': ")
alfarusso_a="а" ; alfarusso_o="о" ;alfarusso_e="е" ;r=0 ;achou=False
original=url
while r<len(url):
    if url[r]=="A" or url[r]=="a":
        url[r]=alfarusso_a
        achou=True
    elif url[r]=="O" or url[r]=="o":
        url[r]=alfarusso_o
        achou=True
    elif url[r]=="E" or url[r]=="e":
        url[r]=alfarusso_e
        achou=True
        break
    r=r+1
if achou==False:
    print("String Nao Pode Ser MOdificada","\U0001F40D")
    print(url)
else:
    print("Url Modificada com Sucesso")
    print("==================================================")
    print("URL Original: "+original+ext)
    print("Url Modificada: "+url+ext)
    print("==================================================")
    print("By: Cyber Root | Cyber Intelligence")
    



