# README.md

# LSB Steganography Detector 🔍🖼️

Мощный инструмент для обнаружения стеганографии LSB в изображениях с улучшенной точностью обнаружения и детальной статистикой.

## Особенности ✨

- Анализ отдельных файлов и целых директорий
- Цветовая визуализация результатов
- Поддержка популярных форматов изображений (JPG, PNG, BMP и др.)
- Статистический анализ с использованием χ²-теста
- Подробные отчеты с метриками
- Кроссплатформенная работа

## Установка ⚙️

1. Клонируйте репозиторий:
git clone https://github.com/sudor269/scan_lsb.git
2. Активируйте venv:
python3 -m venv venv; source venv/bin/activate
3. Установите все необходимые библиотеки:
pip install -r requirements.txt

# Использование 🚀
1. Анализ файла:
python scanner.py -f path/to/image.jpg
2. Анализ директории:
python scanner.py -d path/to/images_folder

# Поддерживаемые форматы 📁
JPEG/JPG; PNG; BMP; GIF; TIFF; WEBP

# Алгоритм работы 🧠
1. Конвертация изображения в RGB

2. Разделение на цветовые каналы

3. Расчет гистограммы распределения значений

4. Вычисление χ²-статистики для каждого канала

5. Сравнение среднего значения с пороговым уровнем (340)

6. Формирование отчета

# Ограничения ⚠️
1. Не обнаруживает сложные методы стеганографии

2. Возможны ложные срабатывания

3. Точность зависит от качества исходного изображения

# Лицензия 📄

```markdown
# EULA.md

# End-User License Agreement (EULA)  
**Версия 1.0**  
*Для проекта "LSB Steganography Detector"*

---

## 1. Принятие условий  
Используя данное программное обеспечение, вы соглашаетесь с условиями настоящего соглашения. Если вы не согласны с любыми пунктами, использование ПО запрещено.

---

## 2. Лицензионные права    
- Использовать ПО в любых целях  
- Модифицировать исходный код  
- Распространять копии  
- Использовать в коммерческих продуктах  

---

## 3. Ограничения  
Запрещается:  
1. Использовать ПО для незаконной деятельности  
2. Обратное проектирование с целью извлечения скрытых алгоритмов  
3. Распространять модифицированные версии без явного указания изменений  
4. Использовать результаты работы ПО как юридическое доказательство без экспертной проверки  

---

## 4. Отказ от гарантий  
ПО предоставляется **«как есть»** без каких-либо гарантий:  
- Не гарантируется корректность результатов анализа  
- Не гарантируется совместимость с будущими версиями ОС  
- Не гарантируется отсутствие скрытых уязвимостей  

---

## 5. Ограничение ответственности  
Разработчик не несет ответственности за:  
- Ложные срабатывания/пропуски при анализе  
- Ущерб, вызванный использованием/неиспользованием ПО  
- Потерю данных в процессе работы  
- Юридические последствия использования ПО  

---

## 6. Конфиденциальность  
Программа:  
- Не собирает персональные данные  
- Не передает информацию третьим лицам  
- Не сохраняет результаты проверок  

---

## 7. Прекращение лицензии  
Ваши права автоматически прекращаются при:  
- Нарушении любых условий EULA  
- Попытке обхода технических ограничений  
- Использовании в целях нарушения авторских прав  

---

*Дата вступления в силу: 01.01.2025*  
