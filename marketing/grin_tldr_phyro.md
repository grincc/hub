![a](https://i.imgur.com/JVBL9Wm.jpeg)
```
Chain validity:            Σkernels + offset*G = Σoutputs - height*60e9*H
Tx validity:               Σkernels + offset*G = Σoutputs - Σinputs
Monetary policy:           1 coin per second forever
Supply:                    height*60
DAA:                       last_diff * W / (W - BLOCK_TIME_SEC + last_block_time) (code[1])
Scripting:                 Scriptless scripts
PoW:                       Cuckoo cycle (spec[2], code[3])
Output:                    commitment (33 bytes)
Historical output:         /

[1] https://github.com/mimblewimble/grin/blob/master/core/src/consensus.rs#L376-L377
[2] https://github.com/tromp/cuckoo/blob/master/doc/mathspec
[3] https://github.com/tromp/cuckoo/blob/master/doc/spec                        
```