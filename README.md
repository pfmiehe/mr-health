# Projeto de Previsão de Demanda de Estoque

## Descrição
Este projeto é um modelo de previsão de demanda de estoque, especialmente projetado para otimizar a gestão de estoques em uma rede de alimentação saudável. Utilizando dados históricos de vendas, o modelo visa prever a demanda futura com base na sazonalidade, permitindo um planejamento mais eficiente das quantidades a serem estocadas em cada unidade.
Instalação

## Recursos
- Python 3.12.2
- Pandas
- Scikit-learn
- Matplotlib e Seaborn

## Instalação
Para utilizar este projeto, é necessário ter o Python3 instalado, além das bibliotecas Pandas, Scikit-learn, Matplotlib e Seaborn. 

```bash
pip install pandas scikit-learn matplotlib seaborn
```

## Uso
1. Os arquivos *itens-analysis.ipybn* e *pedido-analysis* foram utilizados para explorar e modelar as tabelas;
2. O arquivo *dados-combinados-graficos.ipybn* foi utilizado para juntar as 3 tabelas e posteriormente para analisar os dados. Importante executar este arquivo para que o dataset *dados_combinados.csv* seja gerado com a junção de todas as 3 tabelas utilizadas para exploração dos dados;
3. O modelo que faz a predição do modelo pode ser executado no arquivo *prever_demanda.py* e no arquivo em notebook *regressao_linear.ipybn*;


