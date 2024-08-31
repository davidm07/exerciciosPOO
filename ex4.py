import random

class BichinhoVirtualPlus:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = 100
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def set_fome(self, fome):
        self.fome = fome
    
    def get_fome(self):
        return self.fome
    
    def set_saude(self, saude):
        self.saude = saude

    def get_saude(self):
        return self.saude
    
    def set_idade(self, idade):
        self.idade = idade
    
    def get_idade(self):
        return self.idade
    
    def humor(self):
        if self.fome == 0 and self.saude == 0:
            return f"{self.nome} está Morrendo"
        elif self.fome == 0:
            return f"{self.nome} está Faminto"
        elif self.saude == 0:
            return f"{self.nome} está Doente"
        else:
            return f"{self.nome} está Feliz"
    
    def brincar(self, tempo):
        self.tedio = max(0, self.tedio - tempo)

        if self.tedio > 50:
            return f"{self.nome} está entediado"
        elif self.tedio <= 50 and self.tedio > 0:
            return f"{self.nome} está começando a se divertir"
        elif self.tedio == 0:
            return f"{self.nome} não está mais entediado e não pode mais brincar"
        
    def alimentar(self, quantidade):
        self.fome = max(0, self.fome - quantidade)

    def __str__(self):
        return (f"Nome: {self.nome}, Fome: {self.fome}, "
                f"Saúde: {self.saude}, Idade: {self.idade}, "
                f"Tédio: {self.tedio}")

def criar_fazenda(quantidade):
    fazenda = []
    for x in range(quantidade):
        nome = input("Nome do bichinho: ")
        fome_inicial = random.randint(0, 100)
        saude_inicial = random.randint(0, 100)
        idade = 0
        bichinho = BichinhoVirtualPlus(nome, fome_inicial, saude_inicial, idade)
        fazenda.append(bichinho)
    return fazenda
        

def menu_fazenda(fazenda):
    while True:
        print("\n--- Menu Fazenda de Bichinhos ---")
        print("1. Alimentar todos os bichinhos")
        print("2. Brincar com todos os bichinhos")
        print("3. Ver humor de todos os bichinhos")
        print("4. Mostrar detalhes de todos os bichinhos")
        print("5. Sair")

        op = int(input("Escolha uma opção: "))

        if op == 1:
            quantidade = int(input("Quanto de alimento deseja fornecer? "))
            for bichinho in fazenda:
                bichinho.alimentar(quantidade)
            print("Bichinhos alimentados com sucesso!")
        elif op == 2:
            tempo = int(input("Quanto tempo deseja brincar? "))
            for bichinho in fazenda:
                print(bichinho.brincar(tempo))
        elif op == 3:
            for bichinho in fazenda:
                print(bichinho.humor())
        elif op == 4:
            for bichinho in fazenda:
                print(bichinho)
        elif op == 5:
            break
        else:  
            print("Opção inválida. Tente novamente.")

fazenda = criar_fazenda(3)
menu_fazenda(fazenda)
