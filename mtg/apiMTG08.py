#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

import mtgsdk
from mtgsdk import Card

def main():
    cards = Card.where(page=5).where(pageSize=1000).all()
    print(cards)

if __name__ == "__main__":
    main()
