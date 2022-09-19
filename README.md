# api_yamdb
## База отзывов пользователей на книги, музыку и фильмы
## Как запустить проект <img src = "https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /> 

### Как запустить проект:

#### Клонировать репозиторий и перейти в него в командной строке:

```
HTTPS: git clone https://github.com/Ho1yGun/api_yamdb.git
SSH: git clone git@github.com:Ho1yGun/api_yamdb.git
```

```
cd api_yamdb
```

#### Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
или 
python -m venv env для windows, далее так же
```

```
source env/bin/activate
```

#### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

#### Выполнить миграции:

```
python3 manage.py migrate
```

#### Запустить проект:

```
python3 manage.py runserver
```
### Перейти по адресу http://127.0.0.1:8000/redoc/ и посмотреть полную документацию API с примерами
