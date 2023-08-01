# My Clients

## Краткое описание проекта

Проект My Clients представляет собой две клиентские библиотеки для взаимодействия с веб-серверами посредством WebSocket и REST протоколов в асинхронном режиме. Библиотеки предоставляют удобные методы для отправки запросов и обработки ответов, а также поддерживают повторные попытки соединения в случае возникновения ошибок.

## Описание

My Clients представлен двумя файлами: my_clients/websocket/client.py и my_clients/rest/client.py. Каждый файл содержит реализацию соответствующего клиента.

## WebSocket Client (my_clients/websocket/client.py):

* Позволяет подключаться к WebSocket серверу и ожидать приема сообщений.
* Поддерживает отправку инициализационных сообщений при подключении.
* Обрабатывает полученные сообщения с помощью указанного обработчика.

## REST Client (my_clients/rest/client.py):

* Позволяет отправлять HTTP-запросы на указанный URL.
* Поддерживает различные HTTP-методы (GET, POST и др.).

## Установка

Вы можете установить My Clients с помощью pip из GitHub, выполнив следующую команду:

```bash
pip install git+https://github.com/DenisUstinov/my-clients.git --use-pep517
```

## Использование

Для использования My Clients в вашем проекте, выполните следующие шаги:

Импортируйте соответствующий клиент в свой код:

```python
from my_clients.websocket.client import Client as WebSocketClient
from my_clients.rest.client import Client as RestClient
```


Создайте экземпляр клиента:
```python
websocket_client = WebSocketClient(response_handler)
rest_client = RestClient()
```

Для WebSocket клиента:

Используйте метод subscribe_and_listen для подключения к WebSocket серверу и прослушивания сообщений:
```python
await websocket_client.request(data)
```

Для REST клиента:

Используйте метод request для отправки HTTP-запросов:
```python
response = await rest_client.request(url, method, headers, data)
```

Обработайте полученные ответы или сообщения в соответствии с логикой вашего проекта.
При завершении работы с клиентами, убедитесь, что соединение закрыто (только для WebSocket клиента):

```python
await websocket_client.close()
```

## Документация

Полная документация проекта My Clients доступна на [ссылке](https://github.com/DenisUstinov/my-clients/blob/main/README.md).

## Лицензия

Проект My Clients лицензирован под MIT лицензией.

## Автор
Пакет разработан ChatGPT и Denis Ustinov.
