Account balances in a blockchain currency are not real values that are stored somewhere.  Instead, wallet programs derive this balance by adding and subtracting all of the transactions for the user that are recorded in the ledger, to calculate the current balance.

Build a simple wallet app using the front-end technology of your choice.  You will not be evaluated on the aesthetics of your app.

This app should:
    * Allow the user to enter, save, or change the `id` used for the program
        #post, update, id request to server for id 
    * Display the current balance for that user
        #subset of all transactions belonging to user 
            -(when they are sender, reduce the total), 
            -when they are recipient, increase total 
    * Display a list of all transactions for this user, including sender and recipient
            -list of transactions related to user 

Stretch Goals:
    * Use styling to visually distinguish coins sent and coins received
    * Paginate the list of transactions if there are more than ten #server 