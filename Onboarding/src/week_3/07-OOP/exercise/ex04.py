"""Exercise 04"""

# Crie o atributo do tipo list participacoes na classe Projeto e implemente o método add_participacaoque recebe como parâmetro um objeto Participação e adiciona na lista.

from ex01 import Aluno
from ex02 import Projeto
from ex03 import Participacao

class ProjetoParticipacao(Projeto):
    def __init__(self, codigo, titulo, responsavel):
        super().__init__(codigo, titulo, responsavel)
        self.participacoes = []  # Inicializa a lista de participações

    def add_participacao(self, participacao):
        if not isinstance(participacao, Participacao):
            raise ValueError("Participação deve ser uma instância da classe Participacao")
        self.participacoes.append(participacao)

# Testando a classe ProjetoParticipacao
projeto = ProjetoParticipacao.from_string("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
aluno = Aluno.from_string("SP0101,João da Silva,joao@email.com")
participacao = Participacao(1, "2023-01-01", "2023-12-31", aluno, projeto)
projeto.add_participacao(participacao)






                          
