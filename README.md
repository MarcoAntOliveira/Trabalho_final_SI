##

presente trabalho consiste da aplicação e avaliação de algoritmos de classificação em bases de dados
“misteriosas”, isto é, as bases de dados são fornecidas sem nenhuma informação adicional que permita
compreender melhor a origem do problema ou suas características. Cada base é fornecida em um arquivo csv
que contém objetos nas linhas e atributos nas colunas. A última coluna corresponde à classe de cada objeto.

Para este trabalho, espera-se que você aplique uma ou mais técnicas de aprendizado de máquina para o
problema de classificação em pelo menos uma base de dados. Você deve comparar pelo menos três diferentes
classificadores (realizando seleção de hiperparâmetros para cada método ou não). Para tanto, use um dos
estimadores de qualidade/desempenho vistos em sala (o que achar mais apropriado). A métrica de
qualidade/desempenho empregada para avaliação dos métodos é de sua escolha. Você pode ainda realizar
seleção de atributos (para reduzir a dimensionalidade de cada problema) ou aplicar técnicas de pré-
processamento da maneira que achar mais adequada. É desejável que seja realizada alguma análise
exploratória dos dados, a fim de conhecer melhor as características do problema abordado.

1. Realizar uma análise exploratória na base de dados e reportar seus achados mais relevantes. Existem
atributos irrelevantes? redundantes? Podem ser removidos atributos? Por quê? Se você optar por
realizar sua análise considerando diferentes subconjuntos de atributos, justifique.
2. Definir um conjunto de métodos de classificação para serem avaliados no contexto do problema
(pelo menos três modelos diferentes). Você não precisa se limitar a métodos vistos em sala de aula,
podendo explorar outros existentes. Não é necessário implementar os modelos do zero, isto é, você
pode utilizar bibliotecas e/ou códigos prontos que forneçam estes modelos para utilização.
3. Definir quais hiperparâmetros e respectivos valores serão avaliados para cada modelo. A partir desta
definição, realizar uma busca em grade (grid search) para encontrar a melhor configuração de
hiperparâmetros de cada modelo. Note que a forma com a qual a qualidade do modelo será estimada
e as métricas que serão utilizadas para tal estimativa são de livre escolha. Sua escolha, entretanto,
deve ser minimamente justificada e embasada.
4. Fornecer, avaliar e interpretar os resultados obtidos na etapa anterior por meio de tabelas e
principalmente gráficos. Importante: você deve fazer aqui uma análise crítica, discutindo os
resultados. A atribuição de nota considerará não só a qualidade final dos resultados obtidos, mas
também a forma como eles foram apresentados e discutidos. Portanto, pense bem em como
organizar, sumarizar e discutir os resultados obtidos. Dê especial atenção à forma como a avaliação é
conduzida, apresentando suas escolhas de forma justificada. Importante: gráficos e tabelas não são
auto-explicativos; os resultados devem ser discutidos por você, indicando quais os principais pontos
que devem ser observados pelo leitor ao analisar os resultados na forma em que foram apresentados.
Finalmente, espera-se a comparação frente à um baseline, isto é, você deve responder à seguinte
pergunta: qual o desempenho/qualidade minimamente esperado em cada base de dados avaliada?
