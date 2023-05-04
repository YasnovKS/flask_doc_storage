# Doc_storage on Flask

Данное приложение носит ознакомительный характер для изучения стека Flask + peewee.
Для данного приложения не реализована система авторизации пользователей и не была подключена статика.

Доп. задание - описать работу следующей конструкции:
```Python
DirectoryMeasureNpa: peewee.Model

def npa(_measure):
   sorter = itertools.count(1)
        DirectoryMeasureNpa.replace_many(list(zip(
            itertools.repeat(_measure.id),
            list(map(to_unset, map(int, flask.request.values.getlist('id[]')))),
            list(map(strip_tags, flask.request.values.getlist('name[]'))),
            list(map(strip_tags, flask.request.values.getlist('link[]'))),
            sorter)),
            fields=['measure', 'id', 'name', 'link', 'sort']).execute()
```
1. В переменную sorter помещается бесконечный итератор (начиная с единицы с шагом 1);
2. Из запроса получаем списки значений переданных параметров с помощью flask.request.values.getlist;
3. itertools.repeat создает бесконечный итератор из параметра id объекта measure;
4. map() модифицирует полученные значения, применяя функцию из первого аргумента к каждому элементу передаваемой последовательности;
5. list(zip()) упаковывает переданные аргументы, возвращая список кортежей из полученных элементов;
6. DirectoryMeasureNpa.replace_many принимает полученный ранее список кортежей и список полей, в которые нужно вставить данные из list(zip());
7. execute() выполняет указанный запрос.
Таким образом, создается несколько записей в бд, относящихся к одному объекту measure из данных, переданных в запросе, разрешая с помощью replace конфликты, возникающие
при вставке данных в БД.

## Технологии:

- Python
- Flask
- Peewee
- HTML

## Как это работает?

Склонируйте себе репозиторий проекта, создайте и активируйте виртуальное окружение и установите зависимости с помощью команды "pip install -r requirements.txt".

Запустите проект командой:
```Python
flask run
```

## Авторы
#### Яснов Кирилл
https://github.com/YasnovKS
