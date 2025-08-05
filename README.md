# LED Button Game with Buzzer

A fun interactive game using Raspberry Pi, LEDs, buttons, and a buzzer. The player must match the LED that lights up by pressing the correct button. The game gives real-time feedback using lights and sound.

## Features

- 4 LED and Button pairs
- 1 Start button
- Buzzer feedback for correct and wrong answers
- Score tracking and saving using `shelve` database
- 5 rounds of gameplay

## How to Play

1. Connect the LEDs, buttons, and buzzer to your Raspberry Pi as defined in the script.
2. Run the game script.
3. Enter a new username when prompted.
4. Press the correct button that matches the LED that lights up.
5. Game ends after 5 rounds and your score is saved.

## Hardware Setup

- LEDs: GPIO 17, 4, 22, 27
- Buttons: GPIO 19, 13, 6, 5
- Start Button: GPIO 26
- Buzzer: GPIO 14

## Run the Game

```bash
python3 LedGameWithBuzzerClean.py

![WhatsApp Image 2025-08-05 at 4 45 04 PM](https://github.com/user-attachments/assets/e6809b0d-fd1f-43d0-a415-fbd05b0b4476)


Enjoy playing and learning GPIO with Python!
