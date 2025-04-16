from dotenv import load_dotenv
from tools import Tools

import logging
import random
import sys

load_dotenv()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

crypto_tools = Tools()

web3 = crypto_tools.get_RPC_Provider()

private_keys=crypto_tools.fetch_accounts().get("private_keys", None)

wallets = crypto_tools.fetch_accounts().get("wallets", None)

def send_transaction(data):
    sender_key = data["sender_key"]
    sender = data["sender"]
    receiver = data["receiver"]

    tx = {
        'to': receiver,
        'value': web3.to_wei(random.uniform(0.01, 0.1), 'ether'),
        'gas': 21000,
        'gasPrice': web3.to_wei('5', 'gwei'),
        'nonce': web3.eth.get_transaction_count(sender.address),
        'chainId': web3.eth.chain_id,
    }

    signed_tx = web3.eth.account.sign_transaction(tx, sender_key)

    try:
        logging.info(f"sending tx from {sender.address} to {receiver}......")
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        logging.info(f"Sent {tx['value']} ETH from {sender.address} to {receiver}. TX: {tx_hash.hex()}")
    except Exception as e:
        logging.error(e)
