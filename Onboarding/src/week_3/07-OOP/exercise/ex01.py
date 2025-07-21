"""Exercise 01"""

# Crie uma classe Aluno que deve ter como atributos o prontuario, nome e email. Deve ser possível construir um objeto aluno a partir da string prontuario, nome,email ex: SP0101,João da Silva,joao@email.com . Nenhum dos atributos pode ser vazio ou nulos (utilizar propriedades). Dois alunos podem ser considerados iguais caso tenham o mesmo prontuário.

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def from_string(cls , string):
        parts = [i.strip() for i in string.split(',')]
        if len(parts) != 3:
            raise ValueError("String must contain exactly three parts: prontuario, nome, email")
        return cls(parts[0], parts[1], parts[2])
    
    def __eq__(self, other):
        if not isinstance(other, Aluno):
            return NotImplemented
        return self.prontuario == other.prontuario


    @property
    def prontuario(self):
        return self._prontuario
    
    @prontuario.setter
    def prontuario(self, value):
        if not value:
            raise ValueError("Prontuário não pode ser vazio.")
        self._prontuario = value
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError("Nome não pode ser vazio.")
        self._nome = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email não pode ser vazio.")
        self._email = value


aluno = Aluno.from_string("SP0101,João da Silva, Joao@email.com")
aluno2 = Aluno.from_string("SP0101,João da Silva, João@email.com")
aluno3= Aluno("SP0102", "Paulo da Silva", "Paulo@email.com")


print(f"Aluno 1 == Aluno 2: {aluno == aluno2}")  
print(f"Aluno 1 == Aluno 3: {aluno == aluno3}")     
print(f"Prontuário: {aluno.prontuario}, Nome: {aluno.nome}, Email: {aluno.email}")
print(f"Prontuário: {aluno2.prontuario}, Nome: {aluno2.nome}, Email: {aluno2.email}")
print(f"Prontuário: {aluno3.prontuario}, Nome: {aluno3.nome}, Email: {aluno3.email}")