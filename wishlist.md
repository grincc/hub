## Criticals / Must Have

1. [PIBD - (faster and more robust syncing strategy)](https://github.com/stakervali/grin-wishlist/issues/6)
  *In beta and being tested on mainnet*
2. [multi-sig*](https://github.com/stakervali/grin-wishlist/issues/2)
  *Is not happening any time soon if I understand correctly, since there is no solution yet to generate threshold range proofs:*
3. Wallet backend improvements
  *Wallet had many bug fixes and stability improvements, are those what are referred to?*
4. libsecp fork update 
   *not updated, last commit to was 5 years ago*
5. safe cancel*
*WIP, not merged https://github.com/mimblewimble/grin-rfcs/pull/71, part of Grin GUI?*

## Important

1. Tor support for nodes*
2. [light node*](https://github.com/stakervali/grin-wishlist/issues/7)
3. [testnet exchange/ making it easier for exchange integrations](https://github.com/stakervali/grin-wishlist/issues/4)
  *Implemented - [Link]([url](https://github.com/pkariz/grin-wallet/tree/fix/invoice-issues))*
4. payjoins*
  Not really payjoin, but [Coin Swap, MWIXnet]([url](https://forum.grin.mw/t/request-for-funding-scilio-coinswap-implementation/9149)) is nearly implemented, see aggregator
5. [binaries for older systems, older GLIBC or build on low RAM machine < 300MB]()
7. [invoice payment proofs*](https://github.com/stakervali/grin-wishlist/issues/10)
  *Implemented in the grin GUI wallet, part of unified payment proof*
8. hardware wallets*
  *Implemented [Tutorial]([url](https://www.youtube.com/playlist?list=PLb1nuT3sFYbD_sydCVCngbvATsm9RwWyF), [Download the code here]([url](https://github.com/NicolasFlamel1/ledger-live/releases)))* 

## Fix if time / Nice to Have

1. wallet view key*
2. [one-time use slatepack addresses for wallet*](https://github.com/stakervali/grin-wishlist/issues/11)
  *Generate new slatepack address is implemented in Grin++, not yet in grin-wallet*
3. flyclient*
   *Nothing implemented, would require header history or inclusion proof according to discussions on KeyBase*
4. [atomic swaps*](https://github.com/stakervali/grin-wishlist/issues/1)
  *Gene made a first implementation of "non-ideal" atomic swap, grin reaper offered to continue implementation, nothing fixed yet.*
  https://forum.grin.mw/t/questions-about-the-state-of-the-atomic-swap-pr-and-introduction/10332
  https://github.com/mimblewimble/grin-rfcs/pull/83
5. aggregators
  **-mw-mixnet/CoinSwap, third stage under review with two open issues out of 9 issues**
https://forum.grin.mw/t/request-for-funding-scilio-coinswap-implementation/9149**
https://github.com/mimblewimble/mwixnet/issues/11
6. block archive node support*
   *Implemented, fast sync method could still be added in the future*
7. [improve compatibility with OSX](https://github.com/stakervali/grin-wishlist/issues/3)
  *No specific changes as far as I know*
8. anchors*
9. bulletproofs+*
  *Not deemed safe yet I think, or was that bulletproofs++*
10. NRD activation*
11. [Display slatepacks as QR codes in CLI
  *Implemented*
