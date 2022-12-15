# Peripheral training bot

peripheral_training_bot - это бот для Telegram, который умеет присылать изображения
для тренировки периферийного зрения и памяти

![alt text](images/screenshot_1.png)
![alt text](images/screenshot_2.png)
![alt text](images/screenshot_3.png)

### Установка

1. Клонируйте репозиторий, создайте виртуальное окружение
2. Установите зависимости `pip install -r requirements.txt`
3. Создайте файл .env и создайте в нем переменные:
    ```
    KEY = "Ключ вашего бота"
    DB_LINK = "URL к вашему серверу mongodb+srv"
    DB_NAME = "Имя колекции"
    ```