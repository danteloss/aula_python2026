import logging

logging.basicConfig(filename="arquivo_log.log",
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def calcular(c, d):
    try:
        total = c * d
        logging.debug(f"Cálculo do pedido: {c} x {d} = {total}")
        return total
    except:
        logging.error("Erro durante o processamento dos dados")
        return 0


logging.info("Início do programa")

print("Sistema de processamento de pedidos.")
a = input("1 - Quem é o cliente? ")
b = input("2 - Qual o produto comprado? ")
c = int(input("3 - Qual a quantidade de produto? "))
d = float(input("4 - Qual o valor unitário do produto? "))

logging.debug(f"Dados do pedido: cliente={a}, produto={b}, quantidade={c}, valor={d}")

if c <= 0:
    logging.warning("Quantidade igual a zero ou valor negativo")
    print("Pedido inválido.")
else:
    total = calcular(c, d)
    print(f"O total do pedido de {a} é R$ {total}")
    logging.info("Pedido processado com sucesso")

logging.info("Encerramento do programa")