import matplotlib.pyplot as plt

# Data dummy (hapus ini jika kamu sudah punya variabel asli dari eksperimen)
sizes = [100, 1000, 10000]
sorting_times = {
    "Bubble Sort": [0.01, 0.5, 15.2],
    "Insertion Sort": [0.005, 0.3, 10.7],
    "Merge Sort": [0.001, 0.01, 0.08],
    "Quicksort": [0.001, 0.009, 0.07]
}

# Visualisasi
plt.figure(figsize=(10, 5))
for name, times in sorting_times.items():
    plt.plot(sizes, times, marker='o', label=name)

plt.title("Perbandingan Waktu Eksekusi Algoritma Sorting")
plt.xlabel("Jumlah Elemen")
plt.ylabel("Waktu (detik)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
