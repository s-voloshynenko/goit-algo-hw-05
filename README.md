## Результати

```
Time of 'Boyer Moore' for 'алгоритмів' pattern in Text 1 document is 0.000093 secs.
Time of 'Boyer Moore' for 'CUDA' pattern in Text 1 document is 0.007220 secs.
Time of 'Boyer Moore' for 'алгоритмів' pattern in Text 2 document is 0.000961 secs.
Time of 'Boyer Moore' for 'CUDA' pattern in Text 2 document is 0.009355 secs.
Time of 'KMP' for 'алгоритмів' pattern in Text 1 document is 0.000164 secs.
Time of 'KMP' for 'CUDA' pattern in Text 1 document is 0.007773 secs.
Time of 'KMP' for 'алгоритмів' pattern in Text 2 document is 0.002314 secs.
Time of 'KMP' for 'CUDA' pattern in Text 2 document is 0.009930 secs.
Time of 'Rabin Karp' for 'алгоритмів' pattern in Text 1 document is 0.000336 secs.
Time of 'Rabin Karp' for 'CUDA' pattern in Text 1 document is 0.018213 secs.
Time of 'Rabin Karp' for 'алгоритмів' pattern in Text 2 document is 0.004084 secs.
Time of 'Rabin Karp' for 'CUDA' pattern in Text 2 document is 0.023822 secs.
```

## Висновки

### Алгоритм Боєра-Мура
Найшвидший для обох текстів з існуючим підрядком "алгоритмів", зокрема для 1.txt, де він показав найменший час (0.000093 сек.). Для неіснуючого підрядка "CUDA" в обох текстах також досить швидкий, хоча і показує дещо більший час (близько 0.007-0.009 сек.) порівняно з існуючим підрядком.

### Алгоритм Кнута-Морріса-Пратта
Загалом повільніший за Боєра-Мура, але швидший за Рабіна-Карпа в обох текстах. Показує час близько 0.000164–0.0023 сек. для існуючого підрядка і 0.0077–0.0099 сек. для неіснуючого.

### Алгоритм Рабіна-Карпа
Найповільніший серед усіх трьох алгоритмів, особливо при пошуку неіснуючого підрядка. Для існуючого підрядка час становить 0.0003–0.0040 сек., а для неіснуючого підрядка – 0.0182–0.0238 сек.

### Загальна ефективність
При відсутності збігу Рабін-Карп є найповільнішим. Алгоритм Боєра-Мура є найбільш ефективним для обох текстів. КМП - є стабільно ефективним для всіх типів рядків але повільниший за Боєра-Мура.

Алгоритм Боєра-Мура рекомендується для пошуку підрядків у великих текстах, особливо якщо очікується багато неповних збігів. Рабіна-Карпа може бути використаний для простих або хеш-орієнтованих пошуків. Алгоритм Кнута-Морріса-Пратта для загальних завдань.
