from bs4 import BeautifulSoup

class Crawler:
    def obter_links_personagens(self, html_index: str) -> list[str]:
        soup = BeautifulSoup(html_index, 'html.parser')
        links = []
        for a in soup.select('.entry-content a[href*="/personagens/"]'):
            links.append(a['href'])
        return links
