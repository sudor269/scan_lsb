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

1. Убедитесь, что у вас установлен Python 3.8+
2. Клонируйте репозиторий:
git clone https://github.com/sudor269/scan_lsb.git

# Использование 🚀
Анализ файла:
python scanner.py -f path/to/image.jpg
Анализ директории:
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
Проект распространяется под лицензией MIT.


```markdown
# LICENSE.md

# Пользовательское соглашение и лицензия

## Лицензионное соглашение MIT

Copyright (c) [Год] [Ваше имя или название организации]

Настоящим предоставляется бесплатное разрешение любому лицу, получившему копию данного программного обеспечения и сопутствующей документации ("Программное обеспечение"), работать с Программным обеспечением без ограничений, включая, но не ограничиваясь правами на использование, копирование, изменение, объединение, публиковать, распространять, сублицензировать и/или продавать копии Программного обеспечения, а также разрешать лицам, которым предоставляется Программное обеспечение, при соблюдении следующих условий:

Вышеуказанное уведомление об авторских правах и данное разрешение должны быть включены во все копии или существенные части Программного обеспечения.

ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ ГАРАНТИЯМИ ТОВАРНОЙ ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ НАЗНАЧЕНИЮ И ОТСУТСТВИЯ НАРУШЕНИЙ. НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ ОТВЕТСТВЕННОСТИ ЗА ЛЮБЫЕ ИСК, УЩЕРБ ИЛИ ИНУЮ ОТВЕТСТВЕННОСТЬ, БУДУТ ЛИ ОНИ В РЕЗУЛЬТАТЕ ДОГОВОРА, ДЕЛИКТА ИЛИ ИНЫМ ОБРАЗОМ, ВОЗНИКШИЕ ИЗ, ИМЕЮЩИЕ ПРИЧИНОЙ ИЛИ СВЯЗАННЫЕ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ИСПОЛЬЗОВАНИЕМ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИЛИ ИНЫМИ ДЕЙСТВИЯМИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.

## Условия использования

1. **Запрещено** использование для незаконной деятельности
2. **Обязательное** указание авторства при модификациях
3. **Рекомендуется** тестирование на контрольных образцах
4. **Ограничение ответственности**: Разработчик не несет ответственности за:
   - Ложные срабатывания
   - Пропущенные артефакты
   - Любые косвенные убытки
   - Повреждение данных

## Соглашение о конфиденциальности

Программа не собирает и не передает:
- Анализируемые изображения
- Персональные данные пользователей
- Результаты проверок
- Системную информацию

## Изменения в соглашении

Условия могут меняться без предварительного уведомления. Актуальная версия всегда доступна в репозитории проекта.
Это профессиональная документация, которая:

Полностью покрывает функционал

Имеет четкую структуру

Содержит необходимые юридические аспекты

Легка для понимания

Визуально привлекательна

Вы можете разместить эти файлы в корне репозитория. Для большей наглядности рекомендую добавить:

Скриншоты работы

Badges из shields.io

Диаграмму работы алгоритма

Ссылку на демо-версию (если есть)
