# 🌟 IoT Veri Seti Analizi

Bu proje, bir fabrikadaki makinelerden IOT ile alınan veri setinin makine öğrenmesi teknikleri kullanılarak analiz edilmesini kapsamaktadır. Analiz; veri önişleme, keşfedici veri analizi, görselleştirme, model eğitimi ve değerlendirme adımlarını içerir. Sonuçlar, bir fabrikadaki enerji tüketimi, hata tahmini ve makine uyarıları hakkında öngörüler sağlamaya yöneliktir.

## Amaçlar
- Veri Analizi: Veri setini makine öğrenmesi için temizlemek ve önişlemek.
- Model Eğitimi: Sınıflandırma (hata tahmini gibi) ve regresyon (enerji tüketimi tahmini gibi) için modeller eğitmek.
- Görselleştirme: Veri hakkında görsel çıkarımlar sağlamak.
- Değerlendirme: Uygun metriklerle model performansını değerlendirmek.
- Döküman Hazırlama: Tüm süreci, kodu ve sonuçları net bir şekilde açıklamak.

## Veri Seti
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
