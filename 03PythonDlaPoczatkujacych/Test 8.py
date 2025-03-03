import matplotlib.pyplot as plt
import colorsys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return '#' + ''.join(f'{c:02x}' for c in rgb_color)

def generate_harmonic_colors(base_colors, num_variations=5):
    harmonic_colors = []

    for color in base_colors:
        rgb = hex_to_rgb(color)
        # Generowanie harmonijnych odcieni
        for i in range(-num_variations, num_variations + 1):
            # Użyj funkcji colorsys do manipulacji kolorem
            h, l, s = colorsys.rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
            new_luminance = max(0, min(1, l + (i * 0.1)))  # Zmiana jasności
            new_rgb = colorsys.hls_to_rgb(h, new_luminance, s)
            harmonic_colors.append(rgb_to_hex(tuple(int(c * 255) for c in new_rgb)))

    # Usunięcie duplikatów i sortowanie
    unique_harmonic_colors = list(set(harmonic_colors))
    sorted_harmonic_colors = sorted(unique_harmonic_colors, key=hex_to_rgb)

    return sorted_harmonic_colors

# Przykład użycia
base_colors = ['#006400', '#008000', '#66ff66']  # Lista bazowych kolorów
harmonic_colors = generate_harmonic_colors(base_colors)

# Wyświetlenie wygenerowanych kolorów
print("Wygenerowane harmonijne kolory:", harmonic_colors)

# Wizualizacja kolorów
plt.figure(figsize=(10, 2))
plt.bar(range(len(harmonic_colors)), [1] * len(harmonic_colors), color=harmonic_colors)
plt.xticks(range(len(harmonic_colors)), harmonic_colors)
plt.title('Harmonijne kolory')
plt.show()