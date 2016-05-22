

## Tinfoil hat wallet? (synopsis/motivation)

This may be the most secure and private scalable multi-platform wallet ever (assuming that you follow the instructions and it gets some review).

For maximum security and privacy, it lacks any feature or functionality that allows the user to sign anything or to communicate with any network in any way. In that sense, it's not really a wallet, but a "wallet seeder" for other wallets that are able to import addresses and private keys (hopefully in the future some standard will emerge to import/export public and private bip32 subkeys). To generate addresses/privkeys from a given subkey, incremental natural numbers seem to work just fine for now.

Users should be able to organize BIP32 subkeys hierarchically in any custom way and use them in different existing and future scenarios, while maintaining the ability to maintain a single secure storage for the seed private key that can be trusted not to be compromised the most.

This is a tiny step in that direction. The tool currently lacks any storage capabilities and the user is expected to maintain a map/dictionary with subkey_path_string as key and something that makes sense to the user on paper.

Future functionality/vulnerabilities should come with the appropriate new you-are-probably-going-to-be-compromised-here warnings.

It is not user friendly, at this point you're supposed to use it from python's console.

## Installation (Debian/Ubuntu)

```
sudo apt install git python-dev ipython python-pip
git clone https://github.com/jtimon/tinfoil.git
cd tinfoil
pip -r requirements
```

## Basic usage
```
cd tinfoil
ipython
from tinfoil import *
```

## Preparations:

1) Have your favourite live unix live distribution ready in a usb. If you don't use Ubuntu, it is assumed that you know the translation of the Installation section to your OS distribution or have the courage to learn it.
2) Have another usb storage device that is not compromised at the hardware level or more paper.
3) [Optional] A tinfoil hat able to catch mind-reading scalar waves. 

## Example uses:

### Master Private key generation

If you don't have anything to protect, it cannot be secured.
So let's create something for you to be a target before you can be an user of supposedly-secure software.

1) Run your live trusted distro in a machine you trust (or the one that you distrust less), and follow the installation instructions.
2) Get alone in the room, close the windowns, put on the tinfoil hat [optional] and shut down the interwebs.
3) Invent your secret in paper, the default number of words, languages and number of weird symbols is "many", the random function is assumed to be implemented manually by the user, the more sources of randomness the better. The secret string has to be as long and random as possible, while still readable on paper. Store the paper securely (see FAQ section).
4) Produce the master public BIP32 subkey and put it in the trusted storage by introducing the private seed string in the trusted computer's memory.

```
In [1]: from tinfoil import *
In [2]: PublicMasterFromSecretString("change this")
Out[2]: u'xpub661MyMwAqRbcFimkg3kP1LXfxdZejrw6gqDRxmCoaKQKHE9VEfihCF4pUF5uCx99njsSME9kDDCWSApE2KMTR7ar82jWT279JEJMTdUouLn'
```
5) Shut down the live trusted distro.
6) You can remove the tinfoil hat now.

### Importing watch-only addresses to Bitcoin Core



## FAQ

Q: What about standards for seed generation and derivation?

There have been many proposals and BIPs but, for now, just follow BIP32 as a standard.

2.Q1): but what about multisig? multisig is the best for security, everybody knows this, it is known.

Yeah, a random paper string can be cut in peaces right?

If you wanted to do something serious like spending coins or smart contracts, that's fine. Once there's a standard for importing/exporting subkeys between wallets, it is even safe to let the payer participate in your rivate key generation as shown by [1] and [2].



Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.


### Master public key generation

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Contributing:

Given that almost nothing is done here, theres's many things to do, I guess.

## Tests

Yeah, do you want me to use a wallet without tests?

## TODO

- Proper environment

## Contributors

For now, just see requirements.txt

## License

\TheAuthors = Jorge Timón
Copyright (c) 2016-2016 \TheAuthors
Distributed under the MIT software license, see the accompanying
file COPYING or http://www.opensource.org/licenses/mit-license.php.
