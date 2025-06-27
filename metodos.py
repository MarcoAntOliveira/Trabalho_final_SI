from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Carregue seus dados
df = pd.read_csv("dados.csv")
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Pré-processamento: normalização
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Treino/Teste Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 1. Decision Tree
dt = DecisionTreeClassifier(criterion='entropy', random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

# 2. Random Forest
rf = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# 3. Gradient Boosting
gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)

# Métricas
def avaliar_modelo(nome, y_test, y_pred):
    print(f"\n===== {nome} =====")
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))
    print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

avaliar_modelo("Decision Tree", y_test, y_pred_dt)
avaliar_modelo("Random Forest", y_test, y_pred_rf)
avaliar_modelo("Gradient Boosting", y_test, y_pred_gb)
