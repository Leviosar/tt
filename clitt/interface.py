import os
from datetime import datetime

import tweepy
from colorama import Fore, Style, init

init(autoreset=True)

SEPARATOR = "-"
BLANK = " "


def box_border(line_size: int):
    print(f"+{SEPARATOR * (line_size - 2)}+")


def box_header(line_size: int, header_content: str, reverse: bool = False):
    if reverse:
        print(f"|{ BLANK * (line_size - len(header_content) + 6)}{header_content} |")
    else:
        print(f"| {header_content}{ BLANK * (line_size - len(header_content) + 6)}|")


def box_line(line_size: int, line: str, reverse: bool = False):
    if reverse:
        print(f"|{ BLANK * (line_size - len(line) - 3) }{line} |")
    else:
        print(f"| { line }{ BLANK * (line_size - len(line) - 3)}|")


def split_string(string: str, chunk_size: int):
    chunks = len(string)
    return [string[i : (i + chunk_size)] for i in range(0, chunks, chunk_size)]


def show_tweet(tweet: tweepy.Status, reverse: bool = False):
    rows, columns = os.popen("stty size", "r").read().split()
    line_size = int(columns)
    header = (
        f"{tweet.user.name} - {Fore.CYAN}@{tweet.user.screen_name}{Style.RESET_ALL}"
    )
    text = split_string(tweet.text, line_size - 4)

    box_border(line_size)
    box_header(line_size, header)
    for line in text:
        box_line(line_size, line)
    box_border(line_size)


def show_message(message: tweepy.DirectMessage, sender: tweepy.User, reverse=False):
    rows, columns = os.popen("stty size", "r").read().split()
    date = datetime.fromtimestamp(int(message.created_timestamp[0:10]))
    header = (
        f"{sender.name} - {Fore.CYAN}@{sender.screen_name}{Style.RESET_ALL} - {date}"
    )
    line_size = int(columns)
    text = split_string(message.message_create["message_data"]["text"], line_size - 4)

    box_border(line_size)
    box_header(line_size, header, reverse)
    for line in text:
        box_line(line_size, line, reverse)
    box_border(line_size)


def show_user(user: tweepy.User):
    rows, columns = os.popen("stty size", "r").read().split()
    line_size = int(columns)
    header = f"{user.name} - {Fore.CYAN}@{user.screen_name}{Style.RESET_ALL}"
    bio = f"Bio: {user.description}"
    bio = split_string(bio, line_size - 4)
    followers = f"Followers: {user.followers_count}"

    box_border(line_size)
    box_header(line_size, header)
    for line in bio:
        box_line(line_size, line)
    box_line(line_size, followers)
    box_border(line_size)
