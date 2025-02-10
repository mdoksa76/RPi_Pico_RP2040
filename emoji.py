# Rasponi Unicode znakova za emoji
ranges = [
    (0x1F600, 0x1F64F),  # Osnovni emotikoni
    (0x1F300, 0x1F5FF),  # Razni simboli i piktogrami
    (0x1F680, 0x1F6FF),  # Transport i mape
    (0x1F900, 0x1F9FF),  # Dodatni emotikoni
    (0x1F700, 0x1F77F),  # Simboli i piktogrami
]

# Funkcija za ispis emoji znakova
def print_emojis():
    for start, end in ranges:
        for code in range(start, end + 1):
            print(chr(code), end=' ')
        print()

# Poziv funkcije
print_emojis()
