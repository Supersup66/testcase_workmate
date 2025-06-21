# Тестовое задание для Workmate

## Cкрипт для обработки CSV-файла
Поддерживает операции: 
- фильтрацию с операторами «больше», «меньше» и «равно»
- агрегацию с расчетом среднего (avg), минимального (min) и максимального (max) значения
- сортировку вывода по возростанию (asc) и убыванию (desc)

## Примеры работы скрипта:

- Фильтрация таблицы

  ```
  python main.py --file "products.csv" --where "price>300"
  ```
  ![image](https://github.com/user-attachments/assets/d65777d9-611c-41d8-be8d-31adc356cbd5)

  ```
  python main.py --file "products.csv" --where "brand=apple"
  ```
  ![image](https://github.com/user-attachments/assets/a76fcb43-0fa0-4a5b-9d66-f38900e6d166)
  
- Обработка исключений

  ```
  python main.py --file "products.csv" --where "brand%apple"
  ```
  ![image](https://github.com/user-attachments/assets/de79e6b9-060b-4435-9ba9-3b3ad69707d2)

  ```
  python main.py --file "products.csv" --where "error=apple"
  ```
  ![image](https://github.com/user-attachments/assets/eef654bf-6988-4bcd-9be2-32c22ab62832)

- Аггрегация данных
  ```
  python main.py --file "products.csv" --aggregate "rating=avg"
  ```
  ![image](https://github.com/user-attachments/assets/1e8f6384-ab3c-468d-aece-600156cffda1)

  ```
  python main.py --file "products.csv" --aggregate "price=min"
  ```
  ![image](https://github.com/user-attachments/assets/679f34f6-d951-4354-9ae4-a34ba4f6a514)

- Сортировка
  ```
  python main.py --file "products.csv" --order_by "brand=desc"
  ```
  ![image](https://github.com/user-attachments/assets/3b53d45e-cf41-490e-9c59-31246002a9e2)

- Комбинированные запросы
  ```
  python main.py --file "products.csv" --where "price>300" --aggregate "rating=max"
  ```
  ![image](https://github.com/user-attachments/assets/b0c679e7-195d-47af-831f-e49dacc91779)

  ```
  python main.py --file "products.csv" --where "rating>4.5" --order_by "price=asc"
  ```
  ![image](https://github.com/user-attachments/assets/e511fb07-e32e-4f5d-aec4-0e2cec8de849)

## Комментарии
Критический функционал покрыт тестами. Налиие словарей значительно ускорит добавление новых методов обработки таблицы.

Работу выполнил: Порошин Алексей [@](https://github.com/Supersup66/)
  

  




  



