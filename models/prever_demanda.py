import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def carregar_dados(caminho_csv):
    return pd.read_csv(caminho_csv, sep=';')

def preparar_e_treinar_modelo(caminho_csv, dias_sazonais, test_size=0.05, random_state=35):
    dados_combinados = carregar_dados('../data/dados_combinados.csv')

    # Preparação dos dados
    dados_combinados['DATA'] = pd.to_datetime(dados_combinados['DATA'])
    dados_combinados['DIAS'] = (dados_combinados['DATA'] - dados_combinados['DATA'].min()).dt.days
    dados_combinados['SAZONALIDADE_ESPECIFICA'] = dados_combinados['DATA'].dt.day.isin(dias_sazonais).astype(int)

    # Selecionando as características (features) e o alvo (target)
    features = dados_combinados[['DIAS', 'VALOR_TOTAL_ITEM', 'SAZONALIDADE_ESPECIFICA']]
    target = dados_combinados['QUANTIDADE']

    # Dividindo os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=test_size, random_state=random_state)

    # Treinamento do modelo
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # Avaliação do modelo
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return modelo, mse, r2


def prever_estoque_futuro(modelo, dias_inicio, num_dias, media_valor_total, dias_sazonais, data_min):
    dias_futuros = pd.date_range(start=dias_inicio, periods=num_dias)
    df_predicao = pd.DataFrame({
        'DIAS': (dias_futuros - data_min).days,
        'VALOR_TOTAL_ITEM': media_valor_total,
        'SAZONALIDADE_ESPECIFICA': dias_futuros.day.isin(dias_sazonais).astype(int)
    })
    estoque_predito = modelo.predict(df_predicao)
    return estoque_predito


def main():
    caminho_csv = '../data/dados_combinados.csv'
    dias_sazonais = [20, 27, 4, 11, 18, 1, 15]

    # Preparar e treinar o modelo
    modelo, mse, r2 = preparar_e_treinar_modelo(caminho_csv, dias_sazonais)
    print('Resultado para R²:', r2)
    print('Resultado para MSE:', mse)

    # Carregar o DataFrame para obter a data máxima e a média de VALOR_TOTAL_ITEM
    dados_combinados = pd.read_csv(caminho_csv, sep=';')
    dados_combinados['DATA'] = pd.to_datetime(dados_combinados['DATA'])
    data_maxima = dados_combinados['DATA'].max()

    # Obter a data mínima para cálculos futuros
    data_minima = dados_combinados['DATA'].min()

    # Previsão de estoque para os próximos 7 dias
    data_maxima = pd.to_datetime(dados_combinados['DATA']).max()
    estoque_futuro = prever_estoque_futuro(modelo, data_maxima + pd.Timedelta(days=1), 7, dados_combinados['VALOR_TOTAL_ITEM'].mean(), dias_sazonais, data_minima)
    print('Previsão de estoque para os próximos 7 dias:', estoque_futuro)

# Verificar se o script é o ponto de entrada principal
if __name__ == "__main__":
    main()
