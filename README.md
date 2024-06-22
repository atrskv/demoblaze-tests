<p align="center">
  <a href="https://www.medusajs.com">
  <picture>
<img alt="Medusa logo" src="https://demoblaze.com/favicon.ico" width="70" height="70">
    </picture>
  </a>
</p>
<h1 align="center">
  Demoblaze tests
</h1>

<p align="center">
Тест-кейсы для веб-приложения по онлайн-покупке электроники
</p>
<p align="center">
  <a href="https://python-poetry.org">
    <img src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" alt="Medusa is released under the MIT license." />
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="PRs welcome!" />
  </a>
</p>

## Карта функциональных возможностей

```mermaid
        flowchart TD
        
        demoblaze(((Demoblaze))) --> products(Товары)
        
        products --> view(Просмотреть)
        
        view --> categories(Категории)
        
        categories --> phones(Телефоны)
        categories --> laptops(Ноутбуки)
        categories --> monitors(Мониторы)

        products --> add(Добавить в корзину) 

        demoblaze --> cart(Корзина)
        
        cart --> order(Оформить заказ)
        
        order --> name(Имя)
        order --> country(Страна)
        order --> city(Город)
        order --> creditCard(Кредитная карта)
        order --> month(Месяц)
        order --> year(Год)
        
        cart -->  remove(Удалить товар)
        
        demoblaze --> contacts(Контакты)
        
        contacts --> support(Отправить сообщение в тех. поддержку)
        
        support --> email(Контактная эл. почта)
        support --> contactName(Контакное имя)
        support --> message(Сообщение)
        
        account --> logIn(Авторизоваться)
        
        logIn --> userNameForLogIn(Имя пользователя)
        
        userNameForLogIn -->existingUserName(Существующее)
        userNameForLogIn -->notExistingUserName(Несуществующее)
        
        logIn --> passwordForLogIn(Пароль)
        
        passwordForLogIn --> validPassword(Валидный)
        passwordForLogIn --> inValidPassword(Невалидный)
        
        demoblaze --> account(Аккаунт)
        
        account --> signUp(Зарегистрироваться)
        signUp --> userName(Имя пользователя)
        signUp --> password(Пароль)

        click Demoblaze "https://www.demoblaze.com" _blank
        click Account "https://github.com/lrayne/demoblaze-tests/blob/develop/tests/test_account.py" _blank
        click Products "https://github.com/lrayne/demoblaze-tests/blob/develop/tests/test_products.py" _blank
        click Cart "https://github.com/lrayne/demoblaze-tests/blob/develop/tests/test_cart.py" _blank

```

## Используемые инструменты
<img title="Python" src="resources/icons/python.svg" height="30" width="30"/> 
<img title="Jenkins" src="resources/icons/selene.png" height="30" width="30"/>
<img title="Jenkins" src="resources/icons/selenium.svg" height="40" width="40"/>
<img title="Pytest" src="resources/icons/pytest.svg" height="40" width="40"/> 
<img title="Allure Report" src="resources/icons/allure-report.png" height="40" width="40"/> 
<img title="Selenoid" src="resources/icons/selenoid.png" height="40" width="40"/>
<img title="Jenkins" src="resources/icons/jenkins.svg" height="40" width="40"/> 
<img title="GitHub" src="resources/icons/github.svg" height="40" width="40"/> 
<img title="Pycharm" src="resources/icons/pycharm.png" height="40" width="40"/> 
<img title="Telegram" src="resources/icons/telegram.png" height="40" width="40"/> 

## Запуск

<details><summary>Локально</summary>

<br>1. Склонировать репозиторий:

```
git clone https://github.com/lrayne/demoblaze-tests.git
```

2. Установить зависимости:

```
poetry install
```

3. Создать `.env` в корне проекта *(см. `.env.example`)*, внутри него указать:

- **LOGIN** и **PASSWORD** — данные от аккаунта существующего пользователя на [Demoblaze](https://www.demoblaze.com) *(используются в тест-кейсе авторизации)*
- **NAME**, **COUNTRY**, **CITY**, **CREDIT_CARD**, **MONTH**, **YEAR** — данные, необходимые для оформления заказа

4. Запустить тесты:

```
pytest . --mode=local
```
</details>

<details><summary>Удалённо</summary>

<br>1. Склонировать репозиторий:

```
git clone https://github.com/lrayne/demoblaze-tests.git
```

2. Установить зависимости:

```
poetry install
```

3. Создать `.env` в корне проекта *(см. `.env.example`)*, внутри него указать:

- **LOGIN** и **PASSWORD** — данные от аккаунта существующего пользователя на [Demoblaze](https://www.demoblaze.com) *(используются в тест-кейсе авторизации)*
- **NAME**, **COUNTRY**, **CITY**, **CREDIT_CARD**, **MONTH**, **YEAR** — данные, необходимые для оформления заказа
- **SELENOID_LOGIN**, **SELENOID_PASS**, **SELENOID_URL** — учетные данные и URL для удаленного запуска

4. Запустить тесты:
```
pytest . --mode=remote
```

</details>

## Отчёты

<details><summary>Локально</summary>
<br>

```
allure serve allure-results/
```

В результате:

<img src="resources/allure-report-local.png">


</details>

<details><summary>Удалённо</summary>

<br>Идентичный отчёт можно посмотреть в Jenkins:

<img src="resources/allure-report-remote.gif">

</details>

Если тест-кейсы запускались через Jenkins, то в чат telegram'а придёт письмо с результатами:

<img src="resources/telegram-notification.png">

А в Allure report'е можно будет посмотреть видео прохождения тест-кейсов:

<img src="resources/selenoid-video-attach.gif">


## Ветви проекта
```mermaid
gitGraph
   commit id: "Initial commit"
   branch develop
   branch task/short-description
   commit
   commit
   checkout develop
   commit id: "Update README.md"
   commit id: "Update .gitignore"
   merge task/short-description
   checkout main
   merge develop
   checkout develop
   branch fix/short-description
   commit
   commit
   checkout develop
   merge fix/short-description
   checkout main
   merge develop


```


