SHA256
emn178.github.io/online-tools/sh256.html 

Hexadecimal coutning:
Decimal is a base 10 number system (perfect for beings with 10 fingers), and it uses a collection of 10 unique digits, which can be combined to positionally represent numbers.

Hex, like decimal, combines a set of digits to create large numbers. It just so happens that hex uses a set of 16 unique digits. Hex uses the standard 0-9, but it also incorporates six digits you wouldn't usually expect to see creating numbers: A, B, C, D, E, and F.

There are many (infinite!) other numeral systems out there. Binary (base 2) is also popular in the engineering world, because it's the language of computers. The base 2, binary, system uses just two digit values (0 and 1) to represent numbers.

Hex, along with decimal and binary, is one of the most commonly encountered numeral systems in the world of electronics and programming. It's important to understand how hex works, because, in many cases, it makes more sense to represent a number in base 16 than with binary or decimal.

{
    index: 0
    transactions: {brian gets all the coins}
    timestamp: today
    proof of work: according to the system
    hash of previous block: Today I'm gonna be rich


}


Add some data to current block so give you the longest chain of 0's
-need 16 tries to get 0 (16 possible chars counting in hexadecimal)
-but probability doesn't mean you're guranteed to get a leading 0 w/16 or any specific number of tries
-unlikely but possible to never get a leading zero. But if Hash has even distribution should be able to get 
-16^2 to get 2 leading zeros
-16^3 to get 3 leading zeros
-for bitcoin, need 70+ leading zeros 
    -to do this by yourself, on your pc, could take over 200 years 
    -except 0.01 sec ofo quantum computer 
    -to solve, have distribution of miners 
    -we raise prices of gpus, b/c we're leveraging the processing power, but ASICS (software made for mining hashes) has taken over 
        -ASICS - application specific integrated circuits
        -may trend toward going horizontal (more, instead of going faster) Ex/ pc's tapping out at 3.3 gigahertz but 
        built with 62 or 32 cores etc. Broadband internet instead of "fastband"


-changing any of the entries in the hash function, will cause the hash attempt (41, which may create the desired leading zero of 1, may not work anymore)
-In order for hacker to be succesful, must redo all the hashes of all blocks in chain, w/ the correct number of leading zeros.... _before_ the next block is mined by _community_ , in order for hacker's new entry to work & be acceptable 
-what if one person has 51% of the community mining power??? 
    - They can write new ledger entries however they want & retro reverse ledgers
    -IF they have the longest chain, the most cumulative work, they have the truest/trustworthy  ledger (moral issue here?)


ex/ large amount of etherium had chain hacked
    -split between those who wantd to reverse & roll back the changed ledgers & those who wanted to keep the sanctity of the chain & not touch it/ b/c it still abided by the hash principles 
    ^ so etherium choose to _fork_ both versions (one where the manipulated ledgers were rolledback, one where ledgers were kept in place)
    -^ social consensus. 2 diff parties of miners consented to split: Etherium(kept it, did not rollback), Etherium classic(rolledback)

Node:
    -running the blockchain software, has copy of chain, can accpet transactions or claim that someone has mined block succesfully.  node decide which version of software they want to use, and which other nodes they want to cooperate with. 
    # At the end of the day its about who has the longest valid chain, most valid, most in use. Otherwise split can occur or fork that results in change.  
    Ndes do the job of verifying.  Managing mining pool. Takes long to mine coin. Every 10 min have 10 / 100 years chances of getting bitcoin.  if hit, get money, else nothing.  PPL joing mning pool, to look at different segments to look at. If someone in pool gets lucky & gets coin, reward is split within community, based on how many hashes you got.   

MAC Address: unique id assigned to network interface (NIC)
for use as a network address in communications w/in a network segment. 
-conflicting /duplicate NICS ,with same MAC addresses


#PRE STEPS
-familiraize self w/ dependencies, code, questions
-try to run file before writing code 
-will chain do anything (endpoint will run if set up right, even if nothing there)

-run server
-add a response to return (restart if don't see response. doesn't auto start, may have plugin)
-test code in one of your get apis!

