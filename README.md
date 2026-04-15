# Telegram Channel Parser

Минимальный FastAPI для парсинга постов из Telegram-каналов.

## Локальный запуск

1. Клонируйте репозиторий.
2. Установите зависимости: `pip install -r requirements.txt`
3. Запустите: `uvicorn main:app --reload --port 8000`

API доступно на http://localhost:8000/docs

## Деплой на Render/Railway

1. Создайте сервис, подключите GitHub-репозиторий.
2. Установите порт: 10000.
3. Команда запуска: `uvicorn main:app --host 0.0.0.0 --port $PORT` (Render использует $PORT=10000).

## Переменные окружения

Перед первым использованием получите на https://my.telegram.org:

- `TELEGRAM_API_ID=your_api_id`
- `TELEGRAM_API_HASH=your_api_hash`
- `TELEGRAM_PHONE=+1234567890` (опционально, для сессии)

**Важно:** Доработайте авторизацию в `main.py` (await client.start(phone=...)) и фильтрацию по `topics`.

Пример запроса:
```bash
curl -X POST "http://localhost:8000/api/telegram/parse" \
-H "Content-Type: application/json" \
-d '{"channels": ["@channel1"], "topics": ["ИИ"], "days": 7}'
```
