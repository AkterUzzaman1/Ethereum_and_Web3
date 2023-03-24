import web3.eth
from web3 import Web3
from solcx import compile_source

# Need to install the solidity compiler here, this is the code for that ----------------------
from solcx import compile_standard, install_solc
install_solc("0.6.0")
# -----------------------------------------------------------------------------------------------

# connecting to a node
eth = 'http://127.0.0.1:7545'
w3 = Web3(Web3.HTTPProvider(eth))
chain_id = 1337
print("This the status of your connection to the blockchain: " + str(w3.isConnected()))

my_address = "0xFd20313E5A0Fe2bC12dd9cD08cdd360B8656c5Af"
private_key = "11203ca595e39ac576af31ae1c6b02a3495f4bd0eb5d9a193be4d154de6b4157"


# Solidity source code
# ------------------------------------------------------------------------
f = open("Stu_Management.sol", "r")
x = f.read()
compiled_sol = compile_source(x,output_values=['abi', 'bin'])
# ------------------------------------------------------------------------

# retrieve the contract interface -----------------------------------------
contract_id, contract_interface = compiled_sol.popitem()

# get bytecode / bin ----------------
bytecode = contract_interface['bin']
print("This is the bytecode ------------------>")
print(bytecode)
# get abi ---------------------------
abi = contract_interface['abi']
print("This is the ABI ------------------------>")
print(abi)

# The compiled code ------------------------------------
print("This is the compiled code ------------------>")
compiled_sol = compile_source(x,output_values=['abi', 'bin'])



# set pre-funded account as sender, this gives us the first account in the list of accounts
w3.eth.default_account = w3.eth.accounts[0]
print("This is the default account: " + str(w3.eth.default_account))

# Creating the contract object ------------------------------------------------------
STUDENT_MANAGEMENT= w3.eth.contract(abi=abi, bytecode=bytecode)
print(" This is the Student Management contract : " + str(STUDENT_MANAGEMENT))

# Get the latest transactionCount --------------------
nonce = w3.eth.getTransactionCount(my_address)



# Submit the transaction that deploys the contract ------------------------------------
transaction =STUDENT_MANAGEMENT.constructor("Akib",13,"Enrolled",[70]).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)

# Sign the transaction ------------------------------------------------------------------
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")

# Sending the transaction ----------------------------------------------------------------
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")
# -----------------------------------------------------------------------------------------


# Submit the transaction that deploys the contract-------------------------------------
tx_hash =STUDENT_MANAGEMENT.constructor("Joy",24,"Math",[93]).transact()
print("The transaction has occurred and this is the transaction hash: ")
print(tx_hash)


# Calling the greet function -----------------------
# Working with deployed Contracts
STUDENT_MANAGEMENT= w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(f"This is the get_no_sales function:  {STUDENT_MANAGEMENT.functions.getStudents(1).call()}")

# Calling the setGreeting function--------------------------------------------------------------------
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("This is the other transaction hash: " + str(tx_hash))

# Can further iterate the tx_receipt-----------------------
print("This is the transaction receipt")
print(tx_receipt)


# Calling the make_sale_record function -------------------------
print("This is the return from the make_sale_record() function: " )
print(STUDENT_MANAGEMENT.functions.addStudent("Alsaba",24,"Math,Bangla",[66,70]).transact())
print("Data type of this return is: " + str(type(STUDENT_MANAGEMENT.functions.addStudent("karib",22,"English",[90]).transact())))


#  -------------------------------------------------------------
# Reading from the smart contract
# This function is getting us the state variable called greeting
Student_info=STUDENT_MANAGEMENT.functions.getStudents(1).call()
print("This is the task: " + str(Student_info))


# Make  new Transaction using functions ------------------>
def addStudent(student):
    STUDENT_MANAGEMENT.functions.addStudent(student).transact()


def updateStudentInfo(x):
       student= STUDENT_MANAGEMENT.functions.updateStudentInfo(x).transact()
       return student


def updateStudentAge(x):
   student= STUDENT_MANAGEMENT.functions.updateStudentAge(x).transact()
   return student
def getStudents(x):
    student_info = (STUDENT_MANAGEMENT.functions.getStudents(x).call())
    return student_info


print("this is the task:")
print(getStudents(1))
