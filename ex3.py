class BichinhoVirtualPlus():
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
        
    def alimentar(self):
        quantidade = int(input("Em quanto deseja alimentar? "))
        self.fome += quantidade

    def __str__(self):
        return (f"Nome: {self.nome}, Fome: {self.fome}, "
                f"Saúde: {self.saude}, Idade: {self.idade}, "
                f"Tédio: {self.tedio}")



bichinho1= BichinhoVirtualPlus("Rolandinho", 0, 10, 10)

print(bichinho1.humor())
bichinho1.alimentar()
print(bichinho1.humor())

print(bichinho1.brincar(10))
print(bichinho1.brincar(20))
print(bichinho1.brincar(50))
print(bichinho1.brincar(30))

opcao_secreta = input("Digite a palavra chave: ")
if opcao_secreta == "mostrar":
    print(bichinho1)

