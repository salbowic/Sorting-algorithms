import re


def merge_sort(list):
    '''
    Algorytm sortowania przez scalanie
    :param list: lista do posortowania
    :return list: zwraca posortowaną listę
    '''

    list_length = len(list)
    if list_length > 1:

        # Znajdź środek listy
        mid = list_length // 2

        # Podziel listę na pół na dwie części
        left_half = list[:mid]
        right_half = list[mid:]

        # Posortuj każdą połowę oddzielnie
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Pozmieniaj indeksy odpowiednich elementów w aktualnie rozpatrywanej liście
        while i < len(left_half) and j < len(right_half):
            if left_half[i].lower() <= right_half[j].lower():
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1

        # Dołożenie ostatniego elementu, który został w prawej lub lewej połowie na koniec
        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1

    return list

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

def main():
    file_path = "pan-tadeusz.txt"
    for n in range(1000, 10000, 1000):
        data_list = file_into_list(file_path, n)
        B = merge_sort(data_list)
        print(f"Posortowany tekst dla pierwszych {n} wyrazów:")
        print(B)

if __name__ == "__main__":
    main()