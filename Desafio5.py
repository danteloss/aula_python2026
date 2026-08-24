class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

    def descricao(self):
        return f"Aluno {self.nome}, idade {self.idade}, matricula {self.matricula} e curso {self.curso}"

class Professor(Pessoa):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina

    def descricao1(self):
        return f"Professor {self.nome}, idade {self.idade}, salario {self.salario}, disciplina {self.disciplina}"

aluno1 = Aluno("Dante", 18, "G202", "CDD")
prof1 = Professor("Octavio", 34, "15000", "CDD")

print(aluno1.descricao())
print(prof1.descricao1())


