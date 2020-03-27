Most well known cyrpto currences:
Bitcoin
Ethereum
Alt-coins
Libra

Underlying theories are open source so others try to create 
Block-chain- keeping track of series of unmutable transactions
without having to trust anyone

What is a blockchain?
-data structre & support system to keep a public ledger of transactions
-on one owns it
-anyone can make a copy
-everyone has access to the source code 
-yet it is still secure, thanks to the clever use of cryptography

Blocks & Chains

-Index Number
-Timestamp 
-List of Transactions
-Proof used to Mine this Block #very complicated computation 
-Crptographic Hash of Previous Block 
    links rest of the blocks together , can't be modified without ruining rest of the chain   
    Hash function takes any amoutn of data, runs it thru a complicated scramble process & returns back a 
    diff set of data of fixed size & type
    -Must be determinstic: same data input _must_ result in same data output 
    -cryptographic quality: good distribution, no perceptible relationship or pattern between input and output 
    -simple to turn data into hash, but almost impossible to turn output-input
    - when we use a HF on all the data in a block, we get a unique representation of that block, very difficult to fake 
    -b/c hash avoids creating a pattern & outputs from similar inputs, changing just one char, creates a completely differnt hash. 
    

# Blockchain construction 
- Created by stringing together hashes
- Start with Genesis Block 
    -manually created
    -from that point forwards, each block forward contains the hash of the previous block 
    -prev block has a hash of the one before that 

-results in:
    -if bad actor changes the transactions in any of the blocks, the nextblock's prev. hash attribute will not match 
    the hash from previous block. Identitying blocks that are compromised 
    - can't redo, all of the hashes through rest of chain due to "proof" of work

# Review 
 - Each block contains a timestamp, list of transactions, proof & hash of the previous block
 - When the next block is created, the prev block data is hashed, and stored in that block, chaining them together 
 - Because the data for each block includes a hash of the prev block, if a transaction is modified, it will change the hash of that block
 - as a result, the prev hash recorded in the next block and all following blocks will no longer match, thus breaking the chain 

# Proof of Work 

-Created as a technique to combat spam- see hashcash
-An arbitrarily difficult problem that is solved by spending a large maount of computation time
-Work can't be re-used, although some systems are vulnerable to this exploitation 
-Solutions are difficult to compute, but easy to verify 
        (Inverse of hash function ^^^^)

SHA-256 Hash
-SHA stands for secure Hash Algo 
-creates a 32-byte hash
-usually displayed as a 64 digit hexadecimal number


# Simple Proof of work 

-We will be using a process that is similar to Bitcoin, though simpler & easier to find a solution
-Uses SHA-256 Hashing function to create a hash of the last block concatenated with the proposed solution
-The first N char must be zero, where N is a difficulty setting
-What is the time complexity of this arrangment?  
-computation time. When hashed will produce a hash w/ specific properties . specifically when hashed w/ last block, will produce hash with n leading zeros (n difficulty setting, can be varied to adjust amount of work to find solution)
(bitcoin requries more than 70 leading 0)


Review:
-proof of work is an arbitrarily difficult problem, that takes a large amount of computation to solve
-by requiring a solution that uses the hash of the previous block, plus a new value, work can't start ahead of time & can't be reused
-The difficult can be tuned to allow a consistent discovery of proofs, regardless of the total effort spent
-This protects the blockchains by making it very difficult to generate a new block  


# for project: remember to pipenv install flask 
pipenv --rm removes virtual nv 