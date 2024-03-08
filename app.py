bitcoin = {
    "coin": "bitcoin",
    "quantity": 1.3,
    "buy": True
}

ethereum = {
    "coin": "ethereum",
    "quantity": 4.5,
    "buy": True
}

ethereum2 = {
    "coin": "ethereum",
    "quantity": 3.2,
    "buy": False
}

doge = {
    "coin": "doge",
    "quantity": 3.2,
    "buy": False
}

portfolio = [bitcoin,ethereum,ethereum2]
for investment in portfolio:
    print(f"{investment['coin']} - {investment['quantity']}")

def add_investment(info,portfolio):
    portfolio.append(info)
    print(portfolio)

add_investment(info=doge,portfolio=portfolio)

def add_investment1(coin,quantity,buy):
    portfolio.append( {
    "coin": coin,
    "quantity": quantity,
    "buy": buy
    })

add_investment1(doge,4,False)
print(portfolio)