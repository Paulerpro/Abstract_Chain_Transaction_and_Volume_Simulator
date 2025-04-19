from web3 import Web3
import os

class Tools:

    def __init__(self):
        self.RPC_URL = os.getenv("ABSTRACT_CHAIN_RPC")
        self.PRIVATE_KEYS = os.getenv("PRIVATE_KEYS").split(",")
        self.FUNDER_KEY = os.getenv("FUNDER_PRIVATE_KEY")
        
    def get_RPC_Provider(self):
        web3 = Web3(Web3.HTTPProvider(self.RPC_URL))
        return web3

    def fetch_accounts(self):
        # PRIVATE_KEYS = []

        # OPTION 1: create new wallets and have them funded programmatically the randomly send/recieve tokens.
        # wallets = [Account.create() for _ in range(5)]  # Generate 5 wallets

        # store prvt keys in list
        # for i, wallet in enumerate(wallets):
        #     # print(f"Wallet {i+1}: {wallet.address} | Private Key: {wallet.key.hex()}")
            # PRIVATE_KEYS.append(wallet.key.hex())

        # OPTION 2: Use a pool of pre-funded wallets to randomly send/receive tokens
        wallets = ["0xb9BbfF793F311868DDd40743B376e2F9c37aC5c0", 
                "0xf5f5e8bD7DF904754a202B3EbBFBE9F756136DD4", 
                "0x29aa09717020655e62e533C4b6863551213C0A71", 
                "0xcAD937eE9d6D3472535D8599b7f0ddC8C6b61bB4"]

        # Load wallets from private keys (stored in .env)
        private_keys = self.PRIVATE_KEYS

        return {
            "wallets": wallets,
            "private_keys": private_keys
        }
