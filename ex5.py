class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = list()

    def comer(self, alimento):
        if isinstance(alimento, Alimento):
            self.bucho.append(alimento)
        elif isinstance(alimento, Macaco):
            self.bucho.append(alimento)
        else:
            raise ValueError("O alimento deve ser uma instância da classe Alimento ou Macaco")

    def get_bucho(self):
        if not self.bucho:
            return f'O macaco {self.nome} está com o estômago vazio'
        
        itens = []
        for item in self.bucho:
            if isinstance(item, Alimento):
                itens.append(item.get_nome())
            elif isinstance(item, Macaco):
                itens.append(f'{item.nome} (macaco)')
        
        return f'O macaco {self.nome} está com {", ".join(itens)} no estômago'

    def digerir(self):
        self.bucho.clear()

    def __str__(self):
        return f'Nome: {self.nome}'

class Alimento:
    def __init__(self, nome):
        self.nome = nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

godzilla = Macaco('Godzilla')
king_kong = Macaco('King Kong')
banana = Alimento('banana')

godzilla.comer(banana)
godzilla.comer(king_kong)

print(godzilla.get_bucho())
