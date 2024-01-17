import random

drinks_foods = {
    "whiskey" : "chocolate",
    "wine" : "cheese",
    "soju" : "samgyeopsal",
    "goryangju" : "lamb skewers"
    }
#del drinks_foods["whiskey"]
drinks_foods["beer"] = "snack"
# drink = input(drinks_food.keys())
drinks_foods_keys = list(drinks_foods)
# print(drinks_food_keys)
#print(random.choice(drinks_foods_keys)) #random으로 key 나오기.
while True:
    menu = input('\nselect following menu in number.'
                 f'\n1){drinks_foods_keys[0]} '
                 f'2){drinks_foods_keys[1]} '
                 f'3){drinks_foods_keys[2]} '
                 f'4){drinks_foods_keys[3]} '
                 f'5){drinks_foods_keys[4]} '
                 '6)random '
                 '7)quit'
                 '\n : '
                 )
    if menu == '1':
        print(f'{drinks_foods_keys[0]} is best when enjoy with {drinks_foods[drinks_foods_keys[0]]}')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]} is best when enjoy with {drinks_foods[drinks_foods_keys[1]]}')
    elif menu == '3':
        print(f'{drinks_foods_keys[2]} is best when enjoy with {drinks_foods[drinks_foods_keys[2]]}')
    elif menu == '4':
        print(f'{drinks_foods_keys[3]} is best when enjoy with {drinks_foods[drinks_foods_keys[3]]}')
    elif menu == '6':
        random_drink = random.choice(drinks_foods_keys)
        print(f'{random_drink} is best when enjoy with {drinks_foods[random_drink]}')
    elif menu == '5':
        print(f'{drinks_foods_keys[4]} is best when enjoy with {drinks_foods[drinks_foods_keys[4]]}')
    elif menu == '7':
        print("system off")
        break

    else:
        print("That's ill-advised number")
