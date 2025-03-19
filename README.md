> [!WARNING]
> Тут только код для парсинга и создание файлов SQLite и CSV из xlsx файла.

# CIAN Parser

Скрипт на Python для обработки выгрузки из сайта [cian.ru](https://cian.ru) и экспорта данных в CSV и SQLite.

## 📥 Как получить файл с данными

1. Перейдите на сайт [https://city.cian.ru/kupit-kvartiru/](https://izhevsk.cian.ru/kupit-kvartiru/)  
   (можно заменить `city` на нужный вам город).
2. Пролистайте страницу в самый низ.
3. Нажмите кнопку **«Сохранить файл Excel»**.
<img src="https://github.com/user-attachments/assets/28de8aea-1d03-4d13-ab86-0c3c274dd93b" alt="image" width="400">

4. Скачанный файл `offers.xlsx` поместите в папку со скриптом.

## 🚀 Как запустить

1. Установите зависимости:
   ```bash
   pip install pandas openpyxl

2. Запустите скрипт `main.py` 

   
3. Изменится структура проекта
``` shell
cian-parser/
├── main.py       # основной скрипт
├── offers.xlsx   # файл, загружаемый вручную с cian.ru
├── offers.csv    # + файл, результат в CSV
├── offers.db     # + файл, база данных SQLite
└── README.md     # описание проекта
```

4. Используйте CSV или SQLite согласно методическим указаниям НИР. 

> [!TIP]
> Можете посмотреть мою реализацию [тут](https://github.com/AniCatPro/NIR).
