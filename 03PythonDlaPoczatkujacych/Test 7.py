import matplotlib.pyplot as plt

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return '#' + ''.join(f'{c:02x}' for c in rgb_color)

def generate_popular_harmonic_green_palette(num_colors):
    # Przykładowe popularne kolory harmoniczne w odcieniach zieleni
    popular_colors = [
        '#003300',  # Ciemny zielony
        '#006400',  # Zieleń butelkowa
        '#008000',  # Zielony
        '#1f8a1f',  # Ciemnozielony
        '#4caf50',  # Zielony (średni)
        '#66ff66',  # Zielony neonowy
        '#99ff99',  # Biały zielony
        '#00b300',  # Jasny zielony
        '#8bc34a',  # Jasny zielony (paleta Material Design)
        '#a5d6a7',  # Jasnozielony (paleta Material Design)
        '#b2ff59',  # Zielony cytrynowy
        '#c5e1a5'   # Zielony (bardzo jasny)
    ]

    # Jeśli żądana liczba kolorów jest większa niż dostępne kolory, ogranicz do dostępnych
    num_colors = min(num_colors, len(popular_colors))

    # Sortowanie kolorów od najciemniejszego do najjaśniejszego
    sorted_palette = sorted(popular_colors, key=hex_to_rgb)

    # Wybór wymaganej liczby kolorów
    palette = sorted_palette[:num_colors]

    return palette

# Przykład użycia
num_colors = 12  # Liczba kolorów w palecie (można zmienić według potrzeb)
palette = generate_popular_harmonic_green_palette(num_colors)

# Zapisanie kolorów do listy
kolory = palette.copy()

# Dodanie koloru #114444 do listy
kolory.append('#114444')

# Wyświetlenie kolorów
print("Wygenerowane kolory:", kolory)

# Wizualizacja kolorów
plt.figure(figsize=(10, 2))
plt.bar(range(len(kolory)), [1] * len(kolory), color=kolory)
plt.xticks(range(len(kolory)), kolory)
plt.title('Paleta popularnych kolorów harmonicznych zielonych')
plt.show()