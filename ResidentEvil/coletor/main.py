from coletor.http_client import HttpClient
from coletor.scraper import Scraper
from coletor.crawler import Crawler
from coletor.analyzer import Analyzer
from coletor.repository import CSVRepository
from coletor.config import HEADERS, URL_INDEX

def main():
    client = HttpClient(headers=HEADERS)
    crawler = Crawler()
    scraper = Scraper()
    analyzer = Analyzer()
    repo = CSVRepository("saida.csv")

    print("Coletando índice de personagens...")
    html_index = client.get(URL_INDEX)
    links = crawler.obter_links_personagens(html_index)

    print(f"{len(links)} personagens encontrados.")

    for url in links:
        print(f"🔎 Coletando: {url}")
        try:
            html = client.get(url)
            dados = scraper.parse_personagem(html)
            dados = analyzer.analisar(dados)
            repo.salvar(dados)
        except Exception as e:
            print(f"Erro ao coletar {url}: {e}")

if __name__ == "__main__":
    main()
