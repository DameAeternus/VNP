# Чекор 1: Вчитување на библиотеки и податоци
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

# Вчитајте го dataset-от
dataset = pd.read_csv('dataset.csv')

# Чекор 2: Поделба на податоците
# class ќе го тестираме, затоа го 
# droppaме од X-input Y-output array
X = dataset.drop('class', axis=1)
y = dataset['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Чекор 3: Претпроцесирање на податоците
# Нормализација со StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Чекор 4: Креирање на модел
# За XGBoost, може да користите XGBClassifier
model = XGBClassifier(
    learning_rate=0.1,
    n_estimators=100,
    max_depth=3,
    subsample=0.8,
    random_state=42
)

# Чекор 5: Тренирање на моделот
model.fit(X_train, y_train)

# Чекор 6: Евалуација на моделот
y_pred = model.predict(X_test)
f1 = f1_score(y_test, y_pred)

print(f"F1 Score: {f1}")
