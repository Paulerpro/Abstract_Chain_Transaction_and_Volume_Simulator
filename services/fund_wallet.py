from dotenv import load_dotenv
from eth_account import Account
from tools import Tools

import logging
import sys
import random

load_dotenv()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

crypto_tools = Tools()

web3 = crypto_tools.get_RPC_Provider()

# funder_address: 0x982f38734eBEBf2A580b8ed3B807667A2751427e
wallets = crypto_tools.fetch_accounts().get("wallets", None)

funder_key=crypto_tools.FUNDER_KEY

funder_account = web3.eth.account.from_key(funder_key)

private_keys=crypto_tools.fetch_accounts().get("private_keys", None)

# Threshold below which wallet gets topped up (in wei)
THRESHOLD = web3.to_wei(0.001, 'ether') # If a wallet has less than 0.001 ETH, it will be funded.
TOP_UP_AMOUNT = web3.to_wei(0.005, 'ether') # top up 0.005 ETH

GAS_LIMIT = 21000
GAS_PRICE = web3.eth.gas_price # current price of gas from the blockchain


def low_balance(balance):
    if balance < THRESHOLD:
        return True
    return False


def fund_wallet():

    sender_key = random.choice(private_keys)
    tx_sender = Account.from_key(sender_key)

    try:
        tx_receiver = random.choice([w.address for w in wallets if w.address != tx_sender.address])
    except:
        tx_receiver = random.choice([w for w in wallets if w != tx_sender.address])

    balance = web3.eth.get_balance(tx_sender)

    data = {
            "sender_key": sender_key,
            "sender": tx_sender,
            "receiver": tx_receiver
        }

    if low_balance(balance):
        # proceed with refill
        nonce = web3.eth.get_transaction_count(funder_account.address)

        tx = {
            'to': tx_sender,
            'value': TOP_UP_AMOUNT,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': nonce,
            'chainId': web3.eth.chain_id
        }

        signed_tx = web3.eth.account.sign_transaction(tx, funder_key)
        try:
            logging.info(f"Balance low! Refilling {tx_sender} from {funder_account.address}......")
            tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
            logging.info(
                f"Sent {web3.from_wei(TOP_UP_AMOUNT, 'ether')} ETH to {tx_sender} | Tx: {web3.to_hex(tx_hash)}"
                )
        except Exception as e:
            logging.error(e)

    else:
        # proceed to send transaction
        logging.info(
            f"{tx_sender} has enough balance: {web3.from_wei(balance, 'ether')} ETH /n Proceeding to next step...."
            )
    
    return data