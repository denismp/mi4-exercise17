import json
from web3 import Web3, HTTPProvider

PROVIDER = "https://ropsten.infura.io/v3/2c64faa795c242d083706a5e3105e830"
w3 = Web3(HTTPProvider(PROVIDER))

CONTRACT_ADDRESS = "0x7007fb858fe544740efce14f86dd3cb1b591bde4"
PRIVATE_KEY = "0x7EB2255581AED1C929A291B65BC3A37FB70BA8C6783FFFABE18D8C6EC5DCFFC1"
ABI = '[ { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": ' \
      '"string", "name": "newFact", "type": "string" } ], "name": "add", "outputs": [], "stateMutability": ' \
      '"nonpayable", "type": "function" }, { "inputs": [], "name": "count", "outputs": [ { "internalType": "uint256", ' \
      '"name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { ' \
      '"internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "getFact", "outputs": [ { ' \
      '"internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" } ] '

# type_converter("address")(CONTRACT_ADDRESS)
w3.toChecksumAddress(CONTRACT_ADDRESS)
# CONTRACT_INSTANCE = w3.eth.contract(CONTRACT_ADDRESS,abi=json.loads(ABI))
CONTRACT_INSTANCE = w3.eth.contract(w3.toChecksumAddress(CONTRACT_ADDRESS),abi=json.loads(ABI))

ACCOUNT_ADDRESS = "0x28Fcf7997E56f1Fadd4FA39fD834e5B96cb13b2B" # from metamask

def add_fact(contract_instance, private_key, address, fact):
      nonce = w3.eth.getTransactionCount(address) # this must be the account address from metamask.
      add_transaction = contract_instance.functions.add(fact).buildTransaction({
            'gas': 4600000,
            'nonce': nonce
      })

      print(add_transaction)
      signed_txn = w3.eth.account.signTransaction(add_transaction, private_key=private_key)
      w3.eth.sendRawTransaction(signed_txn.rawTransaction)


def get_fact(contract_instance, index):
      fact = contract_instance.functions.getFact(index).call()
      print(fact)

def facts_count(contract_instance):
      count = contract_instance.functions.count().call()
      print('Stored facts in the contract: ', count)

fact = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks'
add_fact(CONTRACT_INSTANCE,PRIVATE_KEY,w3.toChecksumAddress(ACCOUNT_ADDRESS), fact)
get_fact(CONTRACT_INSTANCE, 0)
facts_count(CONTRACT_INSTANCE)
