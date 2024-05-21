# Соколов Василий 16 когорта Финальный проект. Инженер по тестированию плюс

import sender_stand_request
def get_order_id(order):
  return order.json()['track']

def test_order():
  order = sender_stand_request.post_new_order()
  order_response = sender_stand_request.get_order(get_order_id(order))
  assert order_response.status_code == 200
