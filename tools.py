from web3 import Web3
import os

class Tools:

    def __init__(self):
        self.RPC_URL = os.getenv("ABSTRACT_CHAIN_RPC")
        
    def get_RPC_Provider(self):
        web3 = Web3(Web3.HTTPProvider(self.RPC_URL))
        return web3
