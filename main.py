from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

fila_teste = FilaNormal()

fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chamar_cliente(5))
print(fila_teste.chamar_cliente(10))

fila_teste2 = FilaPrioritaria()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chamar_cliente(2))
print(fila_teste2.estatistica("Quarta-feira", "1504", "detail"))
