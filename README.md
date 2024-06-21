<p align="center">
  <a href="https://www.demoblaze.com">
  <picture>
    <img alt="Demoblaze logo" src="https://www.demoblaze.com/bm.png" width="50" height="50">
    </picture>
  </a>
</p>
<h1 align="center">
  Demoblaze ui tests
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

## Карта покрытия пользовательских путей

```mermaid
mindmap
  root(**Demoblaze**)
    Products[<a href='https://github.com/lrayne/demoblaze-tests/tree/develop/tests/test_products.py'>Товары</a>]
      Добавить в корзину
      Просмотреть
        Категории
            Телефоны
            Ноутбуки
            Мониторы
    Cart[<a href='https://github.com/lrayne/demoblaze-tests/tree/develop/tests/test_cart.py'>Корзина</a>]
        Удалить товар
        Оформить заказ
    Account[<a href='https://github.com/lrayne/demoblaze-tests/tree/develop/tests/test_account.py'>Аккаунт</a>]
        Авторизоваться
        Зарегистрироваться
```