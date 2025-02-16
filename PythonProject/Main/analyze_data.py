import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Prisijungiame prie SQLite duomenų bazės
conn = sqlite3.connect('duomenu_baze.db')

# Nuskaitykite duomenis į pandas DataFrame
df = pd.read_sql_query("SELECT grupė, konversija FROM ab_test_data", conn)
conn.close()

print("Pirmos kelios duomenų eilutės:")
print(df.head())

# Apskaičiuojame konversijos rodiklius pagal grupes
group_stats = df.groupby('grupė')['konversija'].agg(['mean', 'count'])
print("\nGrupės statistika:")
print(group_stats)

# Paruošiame kontingencijos lentelę
contingency_table = pd.crosstab(df['grupė'], df['konversija'])
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
print("\nChi-kvadrato testo rezultatai:")
print("Chi2:", chi2)
print("P reikšmė:", p)

# Vizualizuojame konversijos rodiklius pagal grupes
plt.figure(figsize=(8, 5))
group_stats['mean'].plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Konversijos rodiklis pagal grupes')
plt.xlabel('Grupė')
plt.ylabel('Vidutinis konversijos rodiklis')
plt.ylim(0, 0.2)
plt.axhline(y=group_stats['mean'].mean(), color='gray', linestyle='--', label='Bendras vidurkis')
plt.legend()
plt.tight_layout()
plt.show()
