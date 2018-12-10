import utils

broker = utils.Broker(host='127.0.0.1')

exchange_name = 'new_user'

broker.create_exchange(name=exchange_name, type='direct')

broker.send_task(exchange=exchange_name, route='create')

print('Нужно завести нового пользователя')

broker.connection.close()