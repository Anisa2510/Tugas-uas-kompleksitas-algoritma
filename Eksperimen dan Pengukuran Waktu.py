import random
import time
import matplotlib.pyplot as plt

# ----------------------------
# Definisi Algoritma Sorting
# ----------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# ----------------------------
# Definisi Algoritma Searching
# ----------------------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ----------------------------
# Fungsi Pengukur Waktu
# ----------------------------
def measure_time(func, arr, is_sorting=True):
    start = time.time()
    if is_sorting:
        func(arr.copy())  # Sorting biasanya in-place
    else:
        func(arr, random.choice(arr))  # Searching butuh target
    end = time.time()
    return end - start

# ----------------------------
# Eksperimen
# ----------------------------
sizes = [100, 1000, 10000]

sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quicksort": lambda arr: quicksort(arr)  # Quicksort versi pure (non-in-place)
}

searching_algorithms = {
    "Linear Search": linear_search,
    "Binary Search": binary_search
}

sorting_times = {name: [] for name in sorting_algorithms}
searching_times = {name: [] for name in searching_algorithms}

for size in sizes:
    data = [random.randint(1, 10000) for _ in range(size)]

    # Sorting
    for name, func in sorting_algorithms.items():
        t = measure_time(func, data)
        sorting_times[name].append(t)

    # Searching (binary search pakai data terurut)
    sorted_data = sorted(data)
    for name, func in searching_algorithms.items():
        t = measure_time(func, sorted_data if name == "Binary Search" else data, is_sorting=False)
        searching_times[name].append(t)

# ----------------------------
# Visualisasi Grafik
# ----------------------------
plt.figure(figsize=(10, 5))
for name, times in sorting_times.items():
    plt.plot(sizes, times, label=name)
plt.title("Perbandingan Waktu Eksekusi Sorting")
plt.xlabel("Jumlah Elemen")
plt.ylabel("Waktu (detik)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
for name, times in searching_times.items():
    plt.plot(sizes, times, label=name)
plt.title("Perbandingan Waktu Eksekusi Searching")
plt.xlabel("Jumlah Elemen")
plt.ylabel("Waktu (detik)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
