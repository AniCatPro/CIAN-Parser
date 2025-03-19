import pandas as pd
import sqlite3

file_path = "offers.xlsx"
df = pd.read_excel(file_path)
columns_to_drop = ["ID", "Телефоны", "Описание", "Название ЖК"]
df_parsed = df.drop(columns=columns_to_drop).copy()
df_parsed[['Площадь общая', 'Площадь жилая', 'Площадь кухни']] = df_parsed['Площадь, м2'].str.split('/', expand=True)
df_parsed.drop(columns=['Площадь, м2'], inplace=True)
dom_split = df_parsed['Дом'].str.extract(r'(?P<Этаж>\d+)/(?P<Этажей>\d+),?\s*(?P<Тип_дома>.+)?')
df_parsed = pd.concat([df_parsed.drop(columns=['Дом']), dom_split], axis=1)
df_parsed['Цена'] = df_parsed['Цена'].str.extract(r'(\d+)').astype(float)

csv_output = "offers.csv"
df_parsed.to_csv(csv_output, index=False, sep=';')
print(f"CSV сохранён в {csv_output}")

sqlite_output = "offers.sqlite"
conn = sqlite3.connect(sqlite_output)
df_parsed.to_sql("offers", conn, if_exists="replace", index=False)
conn.close()
print(f"SQLite база сохранена в {sqlite_output}")
