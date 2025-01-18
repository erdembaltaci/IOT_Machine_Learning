from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_squared_error, r2_score
)

# Modelleri eğitme
def train_model(X_train, y_train, model):
    """
    Verilen model ile eğitim setinde eğitimi gerçekleştirir.
    - Parametreler:
        - X_train: Eğitim verisinin bağımsız değişkenleri
        - y_train: Eğitim verisinin bağımlı değişkeni
        - model: Kullanılacak model
    - Çıktı:
        - Eğitilmiş model
    """
    model.fit(X_train, y_train)
    return model

# Sınıflandırma modeli değerlendirme
def evaluate_classification_model(model, X_test, y_test):
    """
    Sınıflandırma modeli performansını değerlendirir.
    - Parametreler:
        - model: Test edilecek model
        - X_test: Test verisinin bağımsız değişkenleri
        - y_test: Test verisinin bağımlı değişkeni
    - Çıktı:
        - Accuracy, Precision, Recall, F1 Score
    """
    y_pred = model.predict(X_test)
    return {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, average='weighted'),
        'Recall': recall_score(y_test, y_pred, average='weighted'),
        'F1 Score': f1_score(y_test, y_pred, average='weighted')
    }

# Regresyon modeli değerlendirme
def evaluate_regression_model(model, X_test, y_test):
    """
    Regresyon modeli performansını değerlendirir.
    - Parametreler:
        - model: Test edilecek model
        - X_test: Test verisinin bağımsız değişkenleri
        - y_test: Test verisinin bağımlı değişkeni
    - Çıktı:
        - Mean Squared Error, R2 Score
    """
    y_pred = model.predict(X_test)
    return {
        'Mean Squared Error': mean_squared_error(y_test, y_pred),
        'R2 Score': r2_score(y_test, y_pred)
    }
