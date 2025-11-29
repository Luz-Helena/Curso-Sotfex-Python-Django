class Cachorro:
    def __init__(self,nome: str,cor: str) -> None:
        self.nome = nome
        self.cor = cor
        
    def latir(self, fala: str) -> None:
        print(f'{self.nome} diz: {fala}!')
    
meu_cachorro = Cachorro('Rex', 'preto')

meu_cachorro.latir('Au,Au!')

'''
nome e cor são atributos (variaveis) da class Cachorro
por isso não são chamadas parêntese: ()
print(meu_cachorro.nome)
print(meu_cachorro.cor)

'''