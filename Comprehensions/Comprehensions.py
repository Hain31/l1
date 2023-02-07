import random as rnd

# comprehentions создание списка
c_list1 = [
    rnd.randint(1, 5)
    for i in range(10)
]

print(c_list1)


# comprehentions по словорю
p_dict = {
    1: {'name': 'vasya', 'team': 'team1', 'status': 'rest'},
    2: {'name': 'Petya', 'team': 'team1', 'status': 'play'},
    3: {'name': 'Kolya', 'team': 'team2', 'status': 'rest'},
    4: {'name': 'Serg', 'team': 'team2', 'status': 'play'}
}

team2_play_member = [
    player['name']
    for player in p_dict.values()
    if player['team'] == 'team2' and player['status'] == 'play'
]

print(team2_play_member)

# comprehentions создание словаря
p_list = [
    {'id': 10, 'name': 'vasya', 'team': 'team1', 'status': 'rest'},
    {'id': 11, 'name': 'Petya', 'team': 'team1', 'status': 'play'},
    {'id': 12, 'name': 'Kolya', 'team': 'team2', 'status': 'rest'},
    {'id': 13, 'name': 'Serg', 'team': 'team2', 'status': 'play'},
    {'id': 11, 'name': 'Petya', 'team': 'team1', 'status': 'play'},
    {'id': 13, 'name': 'Serg', 'team': 'team1', 'status': 'play'},
]

u_dict = {i_dict['id']: i_dict for i_dict in p_list}

print(u_dict)