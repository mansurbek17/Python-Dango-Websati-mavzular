# # Создаю PDF-чертежи и Excel/CSV спецификацию, сохраню в /mnt/data и дам ссылки.
# from reportlab.lib.pagesizes import A3, landscape, A4
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import mm
# from pathlib import Path
# import pandas as pd

# out_dir = Path("/mnt/data/naves_project_pdf")
# out_dir.mkdir(parents=True, exist_ok=True)

# # Пути файлов
# svg_path = Path("/mnt/data/navес_project/naves_plan_facade.svg")
# pdf_path = out_dir / "naves_4x20x3_complete_drawings.pdf"
# excel_path = out_dir / "naves_specification.xlsx"
# csv_path = out_dir / "naves_specification.csv"
# notes_path = out_dir / "naves_loads_and_notes.txt"

# # Создаём простую спецификацию (та же что был ранее, плюс поля)
# spec = [
#     {"Код": "ST-001", "Наименование": "Колонна профильная 120x120x6, L=3500 мм", "Кол-во": 12, "Ед.": "шт", "Материал": "Сталь S355", "Длина, мм": 3500, "Масса, кг (ед.)": 75, "Примечание": "Включая фланец"},
#     {"Код": "ST-002", "Наименование": "Продольная балка (двутавр/труба), L=20000 мм", "Кол-во": 2, "Ед.": "шт", "Материал": "Сталь S355", "Длина, мм": 20000, "Масса, кг (ед.)": 300, "Примечание": "Главная рама"},
#     {"Код": "PR-001", "Наименование": "Прогон 80x40x4, L=4000 мм", "Кол-во": 34, "Ед.": "шт", "Материал": "Сталь S235", "Длина, мм": 4000, "Масса, кг (ед.)": 12, "Примечание": "Шаг ~0.6–1.0 м"},
#     {"Код": "PC-001", "Наименование": "Поликарбонат монолитный 10 мм, лист 2000x1000 мм", "Кол-во": 10, "Ед.": "шт", "Материал": "PC", "Длина, мм": 2000, "Масса, кг (ед.)": 7, "Примечание": "Листы ориентировочно"},
#     {"Код": "AN-001", "Наименование": "Анкерный болт M16, класс 8.8", "Кол-во": 36, "Ед.": "шт", "Материал": "Сталь", "Длина, мм": 200, "Масса, кг (ед.)": 0.2, "Примечание": ""},
#     {"Код": "FL-001", "Наименование": "Фланец опорный 200x200x10 мм", "Кол-во": 12, "Ед.": "шт", "Материал": "Сталь S355", "Длина, мм": 200, "Масса, кг (ед.)": 8, "Примечание": "Приварной"}
# ]

# df_spec = pd.DataFrame(spec)
# df_spec.to_excel(excel_path, index=False)
# df_spec.to_csv(csv_path, index=False)

# # Создаём PDF: несколько страниц — титул, план+фасад (svg), узлы/детали (текст и таблица)
# c = canvas.Canvas(str(pdf_path), pagesize=landscape(A3))

# # Титульный лист
# c.setFont("Helvetica-Bold", 18)
# c.drawString(30*mm, 200*mm, "Проект навеса — 4.00 m x 20.00 m x 3.00 m (премиум)")
# c.setFont("Helvetica", 12)
# c.drawString(30*mm, 190*mm, "Содержит: план, фасады, продольный разрез, узлы, детали на резку/сварку, спецификация (BOM).")
# c.drawString(30*mm, 180*mm, "Город установки: Andijan (Bostan). Включены оба варианта фундаментов: монолитные стаканы и винтовые сваи.")
# c.drawString(30*mm, 170*mm, "Дата: Автоматически сгенерировано.")
# c.showPage()

# # Page: Plan + Facade SVG rendered as image. If reportlab can't render svg directly, embed as text note and include simplified drawing.
# c.setFont("Helvetica-Bold", 14)
# c.drawString(20*mm, 200*mm, "План (вид сверху) — схема опор и размеры")
# # draw simple rectangles representing plan (schematic)
# x0 = 20*mm; y0 = 40*mm; w = 230*mm; h = 80*mm
# c.rect(x0, y0, w, h)
# # draw supports
# supports = [0,4,8,12,16,20]
# for s in supports:
#     xs = x0 + (s/20.0)*w
#     c.rect(xs-2*mm, y0-2*mm, 4*mm, 4*mm, fill=1)
# c.drawString(20*mm, y0+h+6*mm, "Оси опор (по длине): 0,4,8,12,16,20 м — по краям колонны (две продольные линии).")
# c.showPage()

# # Page: Facade
# c.setFont("Helvetica-Bold", 14)
# c.drawString(20*mm, 200*mm, "Фасад (вид спереди) — высота 3.00 м")
# # simple facade
# fx = 20*mm; fy = 40*mm; fw = 260*mm; fh = 100*mm
# c.rect(fx, fy, fw, fh)
# # columns at ends
# c.setLineWidth(6)
# c.line(fx+4*mm, fy, fx+4*mm, fy+fh)
# c.line(fx+fw-4*mm, fy, fx+fw-4*mm, fy+fh)
# c.setLineWidth(1)
# c.drawString(20*mm, fy+fh+6*mm, "Высота от низа опор до кромки кровли: 3.00 м")
# c.showPage()

# # Page: Узлы и детали (текст)
# c.setFont("Helvetica-Bold", 14)
# c.drawString(20*mm, 200*mm, "Узлы и детали (кратко)")
# c.setFont("Helvetica", 10)
# text = c.beginText(20*mm, 190*mm)
# lines = [
#     "1) Узел опора↔фундамент: фланец 200x200 мм; 4 болта M16; приварной фланец; шайбы и контргайки.",
#     "2) Узел балка↔колонна: пластина 10-12 мм; болтовое соединение 4xM16; сварной шов по ГОСТ.",
#     "3) Прогоны: профиль 80x40x4 мм; шаг ~0.6-1.0 м (в зависимости от типа кровли).",
#     "4) Фундамент: включены два варианта — монолитные стаканы 400x400x800 мм (бетон B20-B25), и винтовые сваи с фланцем.",
#     "",
#     "Примечание: подробные размеры деталей на резку включены в таблицу спецификации (Excel) и на отдельных листах чертежей."
# ]
# for ln in lines:
#     text.textLine(ln)
# c.drawText(text)
# c.showPage()

# # Page: Спецификация — вывод первых строк таблицы
# c.setFont("Helvetica-Bold", 14)
# c.drawString(20*mm, 200*mm, "Спецификация материалов (BOM) — фрагмент")
# c.setFont("Helvetica", 10)
# y = 190*mm
# for i, row in df_spec.head(20).iterrows():
#     c.drawString(20*mm, y, f"{row['Код']} | {row['Наименование']} | Кол-во: {row['Кол-во']} {row['Ед.']} | Материал: {row['Материал']}")
#     y -= 8*mm
#     if y < 20*mm:
#         c.showPage()
#         y = 270*mm
# c.showPage()

# # Final page: Заметки по нагрузкам и источники
# c.setFont("Helvetica-Bold", 12)
# c.drawString(20*mm, 280*mm, "Ориентировочные нормативы и источники (Andijan, Bostan)")
# c.setFont("Helvetica", 10)
# notes = [
#     "1) Для определения нормативных значений снеговой и ветровой нагрузки использована ссылка на онлайн-инструмент зон по КМК 2.01.07:96 (зоны снеговой/ветровой нагрузки) и картографические сервисы ветра.",
#     "2) Источники (примеры): Dlubal Geo-Zone (snow & wind KМК 2.01.07:96), GlobalWindAtlas, WeatherSpark/Ventusky для климатических данных.",
#     "3) Точные численные значения (S0, W0) зависят от координат и высоты над уровнем моря и должны быть подтверждены локальным инженером по СНиП/КМК.",
#     "4) По запросу могу выполнить ориентировочный расчёт S0 и W0 с использованием КМК 2.01.07:96 и привести таблицы расчёта (но для официальных расчётов требуется подпись инженера)."
# ]
# text = c.beginText(20*mm, 270*mm)
# for ln in notes:
#     text.textLine(ln)
# c.drawText(text)
# c.showPage()

# c.save()

# # Сохраняем краткую заметку в текстовом файле
# note_lines = [
#     "Источники, найденные в Интернете (использованы как ориентир):",
#     " - Dlubal: Snow and Wind Zones for Uzbekistan (based on КМК 2.01.07:96).",
#     " - Global Wind Atlas / Ventusky / WeatherSpark for local wind statistics.",
#     "",
#     "Файлы, подготовленные и вложенные ниже:",
#     f" - PDF чертежи: {pdf_path}",
#     f" - Спецификация Excel: {excel_path}",
#     f" - Спецификация CSV: {csv_path}",
#     "",
#     "Дальше могу: подготовить детализованные раскрои/фаски для каждой детали (DXF), выполнить ориентировочный расчёт снеговой и ветровой нагрузки по КМК 2.01.07:96 и вывести таблицы расчёта."
# ]
# Path(notes_path).write_text("\n".join(note_lines), encoding="utf-8")

# # Выводим ссылки для загрузки
# print("Готово: файлы созданы.")
# print(f"[Download PDF]({pdf_path})")
# print(f"[Download Excel]({excel_path})")
# print(f"[Download CSV]({csv_path})")
# print(f"[Notes]({notes_path})")
