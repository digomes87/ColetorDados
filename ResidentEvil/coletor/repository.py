import csv
from pathlib import Path

class CSVRepository:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.campos = ["nome", "ano_de_nascimento", "tipo_sanguineo", "altura", "peso"]

    def salvar(self, dados: dict):
        is_novo = not self.file_path.exists()
        with self.file_path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.campos)
            if is_novo:
                writer.writeheader()
            writer.writerow({chave: dados.get(chave, "") for chave in self.campos})
