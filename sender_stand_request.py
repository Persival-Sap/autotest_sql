import requests
import configuration
import data

# Создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)




# Получение данных по заказу
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_PATH + str(track))







