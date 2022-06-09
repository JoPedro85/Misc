from datetime import datetime


dish1 = "Prego"
dish2 = "Bifana"


veggies = "spinach"
rice = "rice"
rice_special = "Tomato rice"
fries = "fries"

main_dishes = ["1. "+dish1, "2. "+dish2]
side_dish = ["1. "+veggies, "2. "+rice, "3. "+rice_special, "4. "+fries]
food = [main_dishes, side_dish]

cooking = ["grilled", "fried", "Steamed"]

print("main dish:")
for i in main_dishes:
    print(i)
print("")
print("side dish")
for i in side_dish:
    print(i)


order_count = 0
while True:

    user_input1 = (int(input("select a main dish: "))-1)
    while user_input1 >= len(main_dishes):
        user_input1 = (int(input("select a main dish: ")) - 1)
    else:
        user_input2 = (int(input("select a side dish: "))-1)
    while user_input2 >= len(side_dish):
        user_input2 = (int(input("select a side dish: "))-1)
    else:
        print("")

    order_main = main_dishes[user_input1]
    order_main_dish = order_main[3:]
    order_side = side_dish[user_input2]
    order_side_dish = order_side[3:]

    order_count += 1

    order_time = datetime.now()
    current_time = order_time.strftime("H:M")

    order = (f"""
    Order no{order_count}:
    {order_main_dish}
    {order_side_dish}
    ({order_time})
    """)

    with open("order registry.txt", "a") as file:
        file.write(order)
    print(order)


