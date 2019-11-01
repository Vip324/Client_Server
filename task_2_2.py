import json


def write_order_to_json(my_data):
    with open('orders.json', 'w') as f_n:
        json.dump(my_data, f_n, indent=4)


data_to_json = {
    "item": "Ball",
    "quantity": "2",
    "price": "1,50",
    "buyer": "Petrov",
    "date": "25/10/2019"
}

write_order_to_json(data_to_json)

with open('orders.json') as f_n:
    print(f_n.read())
