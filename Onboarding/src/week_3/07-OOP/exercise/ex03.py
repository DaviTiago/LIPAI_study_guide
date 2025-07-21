"""Exercise 03"""

# Crie uma classe Participacao que deve ter como atributos codigo, data inicio, data fim, aluno e o projeto associado.

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @classmethod
    def from_string(cls, string):
        parts = [i.strip() for i in string.split(',')]
        if len(parts) != 5:
            raise ValueError("String must contain exactly 5 parts: codigo, data_inicio, data_fim, aluno, projeto")
        return cls(int(parts[0]), parts[1], parts[2], parts[3], parts[4])
    
    def __eq__(self, other):
        if not isinstance(other, Participacao):
            return NotImplemented
        return self.codigo == other.codigo
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if not value:
            raise ValueError("Código não pode ser vazio.")
        self._codigo = value

    @property
    def data_inicio(self):
        return self._data_inicio
    
    @data_inicio.setter
    def data_inicio(self, value):
        if not value:
            raise ValueError("Data de início não pode ser vazia.")
        self._data_inicio = value

    @property
    def data_fim(self):
        return self._data_fim
    
    @data_fim.setter
    def data_fim(self, value):
        if not value:
            raise ValueError("Data de fim não pode ser vazia.")
        self._data_fim = value

    @property
    def aluno(self):
        return self._aluno
    
    @aluno.setter
    def aluno(self, value):
        if not value:
            raise ValueError("Aluno não pode ser vazio.")
        self._aluno = value
    
    @property
    def projeto(self):
        return self._projeto
    
    @projeto.setter
    def projeto(self, value):
        if not value:
            raise ValueError("Projeto não pode ser vazio.")
        self._projeto = value

# Testando a classe Participacao
participacao1 = Participacao.from_string("1,2023-01-01,2023-12-31,João da Silva,Projeto A")
participacao2 = Participacao.from_string("1,2023-01-01,2023-12-31,João da Silva,Projeto A")
participacao3 = Participacao.from_string("2,2023-02-01,2023-11-30,Maria Oliveira,Projeto B")

print(f"Participação 1 == Participação 2: {participacao1 == participacao2}")
print(f"Participação 1 == Participação 3: {participacao1 == participacao3}")
print(f"Participação 1: {participacao1.codigo}, {participacao1.data_inicio}, {participacao1.data_fim}, {participacao1.aluno}, {participacao1.projeto}")
print(f"Participação 2: {participacao2.codigo}, {participacao2.data_inicio}, {participacao2.data_fim}, {participacao2.aluno}, {participacao2.projeto}")
print(f"Participação 3: {participacao3.codigo}, {participacao3.data_inicio}, {participacao3.data_fim}, {participacao3.aluno}, {participacao3.projeto}")
