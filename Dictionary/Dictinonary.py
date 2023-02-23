goods = {
    'стул': '12345',
    'стол': '21234',
    'кресло': '32123',
    'дивон': '43212'
}

store = {
    '12345': [
        {'quantity': 23, 'price': 200},
        {'quantity': 25, 'price': 150}
    ],
    '21234': [
        {'quantity': 10, 'price': 2000},
        {'quantity': 15, 'price': 1500}
    ],
    '32123': [
        {'quantity': 10, 'price': 1000},
        {'quantity': 15, 'price': 1500},
        {'quantity': 10, 'price': 1000},
        {'quantity': 15, 'price': 1500}
    ],
    '43212': [
        {'quantity': 10, 'price': 10000},
        {'quantity': 15, 'price': 15000},
        {'quantity': 10, 'price': 10000}
    ]
}

for key, item in goods.items():
    total_q = 0
    total_p = 0
    for li in store[item]:
        total_q += li['quantity']
        total_p += li['quantity'] * li['price']

    print('{0} - {1} шт. Итого: {2} руб.'.format(key, total_q, total_p))

# zip function
