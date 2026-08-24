class Aluno:
    def __init__(self, nome, nota):
        self._nome = nome
        self._aprovado = False
        self.nota = nota

    @property
    def nome(self):
        return self._nome

    @property
    def aprovado(self):
        return self._aprovado

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("Nota não valida")
        self._nota = nota
        if nota >= 6:
            self._aprovado = True
        else:
            self._aprovado = False


c = Aluno("Dante", 10)
print(c.nome, c.nota, c.aprovado)




