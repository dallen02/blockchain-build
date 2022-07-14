##https://hackernoon.com/learn-blockchains-by-building-one-117428612f46##
import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
"""Block Section"""
        self.new_block(previous_hash=1, proof=100)

        def new_block(self, proof, previous_hash=None):
            # Creates a new Block and adds it to the chain
            block = {
                'index': len(self.chain) + 1,
                'timestamp': time(),
                'transactions': self.current_transactions,
                'proof': proof,
                'previous_hash': previous_hash or self.hash(self.chain[-1]),
            }

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
"""Transactions section"""
        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

'''Pycharm tells me the following function is unreachable. I'll look into it unless some finds the issue with it first
- Alivia 07/14/2022'''
        def new_transaction(self, sender, recipient, amount):
            self.current_transactions.append({
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            })
            return self.last_block['index'] + 1

"""Proof of Work Section"""

        def proof_of_work(self, last_proof):
            proof = 0
            while self.valid_proof(last_proof, proof) is False:
                proof += 1
            return proof

        @staticmethod
        def valid_proof(last_proof, proof):
            guess = f'{last_proof}{proof}'.encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            return guess_hash[:4] == "0000"

        @property
        def last_block(self):
            return self.chain[-1]

    @staticmethod
    def hash(block):
        # Hashes a Block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

"""Node Section"""
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
