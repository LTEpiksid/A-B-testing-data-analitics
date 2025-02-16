import sqlite3
import random

# Nustatykite duomenų kiekį
N = 1000

# Sukuriame arba prisijungiame prie SQLite duomenų bazės failo
conn = sqlite3.connect('duomenu_baze.db')
cursor = conn.cursor()

# Sukuriame lentelę (jei dar nėra)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ab_test_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grupė TEXT,
        konversija INTEGER
    )
''')

# Išvalome lentelę, jei norite pradėti nuo švarios bazės (pasirinktinai)
cursor.execute('DELETE FROM ab_test_data')

# Sugeneruojame ir įrašome atsitiktinius duomenis
for _ in range(N):
    # Atsitiktinai priskiriame grupę: 50% tikimybė abiems
    group = random.choice(['A', 'B'])
    # Pavyzdžiui: jei grupė A – 10% tikimybė konversijai, grupė B – 12%
    if group == 'A':
        conversion = 1 if random.random() < 0.10 else 0
    else:
        conversion = 1 if random.random() < 0.12 else 0

    # Įrašome į lentelę
    cursor.execute('INSERT INTO ab_test_data (grupė, konversija) VALUES (?, ?)', (group, conversion))

# Išsaugome pakeitimus ir uždarome ryšį
conn.commit()
conn.close()

print("Duomenys sėkmingai sugeneruoti ir įrašyti į duomenu_baze.db")
