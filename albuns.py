import scrapy
import re

# Incluído a biblioteca de expresões regulares (re) para filtrar as informações da raspagem

class AlbunsSpider(scrapy.Spider):
    name = 'albuns'
    start_urls = ['https://rollingstone.uol.com.br/noticia/os-500-melhores-discos-de-todos-os-tempos-da-rolling-stone/']
    
    def parse(self, response):
        dados = response.css('p:nth-child(29)::text, p:nth-child(26)::text, p:nth-child(22)::text, p:nth-child(19)::text, p:nth-child(16)::text')
        
        for dado in dados:
            posicao = re.findall(r'(^\d+)', dado.get())
            artista = re.findall(r'(?<=-\s)[^,]+(?=,)', dado.get())
            album = re.findall(r'(?<=,\s)[^,]+(?=\s\()', dado.get())
            ano = re.findall(r'\([^\)]+\)', dado.get())
            yield {
                'posicao' : posicao,
                'artista' : artista,
                'album' : album,
                'ano': ano
            }

# Pra rodar: scrapy runspider albuns.py --nolog
# Pra gerar um arquivo: scrapy runspider albuns.py -O melhores_albuns.csv