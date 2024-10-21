from fila_base import FilaBase
from constants import FILA_PRIORITARIA


class FilaPrioritaria(FilaBase):
    def __init__(self):
        super().__init__()

    def gerar_senha_atual(self) -> None:
        self.senha_atual = f"{FILA_PRIORITARIA}{self.codigo}"

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != "detail":
            estatistica = {f"{agencia} - {dia}: {len(self.clientes_atendidos)}"}
        else:
            estatistica = {}
            estatistica["dia"] = dia
            estatistica["agencia"] = agencia
            estatistica["clientes_atendidos"] = self.clientes_atendidos
            estatistica["qtde_clientes_atendidos"] = len(self.clientes_atendidos)

        return estatistica
