##  Оптимизация поиска по биографии
**Задание:**
Предложите метод оптимизации поиска по полю bio для точного совпадения биографии респондента с записью из другой базы данных. Возможно, вам потребуется изменить структуру таблицы или предложить использование специализированных индексов или технологий. Опишите ваше решение и предложите необходимые изменения в структуре таблицы

**Я использую MySQL 9, так как в нем есть LONGTEXT, и есть UUID в виде CHAR(36), прямого UUID нет**

###  Решение 1

  

1.  **Создание отдельной таблицы для биографий**

Создание отдельной таблицы для хранения биографий позволит более эффективно управлять данными и индексами

  

```sql
CREATE  TABLE bios (
bio_id INT AUTO_INCREMENT PRIMARY KEY,
respondent_id CHAR(36) NOT NULL,
bio LONGTEXT,
FOREIGN KEY (respondent_id) REFERENCES evaluations(respondent_id)
);
```

2.  **Изменение существующей таблицы**

  

В таблице evaluations удаляю поле bio, оно теперь хранится в таблице bios

  

```sql
CREATE  TABLE evaluations (
respondent_id CHAR(36) PRIMARY KEY,
department_id CHAR(36),
name  VARCHAR(64),
gender BOOLEAN,
value  INTEGER
);
```
  

###  Решение 2

1.  **Индексация по полю bio**

Индексы позволят MySQL быстро находить строки, соответствующие условиям запроса, не проходя всю таблицу

тут я заиндексировал первые 255 символов в поле bio, cчитаю полезным если это краткие биографии

```sql

CREATE  INDEX idx_bio ON bios(bio(255));
```

Минус если количество больше 255, то может произойти пропуск совпадений

1.1 **Пример использования:**
```sql
SELECT *
FROM bios
WHERE bio = 'Exact text';
```


2.  **Полнотекстный индекс**
Создание таблицы с нуля выглядело бы так 
```sql
CREATE  TABLE evaluations (
respondent_id CHAR(36) PRIMARY KEY, -- ID респондента
department_id CHAR(36), -- ID департамента
name  VARCHAR(64), -- имя респондента
bio LONGTEXT, -- биография респондента
gender BOOLEAN, -- пол: true - мужчина, false - женщина
value  INTEGER, -- Оценка
FULLTEXT  INDEX idx_bio (bio) -- Полнотекстовый индекс для поиска по биографии
);
```
Но она у нас существует, поэтому напишем:
```sql
ALTER TABLE evaluations
ADD FULLTEXT INDEX idx_bio (bio);
```
Из документации выходит минус, то что полнотекстовые индексы могут использоваться только с типами
CHAR, VARCHAR и TEXT, а у нас LONGTEXT

**Пример использования:**
```sql
SELECT *
FROM evaluations
WHERE MATCH(bio) AGAINST('search term' IN NATURAL LANGUAGE MODE);
```