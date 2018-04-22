class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    henrique = Pessoa(nome='Henrique')
    edmundo = Pessoa(henrique, nome='Edmundo')
    print(Pessoa.cumprimentar(edmundo))
    print(id(edmundo))
    print(edmundo.cumprimentar())
    print(edmundo.nome)
    print(edmundo.idade)
    for filho in edmundo.filhos:
        print(filho.nome)

















