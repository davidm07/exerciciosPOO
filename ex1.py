class BichinhoVirtual():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
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
            return f"{self.nome} está Triste"
        elif self.saude == 0:
            return f"{self.nome} está Doente"
        else:
            return f"{self.nome} está Feliz"
        

bicho1 = BichinhoVirtual("Rolandinho", 0, 0, 10)

bicho1.set_saude(10)

bicho1.set_fome(10)

print(bicho1.humor())