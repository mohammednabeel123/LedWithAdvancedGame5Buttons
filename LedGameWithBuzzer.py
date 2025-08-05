from gpiozero import Buzzer, Button, PWMLED
from signal import pause
import random
import time
import shelve

ledGreen = PWMLED(17)
ledBlue = PWMLED(4)
ledRed = PWMLED(22)
ledWhite = PWMLED(27)

buttonGreen = Button(19, pull_up=False, bounce_time=0.1)
buttonBlue = Button(13, pull_up=False, bounce_time=0.1)
buttonRed = Button(6, pull_up=False, bounce_time=0.1)
buttonWhite = Button(5, pull_up=False, bounce_time=0.1)
startButton = Button(26, pull_up=False)
buzzer = Buzzer(14)

pairs = [
    (ledGreen, buttonGreen),
    (ledBlue, buttonBlue),
    (ledRed, buttonRed),
    (ledWhite, buttonWhite)
]

def get_new_user():
    while True:
        name = input("Enter your name: ").strip()
        with shelve.open("scores.db") as db:
            if name in db:
                print("Name already exists. Try another.")
            else:
                db[name] = 0
                return name

def play_game():
    name = get_new_user()
    score = 0
    rounds = 5

    print("\nWelcome, " + name + "!")
    print("Rounds:", rounds)
    time.sleep(2)

    for round_num in range(1, rounds + 1):
        print("\nRound", round_num)
        
        for led, _ in pairs:
            led.on()
            time.sleep(0.5)
            led.off()

        target_index = random.randint(0, len(pairs) - 1)
        target_led, target_button = pairs[target_index]

        print("A random LED has been selected. Press the matching button!")
        target_led.on()
        time.sleep(0.3)
        target_led.off()

        pressed_index = None
        while pressed_index is None:
            for i, (led, button) in enumerate(pairs):
                if button.value:
                    pressed_index = i
                    break
            time.sleep(0.05)

        user_led, _ = pairs[pressed_index]
        user_led.on()

        if pressed_index == target_index:
            print("Correct!")
            score += 5
            buzzer.on()
            time.sleep(0.6)
            buzzer.off()
        else:
            print("Wrong!")
            score -= 2
            for _ in range(3):
                target_led.on()
                buzzer.on()
                time.sleep(0.2)
                target_led.off()
                buzzer.off()
                time.sleep(0.2)

        time.sleep(1.5)

    print("\nGame Over!")
    print("Score:", score)

    with shelve.open("LedGameScores.db") as db:
        db[name] = score
        print("Score saved for", name)

    for led, _ in pairs:
        led.off()

try:
    print("Ready! Press the start button to begin.")
    startButton.wait_for_press()
    play_game()
finally:
    print("GPIO cleanup complete.")