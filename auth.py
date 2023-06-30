import time
import pyotp
import qrcode
import random
import sys
import pygame
from colorama import Fore, Back, Style

k = pyotp.random_base32()
secret_key = "0m3g4_dev_is_the_best"
totp_auth = pyotp.totp.TOTP(
secret_key).provisioning_uri(
name='JohnDoe',
issuer_name='0m3g4_dev')

print(totp_auth)

print("################################################")
print("  ____               _              _     _     ")
print(" |  _ \   _   _     / \     _   _  | |_  | |__  ")
print(" | |_) | | | | |   / _ \   | | | | | __| | '_ \ ")
print(" |  __/  | |_| |  / ___ \  | |_| | | |_  | | | |")
print(" |_|      \__, | /_/   \_\  \__,_|  \__| |_| |_|")
print("          |___/                                 ")
print(Fore.ORANGE + 'Made With ♡ By 0m3g4_dev')
print("################################################")
time.sleep(1.3)
print(Fore.YELLOW + 'Generating QR Code...')
time.sleep(1)
qrcode.make(totp_auth).save("qr_auth.png")
print(Fore.GREEN + 'QR Code Generated At This Folder!')
print(Fore.GREEN + 'Scan It With Google Authenticator.')
time.sleep(0.5)
print(Fore.YELLOW + 'Ready! TOTP Output Generated:')
totp_qr = pyotp.TOTP(secret_key)

def play_fireworks_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('fireworks_sound.mp3')  # Path to your fireworks sound file
    pygame.mixer.music.play()

def print_fireworks():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    width = shutil.get_terminal_size().columns
    height = shutil.get_terminal_size().lines
    max_x = width - 1
    max_y = height - 1
    fireworks = []
    for i in range(20):
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        dx = random.randint(-2, 2)
        dy = random.randint(-1, -4)
        color = random.choice(colors)
        fireworks.append((x, y, dx, dy, color))

    while fireworks:
        for i in range(len(fireworks)):
            x, y, dx, dy, color = fireworks[i]
            if y < max_y:
                print(color + "*", end="", flush=True)
                fireworks[i] = (x + dx, y + dy, dx, dy + 1, color)
            else:
                fireworks[i] = (x, y, dx, dy, color)
        time.sleep(0.1)
        sys.stdout.write("\033[1;1H")  # Move cursor to the top-left corner

totp = pyotp.TOTP(secret_key)
while True:
    code = input((Fore.YELLOW + "Enter the Code : "))
    if totp.verify(code):
        print(Fore.GREEN + "Correct Auth! (◔‿◔)")
        time.sleep(1)  # Delay for 1 second
        print_fireworks()
    else:
        print(Fore.RED + "Error! Incorrect Code. ( ≧Д≦)")



