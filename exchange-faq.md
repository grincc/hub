

## Info Table

| Item | Link/Answer |
| ----------- | ----------- |
| Blockchain Explorer |  https://scan.grin.money/   |
| Technical Docs |  https://docs.grin.mw/ [node](https://docs.rs/grin_api/latest/grin_api/) [wallet](https://docs.rs/grin_wallet_libwallet/5.1.0/grin_wallet_libwallet/)  |
| Average block time | 60 sec |
| UTXO or account model |UTXO |
| Consensus mechanism | Proof of Work |
| Proposed number on-chain confirms for deposit | 30 |

 

### **GRIN SDK Location**  

Link of SDK or library for address generating, offline transaction building, signing, decoding (It can run offline, independent of online wallet or node)
 
 - [GRIN API - Owner](https://docs.rs/grin_api/5.1.2/grin_api/trait.OwnerRpc.html)
 - [GRIN API - Foreign](https://docs.rs/grin_api/5.1.2/grin_api/trait.ForeignRpc.html) 
 - [GRIN wallet API - Owner](https://docs.rs/grin_wallet_api/5.1.0/grin_wallet_api/trait.OwnerRpc.html)
 - [GRIN wallet API - Foreign](https://docs.rs/grin_wallet_api/5.1.0/grin_wallet_api/trait.ForeignRpc.html)
 

 
### **Address Generation**

How to generate address and private key

[Generate private key]
- (https://github.com/grincc/grin-wallet-api-tutorial#generating-a-private-key)

- (https://docs.rs/grin_wallet_api/5.1.0/grin_wallet_api/trait.OwnerRpc.html#tymethod.create_wallet)

[Generate address/wallet]
- (https://github.com/grincc/grin-wallet-api-tutorial#creating-a-wallet)




### **Deposit Scanning**

Tutorial for scanning deposit from the blockchain

https://docs.rs/grin_wallet_api/5.1.0/grin_wallet_api/trait.OwnerRpc.html#tymethod.retrieve_txs

https://github.com/grincc/grin-wallet-api-tutorial#listing-transactions

https://docs.rs/grin_wallet_api/5.1.0/grin_wallet_api/trait.OwnerRpc.html#tymethod.retrieve_summary_info

https://github.com/grincc/grin-wallet-api-tutorial#obtaining-wallet-balance






### **Node**
official repository
https://github.com/mimblewimble/grin/releases

#### - Access instruction of public Nodes

???????


#### - Node API documentation

- [GRIN API - Owner](https://docs.rs/grin_api/5.1.2/grin_api/trait.OwnerRpc.html)
- [GRIN API - Foreign](https://docs.rs/grin_api/5.1.2/grin_api/trait.ForeignRpc.html) 


#### - Node installation (steps or doc file)

https://docs.grin.mw/getting-started/build/


### **Withdraw**

#### - Demo for offline transaction building and signing, which gives outputs with transaction hash and signedTransaction

?????

#### - Demo/Tutorial for signedTransaction decoding 


?????


### **Wallet**
official repository
[https://github.com/mimblewimble/grin-wallet](https://github.com/mimblewimble/grin-wallet/releases/)


#### - GRIN Mining Pool distribution
https://github.com/Grinnode-live/grinnode.live/blob/master/documentation/mining-pools-list.md

Updated every month by volunteers.


