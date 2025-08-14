import time
import sys
import subprocess

AUDIO_FILE = "rock_that_body.m4a"

def play_song(path=AUDIO_FILE):
    subprocess.Popen(["afplay", path])

def rock_that_body():
    lines = [
        ("I wanna da-", 0.06, 0.20),
        ("I wanna dance in the lights", 0.09, 0.75),
        ("I wanna ro-", 0.07, 0.2),
        ("I wanna rock your body", 0.08, 0.8),
        ("I wanna go", 0.08, 0.3),
        ("I wanna go for a ride", 0.09, 0.75),
        ("Hop in the music and", 0.07, 0.4),
        ("Rock your body", 0.08, 0.4),
        ("Rock that body", 0.060, 0.3),
        ("Come on, come on", 0.035, 0.20),
        ("Rock that body", 0.05, 0.3),
        ("(Rock your body)", 0.03, 0.4),
        ("Rock that body", 0.060, 0.4),
        ("Come on, come on", 0.035, 0.20),
        ("Rock that body", 0.09, 0.4),
        ("Rock that body", 0.060, 0.3),
        ("Come on, come on", 0.035, 0.20),
        ("Rock that body", 0.05, 0.3),
        ("(Rock your body)", 0.03, 0.4),
        ("Rock that body", 0.060, 0.35),
        ("Come on, come on", 0.035, 0.20),
        ("Rock that body", 0.09, 0.4),
        ("¯\_(ツ)_/¯", 0.09, 5)
    ]

    for (line, char_delay, line_delay) in lines:
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(char_delay)
        print()
        time.sleep(line_delay)

if __name__ == "__main__":
    play_song()
    rock_that_body()

