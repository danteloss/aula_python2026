from abc import ABC, abstractmethod

class Mensagem(ABC):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    @abstractmethod
    def enviar(self):
        pass

class Email(Mensagem):
    def __init__(self, conteudo, destinatario):
        super().__init__(conteudo,)
        self.destinatario = destinatario

    def enviar(self):
        return f"Enviando email para {self.destinatario}: {self.conteudo}"

class Sms(Mensagem):
    def __init__(self, conteudo, numero_telefone):
        super().__init__(conteudo)
        self.numero_telefone = numero_telefone

    def enviar(self):
        return f"Enviando SMS para {self.numero_telefone}: {self.conteudo}"

while True:
    x = input("Este é o menu de emails e SMS's!\n"
              "1 - Enviar um email\n"
              "2 - Enviar um SMS\n"
              "3 - Sair.\n"
              "Opção: ")
    if x == "1":
        a = input("Informe o nome do email para enviar: ")
        b = input("Digite a mensagem para enviar: ")
        email1 = Email(b, a)
        print(email1.enviar())
        print("Enviado com sucesso!")

    elif x == "2":
        c = input("Informe o numero para enviar: ")
        d = input("Digite a mensagem para enviar: ")
        sms1 = Sms(d, c)
        print(sms1.enviar())
        print("Enviado com sucesso!")

    else:
        break



