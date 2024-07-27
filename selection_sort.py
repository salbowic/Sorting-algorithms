import re


def selection_sort(list):
    '''
    Metoda sortowania przez wybieranie
    :param list: lista słów/liczb do posortowania
    :return: posortowana lista
    '''

    # długość listy
    list_length = len(list)

    # Weź po kolei każdy indeks z listy oraz element mu odpowiadający i jeżeli znajdziesz mniejszy element
    # w grupie elementów o większym indeksie zamień indeksy tych elementów
    for i in range(list_length):
        min_idx = i
        for j in range(i + 1, list_length):
            if list[min_idx].lower() > list[j].lower():
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
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
        B = selection_sort(data_list)
        print("Posortowany tekst:")
        print(B)

if __name__ == "__main__":
    main()
