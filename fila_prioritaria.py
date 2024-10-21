from fila_normal import FilaNormal


class FilaPrioritaria(FilaNormal):
    def __init__(self):
        super().__init__()

    def gerar_senha_atual(self) -> None:
        self.senha_atual = f"PR{self.codigo}"

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
