
from subprocess import call

from pycoin.wallet import Wallet

PATH_TO_BITCOIN_CLI ='/home/jt/code/bitcoin/src/bitcoin-cli'

def ImportAddress(address, label='no-label'):
    call([PATH_TO_BITCOIN_CLI, 'importaddress', address, label])

def ImportPrivKey(privkey, label='no-label'):
    call([PATH_TO_BITCOIN_CLI, 'importprivkey', privkey, label])

def PublicMasterFromSecretString(secretString):
    return Wallet.from_master_secret(secretString).public_copy().wallet_key()

def AddressFromPublicMasterAndSubkeyPath(publicMaster, subkeyPath):
    return Wallet.from_wallet_key(publicMaster).subkey_for_path(subkeyPath).bitcoin_address()

def PrivKeyFromSecretStringAndSubkeyPath(secretString, subkeyPath):
    return Wallet.from_master_secret(secretString).subkey_for_path(subkeyPath).bitcoin_address()

# CreateAddressesFile('0-99-addresses.txt', publicMaster, '0/', 0, 100)
def CreateAddressesFile(path, publicMaster, baseSubkeyPath, firstSubkeyPos, endSubkeyPos):
    with open(path, 'w') as f:
        for i in xrange(firstSubkeyPos, endSubkeyPos, 1):
            subkeyPath = baseSubkeyPath + str(i)
            address = AddressFromPublicMasterAndSubkeyPath(publicMaster, subkeyPath)
            f.write(address + '\n')

# Example: ImportWatchOnlyBatch(publicMaster, '0/0/', 50, 100) will generate from 0/0/50 to 0/0/99 (50 addresses)
def ImportWatchOnlyBatch(publicMaster, baseSubkeyPath, firstSubkeyPos, endSubkeyPos):
    for i in xrange(firstSubkeyPos, endSubkeyPos, 1):
        subkeyPath = baseSubkeyPath + str(i)
        label = 'label-' + subkeyPath + '-' + publicMaster
        address = AddressFromPublicMasterAndSubkeyPath(publicMaster, subkeyPath)
        ImportAddress(address, label)

def ImportPrivkeysBatch(secretString, baseSubkeyPath, firstSubkeyPos, endSubkeyPos):
    for i in xrange(firstSubkeyPos, endSubkeyPos, 1):
        subkeyPath = baseSubkeyPath + str(i)
        label = 'label-' + subkeyPath + '-' + publicMaster
        privkey = PrivKeyFromSecretStringAndSubkeyPath(publicMaster, subkeyPath)
        ImportPrivKey(privkey, label)
