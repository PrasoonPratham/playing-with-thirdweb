from nftlabs import NftlabsSdk, SdkOptions, ListArg, MintArg
import os

from nftlabs.modules.currency import CurrencyModule

# Conncect to the SDK, we're using the testnet to test it
sdk = NftlabsSdk(SdkOptions(), "https://rinkeby-light.eth.linkpool.io/")

# This is your wallet's private key, you can find them in your wallet. This will be used to interact with the contract 
# WARNING: Never share this with anyone.
sdk.set_private_key("a0064ca30a15d338590d95fc7d1e87f889d11fe31897340b391674e84d49f1ee")

# Initiate the modules so you can start interacting with the smart contracts. You can g=et these address in your thirdweb dashboard at https://www.thirdweb.com/dashboard
nft_module = sdk.get_nft_module("0xAC914C57a2a263E54d6516E3a61D35dF88dF8334")
#currency_module = sdk.get_currency_module("0x10E49aaBDad7B8Aa624fbbaCD6b93DC20e3dDBcD")
#market_module = sdk.get_market_module("0x2B1Af44BaC45Bd9C400e6388bff0DD144e6EF4e6")

#print(nft_module.balance())
#print(nft_module.get(0))

name_nft = "new nft!"
description_nft = "NFT EXAMPLE"
image_nft = "ipfs://QmdFeKxt6FJUNvaGgzYuYNRbpNWyHxP2PFzjsgPf1eD2Jf"
prop = {}

 #Mint the NFT!
#print(nft_module.mint(MintArg(name=name_nft, description=description_nft, image_uri=image_nft, properties=prop)))

amount = 1000

# currency_module.mint(amount* (10**18))
# print(CurrencyModule.balance())


#nft_test.balance_of("0x55c9bBb71a5CC11c2f0c40362Bb691b33a78B764")
#print(NftModule.balance("0x55c9bBb71a5CC11c2f0c40362Bb691b33a78B764"))
#print(NftModule.balance_of("0x55c9bBb71a5CC11c2f0c40362Bb691b33a78B764"))

#nft_test = NftModule("0x55c9bBb71a5CC11c2f0c40362Bb691b33a78B764")
#nft_test.balance_of()

#NftModule.balance_of(nft_module, "0x55c9bBb71a5CC11c2f0c40362Bb691b33a78B764")

#https://rinkeby-light.eth.linkpool.io/
#https://rinkeby.arbitrum.io/rpc

