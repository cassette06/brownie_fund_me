from brownie import FundMe,accounts
from scripts.helpful_scripts import  get_account
def fund():
    
    fund_me=FundMe[-1]
    print(fund_me)
    account=get_account()
    print(fund_me.getPrice())
    # entrance_fee=fund_me.getEntranceFee()
    entrance_fee =500000
    print(entrance_fee)
    print(f'the current entry fee is {entrance_fee}')
    fund_me.fund({"from":account,'value':entrance_fee})

def withdraw():
    fund_me=FundMe[-1]
    account=get_account()
    fund_me.withdraw({'from':account})

def main():
    fund()
    withdraw()