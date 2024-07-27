import re

# Bubble Sort

def bubble_sort(array):
    '''
    :param array: tablica do posortowania
    :return array: posortowana tablica
    '''
    array_length = len(array)

    for i in range(0,array_length,1):

        for j in range(0,array_length - i - 1):

            if array[j] > array[j + 1]:

              array[j], array[j + 1] = array[j + 1], array[j]

    return array
  

# Merge Sort

def merge_sort(array):
    '''
    :param array: tablica do posortowania
    :return array: zwraca posortowaną tablice
    '''

    array_length = len(array)
    if array_length > 1:

        # Znajdź środek listy
        mid = array_length // 2

        # Podziel listę na pół na dwie części
        left_half = array[:mid]
        right_half = array[mid:]

        # Posortuj każdą połowę oddzielnie
        merge_sort(left_half)
        merge_sort(right_half)

        merge(array, left_half, right_half)

    return array


def merge(array, left_half, right_half):
    i = j = k = 0
    # Pozmieniaj indeksy odpowiednich elementów w aktualnie rozpatrywanej liście
    while i < len(left_half) and j < len(right_half):
        if left_half[i].lower() <= right_half[j].lower():
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1

    # Dołożenie ostatniego elementu, który został w prawej lub lewej połowie na koniec
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1

# Quick Sort

def quick_sort(array, low, high):
    '''
    :param array: tablica do posortowania
    :return array: zwraca posortowaną tablice
    '''
        
    if low < high:
 
        pi = partition(array, low, high)
 
        quick_sort(array, low, pi - 1)
 
        quick_sort(array, pi + 1, high)

    return array
     
def partition(array, low, high):
 
    pivot = array[high]

    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
 
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

# Selection Sort

def selection_sort(array):
    '''
    :param array: tablica do posortowania
    :return array: zwraca posortowaną tablice
    '''

    # długość listy
    array_length = len(array)

    # Weź po kolei każdy indeks z listy oraz element mu odpowiadający i jeżeli znajdziesz mniejszy element
    # w grupie elementów o większym indeksie zamień indeksy tych elementów
    for i in range(array_length):
        min_idx = i
        for j in range(i + 1, array_length):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

def file_into_list(file_path, num_chars):
    '''
    Metoda zamieniająca plik tekstowy w listę, gdzie każdy element listy to ciąg znaków z alfabetu polskiego
    :param file_path: ścieżka pliku tekstowego
    :param num_chars: liczba znaków jakie chcemy odczytać z pliku
    :return data_list: lista słów w tekście
    '''
    try:
        with open(file_path, "r", encoding='utf-8') as file:

            # Przeczytaj zawartość pliku tekstowego (pierwsze num_chars znaków)
            content = file.read(num_chars)

            # Zamień wszystkie znaki poza literami na spacje
            content = re.sub(r'[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]', ' ', content)

            # Stwórz listę z ciągów znaków oddzielonych spacjami
            data_list = content.split()

            # Usuń zbędne przerwy
            data_list = [item.strip() for item in data_list]

            return data_list

    except FileNotFoundError:
        print(f"Nie znaleziono pliku {file_path}. Proszę podać prawidłową ścieżkę.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
