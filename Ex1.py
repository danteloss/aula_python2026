class Conta:
    def __init__(self, descricao, valor, vencimento, status="Não pago"):
        self.descricao = descricao
        self.valor = valor
        self.vencimento = vencimento
        self.status = status

def pagar(self):
    self.status = "Pago"

contas = []

while True:
    resp = int(input("Digite 1 para cadastrar, 2 para pagar, 3 para listar, 4 para sair: "))
    if resp == 1:
        desc = str(input("Digite o nome da conta: "))
        valor = float(input("Digite o valor: "))
        vencimento = str(input("Vencimento: "))
        nova_conta = Conta(desc, valor, vencimento)
        contas.append(nova_conta)
        print("Essa conta tem ID:", len(contas)-1)
    elif resp == 2:
        id_pgt = int(input("Digite o ID da conta: "))
        contas[id_pgt].pagar()
    elif resp == 3:
        for i in range(len(contas)):
            print(i, contas[i].descricao, contas[i].valor, contas[i].vencimento, contas[i].status)
    else:
        print("Finalizando...")
        break