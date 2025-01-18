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

   ```
         data['Temperature_C'] = data['Temperature_C'].fillna(data['Temperature_C'].mean())
         data['Vibration_ms2'] = data['Vibration_ms2'].fillna(data['Vibration_ms2'].mean())
         data['Error_Status'] = data['Error_Status'].fillna(data['Error_Status'].mode()[0])
         data['Alerts'] = data['Alerts'].fillna(data['Alerts'].mode()[0])
         # Sebep: 'Ortalama' --> sayısal verilerde genel eğilimi korurken 'En sık değer' --> kategorik sütunlarda sınıf dengesini korur.

- Kategorik sütunlar için etiket kodlama (label encoding) yapılmıştır.
- Zaman tabanlı özellikler çıkarılmıştır (saat, gün).
- Aşağıdaki gibi ek özellikler mühendisliği yapılmıştır:
  - Bir üretim birimi başına enerji tüketimi.(Enerji verimliliğini ölçmek için)
  - Titreşim ve sıcaklık oranı. (Makine titreşimi ve sıcaklık arasındaki ilişkiyi analiz etmek için)

 ```
      data['Energy_per_Production'] = data['Energy_Consumption_kWh'] / (data['Production_Count'] + 1e-9)
      data['Vibration_Temperature_Ratio'] = data['Vibration_ms2'] / (data['Temperature_C'] + 1e-9)


&nbsp;
&nbsp;
    
 
### 📊 2. Veri Görselleştirme

- Temel sayısal değişkenler için histogramlar oluşturulmuştur.
- Korelasyon matrisi ısı haritası kullanılmıştır.
- Çoklu değişken ilişkileri için 3D dağılım grafikleri oluşturulmuştur.
- Aykırı değerleri belirlemek için kutu grafikleri hazırlanmıştır.

&nbsp;

### 🧠 3. Model Eğitimi ve Değerlendirme

#### Sınıflandırma Görevleri

- Error_Status: Makine hataları Logistic Regression ile tahmin edilmiştir.
     ```
      Neden seçtik?
      İkili sınıflandırma problemi olduğu için.
      Basit ve açıklanabilir bir model.
- Alerts: Makine uyarıları Decision Tree Classifier ile tahmin edilmiştir.
- Connection_Status: Bağlantı durumu Random Forest Classifier ile tahmin edilmiştir.

#### Regresyon Görevi

- Energy_Consumption_kWh: Enerji tüketimi Random Forest Regressor ile tahmin edilmiştir.


&nbsp; 

### 📈 4. Performans Metrikleri

#### Sınıflandırma

- Doğruluk (Accuracy): Modelin doğru tahmin oranı.
- Kesinlik (Precision): Doğru pozitiflerin toplam pozitif tahmine oranı.
- Duyarlılık (Recall): Doğru pozitiflerin toplam gerçek pozitiflere oranı.
- F1 Skoru: Kesinlik ve duyarlılığın harmonik ortalaması.

#### Regresyon

- Ortalama Kare Hatası (MSE): Tahmin edilen değerlerin gerçek değerlerden sapmasını ölçer.
- R² Skoru: Modelin açıklayıcılık oranını belirtir.

&nbsp;



## 🔍 Sonuçlar

#### Model Performansı

##### Error_Status (Logistic Regression)

- Doğruluk: 0.55
- Kesinlik: 0.55
- Duyarlılık: 0.55
- F1 Skoru: 0.55
##### Yorum: Model, düşük performans gösterdiği için ek özellik mühendisliği veya daha karmaşık algoritmalar kullanılabilir.


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

## 🔭 Sonuçların Yorumlanması

- Error_Status: Logistic Regression sonuçları, sınıflandırma için temel bir performans sağlamaktadır ancak geliştirme gereklidir.
- Alerts: Düşük başarı oranı, daha karmaşık algoritmalar veya özellik mühendisliği gerekliliğini işaret etmektedir.
- Connection_Status: Random Forest Classifier, bağlantı durumunu makul bir doğrulukla tahmin edebilmiştir.
- Energy_Consumption_kWh: Random Forest Regressor, enerji tüketimi tahmininde yüksek bir doğruluk oranı sağlamıştır.

&nbsp;

## 🖥️ Proje Kod Yapısı
project/  <br>
├── dataset.csv                # Veri seti  <br>
├── main.py                    # Ana Python scripti <br>
├── data_preprocessing.py      # Veri önişleme modülü <br>
├── model_training.py          # Model eğitim modülü <br>
├── visualization.py           # Görselleştirme modülü <br>

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
- Proje sunumunu izlemek için [YouTube bağlantısı eklenecektir.]

&nbsp;

## 📅 Gelecek Çalışmalar

- Model performansını artırmak için hiperparametre optimizasyonu yapılabilir.
- IoT verilerinden daha fazla anlamlı özellik türetilebilir.
- XGBoost veya LightGBM gibi ileri algoritmalar uygulanabilir.
