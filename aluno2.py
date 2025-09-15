class Aluno:
    nome =""
    idade = 0

    def mostrarSituacao(self):
        if self.idade >=18:
            print(self.nome, "maior de idade")
        else:
            print(self.nome, "menor de idade")

a1 = Aluno()
a1.nome = "Diego"
a1.idade = 18

a1.mostrarSituacao()

a2 = Aluno()
a2.nome = "Gabriel Oliveira"
a2.idade = 16

a2.mostrarSituacao()

a3 = Aluno()
a3.nome = "Matheus Morais"
a3.idade = 16

a3.mostrarSituacao()

a4 = Aluno()
a4.nome = "Yamil"
a4.idade = 160

a4.mostrarSituacao()

a5 = Aluno()
a5.nome = "Luan"
a5.idade = 17

a5.mostrarSituacao()

a6 = Aluno()
a6.nome = "Leandro"
a6.idade = 16

a6.mostrarSituacao()


a7 = Aluno()
a7.nome = "Matheus Santos"
a7.idade = 17

a7.mostrarSituacao()

a8 = Aluno()
a8.nome = "Andrew"
a8.idade = 16

a8.mostrarSituacao()

a9 = Aluno()
a9.nome = "Jonathan"
a9.idade = 16

a9.mostrarSituacao()

a10 = Aluno()
a10.nome = "Matheus Aliaga"
a10.idade = 17

a10.mostrarSituacao()
