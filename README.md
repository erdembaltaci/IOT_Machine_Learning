# 🌟 IoT Veri Seti Analizi

Bu proje, bir fabrikadaki makinelerden IOT ile alınan veri setinin makine öğrenmesi teknikleri kullanılarak analiz edilmesini kapsamaktadır. Analiz; veri önişleme, keşfedici veri analizi, görselleştirme, model eğitimi ve değerlendirme adımlarını içerir. Sonuçlar, bir fabrikadaki enerji tüketimi, hata tahmini ve makine uyarıları hakkında öngörüler sağlamaya yöneliktir.

&nbsp;


## 🎯 Amaçlar
- Veri Analizi: Veri setini makine öğrenmesi için temizlemek ve önişlemek.
- Model Eğitimi: Sınıflandırma (hata tahmini gibi) ve regresyon (enerji tüketimi tahmini gibi) için modeller eğitmek.
- Görselleştirme: Veri hakkında görsel çıkarımlar sağlamak.
- Değerlendirme: Uygun metriklerle model performansını değerlendirmek.
- Döküman Hazırlama: Tüm süreci, kodu ve sonuçları net bir şekilde açıklamak.


&nbsp;


## 📊 Veri Seti

### Açıklama
Veri seti, bir fabrikadan IoT sensör okumalarını içermektedir ve şu sütunlardan oluşmaktadır:

- Machine_ID: Her makine için benzersiz bir tanımlayıcı.
- Timestamp: Okumanın alındığı zaman.
- Temperature_C: Makine sıcaklığı (Celsius cinsinden).
- Vibration_ms2: Titreşim seviyesi (m/s² cinsinden).
- Error_Status: Makine hatalarını belirten ikili durum (0 veya 1).
- Production_Count: Okuma süresince üretim miktarı.
- Energy_Consumption_kWh: Enerji tüketimi (kWh cinsinden).
- Connection_Status: Makine bağlantı durumu (0 veya 1).
- Alerts: Makine tarafından tetiklenen uyarılar.

&nbsp;


### 📘 Kaynak
Bu veri seti ham bir şekilde ,fabrikalara IOT çözümü sunan bir yazılım firmasından alınmıştır.


&nbsp;


## ✅ Metodoloji

###  🛠 1. Veri Önişleme

- Eksik veriler uygun stratejilerle doldurulmuştur (sayısal veriler için ortalama, kategorik veriler için en sık değer).
- Kategorik sütunlar için etiket kodlama (label encoding) yapılmıştır.
- Zaman tabanlı özellikler çıkarılmıştır (saat, gün).
- Aşağıdaki gibi ek özellikler mühendisliği yapılmıştır:
  - Bir üretim birimi başına enerji tüketimi.
  - Titreşim ve sıcaklık oranı.

&nbsp;
&nbsp;
    
 
### 📊 2. Veri Görselleştirme

- Temel sayısal değişkenler için histogramlar.
- Korelasyon matrisi ısı haritası.
- Çoklu değişken ilişkileri için 3D dağılım grafikleri.
- Aykırı değerleri belirlemek için kutu grafikleri.

&nbsp;

### 🧠 3. Model Eğitimi ve Değerlendirme

#### Sınıflandırma Görevleri

- Error_Status: Makine hataları Logistic Regression ile tahmin edilecek.
- Alerts: Makine uyarıları Decision Tree Classifier ile tahmin edilecek.
- Connection_Status: Bağlantı durumu Random Forest Classifier ile tahmin edilecek.

#### Regresyon Görevi

- Energy_Consumption_kWh: Enerji tüketimi Random Forest Regressor ile tahmin edilecek.

&nbsp; 

### 📈 4. Performans Metrikleri

#### Sınıflandırma

- Doğruluk (Accuracy)
- Kesinlik (Precision)
- Duyarlılık (Recall)
- F1 Skoru

#### Regresyon

- Ortalama Kare Hatası (MSE)
- R² Skoru

&nbsp;



## 🔍 Sonuçlar

#### Model Performansı

##### Error_Status (Logistic Regression)

- Doğruluk: 0.55
- Kesinlik: 0.55
- Duyarlılık: 0.55
- F1 Skoru: 0.55


##### Alerts (Decision Tree Classifier)

- Doğruluk: 0.30
- Kesinlik: 0.24
- Duyarlılık: 0.30
- F1 Skoru: 0.20


##### Connection_Status (Random Forest Classifier)

- Doğruluk: 0.66
- Kesinlik: 0.67
- Duyarlılık: 0.66
- F1 Skoru: 0.66


##### Energy_Consumption_kWh (Random Forest Regressor)

- MSE: 2.70
- R² Skoru: 0.90

&nbsp;


## 🖥️ Proje Kod Yapısı
project  
├── dataset.csv  
├── main.py  
├── data_preprocessing.py  
├── model_training.py  
├── visualization.py 

&nbsp;


## Araçlar ve Kütüphaneler
#### Programlama Dili: 
- 🐍 Python

#### 📦 Kütüphaneler:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- imbalanced-learn

&nbsp;


## ▶️ Video Sunum
- youtube linki eklenecektir.!!!!!!!!!!!
