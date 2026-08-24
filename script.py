class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Vendedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10

class Gestor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15

func1 = Funcionario(nome="Dante", salario=1000)
print(func1.nome, func1.salario)

vend1 = Vendedor(nome="Maria", salario=1000)
print(vend1.nome, vend1.salario, vend1.calcular_bonus())

gest1 = Gestor(nome="Kleber", salario=1000)
print(gest1.nome, gest1.salario, gest1.calcular_bonus())
