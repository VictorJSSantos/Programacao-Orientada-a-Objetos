import abc

from constants import *


class FilaBase(metaclass=abc.ABCMeta):
    def __init__(self):
        self.codigo = 0
        self.fila = []
        self.clientes_atendidos = []
        self.senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= POSICAO_MAXIMA_NA_FILA:
            self.codigo = POSICAO_INICIAL_NA_FILA
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gerar_senha_atual()
        self.fila.append(self.senha_atual)

    def chamar_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente atual {cliente_atual} dirija-se ao caixa {caixa}."

    @abc.abstractmethod
    def gerar_senha_atual(self): ...
