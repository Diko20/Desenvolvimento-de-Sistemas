# def cria funções (ou métodos dentro da classe)
class Animal:
    nome = ""
    espécie = "" 
    idade = 0

    def comer(self):
        print(" Ele está comendo ")

    def dormir(self):
        print(" Dormindo ")

    def andar(self):
        print(" Ele está andando ")


a1 = Animal()
a1.nome = "Ozzy"
a1.espécie = "Cachorro"
a1.idade = 5

a2 = Animal()
a2.nome = "Liten"
a2.espécie = "Gato"
a2.idade = 7

a3 = Animal()
a3.nome = "Bolinha"
a3.espécie = "hamster"
a3.idade = 2

a4 = Animal()
a4.nome = "Fubá"
a4.espécie = "Coelho"
a4.idade = 4

a5 = Animal()
a5.nome = "Loro"
a5.espécie = "Papagaio"
a5.idade = 3

c1