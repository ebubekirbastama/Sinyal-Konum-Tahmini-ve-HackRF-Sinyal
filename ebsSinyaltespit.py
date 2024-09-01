import numpy as np
from pyhackrf import HackRF
from scipy.optimize import minimize

# Referans noktalarının koordinatları (x, y) ve bu noktalardaki sinyal güçleri (dBm)
reference_points = np.array([
    [0, 0],       # Nokta 1 (x1, y1)
    [10, 0],      # Nokta 2 (x2, y2)
    [0, 10],      # Nokta 3 (x3, y3)
    [10, 10]      # Nokta 4 (x4, y4)
])
signal_powers = np.array([
    -50,  # Güç Nokta 1
    -45,  # Güç Nokta 2
    -55,  # Güç Nokta 3
    -60   # Güç Nokta 4
])

# Sinyal gücünden mesafeyi tahmin etme fonksiyonu
def power_to_distance(power):
    return 10**((power - 50) / (-20))  # Basit bir dönüşüm (dBm cinsinden)

# Mesafe hesaplama fonksiyonu
def compute_distances(positions, reference_points, signal_powers):
    distances = np.zeros(len(reference_points))
    for i, (point, power) in enumerate(zip(reference_points, signal_powers)):
        distances[i] = power_to_distance(power)
    return distances

# Hedef konumun tahmini
def estimate_location(xy, reference_points, signal_powers):
    distances = compute_distances(xy, reference_points, signal_powers)
    return np.sum((np.linalg.norm(reference_points - xy, axis=1) - distances)**2)

# Tahmin işlemi
result = minimize(estimate_location, [5, 5], args=(reference_points, signal_powers), method='Nelder-Mead')

# Sonuçlar
estimated_location = result.x
print(f"Tahmin Edilen Konum: X={estimated_location[0]:.2f}, Y={estimated_location[1]:.2f}")

# HackRF ile bağlantı kurma ve sinyal ölçme fonksiyonları
def init_hackrf(frequency):
    device = HackRF()
    device.setup(frequency=frequency, sample_rate=10e6, center_freq=frequency, bandwidth=10e6)
    return device

def detect_signals(device, duration=1):
    samples = device.receive(duration=duration)
    power = np.abs(samples)
    return np.mean(20 * np.log10(power))  # Ortalama sinyal gücü (dBm)

# Frekansları belirleyin ve sinyal güçlerini ölçün
frequencies = [900e6, 1800e6, 2100e6, 2600e6]

for freq in frequencies:
    device = init_hackrf(freq)
    power = detect_signals(device, duration=2)
    print(f"{freq/1e6} MHz frekansında ölçülen sinyal gücü: {power:.2f} dBm")
    device.close()

# Sonuçları görselleştirme (opsiyonel)
import matplotlib.pyplot as plt

plt.scatter(reference_points[:, 0], reference_points[:, 1], c='red', label='Referans Noktaları')
plt.scatter(estimated_location[0], estimated_location[1], c='blue', label='Tahmin Edilen Konum')
plt.xlabel('X Koordinatı')
plt.ylabel('Y Koordinatı')
plt.title('Sinyal Konum Tahmini')
plt.legend()
plt.show()
