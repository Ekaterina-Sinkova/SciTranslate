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
![Container](http://plantuml.com/plantuml/svg/jLPDQnjN5DthLxoABcIm9IXT5GofRD4uoB9YIMHJ43EQ5sd8QCRCUwfZIY6sagObfiwYq5K_DjtBZjr8jYN_XJV_gEVU9oMZgKKtRGA6kH_tddFklSz-eBGJwq4_o7tYXvrWu4dHq_f0VL4gnSvXiUlhti0TA1bteb3BK1SxKRzq43WXvMmexGM-MzhwVADEfjPkjTHtb9OnJEqjodYkYmV_MtN73sLiw-SQ3_UUjEkL_SPUhRtNQbPtQfN2MkvBpwi4ie_IJQTRo9UTpZCPUWqPV-DtP7vTVAfwpe7ShFZTdcxudlGQz5rOWyVjRaL156_cjw8uV1f4Xp8k1mDEUehUS-TXpzTi2sGNbPiWl9btRHkXR9-lGqdrXQ86-N-0QkWeThefDFlH84HaENf-3vg0eJuxMebb3LeSGQL-kqnrdFYeqFbiNUGR7RyPEw4A70eIt-O4_drGiN0etTOEmfv8LvYncIOdvYfvaRmqLsQI7ACJSCRIwGU-NXVr8zsBGZAQtytCl3SN-7cJd27bH9Wx_ZY5UGR7Y2hX-oTXflWuJawI5sQ45knAJj6jXAyRCnR9CHUxX7lXvDXpCqjUeyYLWFyQg8RcBtnEaGRJ9NKMo1jHPlAQ000w0WWLJ91acMiO16u_ycG00hjLjALuH8yjqLgrMXRiPuQ_Bb2ZsiHScr4ACShFyFyy6J90YoZvWJ7Vm34b2OIvPI1Nd5AWOfJEx62yBEABMLD-ShOE0jQ1F0ZAie7WZ6io5bPD92T5SrTSeotGJbU9JP5Ty2pnlbGAguQJ8-RsGvG7YdZkEwxhwzt7ywbQ1LbGCu94pF8D8v-msEn_1y1Mcp7hSy4afWXynUC6QgIo2YJCyOTndgG3GPT73b54CgHGrlKMTAscapcJkenL51RqV8-ZE8sLfmsqOtFD7DwQ2xIPmGTvqzZCPDMEdW8YpvH93JdgLfXhUn5C5DPRGaL-cEsPS07QQ3259ZD1aoQUyqOB-whLdFEIdWzEo-p-i5CmrvRBVywCqRo71J4q5URrSKp96yQS5JYBt7Eqepg-3BMlD5_LHdBCYTyZV4HoK6D6__Cz9sF631m0tr5NXiwNTfdU4tlfjMfzwQAoMxxj5Ze3fQE-ZDkUYuxR0ESwIbBtUgHqDvQDnrN6yYSpdQPmeDTBaXOTHWpU8XE0CwD0W9wITiamAymmVOZAFkh0zbqkbzkNGNj_QMqNpsrBIRw-XyrclO5eYgnc5-5VubjP-TFlMpR1WjbElu6BskOtAB-unSLhdhvyY3-V0MntzgYJ7rayzj71jtPOhxpzLTA8y1vfmibDkLCA7pSrvwmeMYx6i7A90OR6C5an9-pOnqpirncXSDHHs5aNZnfxjTAo2DMq24jFetcBIjJY5RzggTjA3NnLSHvskdHw6-_RkUoRWA17s-Kjb4hBbeNuYndni73HLdbBVVciHbaUgz-X-PzGrSfNbTfsOIttG8RUe1_y3G00)