"""Exercise 02"""

#  Crie uma classe Projeto que deve ter como atributos o  codigo (número inteiro que representa o código do projeto), titulo e responsável (nome do professor responsável pelo projeto). Deve ser possível construir um objeto projeto a partir da string codigo, titulo, responsavel ex: 1,Laboratório de Desenvolvimento de Software,Pedro Gomes . Nenhum dos atributos pode ser vazio ou nulos (utilizar propriedades). Dois projetos podem ser considerados iguais caso tenham o mesmo codigo.

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @classmethod
    def from_string(cls, string):
        parts = [i.strip() for i in string.split(',')]
        if len(parts)<3:
            raise ValueError("String must contain exactly 3 parts: Código, Titulo, Rersponsável")
        codigo = int(parts[0])
        return cls(codigo, parts[1], parts[2])
        
    def __eq__(self, other):
        if not isinstance(other, Projeto):
            return NotImplemented
        return self.codigo == other.codigo
    
    @property
    def codigo(self):
        return self._codigo
    
    
    @codigo.setter
    def codigo(self, value):
        if not value and value != 0:
            raise ValueError("Código não pode ser vazio.")
        self._codigo = value


    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError("Titulo não pode ser vazio")
        self._titulo = value
        
    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if not value:
            raise ValueError("Responsável não pode ser vazio")
        self._responsavel = value

# Testando a classe Projeto
projeto1 = Projeto.from_string("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
projeto2 = Projeto.from_string("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
projeto3 = Projeto.from_string("2,Projeto de Pesquisa,João Silva")  

print(f"Projeto 1 == Projeto 2: {projeto1 == projeto2}")
print(f"Projeto 1 == Projeto 3: {projeto1 == projeto3}")
print(f"Projeto 1: {projeto1.codigo}, {projeto1.titulo}, {projeto1.responsavel}")
print(f"Projeto 2: {projeto2.codigo}, {projeto2.titulo}, {projeto2.responsavel}")
print(f"Projeto 3: {projeto3.codigo}, {projeto3.titulo }, {projeto3.responsavel}")
        