#!/usr/bin/python3
import os
import sys
import click
from termcolor import colored
import subprocess

def asciiBanner():
    import pyfiglet
    banner = pyfiglet.figlet_format("Email Enum")
    return banner

@click.command()
@click.argument('email', nargs=1)
def emailEnum(email):
    print(colored(asciiBanner(), 'magenta'))
    print(colored("Author: ", 'green') + "Frinto")
    print(colored("Version: ", 'green') + colored("v0.5", 'yellow'))
    print("\n\n")
    try:
        firefox_check = subprocess.check_output(['which', 'firefox'])
    except subprocess.CalledProcessError as exc:
        print(colored("Firefox not installed or isn't in PATH, exiting...", 'yellow'))
        sys.exit()
    import sites
    insta_response = sites.instagramCheck(email)
    print("[*] Instagram: " + insta_response)
    twit_response = sites.twitterCheck(email)
    print("[*] Twitter: " + twit_response)
    snap_response = sites.snapchatCheck(email)
    print("[*] Snapchat: " + snap_response)
    face_response = sites.facebookCheck(email)
    print("[*] Facebook: " + face_response)
    sites.quitSelenium()

emailEnum()
