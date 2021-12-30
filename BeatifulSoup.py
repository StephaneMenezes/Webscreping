import requests
from bs4 import BeautifulSoup
import pandas as pd 

lista_noticias = []

resposta = requests.get('https://g1.globo.com/')                                #Adicionando uma Url 

content = resposta.content                                     

site = BeautifulSoup(content, 'html.parser')                           #Tranformando para p type Beatifulsoup 


#HTML da noticia
noticias = site.findAll ('div', attrs = {'class':'feed-post-body'})    #Selecionando uma div especifica   #find PROCURA UM ITEM COM ESSE NOME O findAll PROCURA TODOS OS ITENS 

#print(noticias)                                                       #Olhando o div de forma organizada

print("**************PRINT DAS NÓTICIAS DO G1 ********************")   
for noticia in noticias:                                               #Trazendo todos os links da página utilizando o for 
# pegando um pedaço especifico no caso o titulo 
    titulo = noticia.find('a', attrs={'class':'feed-post-link'})
    print(titulo.text)                                                 #Selecionando apenas o texto da tag a 
    print()
    print(titulo['href'])                                              #Trazendo também o link das nóticias
    print()

    subtitulo = noticia.find('div', attrs={'class':'feed-post-body-resumo'})
    if (subtitulo):
     print(subtitulo.text)
     lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else: 
        lista_noticias.append([titulo.text, ' ', titulo['href']])
news=pd.DataFrame(lista_noticias, columns=["Título", "Subtítulo","Link"])    #Criando uma lista com os dados

news.to_csv('noticias.xlsx', index=False)                                    #Criando um arquivo um csv (excel), o index falso é para não salvar a numeração. 
