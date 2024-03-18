## Criticals / Must Have

1. [PIBD - (faster and more robust syncing strategy)](https://github.com/stakervali/grin-wishlist/issues/6)
  *-In beta, being tested on mainnet*
2. [multi-sig*](https://github.com/stakervali/grin-wishlist/issues/2)
  *-Requires building and signing in reverse order, not happening any time soon due to complexity with payment proofs, but perhapps multisig with HW is ok since it is strictly two parties involved:*
3. Wallet backend improvements
  *- Grin-wallet had many bug fixes and stability improvements*
4. libsecp fork update 
   *-not updated, last commit to libsecp was 5 years ago*
5. safe cancel*
   *WIP, not merged https://github.com/mimblewimble/grin-rfcs/pull/71, part of Grin GUI?*

## Important

1. Tor support for nodes*
2. [light node*](https://github.com/stakervali/grin-wishlist/issues/7)
3. [testnet exchange/ making it easier for exchange integrations](https://github.com/stakervali/grin-wishlist/issues/4)
 *-Implemented - [Link]([url](https://github.com/stakervali/grin-wishlist/issues/4))*
4. payjoins*
  *-Not really payjoin, but [Coin Swap, mwixnet]([url](https://forum.grin.mw/t/request-for-funding-scilio-coinswap-implementation/9149)) is nearly implemented, see aggregator*
5. [binaries for older systems, older GLIBC or build on low RAM machine < 300MB]()
7. [invoice payment proofs*](https://github.com/stakervali/grin-wishlist/issues/10)
    *-Implemented in the under contract flow branch [grin GUI wallet]([url](https://github.com/mimblewimble/grin-wallet/pull/681)), part of unified/[biderection payment proofs]([url](https://phyro.github.io/grinvestigation/bidirectional_paymentproofs.html))*
8. hardware wallets*
  *-Leger HW support for Grin is implemented. [Tutorial]([url](https://www.youtube.com/playlist?list=PLb1nuT3sFYbD_sydCVCngbvATsm9RwWyF), [Download the code here]([url](https://github.com/NicolasFlamel1/ledger-live/releases)))* 

## Fix if time / Nice to Have

1. [wallet view key*](https://forum.grin.mw/t/looking-for-a-tutorial-of-grin-wallet-cli-view-wallet-function-rewind-hash-and-scan-rewind-hash-150-grin-bounty/9444/11)
   *-Implemented in grin-wallet, not yet in Grin++*
3. [one-time use slatepack addresses for wallet*](https://github.com/stakervali/grin-wishlist/issues/11)
  *-Generate new slatepack address is implemented in Grin++, not yet in grin-wallet*
4. flyclient*
   *-Nothing implemented, would require header history or inclusion proof according to discussions on KeyBase*
5. [atomic swaps*](https://github.com/stakervali/grin-wishlist/issues/1)
  *-Gene made a first implementation of "non-ideal" atomic swap, grin reaper offered to continue implementation, nothing fixed yet.*
  https://forum.grin.mw/t/questions-about-the-state-of-the-atomic-swap-pr-and-introduction/10332
  https://github.com/mimblewimble/grin-rfcs/pull/83
6. aggregators
  *-mwixnet/CoinSwap, third stage under review with two open issues out of 9 issues*
https://forum.grin.mw/t/request-for-funding-scilio-coinswap-implementation/9149**
https://github.com/mimblewimble/mwixnet/issues/11
7. block archive node support*
   *-Implemented, fast sync method could still be added in the future*
8. [improve compatibility with OSX](https://github.com/stakervali/grin-wishlist/issues/3)
  *-No specific changes as far as I know, or are these part of the many changes to grin-wallet*
9. anchors*
10. bulletproofs+*
  *-[Not deemed safe/well tested enough yet in 2020](keybase://chat/grincoin#dev/5873), 
  *-Had a [positive review]([url](https://tari.substack.com/p/taris-bulletproofs-audit-is-done)) in Tari, (see [full report]([url](https://github.com/tari-project/bulletproofs-plus/blob/main/docs/quarkslab-audit/report.pdf)https://github.com/tari-project/bulletproofs-plus/blob/main/docs/quarkslab-audit/report.pdf)). 
11. NRD activation*
12. [Display slatepacks as QR codes in CLI
  *-Implemented*
