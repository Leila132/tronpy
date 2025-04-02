from tronpy import Tron
import time
from typing import Dict


class TronApiClient:
    def __init__(self):
        self.client = Tron()

    def get_tron_data(self, address: str) -> Dict:
        balance = self.client.get_account_balance(address.address)
        time.sleep(2)
        account = self.client.get_account_resource(address.address)
        return {
            "address": address.address,
            "balance": balance,
            "bandwidth": account["TotalNetWeight"],
            "energy": account["TotalEnergyWeight"],
        }
