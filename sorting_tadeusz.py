import sys
import time
import matplotlib.pyplot as plt
import copy
import gc

import sorting_algorithms as sa

sys.setrecursionlimit(10000)

gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
gc.disable()             # wyłącz odśmiecanie


def main():
    file_path = "pan-tadeusz.txt"

    algorithms = ["bubble_sort", "merge_sort", "quick_sort", "selection_sort"]
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    for i, algorythm in enumerate(algorithms):
        n_values = []
        times = []

        for n in range(1000, 20000, 1000):
            data_list = sa.file_into_list(file_path, n)
            gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
            gc.disable()
            start = time.perf_counter()
            if algorythm == "bubble_sort":
                sorted_list = sa.bubble_sort(data_list)

            elif algorythm == "merge_sort":
                sorted_list = sa.merge_sort(data_list)

            elif algorythm == "quick_sort":
                list_len = len(data_list)
                sorted_list = sa.quick_sort(data_list, 0, list_len-1)

            elif algorythm == "selection_sort":
                sorted_list = sa.selection_sort(data_list)

            end = time.perf_counter()

            if gc_old: gc.enable()   # przywróć pierwotny stan odśmiecania

            total = end - start
            time_ms = total * 1000

            n_values.append(n)
            times.append(time_ms)

        ax = axes[i // 2, i % 2]
        ax.plot(n_values, times)
        ax.set_xlabel("Liczba znaków")
        ax.set_ylabel("Czas [ms]")

        if algorythm == "bubble_sort":
            ax.set_title("Wydajność algorytmu sortowania bąbelkowego")

        elif algorythm == "merge_sort":
            ax.set_title("Wydajność algorytmu sortowania przez scalanie")

        elif algorythm == "quick_sort":
            ax.set_title("Wydajność algorytmu sortowania szybkiego")

        elif algorythm == "selection_sort":
            ax.set_title("Wydajność algorytmu sortowania przez wybieranie")

    plt.tight_layout()
    plt.savefig('wykresy2.png')
    plt.show()



if __name__ == "__main__":
    main()
