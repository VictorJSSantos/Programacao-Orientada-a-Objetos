class FilaBase:
    def __init__(self):
        self.codigo = 0
        self.fila = []
        self.clientes_atendidos = []
        self.senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1
