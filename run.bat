HParse gram wdnet
HDman -l log.txt -n stats.txt dict_used lexicon/dict
HLEd -A -D -T 1 -l * -d dict_used -i phones0.mlf mkphones0.led words.mlf
HLEd -A -D -T 1 -l * -d dict_used -i phones1.mlf mkphones1.led words.mlf
HCopy -A -D -T 1 -C wav_config -S codetrain.scp
