# ML System Design Doc - [RU]
# Дизайн ML системы - SciTranslate
## Термины и Сокращения
* NMT - neural machine translation. Нейросетевой перевод
* MVP - minimum viable product. Минимально жизнеспособный продукт
* API - application programming interface. Программный интерфейс 
## 1. Цели и предпосылки
### 1.1. Зачем идем в разработку продукта?
* Бизнес-цель: внедрить современные нейросетевые модели в процесс перевода научных статей в англоязычных версиях журналов Кристаллография, Нанотехнологии, Оптика и Спектроскопия, издаваемых Российской Академией Наук.   
* Использование нейросетевого машинного перевода (NMT) позволит уменьшить время, затрачиваемое на перевод статей. Сейчас переводчики используют полуавтоматизированную обработку текста с помощью самописных скриптов на Delphi. Текст после такой обработки требует значительного преобразования. 
* Критерий успеха итерации: уменьшение времени, затрачиваемого на перевод статей.
### 1.2. Бизнес-требования и ограничения
* Продукт должен обеспечивать терминологически и лексически точный перевод в направлении рус --> англ в доменных областях Кристаллография, Нанотехнологии, Оптика и Спектроскопия. 
* Продукт должен содержать пользовательский интерфейс, с помощью которого переводчик сможет загрузить текстовый файл на русском языке и скачать текстовый файл с переводом. Сервис должен обеспечивать перевод объемных обзорных статей, размером до 100_000 знаков. В сервисе должна быть реализована функция перевода отдельных фраз и предложений в специальном окне без загрузки файла. 
* Сервис должен сохранять информацию о действиях пользователей, оригиналы статей и результаты переводов. 
* Требования к быстродействию системы не предъявляются. Требования к сохранению форматирования текста не предъявляются. 
* Временные ограничения на разработку продукта - до 12.12.2023     
* Критерий успеха пилота: увеличение производительности труда переводчика, которую можно количественно оценить как уменьшение времени, затрачиваемого на перевод 1 статьи. Повышение метрик лексической и терминологической точности перевода после дообучения модели на собранных данных
### 1.3. Что входит в скоуп проекта/итерации, что не входит
Задачи текущей итерации:
* Сбор и разметка обучающих данных из архива переведенных статей
* Определение иерархии метрик оценки качества выполненных работ
* Решение задачи fine-tuning of an NMT model. Разработка ML-сервиса для дообучения и инференса модели.
* Разработка пользовательского веб-сервиса, интеграция модели.
* Разработка системы хранения пользовательских данных, статей и результатов перевода.
* Возможные пути развития проекта, не входящие в скоуп итерации:
  - добавление новых направлений перевода
  - добавление новых доменных областей перевода
  - обработка файлов в pdf формате
  - внедрение семантического поиска похожих фраз по базе выполненных переводов
  - разработка автоматических систем по сбору обучающих данных. (1) веб-парсинг литературных источников из соответствующих областей знаний и (2) система экспертной разметки перевода, где эксперт может отдельно оценивать перевод каждого предложения и выбирать лучший из нескольких вариантов перевода одного предложения.
### 1.4. Предпосылки решения
Современные SOTA модели машинного перевода часто успешно справляются с грамматикой, но могут неточно переводить отдельные термины, что недопустимо в научном переводе. Дообучение нейросетвой модели на собранных данных позволит улучшить качество общелексическое и терминологическое перевода.
## 2. Методология 
### 2.1. Постановка задачи
Что делаем с технической точки зрения: система нейросетевого машинного перевода
### 2.2. Блок-схема решения 
- MVP - сервис с опенсорсным API (например, google translate) 
- Бейзлайн - fine-tuned NLLB
Блок-схема: 
![schematic.jpg](schematic.jpg)
### 2.3. Этапы решения задачи
* Сбор сырых данных (для MVP не требуется)
  - подготовка документов с текстами статей и их переводами. На выходе -- архив, в котором каждая статья с переводом находятся в отдельных папках
* Подготовка данных для дообучения 
  - написание модуля data_preparation_module, в котором реализовано чтение word-файлов статей и переводов, токенизация на предложения, очистка от неважных для обучения разделов (например, список литературы) и сохранения в гугл-док пар предложений оригинал--перевод (для каждой статьи отдельная вкладка). 
  - ручная разметка подготовленных данных, проверка корректности токенизации русских и английских текстов и разбиения на пары предложений
* Дообучение модели (для MVP не требуется)
  - разработка микросервисной архитектуры для дообучению модели 
  - разработка пайплайна дообучения
  - дизайн экспериментов по подбору гиперпараметров, построение learning curve, loss curve 
  - реализация логирования результатов экспериментов, сохранения метрик, версионирования обучающих данных
* Оценка качества (для MVP не требуется)
  - используем общелексическую метрику качества перевода meteor (считает точное количество точных и частичных совпадений с учетом стемминга как f1 меру относительно стемов из референса). 
  - терминологическую точность перевода оцениваем с помощью метрик success rate и term consistency. Success rate считается как доля правильно переведенных терминов в датасете. Term consistency считается как доля правильных и одинаковых переводов терминов в разных контекстах. 
  - для оценки всех метрик необходимо собрать валидационные датасеты 
  - необходимым результатом этапа считаем meteor >= 50, success rate >= 0.5, term consistency >= 0.7.
* Разработка и деплой MVP
  - разработка микросервисной архитектуры, включающей в себя фронтенд (streamlit) и бекенд (FastApi) компоненты
  - реализация функций, предусмотренных описанием пользовательского use case и требованиями к продукту
* Интеграция модели в веб-сервис
  - предполагается, что деплой MVP и подготовка данных и дообучение модели производятся параллельно и независимо
  - после достижения требуемого качества, дообученная модель интегрируется в веб-сервис вместо API гугл-переводчика
  - проводится сбор обратной связи от пользователей сервиса, оценивается повышение производительности труда и результат всего проекта
* Подготовка отчета
  - подготовка обоснования выбора модели
  - сравнительный анализ метрик качества машинного перевода
  - описание экспериментов по дообучению модели
  - описание технической реализации веб-сервиса
* Закрытие технического долга


## 3. Системная архитектура (в нотации C4)
### 3.1. Level 1. Context
![Context](http://plantuml.com/plantuml/svg/hLJ1JlD66BpdAROvWTIG7dhYK24eju0G5FKO6NiBLXqxNQyBgAf4QDCUgDGUUk1Ku0r2m8f9QFeAdz-eCpYk4YUYhVGZ8MVNtyxCzyrujsBh69jqWjf7VkW6YQVLcRNTUBFPDCxvngblpvAJ9DR6ZKAhGxlXHfrcDt12dcd4rWlya-REfuq3RXtljPeT9xRQOAkzmnCNTgDBzDek5gPh_5YtjwCaz1npkUP-yh6gowsCv5a6-RMaCib_oNluDPIfaZ-n-KF-CvvJUL4oaOmr-HLhyU8glwclg-zg2dz7bs3jhCMkRuqJne5ZDQ2FNF-BSbd7Ug-byXvGo93AgmoK36I8nPGBF3EmfIWPO-U94luYdwJKGurpclARlA-8D5F-WeKoIUFmM3K-KpfixExNr-UrESOzyx-bBFaDslkIoV0zF0gMXmMrUP_DuqoA_op_zLqvCkR4MChDpLBRAccUOnqt2WBjMZyAmVkbFb4k_0-qMIMZ9uyofHGbMMMY7AACyFm9p-pVvWMKQndJIJZAWXdKb2S0G1-6gwKVQ1D7uLffTsIeysxUBc00eVusSBfCoHH7J4wHcY037a-Pk_95cKFgasSSwZ5jh99N31KISP1xLzXzvNpvNis7azO2lyWGNU2yPaJSNvcjnRwqvwEdnUxk9MMXZ8jUFdXdL2CZxA2cy0bziIFAfq54N1fmLJd3XEzGXzQFxTj7rq14U92H670S9APw-HqmKtbaGefCIyf8KH84Ff6Lqaa2nMLhUP-B2VA_tpfGy835AO6XvFjQhLR4khrxOV7LMTyDTFoM3hJsoB8YZ-0gyuWPPHGaVr1a_YDwd1zbMkPurRbYGgDIM5QzpI0-AnHZp8I5oDgX3jg72-6jN5roYvEbV_GapQzNHcyvHpYDJrTvaPjqu0Be2hP5XbK1koCVsqH3v0FB4C25yabvwv3W7o1FdKVcwnd7STNyQbFtPPQ4jmZiQsqJpOrG7oPH4YkK-w4VdiuGFwyYpjsY3yKjz9y2GnOYgQxHNSSulETc5Asbwwz2-N_cSggj2YFhVtLPZdq9VI6HGCWOaQMRFzRiL1dzJQ9ZUhYbGo_f17y3)


### 3.2. Level 2. Container
![Container](http://plantuml.com/plantuml/svg/jLRDRjj65zthAUOJleKCE1BGT9N2GE8VD0uKMpKbP5D0eAY9n6P86fnH7RSe44j9qxH1qqMtJHT5zx9hfPOjAQ_0UQEUkI8fIepGR9e0XcRc_fnpxvaxl2kL7QgU9mh_Str7zDgSTPKwbdSgbT0-ANTSrUsrUfA7Jk0hxgko4tYLOs7xnkUML6tXjYexdzwgcQt6msh5iwNY8RQQEyRZgIeV_sVHRTVduJn-mRf_-AXPspko3W-QXurwTVzWhxHHkDTkxmdk8NJTxfIAsxRpXFjjYuTVkmulRhB_owvzpBVst4vNMMwRjospBctWfDNP2KGGRXLtWj1_B88J7cwB7ZazHkxuyAJhAjeJl8F8TH3UAhRcQPYSv_dIvoO-aoP1CGVAKa5eTp9eZeAU3yljuEa7q0Y2-kHqBPODrE8KLVAQsoQE7PwMd4ysMT5ot7fe-rBOneXzMs3ubrQnTC9RZNsOFU8j5br5KzsFHlgPVXwDeh4-GoRW3Bdj2LTjijgfwWQ-sOn-ZsRHtz45_jxeDt3fi-WzBLvZUuQ3eOc4zSyicc9nfllwMJH42ZhIhv6jWjLDTCNq6GMxn75oIBRdqKo_H90Hm_arK0sYTrXEuOQjIvEPmMzeFFLB0m3GOG1KPWibMURg2z7oWZON8F2mYhJ67jPNSw87rUesetDY-5k26j76qNKqp216-1d-d-i102Q8z0-4-GO7KrC25aq8o8XSIYQOSITssBmiOqMiZRz-ima2ymFueQ1KDX2SKKp2GbLZkb-EtfStZ0gKtP5iYwq8F4VS4qR8nDhyCFHmjTJZ8FI8wXycCrN_Pb7VTmHlIXjJ_LCqOVfxR5qJmSaIkJjClw00quNxbQ4pCDZ9QKZEuwmR5FOPesX_WV-pkMeIToe1Dk5BiIwmFZCcvPXTZOSoy4igrdOGaYgp2a1hu4q4VuakKD0PnOlb6RCQhzCjkdH6VQR23yXgmWWD7B57UWHCkZD3d573Z22cH6csJf0nyhQjREcut5UkLDIRMs085whKqDJDf27yl-Ra5bUO0YENxXDuKkbbGaw_I6x9GRMsrB1LXUosIavFgi3ZORFTGiPTW6lPafDK0gaw8RU-g1AMFtETHgxdLDp9lCqnCWOuCsCObsIY1oibqOFDL0067zfbT92zc8PMmYAcUKu0uac0xIwtXUgYNIGIMCHeXjaR8kDfcoSkRuFLOUihxYYscCb5wpQnVOjqFoBLDG8R4gE5r6aKw5UBMNJiEay4PoL3df12BESm7Ul-1WCe_2As5ny7p1681mmOyptFjqEMRSgEERmVz2J_S5EcSKFIYvMLH4uV6N5HJJy2OCbsmtYgtADV-R7o5hcler4wHMDzfjKnMslX63zIImhAUDwGyTAqM7a4C1y7g-ECVAdyIOIXAOqP9TyL2eKZBff7IvCaUHKRaaj3vNwzNhDWJPQhDpSjH6hkX87FP9SBiSudVOhM96cavVrNqzs5gITMWDohxSTMrL9oI7fF32mUkhPmlx6L6_YfAKpoiNQvp1iZUmPVhDYy73zESy2B4UGw25t81OzxGhBg9mrEFpveK9mZVD-4ogI0s6Wil4hIq9XcZNtION7-vMC5U3vLoYZEbCbDSu3kV-Q9NFjo08pHzdZDQCHKMtYY0iJSbgU-iyaUu3ksigos38piZCvNEV_UmEZ1xlOErJF-LAxkVRvti8jFvBlSR_SyyGy0)
