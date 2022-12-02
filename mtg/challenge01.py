#!/usr/bin/env python3

import requests
from pprint import pprint
import json

API = "https://api.magicthegathering.io/v1/" 

def main():

    setcode = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower() 

    resp = requests.get(f"{API}cards?set={setcode}") 

    cards = resp.json()
    
    # SOLUTION
    with open(setcode + "-set.json", "w") as foo:
        json.dump(cards, foo, indent=4)

if __name__ == "__main__":
    main()
