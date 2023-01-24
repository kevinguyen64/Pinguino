import requests
import sys
import json # Only necessary for json.dumps()
import random
import re
import csv
from cowsay import tux, cow, turtle, fox, kitty, pig
from emoji import emojize
from os import system


def main():
# Player's name
    player = arguments()

# Initialization of lives and random artist's name
    lives = "🐧🐧🐧🐧🐧"
    n = name()

# Intro
    system("clear")
    print(f"\nHey there, {player}, welcome to Guess The Musical Artist with Pinguino the penguin! {emojize(':penguin:', language='alias')}\n")
    print(f"Pinguino likes to imagine himself as a musical artist and it is your job with the help of some friends 🐮🐷🦊🐱🐢 to guess which artist 🐧{emojize(':microphone:', language='alias')} is.\n")
    ready = input("When you're ready, click Enter to begin! ")
    while True:
        if ready == "":
            system("clear")
            break
        else:
            ready = input("Click Enter to begin ")
            continue


# Guess 1
    print(f"\nLives: {lives}")
    cow(f"Hint #1: The musical artist is {gender(n)}")
    guess_1 = input("Who am I? ").title()
    print(guess(guess_1, n))


# Guess 2
    lives = lives.replace("🐧", "", 1)
    print(f"Lives: {lives}")
    pig(f"Hint #2: The artist was born on {birthdate(n)}")
    guess_2 = input("Who am I? ").title()
    print(guess(guess_2, n))


# Guess 3
    lives = lives.replace("🐧", "", 1)
    print(f"Lives: {lives}")
    fox(f"Hint #3: The artist falls under the genre: {genre(n)}")
    guess_3 = input("Who am I? ").title()
    print(guess(guess_3, n))


# Guess 4
    lives = lives.replace("🐧", "", 1)
    print(f"Lives: {lives}")
    kitty(f"Hint #4: The musical artist has {grammys(n)} grammys")
    guess_4 = input("Who am I? ").title()
    print(guess(guess_4, n))


# Guess 5
    lives = lives.replace("🐧", "", 1)
    print(f"Lives: {lives}")
    turtle(f"Hint #5: {song(n)}")
    guess_5 = input("Who am I? ").title()
    system("clear")
    if guess_5 == n:
        tux(f"That's correct! It is I, {n}!")
        sys.exit()
    else:
        print(f"\nSorry! Pinguino is not {guess_5}...")
        tux(f"Rather, it is I, {n}!")


def arguments():
    if len(sys.argv) < 2:
        sys.exit("Not enough command-line arguments. Your name is required.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        return sys.argv[1] + " " + sys.argv[2]
    else:
        return sys.argv[1]


def name():
    names = []
    try:
        with open("artists.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.append(row["name"])
        return random.choice(names)
    except FileNotFoundError:
        sys.exit("Csv does not exist")


def guess(g, name):
    system("clear")
    if g == name:
        tux(f"That's correct! It is I, {name}!")
        sys.exit()
    else:
        return f"\nSorry! Pinguino is not {g}. Here's another hint..."


def gender(name):
    try:
        with open("artists.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"] == name:
                    return row["gender"]
    except FileNotFoundError:
        sys.exit("Csv does not exist")


def birthdate(name):
    try:
        with open("artists.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"] == name:
                    return row["birthdate"]
    except FileNotFoundError:
        sys.exit("Csv does not exist")


def genre(name):
    try:
        with open("artists.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"] == name:
                    return row["genre"]
    except FileNotFoundError:
        sys.exit("Csv does not exist")


def grammys(name):
    try:
        with open("artists.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"] == name:
                    return row["grammys"]
    except FileNotFoundError:
        sys.exit("Csv does not exist")


def song(name):
    while True:
        songs = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + name)
        o = songs.json()
        # JSON object in string format: s = json.dumps(o, indent=2)
        song_name = o["results"][random.randint(0,49)]["trackName"]
        if name == song_name:
            continue
        if "feat" in song_name:
            if matches := re.search(r"^([\w\s\W]+) \Wfeat\. ([\w\s\W]+)\W$", song_name):
                if name in matches.group(2):
                    return f'I was a feature on the song "{matches.group(1)}"'

        return f'A song of mine is called "{song_name}"'


if __name__ == "__main__":
    main()