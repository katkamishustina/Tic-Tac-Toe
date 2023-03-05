import random

field = '- - -\n- - -\n- - -'
field = list(field)
print(field)


def choose(game_field, choice, ox):
    possible_choices_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if choice in possible_choices_2:
        if choice == 7:
            game_field[0] = ox
        elif choice == 8:
            game_field[2] = ox
        elif choice == 9:
            game_field[4] = ox
        elif choice == 4:
            game_field[6] = ox
        elif choice == 5:
            game_field[8] = ox
        elif choice == 6:
            game_field[10] = ox
        elif choice == 1:
            game_field[12] = ox
        elif choice == 2:
            game_field[14] = ox
        elif choice == 3:
            game_field[16] = ox


possible_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while len(possible_choices) != 0:
    user_input = int(input('Choose position: '))
    # print('you chosen ', user_input)
    possible_choices.remove(user_input)
    choose(field, user_input, 'x')
    if len(possible_choices) != 0:
        pc_choice = random.choice(possible_choices)
        possible_choices.remove(pc_choice)
        # print('pc chosen ', pc_choice)
        choose(field, pc_choice, 'o')

    # ......................horizontal ...........................
    if field[0] == 'x' and field[2] == 'x' and field[4] == 'x':
        print('3 x in one line! USER WON')
        break
    elif field[0] == 'o' and field[2] == 'o' and field[4] == 'o':
        print('3 x in one line! PC WON')
        break
    elif field[6] == 'x' and field[8] == 'x' and field[10] == 'x':
        print('3 x in one line! USER WON')
        break
    elif field[6] == 'o' and field[8] == 'o' and field[10] == 'o':
        print('3 x in one line! PC WON')
        break
    elif field[12] == 'x' and field[14] == 'x' and field[16] == 'x':
        print('3 x in one line! USER WON')
        break
    elif field[12] == 'o' and field[14] == 'o' and field[16] == 'o':
        print('3 x in one line! PC WON')
        break
    # ...................... vertical ...........................
    elif field[0] == 'x' and field[6] == 'x' and field[12] == 'x':
        print('3 x in one line! USER WON')
        break
    elif field[0] == 'o' and field[6] == 'o' and field[12] == 'o':
        print('3 x in one line! PC WON')
        break
    elif field[2] == 'x' and field[8] == 'x' and field[14] == 'x':
        print('3 x in one line! USER WON')
        break
    elif field[2] == 'o' and field[8] == 'o' and field[14] == 'o':
        print('3 x in one line! PC WON')
        break
    elif field[4] == 'x' and field[10] == 'x' and field[14] == 'x':
        print('3 x in one line! PC WON')
        break
    elif field[4] == 'o' and field[10] == 'o' and field[14] == 'o':
        print('3 x in one line! PC WON')
        break
    # ...................... diagonal ...........................
    elif field[0] == 'x' and field[8] == 'x' and field[16] == 'x':
        print('3 x in one line! USER WON')
        break
    elif field[0] == 'o' and field[8] == 'o' and field[16] == 'o':
        print('3 x in one line! PC WON')
        break
    elif field[4] == 'x' and field[8] == 'x' and field[12] == 'x':
        print('3 x in one line! USER WON')
        break
    elif field[4] == 'o' and field[8] == 'o' and field[12] == 'o':
        print('3 x in one line! PC WON')
        break
    # ................................................................
    new_field = ''
    for i in field:
        new_field += i
    print(new_field)

new_field = ''
for i in field:
    new_field += i
print(new_field)
