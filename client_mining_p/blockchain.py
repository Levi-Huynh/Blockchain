import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

"""
In the initial blockchain demonstration, we've created a small problem. 
The mine endpoint is called on the server, which means we're the ones 
spending all of the electricity to generate a new block. This won't do at all!

Furthermore, the amount of work needed to actually mine a block is a bit low. 
We need it to be harder to preserve the integrity of the chain.
"""


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        A block should have:
        * Index
        * Timestamp
        * List of current transactions
        * The proof used to mine this block
        * The hash of the previous block
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        """
          block_string = json.dumps(block, sort_keys=True)

        proof = 0
        while self.valid_proof(block_string, proof) is False:
            proof += 1

        return proof
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block)
        }

        # Reset the current list of transactions
        self.current_transactions = []
        # Append the chain to the block
        self.chain.append(block)
        # Return the new block
        return block

    def hash(self, block):
        """
        Creates a SHA-256 hash of a Block
        :param block": <dict> Block
        "return": <str>
        """

        # Use json.dumps to convert json into a string
        string_block = json.dumps(block, sort_keys=True)
        # Use hashlib.sha256 to create a hash
        # It requires a `bytes-like` object, which is what
        # .encode() does.
        raw_hash = hashlib.sha256(string_block.encode())
        # It converts the Python string into a byte string.
        # We must make sure that the Dictionary is Ordered,
        # or we'll have inconsistent hashes

        # TODO: Create the block_string

        # TODO: Hash this string using sha256

        # By itself, the sha256 function returns the hash in a raw string
        # that will likely include escaped characters.
        # This can be hard to read, but .hexdigest() converts the
        # hash to a string of hexadecimal characters, which is
        # easier to work with and understand
        hex_hash = raw_hash.hexdigest()
        # TODO: Return the hashed block string in hexadecimal format
        return hex_hash

    @property #dont have to use invoke() after calling these 
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        """
        Simple Proof of Work Algorithm
        Stringify the block and look for a proof.
        Loop through possibilities, checking each one against `valid_proof`
        in an effort to find a number that is a valid proof
        :return: A valid proof for the provided block
        """
        block_string = json.dumps(block, sort_keys=True)

        proof = 0
        while self.valid_proof(block_string, proof) is False:
            proof += 1

        return proof

        # return proof

    @staticmethod
    def valid_proof(block_string, proof):
        """
        Validates the Proof:  Does hash(block_string, proof) contain 3
        leading zeroes?  Return true if the proof is valid
        :param block_string: <string> The stringified block to use to
        check in combination with `proof`
        :param proof: <int?> The value that when combined with the
        stringified previous block results in a hash that has the
        correct number of leading zeroes.
        :return: True if the resulting hash is a valid proof, False otherwise
        """
        guess = f'{block_string}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:3] == "000"
# return True or False


# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

"""
@app.route('/mine', methods=['POST'])
def mine():
    data = request.get_json()
    if not request.json or "proof" not in request.json or "id" not in request.json:
        response = (
            "Please include proof or id, or make sure it is a post request",

        )
        return jsonify(response), 400
    # Run the proof of work algorithm to get the next proof
    #proof = blockchain.proof_of_work(blockchain.last_block)
    block_string = json.dumps(data, sort_keys=True)
    #proof = blockchain.proof_of_work(block_string)
    print("data from client's post", data['proof'])
    dataProof = data['proof']
    guess = f'{block_string}{dataProof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    def test():
        if guess_hash[:3] == "000":
            return 'New Block Forged'
        else:
            return 'Proof not verified'
    mytest = test()
    # Forge the new Block by adding it to the chain with the proof
    #previous_hash = blockchain.hash(blockchain.last_block)
    #block = blockchain.new_block(proof, previous_hash)

    response = {
        # TODO: Send a JSON response valid or not valid
        'proof': mytest

    }

    return jsonify(response), 200
"""
@app.route('/mine', methods=['POST'])
def mine():
    values = request.get_json()
    #breakpoint() here to investigate whats in values & what u think you're getting 
   

    """
    * Modify the `mine` endpoint to instead receive and validate or reject a new proof sent by a client.
    * It should accept a POST
    * Use `data = request.get_json()` to pull the data out of the POST
    * Note that `request` and `requests` both exist in this project
    * Check that 'proof', and 'id' are present
    * return a 400 error using `jsonify(response)` with a 'message'
    * Return a message indicating success or failure.  Remember, a valid proof should fail for all senders except the first. (Those who mined in second place should fail)
    """    
    
    required = ['proof', 'id']
    if not all(k in values for k in required): #nested for loop rt O(2n) 2 constant, n linear for what will be in values
        response = {'message': 'Youre missing values'}
        return jsonify(response), 400 

    submitted_proof = values['proof']

    block_string = json.dumps(blockchain.last_block, sort_keys=True)
  
    if blockchain.valid_proof(block_string, submitted_proof):
        #Forge the new Block by adding it to the chain with the proof
        previous_hash = blockchain.hash(blockchain.last_block)
        block = blockchain.new_block(submitted_proof, previous_hash)


        response = {
            # TODO: Send a JSON response valid or not valid
            'new_block': block

                    }

        return jsonify(response), 200
    else:
        response ={
            'message': 'Proof was invalid or already submitted' #will auto reject b/c what a late minr uses as proof for something, may not be correct block
        }
        return jsonify(response), 200

#late miner: only first miner that gets correct roof gets credit for it
#public ledger is just one big chain of blocks

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        # TODO: Return the chain and its current length
        'chain': blockchain.chain,
        'length': len(blockchain.chain)


    }
    return jsonify(response), 200


@app.route('/last_block', methods=['GET'])
def last_block():
    response = {
        # TODO: Return the chain and its current length
        'last_block': blockchain.last_block


    }
    return jsonify(response), 200


# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
