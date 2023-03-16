import json

import requests


def get_addresses(path: str = 'address.txt') -> list:
    with open(path) as file:
        lines = file.readlines()
    return [line.rstrip() for line in lines]


def get_token(address: str):
    response = session.get(url=f"https://arbitrum.foundation/_next/data/lB0zTjQwwi0nJOMcTT0Td/eligibility.json?"
                               f"address={address.lower()}")
    result = json.loads(response.content)['pageProps']
    if result['isEligible']:
        return result['eligibility']['tokens']
    else:
        return 0


if __name__ == '__main__':
    total_amount = 0
    session = requests.session()
    for address in get_addresses():
        amount = get_token(address=address)
        total_amount += amount
        print(f"{address}: {amount}.")
    print(f"total: {total_amount}.")
