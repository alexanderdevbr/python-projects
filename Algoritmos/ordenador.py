class Animal:

    def __init__(self):
        pass

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

obj1 = Animal()
obj1.setNome("Bob")
print(obj1.getNome())

lista = ['um', 'dois', 'tres']

for item in lista:
    print(item)

print("Tamanho: " + str(len(lista)))