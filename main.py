from tools import Tools
from dotenv import load_dotenv
from services import fund_wallet, send_transaction

import logging
import random
import time
import sys

load_dotenv()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

crypto_tools = Tools()

web3 = crypto_tools.get_RPC_Provider()

if web3.is_connected():
    logging.info("Connected to Abstract Chain!...Let's get to business")
else:
    logging.error("Connection failed.")

data = fund_wallet.fund_wallet()

