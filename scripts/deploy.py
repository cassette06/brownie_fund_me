from brownie import FundMe,MockV3Aggregator,network,config 
from scripts.helpful_scripts import get_account,deploy_mocks,LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account=get_account()
    print(account)
    # fund_me = FundMe.deploy({"from":account},publish_source=True)
    # publish_source=True表示是否可以在etherscan上看到合约代码，但是我一直执行失败，可能是vpn问题吧


    # pass the price feed address to our fundme contract
    # if we are on a persistant network like rinkeby, use the associated address
    # otherwise,deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS :
        print(network.show_active())
        price_feed_address=config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address=MockV3Aggregator[-1].address
        

    fund_me = FundMe.deploy(price_feed_address,{"from":account})

    print(f'contract deployed to {fund_me.address}')
    return fund_me

def main():
    deploy_fund_me()