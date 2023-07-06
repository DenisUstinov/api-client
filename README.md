# API Clients

## Краткое описание проекта или пакета

Проект API Clients представляет собой две клиентские библиотеки для взаимодействия с веб-серверами посредством WebSocket и REST протоколов. Библиотеки предоставляют удобные методы для отправки запросов и обработки ответов, а также поддерживают повторные попытки соединения в случае возникновения ошибок.

## Описание

API Clients представлен двумя файлами: api-clients/websocket/client.py и api-clients/rest/client.py. Каждый файл содержит реализацию соответствующего клиента.

### WebSocket Client (api-clients/websocket/client.py):

Позволяет подключаться к WebSocket серверу и ожидать приема сообщений
Поддерживает отправку инициализационных сообщений при подключении
Обрабатывает полученные сообщения с помощью указанного обработчика

### REST Client (api-clients/rest/client.py):

Позволяет отправлять HTTP-запросы на указанный URL
Поддерживает различные HTTP-методы (GET, POST и др.)
Обрабатывает полученные ответы в формате JSON

## Установка
Вы можете установить exmo с помощью pip из GitHub, выполнив следующую команду:
```bash
pip install git+https://github.com/DenisUstinov/api-clients.git --use-pep517
```

## Использование

Для использования API Clients в вашем проекте, выполните следующие шаги:

Импортируйте соответствующий клиент в свой код:
```python
from api_clients.websocket.client import Client as WebSocketClient
from api_clients.rest.client import Client as RestClient
```


Создайте экземпляр клиента:
```python
websocket_client = WebSocketClient(response_handler)
rest_client = RestClient()
```

Для WebSocket клиента:

Используйте метод subscribe_and_listen для подключения к WebSocket серверу и прослушивания сообщений:
```python
await websocket_client.subscribe_and_listen(data)
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

Полная документация проекта API Clients доступна на [ссылке](https://github.com/DenisUstinov/api-clients/blob/main/README.md).

## Лицензия

Проект API Clients лицензирован под MIT лицензией.

## Автор
Пакет разработан ChatGPT и Denis Ustinov.