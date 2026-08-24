class Ingresso:
    def __init__(self, evento, preco):
        self.evento = evento
        self.preco = preco

    def __str__(self):
        return f"{self.evento} - R$ {self.calcular_preco()}"

    def __repr__(self):
        return f"Ingresso({self.evento} - R$ {self.calcular_preco()})"


class IngressoInteiro(Ingresso):
    def calcular_preco(self):
        return self.preco


class MeiaEntrada(Ingresso):
    def calcular_preco(self):
        return self.preco * 0.5


print("Ingressos para o Show do Coldplay - R$ 100")
print("1 - Inteira")
print("2 - Meia")
opcao = input("Opção: ")

if opcao == "1":
    ingresso = IngressoInteiro("Show do Coldplay", 100)
else:
    ingresso = MeiaEntrada("Show do Coldplay", 100)

print("Comprado:", ingresso)