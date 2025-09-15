class Aluno:
    nome =""
    nota = 0

    def mostrarSituacao(self):
        if self.nota >=5:
            print(self.nome, "foi aprovado")
        else:
            print(self.nome, "foi reprovado")

a1 = Aluno()
a1.nome = "Diego"
a1.nota = 3

a1.mostrarSituacao()

a2 = Aluno()
a2.nome = "Gabriel"
a2.nota = 6

a2.mostrarSituacao()

a3 = Aluno()
a3.nome = "Morais"
a3.nota = 9.5

a3.mostrarSituacao()

a4 = Aluno()
a4.nome = "Yamil"
a4.nota = 5

a4.mostrarSituacao()

a5 = Aluno()
a5.nome = "Luan"
a5.nota = 4

a5.mostrarSituacao()

a6 = Aluno()
a6.nome = "Leandro"
a6.nota = 3

a6.mostrarSituacao()

a7 = Aluno()
a7.nome = "Matheus Santos"
a7.nota = -10000

a7.mostrarSituacao()