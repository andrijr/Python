import matplotlib.pyplot as plt


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    return '#' + ''.join(f'{c:02x}' for c in rgb_color)


def generate_popular_harmonic_green_palette(num_colors):
    # Przykładowe popularne kolory harmoniczne w odcieniach zieleni
    popular_colors = [
        '#008000',  # Zielony
        '#00b300',  # Jasny zielony
        '#66ff66',  # Zielony neonowy
        '#003300',  # Ciemny zielony
        '#99ff99',  # Biały zielony
        '#669966',  # Oliwkowy
        '#1f8a1f',  # Ciemnozielony
        '#006600'  # Ciemny zielony
    ]

    # Jeśli żądana liczba kolorów jest większa niż dostępne kolory, ogranicz do dostępnych
    num_colors = min(num_colors, len(popular_colors))

    palette = popular_colors[:num_colors]

    return palette


# Przykład użycia
num_colors = 18  # Liczba kolorów w palecie (można zmienić według potrzeb)
palette = generate_popular_harmonic_green_palette(num_colors)

# Zapisanie kolorów do listy
kolory = palette.copy()

# Wyświetlenie kolorów
print("Wygenerowane kolory:", kolory)

# Wizualizacja kolorów
plt.figure(figsize=(8, 2))
plt.bar(range(len(palette)), [1] * len(palette), color=palette)
plt.xticks(range(len(palette)), palette)
plt.title('Paleta popularnych kolorów harmonicznych zielonych')
plt.show()