from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

fila_teste = FilaNormal()

fila_teste.atualizafila()
fila_teste.atualizafila()
fila_teste.atualizafila()
print(fila_teste.chamar_cliente(5))
print(fila_teste.chamar_cliente(10))

fila_teste2 = FilaPrioritaria()
fila_teste2.atualizafila()
fila_teste2.atualizafila()
fila_teste2.atualizafila()
fila_teste2.atualizafila()
print(fila_teste2.chamar_cliente(2))
print(fila_teste2.estatistica("Quarta-feira", "1504", "detail"))