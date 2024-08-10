<p align="center">
  <a href="https://demoblaze.com">
  <picture>
<img alt="Demoblaze" src="https://demoblaze.com/favicon.ico" width="70" height="70">
    </picture>
  </a>
</p>
<h1 align="center">
  Demoblaze tests
</h1>

<p align="center">
Тест-кейсы для веб-приложения по онлайн-покупке электроники
</p>
<p align="center"> <b><em>
Используемые инструменты:</em></b></p>
<p align="center">
<img title="Python" src="resources/icons/python.svg" height="30" width="30"/> <img title="Selene" src="resources/icons/selene.png" height="30" width="30"/>  <img title="Pytest" src="resources/icons/pytest.svg" height="30" width="30"/> <img title="Allure Report" src="resources/icons/allure-report.png" height="30" width="30"/> <img title="Allure TestOps" src="resources/icons/allure-testops.png" height="30" width="30"/> <img title="Selenoid" src="resources/icons/selenoid.png" height="30" width="30"/> <img title="Jenkins" src="resources/icons/jenkins.svg" height="30" width="30"/> <img title="GitHub" src="resources/icons/github.svg" height="30" width="30"/> <img title="Pycharm" src="resources/icons/pycharm.png" height="30" width="30"/> <img title="Telegram" src="resources/icons/telegram.png" height="30" width="30"/> <img title="Jira" src="resources/icons/jira.png" height="30" width="30"/> <img title="Requests" src="resources/icons/requests.png" height="30" width="30"/> <img title="Mimesis" src="resources/icons/mimesis.svg" height="30" width="30"/> <img title="Pydantic" src="resources/icons/pydantic.svg" height="30" width="30"/>
</p>

## Структура проекта

<details><summary>Диаграмма</summary>
<br>

```mermaid
        flowchart LR
            
        demoblaze --> tests(tests)

        demoblaze{{demoblaze-tests}} --> demoblaze_tests(demoblaze_tests)
        demoblaze_tests --> app(app.py)  

        model --> pages(pages)
        demoblaze_tests --> model(model) --> components(components)
        demoblaze_tests --> data(data) --> files(files)
        data --> other_data(...)
        model --> client(client.py)
        demoblaze_tests --> utils(utils.py)
        
        demoblaze --> settings(settings.py)
        demoblaze --> config(.config.*.env)
        demoblaze --> pyproject(pyproject.toml)
        demoblaze --> poetry(poetry.lock)

        demoblaze --> gitignore(.gitignore)
        
        demoblaze --> resources(resources) --> icons(icons)
        resources --> other_resources(...)

        demoblaze --> readme(README.md)
```
</details>

## Запуск

1. Склонировать репозиторий:

```
git clone https://github.com/lrayne/demoblaze-tests.git
```

2. Установить зависимости:

```
poetry install
```
3. Открыть проект в PyCharm, настроить интерпретатор

4. Скопировать содержимое из `config.*.env.example` в `config.*.env`, где `*` — `local` или `remote`
5. Поместить `config.*.env` в корень проекта 
6. При необходимости изменить значения у параметров в `config.*.env`

7. Запустить тест-кейсы, исходя из выбранного контекста:

```
context='local' pytest tests/
```

```
context='remote' pytest tests/
```


## <img title="Jenkins" src="resources/icons/jenkins.svg" height="30" width="30"/> Jenkins

[![Button](https://img.shields.io/badge/Открыть%20сборку-d33732)](https://jenkins.autotests.cloud/job/demoblaze-tests/)

### Параметры сборки:

- `TEST_SUITE` — тестовый набор
- `DRIVER_NAME` — наименование браузера
- `DRIVER_VERSION` — версия браузера
- `WINDOW_WIDTH` и `WINDOW_HEIGHT` — разрешение окна
- `TIMEOUT` – максимальное время ожидания элемента
- `ENVIRONMENT` — окружение, `COMMENT` — комментарий. Будут отображаться в уведомлении telegram'а



## <img title="Allure TestOps" src="resources/icons/allure-testops.png" height="30" width="30"/> Allure TestOps

## <img title="Jira" src="resources/icons/jira.png" height="30" width="30"/>  Jira


## Отчёты

<details><summary>При локальном запуске</summary>
<br>

```
allure serve allure-results/
```

В результате:

<img src="resources/allure-report-local.png">


</details>

<details><summary>При удаленном запуске</summary>

<br>[Отчёт можно посмотреть в Jenkins](https://jenkins.autotests.cloud/job/13-telegram_torsukov-unit14/10/allure/):

<img src="resources/allure-report-remote.gif">

<br>Если тест-кейсы запускались [через Jenkins](https://jenkins.autotests.cloud/job/13-telegram_torsukov-unit14/build?delay=0sec), то в чат telegram'а придёт письмо с результатами:

<img src="resources/telegram-notification.png">

А в [отчёте](https://jenkins.autotests.cloud/job/13-telegram_torsukov-unit14/10/allure/) можно будет посмотреть видео прохождения тест-кейсов:
<br>

<img src="resources/selenoid-video-attach.gif">

</details>


 
