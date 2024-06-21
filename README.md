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

## Запуск

<details><summary>Локально</summary>

1. Склонировать репозиторий:

```
git clone https://github.com/lrayne/demoblaze-tests.git
```

2. Установить зависимости:

```
poetry install
```

3. Создать `.env` в корне проекта (см. `.env.example`), внутри него указать:

- **LOGIN** и **PASSWORD** — данные от аккаунта существующего пользователя на `demoblaze.com` *(используются в тест-кейсе авторизации)*
- **NAME**, **COUNTRY**, **CITY**, **CREDIT_CARD**, **MONTH**, **YEAR** — данные, необходимые для оформления заказа

4. Запустить тесты:

```
pytest . --mode=local
```
</details>

<details><summary>Удалённо</summary>

1. Склонировать репозиторий:

```
git clone https://github.com/lrayne/demoblaze-tests.git
```

2. Установить зависимости:

```
poetry install
```

3. Создать `.env` в корне проекта (см. `.env.example`), внутри него указать:

- **LOGIN** и **PASSWORD** — данные от аккаунта существующего пользователя на `demoblaze.com` *(используются в тест-кейсе авторизации)*
- **NAME**, **COUNTRY**, **CITY**, **CREDIT_CARD**, **MONTH**, **YEAR** — данные, необходимые для оформления заказа
- **SELENOID_LOGIN**, **SELENOID_PASS**, **SELENOID_URL** — учетные данные и URL для удаленного запуска

4. Запустить тесты:
```
pytest . --mode=remote
```

</details>

## Отчёты

### Allure
<details><summary>Локально</summary>

```
allure serve allure-results/
```

В результате:

<img src="resources/allure-report-local.png">


</details>

<details><summary>Удалённо</summary>

```
allure serve allure-results/
```

</details>

### Telegram


## Стратегия ветвления
```mermaid
gitGraph
   commit id: "Initial commit"
   branch develop
   branch task/short-description
   commit
   commit
   checkout develop
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