import utils

broker = utils.Broker(host='127.0.0.1')

exchange_name = 'new_user'

broker.create_exchange(name=exchange_name, type='direct')

queue_name = 'create'

broker.create_queue(name=queue_name)

broker.bind_queue_exchange(exchange=exchange_name, queue=queue_name, route=queue_name)


def callback(ch, method, properties, body):
    print('Создалась учётка для нового пользователя')

broker.bind_callback_queue(callback=callback, queue=queue_name)

broker.start_infinity_process()
