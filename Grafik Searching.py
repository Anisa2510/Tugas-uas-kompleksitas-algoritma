import matplotlib.pyplot as plt

# Data ukuran input
sizes = [100, 1000, 10000]

# Contoh data hasil pengukuran waktu (ganti dengan data asli jika ada)
searching_times = {
    "Linear Search": [0.0002, 0.0015, 0.012],
    "Binary Search": [0.00005, 0.00006, 0.00007]
}

# Plot grafik
plt.figure(figsize=(10, 5))
for name, times in searching_times.items():
    plt.plot(sizes, times, marker='o', label=name)

plt.title("Perbandingan Waktu Eksekusi Algoritma Searching")
plt.xlabel("Jumlah Elemen")
plt.ylabel("Waktu (detik)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
