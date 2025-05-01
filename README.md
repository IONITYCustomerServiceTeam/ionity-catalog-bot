
# IONITY Catalog Bot

Це Telegram WebApp бот, який при запуску відкриває сайт https://ionity.ua/shop через кнопку "КАТАЛОГ".

## Структура:
- main.py — основний код
- requirements.txt — залежності (aiogram)
- Procfile — команда для запуску на Render

## Як запустити на Render.com:

1. Зареєструйся на https://render.com
2. Створи новий Web Service
3. Підключи цей репозиторій з GitHub
4. Установи:
   - Runtime: Python 3
   - Start command: `python main.py`
   - Environment variable:
     - `API_TOKEN=тут_твій_токен_бота`

Після деплою бот буде працювати за посиланням:
`https://t.me/ionity_openbot?startapp=shop`
