## Exercícios:

**1 - Com base no material apresentado no notebook, o que é uma função de ativação (como a ReLU)? Por que normalmente usamos entre as camadas?**

Uma função de ativação é uma função matemática aplicada à saída de cada neurônio em uma rede neural. Ela transforma a soma ponderada das entradas, determinando a saída final do neurônio e se ele deve ser "ativado" para passar informação para a próxima camada. A função ReLU (Rectified Linear Unit), por exemplo, simplesmente retorna o valor de entrada se ele for positivo, e zero caso contrário (`f(x) = max(0, x)`).
A principal razão para usar funções de ativação (especialmente as não-lineares, como a ReLU) é introduzir a **não linearidade** no modelo. Sem elas, uma rede neural, por mais profunda que fosse, se comportaria como um simples modelo de regressão linear, pois a composição de múltiplas transformações lineares resulta em outra transformação linear. A não linearidade permite que a rede aprenda e represente relações muito mais complexas e sofisticadas entre os dados de entrada e saída, o que é essencial para a maioria das tarefas do mundo real, como reconhecimento de imagem e processamento de linguagem natural.

2 -  Explique o que cada uma das seguintes linhas de código faz e por que ela é necessária:

1. model.train(): Esta linha coloca o modelo em modo de treinamento. Isso é importante porque algumas camadas, como Dropout e BatchNorm, se comportam de maneira diferente durante o treinamento e a avaliação. No modo de treinamento, o Dropout desativa aleatoriamente algumas unidades para evitar overfitting, zerando valores de algun neurônios durante o treinamento. Já o BatchNorm normaliza os dados com base nas estatísticas do batch atual. Portanto, é crucial chamar `model.train()` antes de iniciar o processo de treinamento para garantir que essas camadas funcionem corretamente. 

2. optimizer.step(): Ela atualiza os parâmetros do modelo (pesos e vieses) com base nos gradientes calculados durante a retropropagação (loss.backward()). O algoritmo de otimização específico usado determina como essa atualização é feita, usando a taxa de aprendizado e outros hiperparâmetros definidos no otimizador, ultilizando gradientes para ajustar os parametros na direção que minimiza a função de perda.

3. Qual a diferença fundamental entre os modos model.train() e model.eval()?
model.train(): Este modo coloca o modelo em modo de treinamento. Durante o treinamento, certas camadas se comportam de maneira diferente. Por exemplo, camadas como Dropout e BatchNorm (se houver) estão ativas e se comportam como esperado durante o treinamento (aplicando dropout aleatório ou atualizando estatísticas de normalização em lote). Além disso, o PyTorch rastreia os gradientes das operações no modo de treinamento, o que é necessário para a retropropagação.
model.eval(): Este modo coloca o modelo em modo de avaliação. Em contraste com o modo de treinamento, camadas como Dropout são desativadas (não aplicam dropout) e BatchNorm usa as estatísticas médias e de variância aprendidas durante o treinamento (em vez de calcular novas estatísticas para cada lote de avaliação). O PyTorch também desativa o cálculo de gradientes por padrão no modo de avaliação para economizar memória e computação, pois os gradientes não são necessários para a inferência.

3 - Modifique a classe ClassBin para que a rede tenha a seguinte arquitetura:

1. Camada de Entrada: Mantém as 4 features de entrada.
2. Primeira Camada Oculta: nn.Linear com 4 neurônios de entrada e 16 neurônios de saída, seguida por uma ativação ReLU.
3. Segunda Camada Oculta: nn.Linear com 16 neurônios de entrada e 8 neurônios de saída, seguida por uma ativação ReLU.
4. Camada de Saída: nn.Linear com 8 neurônios de entrada e 1 neurônio de saída, seguida por uma ativação Sigmoid.
5. Remova todas as camadas de Dropout para uma nova arquitetura.
6. Treine o novo modelo com os mesmos hiperparâmetros (épocas, taxa de aprendizado, etc.) e compare a acurácia final (de treino e teste) com a do modelo original.

4 -  Usando o modelo original do notebook:

1. Mude o Otimizador: Substitua o otimizador **Adam** por SGD (Stochastic Gradient Descent). 
2. Treine o modelo com o SGD.
3. O que aconteceu com o custo (loss) durante o treinamento? A acurácia final foi melhor ou pior? O SGD com essa taxa de aprendizado pareceu uma boa escolha?

5 - Usando o modelo original e o otimizador Adam:

1. No DataLoader, mude o batch_size de 32 para um valor muito maior, como 512.
2. Treine o modelo e observe a acurácia.
3. Agora, faça o oposto. Mude o batch_size para um valor bem pequeno, como 4, e treine novamente.
4. Como a mudança no batch_size afetou a estabilidade do custo (loss) a cada época e a acurácia final do modelo?