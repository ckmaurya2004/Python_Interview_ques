import time

def run():
    print("Press Enter for continue and ctrl+c for second hand ")
    attempts = 1
    point = 0
    point_table = {}
    name = input("enter the player name! " )
    while True:
        for digit in range(1,12):
            try:
                print(digit)
                time.sleep(0.2)
            except KeyboardInterrupt:
                print(f"stopped at {digit}")
                print("points are added ")
                if digit in [1,5,9,11]:
                    point = point + 10
                elif digit in [4,7,8,10]:
                    point = point + 20
                elif point in [3,2,6,12]:
                    point = point + 30
                attempts += 1
                if attempts == 5:
                    print(f"name is {name} and points is {point}")
                    point_table[name] = point
                    ans = input("enter any other player (y/n)? ").lower()
                    if ans == 'y':
                        name = input("enter enter the player name! ")
                        attempts = 1
                        point = 1
                    else:
                        print("thank you ")
                        print(f"final result {point_table}")
                        return

run()

