from fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    def __init__(self):
        super().__init__()

    def gerar_senha_atual(self) -> None:
        self.senha_atual = f"PR{self.codigo}"

    def atualizafila(self) -> None:
        self.reseta_fila()
        self.gerar_senha_atual()
        self.fila.append(self.senha_atual)

    def chamar_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente atual {cliente_atual} dirija-se ao caixa {caixa}."

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
