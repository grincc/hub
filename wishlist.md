## Criticals / Must Have

1. [PIBD - Parallel Innitial Block Download](https://github.com/stakervali/grin-wishlist/issues/6)
  *- Done, Implemented*
2. Faster Header Sync. Header sync accounts for 70% of all data, yet sync is in parallel.  
3. [multi-sig](https://github.com/stakervali/grin-wishlist/issues/2)
  *- Requires building and signing in reverse order, not happening any time soon due to complexity with payment proofs. Use experience from Beam to implement MultiSig*
4. Wallet backend improvements
  *- Done, Grin-wallet had many bug fixes and stability improvements*
5. libsecp fork update 
   *- not updated, last commit to libsecp was 5 years ago*
6. safe cancel (cancel by self spend)
   *WIP, Done but p [Testing needed]*

## Important

1. Tor support for nodes*
2. [light node*](https://github.com/stakervali/grin-wishlist/issues/7)
3. [testnet exchange/ making it easier for exchange integrations](https://github.com/stakervali/grin-wishlist/issues/4)
 *- Done, Implemented - [Link]([url](https://github.com/stakervali/grin-wishlist/issues/4))*
4. payjoins
  *- Implemented in the contract branch and in grin GUI when you enable contract flow*
5. [binaries for older systems, older GLIBC or build on low RAM machine < 300MB]()
7. [invoice payment proofs*](https://github.com/stakervali/grin-wishlist/issues/10)
   *- Done [testing needed, contract branch], Bidirectional payment proofs have been implemented in the contract  branch and GUI branch wallet]([url](https://github.com/mimblewimble/grin-wallet/pull/681))*
8. hardware wallets \
  *- Done, Leger HW support for Grin is implemented, inofficial since a formal review costs money. [Tutorial](https://www.youtube.com/playlist?list=PLb1nuT3sFYbD_sydCVCngbvATsm9RwWyF), [Download the code here](https://github.com/NicolasFlamel1/ledger-live/releases)*   
  *- Done, Trezor HW support for grin is implemented. Also inoficial support requires flashing custom firmware for your Trezor  [Tutorial](https://www.youtube.com/watch?v=UXYfVNGxZM8)*

## Fix if time / Nice to Have

1. [wallet view key](https://forum.grin.mw/t/looking-for-a-tutorial-of-grin-wallet-cli-view-wallet-function-rewind-hash-and-scan-rewind-hash-150-grin-bounty/9444/11)
   *- Done, rewind hash has been implemented in grin-wallet*
3. [one-time use slatepack addresses for wallet*](https://github.com/stakervali/grin-wishlist/issues/11)
  *- Implemented in Grin++, not implemented in grin-wallet*
4. flyclient
   *- Nothing implemented, would require header history or inclusion proof according to discussions on KeyBase*
5. [atomic swaps*](https://github.com/stakervali/grin-wishlist/issues/1)
  *- Gene made a first implementation of "non-ideal" atomic swap, grin reaper offered to continue implementation, nothing fixed yet.*
  https://forum.grin.mw/t/questions-about-the-state-of-the-atomic-swap-pr-and-introduction/10332
  https://github.com/mimblewimble/grin-rfcs/pull/83
6. aggregators
  *- Done [testing needed, contract branch], mwixnet/CoinSwap is implemented on its way for integration in grin-wallet + plans from Ardocrat to work on integration in Grim*
[https://forum.grin.mw/t/request-for-funding-scilio-coinswap-implementation/9149**](https://forum.grin.mw/t/mwixnet-community-test/11405/19)
7. block archive node support*
   *- Done, fast sync method could still be added in the future*
8. [improve compatibility with OSX](https://github.com/stakervali/grin-wishlist/issues/3)
  *- No specific changes to my knowledge*
9. anchors, not needed if we have a daily aggregator which also protects against replay attacks [[REF]([url](https://forum.grin.mw/t/replay-resistance-through-payjoins-and-aggregators/8295/3))]
10. bulletproofs+
  *- [Not deemed safe/well tested enough yet in 2020](keybase://chat/grincoin#dev/5873)*, 
  *- [Had a positive review]([url](https://tari.substack.com/p/taris-bulletproofs-audit-is-done)) in Tari, (see [full report]([url](https://github.com/tari-project/bulletproofs-plus/blob/main/docs/quarkslab-audit/report.pdf)https://github.com/tari-project/bulletproofs-plus/blob/main/docs/quarkslab-audit/report.pdf)). 
11. None Recent Duplicate Kernels ([NRD]([url](https://docs.grin.mw/wiki/miscellaneous/nrd-kernels/))) activation, needed for lightning
*- WIP, Active on testnet*
12. [Display slatepacks as QR codes in CLI
  *Done, Implemented*
