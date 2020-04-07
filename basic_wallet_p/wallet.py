import hashlib
import requests

import sys
import json


def proof_of_work(block):
    """
    Simple Proof of Work Algorithm
    Stringify the block and look for a proof.
    Loop through possibilities, checking each one against `valid_proof`
    in an effort to find a number that is a valid proof
    :return: A valid proof for the provided block
    """
    block_string = json.dumps(block, sort_keys=True)

    new_proof = 0
    while valid_proof(block_string, new_proof) is False:
        new_proof += 1

    return new_proof


def valid_proof(block_string, new_proof):
    """
    Validates the Proof:  Does hash(block_string, proof) contain 6
    leading zeroes?  Return true if the proof is valid
    :param block_string: <string> The stringified block to use to
    check in combination with `proof`
    :param proof: <int?> The value that when combined with the
    stringified previous block results in a hash that has the
    correct number of leading zeroes.
    :return: True if the resulting hash is a valid proof, False otherwise
    """
    guess = f'{block_string}{new_proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    return guess_hash[:3] == "000"


if __name__ == '__main__':
    # What is the server address? IE `python3 miner.py https://server.com/api/`
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

# enter new ID

    nameInput = str(input(
        "enter new ID or update your curr ID, otherwise enter [skip] if already have ID: "))

    if "skip" not in nameInput:
        f = open("my_id.txt", "w+")
        check1 = f.write(nameInput)
        f.close()
        f = open("my_id.txt", "r")
        id = f.read()
        print("ID is", id)
        f.close()
    else:
        pass


# Load current ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    # break

# breakpoint()
# {'chain': [{'index': 1, 'previous_hash': 1, 'proof': 100,
# 'timestamp': 1585259688.7443342, 'transactions': []}], 'length': 1}
"""
This app should:
    * X Allow the user to enter, save, or change the `id` used for the program
        # post, update, id request to server for id
    * X Display the current balance for that user
        # subset of all transactions belonging to user
            -(when they are sender, reduce the total),
            -when they are recipient, increase total
    * Display a list of all transactions for this user, including sender and recipient
            -list of transactions related to user
"""
# Run forever until interrupted
coins = 0
userTotal = 0
transactionList = []
print("Starting mining")
while True:
    r = requests.get(url=node + "/last_block")
    # Handle non-json response
    try:
        data = r.json()
        # print("data from get", data)
    except ValueError:
        print("Error:  Non-json response")
        print("Response returned:")
        print(r)
        # break

    # breakpoint() === a cool python debugger!
    # need to always grab the last block to build the chain
    block = data['last_block']
    # old_proof= block['proof']
    # TODO: Get the block from `data` and use it to look for a new proof
    # new_proof = ???
    # block data here
    # When found, POST it to the server {"proof": new_proof, "id": id}

    new_proof = proof_of_work(block)
    print(f"Proof found: {new_proof}")
    post_data = {"proof": new_proof, "id": id}

    r = requests.post(url=node + "/mine", json=post_data)
    print("finished mine")
    try:
        data = r.json()
    except ValueError:
        print("Error:  Non-json response")
        print("Response returned:")
        print(r)
        # break

    # get /chain endpoint
    r = requests.get(url=node + "/chain")
    print("finished chain")
    try:
        data = r.json()
    except ValueError:
        print("Error:  Non-json response")
        print("Response returned:")
        print(r)

    #total = data['chain'][1]['transactions'][0]['recipient']
    total = data['chain']
    # total3 = total2[]
    # print(total)
    for chainElement in total:

        print("here", chainElement)
        if len(chainElement['transactions']) > 0:
            for i in range(len(chainElement['transactions'])):
                if chainElement['transactions'][i]['recipient'] == id:
                    userTotal += chainElement['transactions'][i]['amount']
                    transactionList.append(chainElement['transactions'])
                if chainElement['transactions'][i]['sender'] == id:
                    userTotal -= chainElement['transactions'][i]['amount']
                    transactionList.append(chainElement['transactions'])

    print(f"User balance for {id} is {userTotal}")

    ViewTransactions = input(
        "To view list of user transactions, enter [transactions] otherwise enter [skip]:")
    if "transactions" in ViewTransactions:
        print(transactionList)
    else:
        pass

    # breakpoint()


def getBalance():
    r = requests.get(url=node + "/chain")
    try:
        data = r.json()
    except ValueError:
        print("Error:  Non-json response")
        print("Response returned:")
        print(r)


getBalance()

breakpoint()
