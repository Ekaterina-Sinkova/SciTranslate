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
![Container](http://plantuml.com/plantuml/svg/jLPDQnjN5DthLxoABcHm92XT5GofRD4aoBBYaSYc86OqBzAGqOoPzrJ7b48i9qrBJ9r5eQj-RBgN7RkHPKl-2s_-KS-zprL6aoZTj0aOvjsFUywv7_PTfTr43mTXuPCWweP3Nug-rdlgYqebSVVBlK3tXzvGoQGRHrf6kjoD1vMzq8qevexIVXXubStFxpJfgRrThmnSfMM2fyucHJpLvRt_BRiRH3An-GlElPr7dMPjrzbfT7RQhVhzHgsqLlZIzskX721ro-sLYbMt-qH6lYEJRuAkBAwBJrNVtPCRjQ3NrqxWIz-Xxz8QB5vlCmxZPAEu6IVHup3Ubqar77BGOzI-DUxt0yrleUmXSmk4DugUBIEKhVDr92c_K5IW-1ueHyU9sykWsOs74JohyTCFe0aPwfE3bLZMeCK1L1fqgfJ7JGvAtS_MHT7f1gt4ZLJeafFujY3mRw5YQLzwxVjmUoGzOIPcbexCHVeiVMukp6LwY4h0cKXt40PwNJGFT3-EwD7yRkRchJd3pwlq124ZOMxuunZFSnZ6b0dVFmapmyTXEagVcJ5Ai2azHhKAlgxCHAI7dEpSZ1T6zZqry_Gbabm8sAT0TMJ-mkSCONWwfye2SMEAJ5yI04270w724oHPvXg5eJU8VHc2m7OTPSaVtXDBj56lLmNRcU6l2zHpSsccPfn1ZFHp_3zDZnYWHPJ-m9YlO9YH1C9SCv0B3YbHCWfdTdWyB-EBMLDyUh8E0jQ0E0ZAie7Wd7Co5bPDfAEokIclqHHejwV4XiWFU9xuG2g5KSFA4NFx8Qf3HJntNSyBzFP3srMhe1MK65jqi_HL-eAbPkiRmBNAJ5YTiwmJK0Cpj6KDI9R3HJD7kMmVRrnJ9YgEIlfsUkE44MPTWN5YfepyjJb3-Zbi43MBoLokcinZGEDECfaZzheMPchtW0dYzPhwItOys-NW19XZOWWjveBwI_nk2otUFyvB-W4uBRFxmsflffRBVywCqRp52toe6yphNNlILumvBt0UkUzgLtK36Ub0QTwbE-aX1tuFzp79GOKP_SyVM1GpOU00-8QgClHfVjfkzxjHRoxjKNwsjxnITwXqF919n_TGSGlWF5T9gjwCbUubqdbOPon_CjDP1WTgFITfKM7Cu2qo0JXpSWJe6McN7kM5ESgkdxAd7DY-AnGAkpBix2wDxJz7jgqaxzozLglfm9iyw_b1-1V_Tbx-x5NB1rWmMvdBjyXjVeFoDwp8sUA6yoK-XVuZkaYB6pldTft1vKSMZssqwEtxh5VH_W9nObmXpJYfA5TQmeUYvfGLHSb56rODCS1G6ovNz0apzYuIytL2A5nr47NNnGDdfr5P5g6U5M7f89hNo4GbNl0ro-nMfk6hadEpiwcNf_7zcSlV13WzsAfk8bLMjZp4NyoOcuMDjifRwijhDSxpM7s7RlzmgjU-gZMsIck5kpBoXuFmRm00)