# 2、使用while、if来完成剪刀石头布程序，要求，当玩家总共3次获胜时才退出游戏，否则继续玩。
import random

scissors = "scissors"
stone = "stone"
cloth = "cloth"
gestures = (scissors, stone, cloth)
victory_times = 0

while victory_times < 3:
    try:
        num = int(input("Plz input your gesture: (scissors=1, stone=2, cloth=3)\n"))
    except ValueError:
        print("Plz input number!")
        continue
    if num > 3 or num < 1:
        print("Plz input only 1,2,3! ")
        continue
    if num == 1:
        gesture_player = scissors
    elif num == 2:
        gesture_player = stone
    elif num == 3:
        gesture_player = cloth
    else:
        print("What happened? %d" % num)
    print("Your choice: %s" % gesture_player)
    gesture_com = random.choice(gestures)
    print("Com choice: %s" % gesture_com)
    if (gesture_com == scissors and gesture_player == cloth) or (
                    gesture_com == stone and gesture_player == scissors) or (
                    gesture_com == cloth and gesture_player == stone):
        print("You lose, plz try again.")
        continue
    elif gesture_com == gesture_player:
        print("Draw! Plz try again.")
    else:
        print("You win!")
        victory_times += 1
        if victory_times < 3:
            print("Remain %d times" % (3 - victory_times))

print("Game Over!")
