class Math:

    @staticmethod
    def add5(x):  # nao acede nada, apenas é uma funcao dentro de um bloco de função
        return x + 5

print(Math.add5(3))  # we can use dot notation in the class because it is a static method