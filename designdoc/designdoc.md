# ML System Design Doc - [RU]
# Дизайн ML системы - SciTranslate
## 1. Цели и предпосылки
### 1.1. Зачем идем в разработку продукта?
* Бизнес-цель: внедрить современные нейросетевые модели в процесс перевода научных статей в англоязычных версиях журналов Кристаллография и Оптика и Спектроскопия, издаваемых Российской Академией Наук.   
* Использование ML позволит уменьшить время, затрачиваемое на перевод статей. Сейчас переводчики используют полуавтоматизированную обработку текста с помощью самописных скриптов на Delphi. Текст после такой обработки требует значительного преобразования. 
* Критерий успеха итерации: уменьшение времени, затрачиваемого на перевод.
### 1.2. Бизнес-требования и ограничения
* Бизнес-требования: продукт должен обеспечивать перевод в направлении рус --> англ и терминологическую точность в доменных областях Кристаллография, Оптика и Спектроскопия. Продукт должен содержать пользовательский интерфейс, с помощью которого переводчик сможет загрузить текстовый файл на русском языке и скачать текстовый файл с переводом. Сервис должен обеспечивать перевод объемных обзорных статей, размером до 100_000 знаков. Требования к быстродействию системы не предъявляются. Требования к сохранению форматирования текста не предъявляются. 
* Бизнес-ограничения: Временные ограничения на разработку продукта - до 12.12.2023     
* Критерий успеха пилота: увеличение производительности труда переводчика, которую можно количественно оценить как уменьшение времени, затрачиваемого на перевод 1 статьи.
* Возможные пути развития проекта, не входящие в скоуп итерации:
  - добавление новых направлений перевода
  - добавление новых доменных областей перевода
  - добавление в интерфейс окна для перевода текста произвольной длины без загрузки файлов
  - обработка файлов в pdf формате
  - разработка автоматических систем по сбору обучающих данных. (1) веб-парсинг литературных источников из соответствующих областей знаний и (2) система экспертной разметки перевода, где эксперт может отдельно оценивать перевод каждого предложения и выбирать лучший из нескольких вариантов перевода одного предложения.

## 2. Методология 
### 2.1. Постановка задачи
Что делаем с технической точки зрения: система по машинному переводу
### 2.2. Блок-схема решения 
- MVP - сервис с опенсорсным API (например, DeepL) 

    Блок-схема:  TODO
- Бейзлайн -  дообученная модель NLLB

    Блок-схема: 

![img.png](img.png)
### 2.3. Этапы решения задачи
TODO: заполняется отдельно для бейзлайна, отдельно для mvp


## 3. Системная архитектура (в нотации C4)
### 3.1. Level 1. Context
![Context](http://plantuml.com/plantuml/svg/hLJ1JlD66BpdAROvWTIG7dhYK24eju0G5FKO6NiBLXqxNQyBgAf4QDCUgDGUUk1Ku0r2m8f9QFeAdz-eCpYk4YUYhVGZ8MVNtyxCzyrujsBh69jqWjf7VkW6YQVLcRNTUBFPDCxvngblpvAJ9DR6ZKAhGxlXHfrcDt12dcd4rWlya-REfuq3RXtljPeT9xRQOAkzmnCNTgDBzDek5gPh_5YtjwCaz1npkUP-yh6gowsCv5a6-RMaCib_oNluDPIfaZ-n-KF-CvvJUL4oaOmr-HLhyU8glwclg-zg2dz7bs3jhCMkRuqJne5ZDQ2FNF-BSbd7Ug-byXvGo93AgmoK36I8nPGBF3EmfIWPO-U94luYdwJKGurpclARlA-8D5F-WeKoIUFmM3K-KpfixExNr-UrESOzyx-bBFaDslkIoV0zF0gMXmMrUP_DuqoA_op_zLqvCkR4MChDpLBRAccUOnqt2WBjMZyAmVkbFb4k_0-qMIMZ9uyofHGbMMMY7AACyFm9p-pVvWMKQndJIJZAWXdKb2S0G1-6gwKVQ1D7uLffTsIeysxUBc00eVusSBfCoHH7J4wHcY037a-Pk_95cKFgasSSwZ5jh99N31KISP1xLzXzvNpvNis7azO2lyWGNU2yPaJSNvcjnRwqvwEdnUxk9MMXZ8jUFdXdL2CZxA2cy0bziIFAfq54N1fmLJd3XEzGXzQFxTj7rq14U92H670S9APw-HqmKtbaGefCIyf8KH84Ff6Lqaa2nMLhUP-B2VA_tpfGy835AO6XvFjQhLR4khrxOV7LMTyDTFoM3hJsoB8YZ-0gyuWPPHGaVr1a_YDwd1zbMkPurRbYGgDIM5QzpI0-AnHZp8I5oDgX3jg72-6jN5roYvEbV_GapQzNHcyvHpYDJrTvaPjqu0Be2hP5XbK1koCVsqH3v0FB4C25yabvwv3W7o1FdKVcwnd7STNyQbFtPPQ4jmZiQsqJpOrG7oPH4YkK-w4VdiuGFwyYpjsY3yKjz9y2GnOYgQxHNSSulETc5Asbwwz2-N_cSggj2YFhVtLPZdq9VI6HGCWOaQMRFzRiL1dzJQ9ZUhYbGo_f17y3)


### 3.2. Level 2. Container
![]()
