class Entrega:
    def __init__(self, distancia, peso):
        self.distancia = distancia
        self.peso = peso


class EntregaComum(Entrega):
    def calcular_frete(self):
        return self.distancia * 2.00 + self.peso * 1.00


class EntregaExpressa(Entrega):
    def calcular_frete(self):
        return self.distancia * 3.50 + self.peso * 2.00 + 10.00


while True:
    print("Bem vindos ao sistema de entregas!")
    print()
    opcao = int(input("O que deseja fazer?\n"
                      "1 - Entrega Comum\n"
                      "2 - Entrega Expressa\n"
                      "3 - Sair\n"))

    if opcao == 1:
        distancia = float(input("Distância (km): "))
        peso = float(input("Peso (kg): "))
        entrega = EntregaComum(distancia, peso)
        print("Entrega comum registrada, o frete é: R$", entrega.calcular_frete())
        print()

    elif opcao == 2:
        distancia = float(input("Distância (km): "))
        peso = float(input("Peso (kg): "))
        entrega = EntregaExpressa(distancia, peso)
        print("Entrega expressa registrada, o frete é: R$", entrega.calcular_frete())
        print()

    else:
        break