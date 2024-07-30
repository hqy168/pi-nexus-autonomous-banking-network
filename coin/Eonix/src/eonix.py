# eonix.py
from blockchain import Blockchain
from wallet import Wallet
from transaction import Transaction
from contract import EonixContract
from database import EonixDatabase
from ai import EonixAI
from ml import EonixML
from nlp import EonixNLP

class Eonix:
    def __init__(self):
        self.blockchain = Blockchain()
        self.wallet = Wallet()
        self.contract_manager = EonixContractManager()
        self.database = EonixDatabase()
        self.ai = EonixAI()
        self.ml = EonixML()
        self.nlp = EonixNLP()

    def create_transaction(self, recipient, amount):
        transaction = Transaction(self.wallet.public_key, recipient, amount)
        self.blockchain.add_transaction(transaction)

    def mine_block(self):
        self.blockchain.mine_pending_transactions()

    def get_balance(self):
        balance = 0
        for block in self.blockchain.chain:
            for transaction in block.transactions:
                if transaction.recipient == self.wallet.public_key:
                    balance += transaction.amount
                elif transaction.sender == self.wallet.public_key:
                    balance -= transaction.amount
        return balance

    def execute_contract(self, code, inputs):
        contract = EonixContract(code)
        return contract.execute(inputs)

    def store_data(self, data):
        return self.database.store_data(data)

    def retrieve_data(self, cid):
        return self.database.retrieve_data(cid)

    def predict_transaction_outcome(self, transaction):
        return self.ai.predict_outcome(transaction)

    def detect_fraudulent_transaction(self, transaction):
        return self.ml.predict_fraud(transaction)

    def analyze_sentiment(self, text):
        return self.nlp.analyze_sentiment(text)

    def extract_entities(self, text):
        return self.nlp.extract_entities(text)
