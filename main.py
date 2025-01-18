from data_preprocessing import *
from model_training import *
from visualization import *

# Veri seti dosya yolu
file_path = 'iot_factory_dataset.csv'

# Adım 1: Veri Hazırlığı
print("Veri seti yükleniyor ve hazırlanıyor...")
data = load_and_examine_data(file_path)
data = handle_missing_values(data)
data = convert_categorical_data(data)
data = extract_time_features(data)
data = feature_engineering(data)

# Adım 2: Veri Görselleştirme
print("\nVeri Görselleştirme...")
# Histogramlar ve dağılımlar
plot_distributions(data, ['Temperature_C', 'Vibration_ms2', 'Production_Count', 'Energy_Consumption_kWh'])

# Korelasyon matrisi
plot_correlation_matrix(data)

# 3D dağılım grafiği (örnek: Üretim, enerji tüketimi ve titreşim)
plot_3d_scatter(data, 'Production_Count', 'Energy_Consumption_kWh', 'Vibration_ms2', target='Error_Status')

# Kutu grafikleri
plot_boxplots(data, ['Temperature_C', 'Vibration_ms2', 'Production_Count', 'Energy_Consumption_kWh'])

# Adım 3: Model Eğitim ve Değerlendirme
print("\nModel Eğitim ve Değerlendirme...")
target_model_mapping = {
    'Error_Status': LogisticRegression(max_iter=5000, random_state=42),
    'Alerts': DecisionTreeClassifier(random_state=42, max_depth=5),
    'Connection_Status': RandomForestClassifier(random_state=42, n_estimators=100),
    'Energy_Consumption_kWh': RandomForestRegressor(random_state=42, n_estimators=100)
}

for target_column, model in target_model_mapping.items():
    print(f"\n*** {target_column} için model eğitimi ve değerlendirme ***")
    
    # X ve y
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_scaled = scale_features(X)
    
    # Eğitim ve test setleri
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    # Model eğitimi
    trained_model = train_model(X_train, y_train, model)
    
    # Model değerlendirme
    if target_column == 'Energy_Consumption_kWh':
        results = evaluate_regression_model(trained_model, X_test, y_test)
    else:
        results = evaluate_classification_model(trained_model, X_test, y_test)
    
    print(f"{type(model).__name__} sonuçları: {results}")