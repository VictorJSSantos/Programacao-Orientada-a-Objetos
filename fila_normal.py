from fila_base import FilaBase
from constants import FILA_NORMAL


class FilaNormal(FilaBase):
    def __init__(self):
        super().__init__()

    def gerar_senha_atual(self) -> None:
        self.senha_atual = f"{FILA_NORMAL}{self.codigo}"
