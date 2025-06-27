import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. Carregamento da base de dados
df = pd.read_csv('bases/05.csv')

print(f"Dimensão da base: {df.shape[0]} linhas × {df.shape[1]} colunas")

# 2. Separando atributos e rótulo (supondo que a última coluna é o alvo)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# 3. Verificando valores constantes ou com baixa variância
variancia = X.var()
baixa_variancia = variancia[variancia < 1e-2]  # Threshold ajustável

print(f"\nNúmero de atributos com baixa variância: {len(baixa_variancia)}")
print("Atributos candidatos à remoção (baixa variância):")
print(baixa_variancia.head())

# 4. Removendo atributos com baixa variância
selector = VarianceThreshold(threshold=1e-2)
X_reduzido = selector.fit_transform(X)
print(f"\nDimensão após remoção de baixa variância: {X_reduzido.shape}")

# 5. Correlação entre atributos
X_corr_df = pd.DataFrame(X_reduzido)
corr = X_corr_df.corr().abs()

# Remoção de atributos altamente correlacionados
upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]

print(f"\nAtributos altamente correlacionados (> 0.95): {len(to_drop)}")
X_corr_reduzido = X_corr_df.drop(columns=to_drop)
print(f"Dimensão após remoção de atributos redundantes: {X_corr_reduzido.shape}")

# 6. Padronização para PCA ou modelagem
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_corr_reduzido)

# 7. PCA para análise de dimensionalidade
pca = PCA(n_components=0.95)  # Mantém 95% da variância
X_pca = pca.fit_transform(X_scaled)
print(f"\nNúmero de componentes principais para 95% da variância: {X_pca.shape[1]}")

# 8. Análise da variável alvo
print("\nDistribuição da variável alvo:")
print(y.value_counts(normalize=True))

sns.countplot(x=y)
plt.title("Distribuição da Classe")
plt.show()

# 9. (Opcional) Visualização em 2D com PCA
if X_pca.shape[1] >= 2:
    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='coolwarm', alpha=0.7)
    plt.xlabel("Componente Principal 1")
    plt.ylabel("Componente Principal 2")
    plt.title("Projeção PCA dos dados")
    plt.show()
