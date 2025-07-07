from bs4 import BeautifulSoup
import re

class Scraper:
    def normalizar_chave(self, chave: str) -> str:
        chave = chave.lower()
        chave = re.sub(r"[^\w\s]", "", chave)
        chave = re.sub(r"\s+", "_", chave)
        return chave.strip("_")

    def parse_personagem(self, html: str) -> dict:
        soup = BeautifulSoup(html, 'html.parser')
        div_page = soup.find_all("p")[1]
        ems = soup.find_all("em")
        nome = div_page.get_text(strip=True) if div_page else 'NOME NÃO ENCONTRADO'

        data = {"nome": nome}

        for i in ems:
            partes = i.text.split(":")
            if len(partes) == 2:
                chave, valor = partes
                chave = self.normalizar_chave(chave.strip())
                data[chave] = valor.strip()

        return data
