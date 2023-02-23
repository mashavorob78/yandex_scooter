import sender_stand_request
import data

def get_new_order_track():
    order_response = sender_stand_request.post_create_order(data.order_body)
    order_track = order_response.json()["track"]
    # Возвращает трек номер заказа
    return order_track

def get_order(order_track):
    order_response = sender_stand_request.get_order(order_track)
    return order_response

def test_get_order():
    track = get_new_order_track()
    order_response = get_order(track)
    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200
    # Проверяется, что есть тело ответа
    assert order_response.json()

