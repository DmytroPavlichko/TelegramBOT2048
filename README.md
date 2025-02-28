# 2048Bot

**2048Bot** — это MiniApp + Telegram-бот для игры в популярную головоломку 2048. Игра позволяет сохранять рекорды, сравнивать свои достижения с другими игроками и поддерживает возможности просмотра и очистки личного рекорда.

## Основные функции

- 🎮 **Играйте в 2048:** Получите доступ к классической игре, используя ваш Telegram.
- 🏆 **Рекорды:** Сохранение личного рекорда в базе данных для сравнения с достижениями других игроков.
- 📋 **Локальное хранилище:** Текущие данные игры сохраняются в локальном хранилище MiniApp, что обеспечивает быстрый доступ и удобство продолжения игры.
- 🔄 **Просмотр и очистка рекордов:** Возможность просмотреть личный рекорд или рекорды других игроков, а также очистить свои достижения.

## Стек технологий

- **FastAPI** — для реализации API методов и обработки вебхуков.
- **Aiogram** — для создания Telegram-бота и обработки сообщений.
- **SQLAlchemy + Alembic** — для работы с базой данных и управления миграциями.
- **SQLite** — база данных для хранения рекордов пользователей.

## Переменные окружения

Проект использует файл `.env` для хранения конфиденциальных данных. Пример содержимого файла:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
BASE_SITE=https://your-base-url.io
ADMIN_IDS=[ADMINid1, ADMINid2]
```

- `BOT_TOKEN` — токен Telegram-бота.
- `BASE_SITE` — базовый URL для MiniApp и вебхуков.
- `ADMIN_IDS` — Список из TelegramIDs администраторов.

## Установка проекта

1. **Склонируйте репозиторий**:
   ```bash
   git clone https://github.com/Yakvenalex/2048Bot.git
   cd 2048Bot
   ```

2. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Создайте файл `.env`** с вашими настройками (см. раздел "Переменные окружения").

4. **Запустите приложение**:
   ```bash
   uvicorn app.main:app --reload
   ```

## Зависимости

Проект использует следующие зависимости:

```text
aiogram==3.13.1
fastapi==0.115.0
pydantic==2.9.2
uvicorn==0.31.0
jinja2==3.1.4
pydantic_settings==2.5.2
aiosqlite==0.20.0
alembic==1.13.3
loguru==0.7.2
SQLAlchemy==2.0.35
   ```
## 2048Bot DEMO

*Видео-демонстрация возможностей бота* доступна [здесь](https://rutube.ru/shorts/38bae2fcdb307aa180317f562b38424b/). Попробуйте и оцените игру в [2048Bot на Telegram](https://t.me/fast_api_2048BOT).

P.S. Вдохновлено проектом: [2048](https://github.com/edopedia/2048)
