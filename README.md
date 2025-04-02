# Tronpy project

Микросервис на FastAPI, который предоставляет информацию о кошельках в сети Tron (баланс TRX, bandwidth, energy) по их адресу. Каждый запрос сохраняется в базу данных (SQLAlchemy ORM) для истории обращений. Сервис включает два эндпоинта: POST для получения данных о кошельке и GET для просмотра истории запросов. Интеграция с блокчейном реализована через библиотеку tronpy, код покрыт юнит- и интеграционными тестами (Pytest).

## Установка

1. Клонируйте репозиторий:

`git clone https://github.com/Leila132/tronpy.git`

2. Перейдите в директорию проекта:

`cd tronpy`

3. Установите зависимости:

`pip install -r requirements.txt`

4. Создайте файл с переменными окружения:

```
.env
`SQL_DB_URL = 'sqlite:///./new_db.db'`
`SQL_TEST_DB_URL = 'sqlite:///./new_db.db'`
```

## Запуск

`uvicorn main:app --reload`

## Использование

1. GET /tronpy_manager/

Response:

```JSON
{
    {
        "address": "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL", 
        "balance": 220.040002, 
        "bandwidth": 26480544052, 
        "energy": 16551936254
    }, 
    {
        "address": "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL", 
        "balance": 220.040002, 
        "bandwidth": 26480544052, 
        "energy": 16552304745
    }
}
```

2. POST /tronpy_manager/
```JSON
{
    "address": "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL"
}
```
