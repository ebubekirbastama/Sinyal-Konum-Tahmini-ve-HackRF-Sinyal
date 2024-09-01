# Sinyal Konum Tahmini

Bu proje, sinyal güçleri kullanarak bir hedefin konumunu tahmin etmek amacıyla geliştirilmiştir. Proje, HackRF cihazını kullanarak sinyal gücünü ölçer ve bu ölçümleri kullanarak tahmini bir konum hesaplar.

## İçindekiler

- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Fonksiyonlar](#fonksiyonlar)
- [Sonuçlar](#sonuçlar)
- [Görselleştirme](#görselleştirme)
- [Gereksinimler](#gereksinimler)

## Kurulum

Bu proje Python 3 ve aşağıdaki kütüphaneleri gerektirir:

- `numpy`
- `scipy`
- `matplotlib`
- `pyhackrf`

Gerekli kütüphaneleri yüklemek için:

```bash
pip install numpy scipy matplotlib pyhackrf
```
## Kullanım

1. **Sinyal Gücü Ölçümü ve Tahmin**

   Kod, belirli frekansta sinyal gücünü ölçer ve bu ölçümleri kullanarak tahmin edilen bir konumu hesaplar. Tahmin işlemi `scipy.optimize.minimize` fonksiyonu kullanılarak yapılır.

2. **Sinyal Gücü Ölçme**

   `HackRF` cihazı ile belirli frekansta sinyal gücü ölçülür. Ölçülen sinyal gücü, frekanslara bağlı olarak dBm cinsinden hesaplanır.

3. **Sonuçların Görselleştirilmesi**

   Hesaplanan tahmin edilen konum ve referans noktaları matplotlib kullanılarak görselleştirilir.

## Fonksiyonlar

- `power_to_distance(power)`: Sinyal gücünü mesafeye dönüştürür.
- `compute_distances(positions, reference_points, signal_powers)`: Mesafeleri hesaplar.
- `estimate_location(xy, reference_points, signal_powers)`: Tahmin edilen konumu hesaplar.
- `init_hackrf(frequency)`: HackRF cihazını başlatır ve belirli frekansta ayarlar.
- `detect_signals(device, duration=1)`: Sinyal gücünü ölçer.

## Sonuçlar

Kod çalıştırıldığında, HackRF cihazı ile ölçülen sinyal güçleri ve tahmin edilen konum ekrana yazdırılır. Ayrıca, referans noktaları ve tahmin edilen konum matplotlib kullanılarak görselleştirilir.

## Görselleştirme

Tahmin edilen konum ve referans noktaları, matplotlib ile X-Y koordinat düzleminde görselleştirilir.

## Gereksinimler

- Python 3
- HackRF cihazı (sinyal ölçümü için)

---

Bu README, projenin temel işlevselliğini ve nasıl kullanılacağını anlamanıza yardımcı olmayı amaçlamaktadır. Daha fazla bilgi veya destek için proje sayfasına başvurabilirsiniz.

