from fila_base import FilaBase


class FilaNormal(FilaBase):
    def __init__(self):
        super().__init__()

    def gerar_senha_atual(self) -> None:
        self.senha_atual = f"NM{self.codigo}"
