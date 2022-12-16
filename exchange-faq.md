## Info Table

| Item | Link/Answer |
| ---- | ----------- |
| Blockchain explorer | [GrinExplorer](https://grinexplorer.net) |
| Technical documentation | [Grin documentation](https://docs.grin.mw), [Grin node API](https://docs.rs/grin_api/latest/grin_api), and [Grin wallet API](https://docs.rs/grin_wallet_api/latest/grin_wallet_api) |
| Average block time | 60 seconds |
| UTXO or account model | UTXO |
| Consensus mechanism | Proof of work |
| Proposed number of on-chain confirms for deposit | 30 |


## Grin SDK Location

The official [Grin node](https://github.com/mimblewimble/grin) and [Grin wallet](https://github.com/mimblewimble/grin-wallet) implementations provide APIs for address generating, offline transaction building, signing, decoding, etc. These API endpoints are separated into owner and foreign accessible methods which are documented here.

- [Grin node owner API](https://docs.rs/grin_api/latest/grin_api/trait.OwnerRpc.html)
- [Grin node foreign API](https://docs.rs/grin_api/latest/grin_api/trait.ForeignRpc.html)
- [Grin wallet owner API](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html)
- [Grin wallet foreign API](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.ForeignRpc.html)


## Private Key And Address Generation

The Grin wallet owner API exposes methods for creating a wallet with a provided mnemonic passphrase and for retrieving an existing wallet's mnemonic passphrase. Each passphrase is used internally to derive the extended private key for its corresponding wallet.

Creating a wallet is accomplished with the `create_wallet` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.create_wallet), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#creating-a-wallet).

Retrieving a wallet's mnemonic passphrase can be performed with the `get_mnemonic` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.get_mnemonic), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#getting-the-wallet-seed-phrase-or-recovery-phrase).

After a wallet has been created, its Slatepack address can be obtained using the Grin wallet owner API. Slatepack addresses are used to decrypt transaction data and sign payment proofs. Slatepack addresses do not appear on-chain like traditional cryptocurrency addresses, and they are not required to perform a Grin transaction.

A wallet's Slatepack address can be obtained with the `get_slatepack_address` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.get_slatepack_address), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#getting-the-wallet-address-slatepack-address).


## Deposit Scanning

The Grin wallet owner API provides methods for retrieving a wallet's list of transactions and current balance. These methods can be used to obtain up-to-date information about a wallet's transactions and balance by scanning for transaction changes with a node.

A wallet's list of transactions can be obtained with the `retrieve_txs` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.retrieve_txs), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#listing-transactions).

A wallet's balance can be obtained with the `retrieve_summary_info` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.retrieve_summary_info), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#obtaining-wallet-balance).


## Node

The official Grin node GitHub repository can be found [here](https://github.com/mimblewimble/grin), and compiled versions of it can be downloaded for Windows, macOS, and Linux [here](https://github.com/mimblewimble/grin/releases).


### Access Instruction Of Public Nodes

A public Grin node can be interacted with by making JSON-RPC calls to its foreign API interface. Here's an example of getting a node's current block height by using the `get_tip` method. All node foreign API methods are documented [here](https://docs.rs/grin_api/latest/grin_api/trait.ForeignRpc.html).

Request:
```
curl https://grinnode.live:3413/v2/foreign -d "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"get_tip\",\"params\":[]}"
```

Response:
```
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "Ok": {
      "height": 1604333,
      "last_block_pushed": "001bac4450afe324cb46b95bafee5abe57340f07aa35b25f6a8aae25bec70498",
      "prev_block_to_last": "0018ef66711879e0e8be0c774e1af2b7e1865c909767cbd4c0e9d55f51540208",
      "total_difficulty": 169285794666453
    }
  }
}
```


### Node API Documentation

The Grin node API endpoints are separated into owner and foreign accessible methods which are documented here.

- [Grin node owner API](https://docs.rs/grin_api/latest/grin_api/trait.OwnerRpc.html)
- [Grin node foreign API](https://docs.rs/grin_api/latest/grin_api/trait.ForeignRpc.html)


### Node Installation

Compiled versions of the official Grin node can be downloaded for Windows, macOS, and Linux [here](https://github.com/mimblewimble/grin/releases), or instructions for building it from scratch can be found [here](https://docs.grin.mw/getting-started/build).


## Withdraw


### Building And Signing Transactions

The Grin wallet [owner API](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html) and [foreign API](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.ForeignRpc.html) provide the methods needed to send and receive Grin.

The process for sending Grin via a Slatepack from the sender's perspective involves the following steps.

1. The sender creates a slate with the `init_send_tx` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.init_send_tx), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#sending-a-transaction).

2. The `init_send_tx` method returns a slate which needs to be encoded as a Slatepack before it can be sent to the transaction's recipient, so the sender encodes it with the `create_slatepack_message` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.create_slatepack_message), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#preparing-slate-to-be-sent-slate--slatepack-message).

3. The Slatepack that was returned by the `create_slatepack_message` method is then given to the transaction's recipient, and the recipient processes it and returns the Slatepack response to the transaction's sender.

4. The Slatepack response needs to be decoded by the transaction's sender before they can finalize it, and this can be done with the `slate_from_slatepack_message` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.slate_from_slatepack_message), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#finalizing-a-transaction).

5. The outputs associated with the inputs being spent in the transaction need to be locked with the `tx_lock_outputs` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.tx_lock_outputs), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#finalizing-a-transaction).

6. The `slate_from_slatepack_message` method returns the slate response that the sender can finalize with the `finalize_tx` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.finalize_tx), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#finalizing-a-transaction).

7. The finalized slate that the `finalize_tx` method returns can then be broadcast to the Grin network with the `post_tx` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.post_tx), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#posting-a-transaction).

A more detailed explanation of this process can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#sending-a-transaction).

The process for receiving Grin via a Slatepack from the recipient's perspective involves the following steps.

1. The transaction's sender will give a Slatepack to the transaction's recipient. This Slatepack needs to be decoded before the recipient can process it which can be done with the `slate_from_slatepack_message` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.slate_from_slatepack_message), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#receiving-a-transaction).

2. The slate that the `slate_from_slatepack_message` method returns can then be processed by the recipient with the `receive_tx` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.ForeignRpc.html#tymethod.receive_tx), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#receiving-a-transaction).

3. The slate response that the `receive_tx` method returns then needs to be encoded before it can be given to the transaction's sender using the `create_slatepack_message` method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.create_slatepack_message), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#receiving-a-transaction).

4. The Satepack response returned by the `create_slatepack_message` method can then be given to the transaction's sender for them to finalize it.

A more detailed explanation of this process can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#receiving-a-transaction).

Grin transactions can also be sent and received via Tor by sending Grin to a wallet's Slatepack address converted to a Tor address. This is explained more [here](https://github.com/grincc/grin-wallet-api-tutorial#sending-slates-via-the-foreign-api-using-tor). The recipient must be listening at its Tor address at the time of the transaction in order to receive it. The only difference in the transaction process when done via Tor is that slates, not Slatepacks, are sent to and returned from the recipient, so there's no need for the `create_slatepack_message` and `slate_from_slatepack_message` methods in this case.

### Signed Transaction Decoding

A slate which represents a Grin transaction object is returned as serialized JSON by all Grin wallet API JSON-RPC endpoints. This is trivial to decode.

A Slatepack which encodes a slate for transport can be decoded with the `slate_from_slatepack_message` wallet owner API method which is documented [here](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html#tymethod.slate_from_slatepack_message), and an example of using it can be found [here](https://github.com/grincc/grin-wallet-api-tutorial#receiving-a-transaction).

A slate serialized as JSON will look similar to the following. The purpose of each component is explained [here](https://docs.grin.mw/wiki/transactions/slates).
```
{
  "ver": "4:2",
  "id": "0436430c-2b02-624c-2032-570501212b00",
  "sta": "S3",
  "off": "750dbf4fd43b7f4cfd68d2698a522f3ff6e6a00ad9895b33f1ec46493b837b49",
  "fee": "23500000",
  "sigs": [
    {
      "xs": "033bbe2a419ea2e9d6810a8d66552e709d1783ca50759a44dbaf63fc79c0164c4c",
      "nonce": "031b84c5567b126440995d3ed5aaba0565d71e1834604819ff9c17f5e9d5dd078f",
      "part": "8f07ddd5e9f5179cff19486034181ed76505baaad53e5d994064127b56c5841b92c7c53280dd79f8b028cd9863bac89820267cac794b121e217541efb061ad53"
    },
    {
      "xs": "02b57c1f4fea69a3ee070309cf8f06082022fe06f25a9be1851b56ef0fa18f25d6",
      "nonce": "031b84c5567b126440995d3ed5aaba0565d71e1834604819ff9c17f5e9d5dd078f",
      "part": "8f07ddd5e9f5179cff19486034181ed76505baaad53e5d994064127b56c5841b4cd4afef1cd2d708100cd1680d6566e4e987ac5c939ace9c0e036a679121c7a8"
    }
  ],
  "coms": [
    {
      "f": 1,
      "c": "087df32304c5d4ae8b2af0bc31e700019d722910ef87dd4eec3197b80b207e3045"
    },
    {
      "f": 1,
      "c": "08e1da9e6dc4d6e808a718b2f110a991dd775d65ce5ae408a4e1f002a4961aa9e7"
    },
    {
      "c": "099b48cfb1f80a2347dc89818449e68e76a3c6817a532a8e9ef2b4a5ccf4363850",
      "p": "29701ceae262cac77b79b868c883a292e61e6de8192b868edcd1300b0973d91396b156ace6bd673402a303de10ddd8a5e6b7f17ba6557a574a672bd04cc273ab04ed8e2ca80bac483345c0ec843f521814ce1301ec9adc38956a12b4d948acce71295a4f52bcdeb8a1c9f2d6b2da5d731262a5e9c0276ef904df9ef8d48001420cd59f75a2f1ae5c7a1c7c6b9f140e7613e52ef9e249f29f9340b7efb80699e460164324616f98fd4cde3db52497c919e95222fffeacb7e65deca7e368a80ce713c19de7da5369726228ee336f5bd494538c12ccbffeb1b9bfd5fc8906d1c64245b516f103fa96d9c56975837652c1e0fa5803d7ccf1147d8f927e36da717f7ad79471dbe192f5f50f87a79fc3fe030dba569b634b92d2cf307993cce545633af263897cd7e6ebf4dcafb176d07358bdc38d03e45a49dfa9c8c6517cd68d167ffbf6c3b4de0e2dd21909cbad4c467b84e5700be473a39ac59c669d7c155c4bcab9b8026eea3431c779cd277e4922d2b9742e1f6678cbe869ec3b5b7ef4132ddb6cdd06cf27dbeb28be72b949fa897610e48e3a0d789fd2eea75abc97b3dc7e00e5c8b3d24e40c6f24112adb72352b89a2bef0599345338e9e76202a3c46efa6370952b2aca41aadbae0ea32531acafcdab6dd066d769ebf50cf4f3c0a59d2d5fa79600a207b9417c623f76ad05e8cccfcd4038f9448bc40f127ca7c0d372e46074e334fe49f5a956ec0056f4da601e6af80eb1a6c4951054869e665b296d8c14f344ca2dc5fdd5df4a3652536365a1615ad9b422165c77bf8fe65a835c8e0c41e070014eb66ef8c525204e990b3a3d663c1e42221b496895c37a2f0c1bf05e91235409c3fe3d89a9a79d6c78609ab18a463311911f71fa37bb73b15fcd38143d1404fd2ce81004dc7ff89cf1115dcc0c35ce1c1bf9941586fb959770f2618ccb7118a7"
    },
    {
      "c": "09ede20409d5ae0d1c0d3f3d2c68038a384cdd6b7cc5ca2aab670f570adc2dffc3",
      "p": "6d86fe00220f8c6ac2ad4e338d80063dba5423af525bd273ecfac8ef6b509192732a8cd0c53d3313e663ac5ccece3d589fd2634e29f96e82b99ca6f8b953645a005d1bc73493f8c41f84fb8e327d4cbe6711dba194a60db30700df94a41e1fda7afe0619169389f8d8ee12bddf736c4bc86cd5b1809a5a27f195209147dc38d0de6f6710ce9350f3b8e7e6820bfe5182e6e58f0b41b82b6ec6bb01ffe1d8b3c2368ebf1e31dfdb9e00f0bc68d9119a38d19c038c29c7b37e31246e7bba56019bc88881d7d695d32557fc0e93635b5f24deffefc787787144e5de7e86281e79934e7e20d9408c34317c778e6b218ee26d0a5e56b8b84a883e3ddf8603826010234531281486454f8c2cf3fee074f242f9fc1da3c6636b86fb6f941eb8b633d6e3b3f87dfe5ae261a40190bd4636f433bcdd5e3400255594e282c5396db8999d95be08a35be9a8f70fdb7cf5353b90584523daee6e27e208b2ca0e5758b8a24b974dca00bab162505a2aa4bcefd8320f111240b62f861261f0ce9b35979f9f92da7dd6989fe1f41ec46049fd514d9142ce23755f52ec7e64df2af33579e9b8356171b91bc96b875511bef6062dd59ef3fe2ddcc152147554405b12c7c5231513405eb062aa8fa093e3414a144c544d551c4f1f9bf5d5d2ff5b50a3f296c800907704bed8d8ee948c0855eff65ad44413af641cdc68a06a7c855be7ed7dd64d5f623bbc9645763d48774ba2258240a83f8f89ef84d21c65bcb75895ebca08b0090b40aafb7ddef039fcaf4bad2dbbac72336c4412c600e854d368ed775597c15d2e66775ab47024ce7e62fd31bf90b183149990c10b5b678501dbac1af8b2897b67d085d87cab7af4036cba3bdcfdcc7548d7710511045813c6818d859e192e03adc0d6a6b30c4cbac20a0d6f8719c7a9c3ad46d62eec464c4c44b58fca463fea3ce1fc51"
    }
  ]
}
```


## Wallet

The official Grin wallet GitHub repository can be found [here](https://github.com/mimblewimble/grin-wallet), and compiled versions of it can be downloaded for Windows, macOS, and Linux [here](https://github.com/mimblewimble/grin-wallet/releases).


## Grin Mining Pool Distribution

A list of current mining pools for Grin and their corresponding distributions can be found [here](https://github.com/Grinnode-live/grinnode.live/blob/master/documentation/mining-pools-list.md). This information is updated every month by volunteers.
