from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    @abstractmethod
    def calcular_ipva(self):
        pass

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, valor, portas):
        super().__init__(marca, modelo, ano, valor)
        self.portas = portas

    def calcular_ipva(self):
        return self.valor*0.04

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, valor, cilindrada):
        super().__init__(marca, modelo, ano, valor)
        self.cilindrada = cilindrada

    def calcular_ipva(self):
        return self.valor*0.02

carro1 = Carro("Volks", "Nivus", 2024, 120000, 4)
moto1 = Moto("Honda", "Bros", 2023, 20000, 200)
veic1 = Veiculo("Marca","Modelo",2000,1000)

print(carro1.calcular_ipva())
print(moto1.calcular_ipva())