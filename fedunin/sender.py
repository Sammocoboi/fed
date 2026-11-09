#две независиые логики
# первая отправляет заказ вторая получет его из очереди

import json
import uuid 
import pika 
import redis

#подключаемся к redis
r = redis.Redis(
    host = "localhost",
    port=6379,
    decode_response=True
)

#создаём заказ
order_id = str(uuid.uuid4())[:8]

order = {
    "id":order_id,
    "product":"Iphone18"
}

# Сохраняем статус в redis с хэшированием

r.hset(f"order:{order_id}",mapping={
    "product":"iphone18",
    "status":"confirm"
})

# подключиться к rabbitMq
#создаём для подключения логин и пароль
credentinal = pika.PlainCredentials(
    "demo","demo123"
)

coonection = pika.BlockingConnection(
    pika.connection(
        host = "localhost",
        credentinal = credentinal
    )
)

channel = coonection.channel()
# создаём очередь
channel.queue_declare(
    queue="orders",
    durable=True,
    arguments={"x-queue-type:":"quorum"}
)

# включаем потдверждение публикации 
channel.confirm_delivery()

# отправка сообщения 
channel.basic_publish(
    exchange="",
    routing_key="orders",
    body=json.dump(order),encode=("utf-8"),
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent,
        content_type="application/json"
    ),
    mandatory=True
)
print(f"заказ вставлен в очередь {order_id}")

coonection.close()


# создаётся уникальный нмоер заказа 
# redis сохраняет товар и статус queue - ожидание обработки
# python подключается к RabbitMq
# создаёт очередь с именем orders если её ещё нету 
# python отправляет сообщение с ID заказа и товара 
# Rabbitmq - принимает сообщение и помещает его в очередь 
# другая программа worker забирает сообщение и выполняет задачу 

# ваш код сам ничего не доставляет и не обрабатывает 
# он только создаёт заказ и отправляет сообщение 
# connection - каналы - сетевое TCP - соединение с RabbitMQ
# channel - логической канал AMQP - внутри этого соединения 


# pika.PlainCredentials - создать реквизиты авторизации 
# pika.ConnectionParameters - задать параметры соединения 
# pika.BlockingConnection - подключиться к RabbitMq
# coonection.channel - открыть AMQP - соединения 
# queue.declare() - обьявить очередь 
# confirm_delivery() - включить потдвеждение публикации 
# basic_publish() - опубликовать сообщения 
# pika.BasicProperties - задать свойства подключения 
# start_consuming () - запустить полученное сообщение 
# basic_qos() - ограничить кол неподтверждённых сообщений 
# basic_ack() - потдвердить обработку 
# basic_hack() - отрицательно потдвердить обработку 
# basic_get()  - получить одно сообщение без постоянной подписи 
#queue_purge() - очистка ожидающие сообщения очереди 
# queue_delete() - удалить очередь 
# connection.close() - закрыть соединение 

#отпраитель sender.py не обязан знать кто именно будет выполнять заказ 
# он передает сообщение в RabbiqMq а отдельный worker забираетт задачу 
# тогда когда готов её выполнить 
#и меню на этом строится принцип всех микросервисов фоновых задач очереди и обработки изображений почтовые сообщения 
# и другие backend структуры