class Veiculos:
    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


class Carro_ipva(Veiculos):
    def calcular_ipva(self):
        return self.valor * 0.04


class Moto_ipva(Veiculos):
    def calcular_ipva(self):
        return self.valor * 0.02


while True:
    print("Bem vindos ao menu para cadastro de Veículos e calculadora de IPVA!")
    print()
    opcao = int(input("O que deseja fazer?\n"
                      "1 - Cadastro de Carros\n"
                      "2 - Cadastro de Motos\n"
                      "3 - Sair\n"))

    if opcao == 1:
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        valor = float(input("Valor: "))
        carro = Carro_ipva(marca, modelo, ano, valor)
        print("Carro registrado, o IPVA a ser pago é: R$", carro.calcular_ipva())
        print()

    elif opcao == 2:
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        valor = float(input("Valor: "))
        moto = Moto_ipva(marca, modelo, ano, valor)
        print("Moto registrada, o IPVA a ser pago é: R$", moto.calcular_ipva())
        print()

    else:
        break