import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Veri setini yükleyip ilk bilgileri görüntüleme
def load_and_examine_data(file_path):
    """
    Verilen dosya yolundan veri setini yükler ve temel bilgileri ekrana yazdırır.
    - İlk 5 satır
    - Sütun bilgileri ve veri türleri
    """
    data = pd.read_csv(file_path)
    data.head(5)  # İlk 5 satırı göster
    data.info()   # Veri seti hakkında bilgi
    return data

# Eksik değerleri doldurma
def handle_missing_values(data):
    """
    Eksik değerleri uygun yöntemlerle doldurur.
    - Sayısal sütunlar için mean (ortalama) kullanılır.
    - Kategorik sütunlar için mode (en sık görülen değer) kullanılır.
    """
    data['Temperature_C'] = data['Temperature_C'].fillna(data['Temperature_C'].mean())
    data['Vibration_ms2'] = data['Vibration_ms2'].fillna(data['Vibration_ms2'].mean())
    data['Error_Status'] = data['Error_Status'].fillna(data['Error_Status'].mode()[0])
    data['Alerts'] = data['Alerts'].fillna(data['Alerts'].mode()[0])
    return data

# Kategorik verileri sayısal değerlere dönüştürme
def convert_categorical_data(data):
    """
    Kategorik sütunları sayısal değerlere dönüştürür.
    - 'Error_Status' ve 'Alerts' gibi kategorik sütunlar için Label Encoding kullanılır.
    """
    label_encoder = LabelEncoder()
    data['Error_Status'] = label_encoder.fit_transform(data['Error_Status'])
    data['Alerts'] = label_encoder.fit_transform(data['Alerts'])
    return data

# Zaman özellikleri türetme
def extract_time_features(data):
    """
    Zaman damgasından anlamlı özellikler türetir.
    - Saat (Hour)
    - Gün (Day)
    Orijinal zaman damgası sütunu çıkarılır.
    """
    data['Hour'] = pd.to_datetime(data['Timestamp']).dt.hour
    data['Day'] = pd.to_datetime(data['Timestamp']).dt.day
    data.drop(columns=['Timestamp', 'Machine_ID'], inplace=True)
    return data

# Verileri ölçeklendirme
def scale_features(X):
    """
    Verileri ölçeklendirir.
    - StandardScaler kullanılarak özellikler sıfır-ortalama ve birim-standart sapma olacak şekilde ölçeklenir.
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return pd.DataFrame(X_scaled, columns=X.columns)

# Yeni özellikler türetme
def feature_engineering(data):
    """
    Yeni özellikler türetir.
    - Üretim başına enerji tüketimi (Energy_per_Production)
    - Titreşim ve sıcaklık oranı (Vibration_Temperature_Ratio)
    """
    data['Energy_per_Production'] = data['Energy_Consumption_kWh'] / (data['Production_Count'] + 1e-9)
    data['Vibration_Temperature_Ratio'] = data['Vibration_ms2'] / (data['Temperature_C'] + 1e-9)
    return data
