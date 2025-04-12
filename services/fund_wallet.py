from dotenv import load_dotenv

from tools import Tools
import logging
import sys

load_dotenv()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

crypto_tools = Tools()

web3 = crypto_tools.get_RPC_Provider()

# funder_address: 0x982f38734eBEBf2A580b8ed3B807667A2751427e
wallets = crypto_tools.fetch_accounts().get("wallets", None)

funder_key=crypto_tools.FUNDER_KEY

funder_account = web3.eth.account.from_key(funder_key)

# funding logic here
def fund_wallet():
    pass