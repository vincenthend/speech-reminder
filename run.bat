rem created a set of folder
mkdir generated
mkdir generated\phones
mkdir logs
mkdir train\mfcc

rem parse grammar (gram) and generate the word network
HParse train/gram generated/wdnet

rem create dictionary used in the training
HDman -l logs/log.txt -n generated/monophones1 generated/dict_used train/lexicon/dict

rem create monophones file with silence
py scripts/monophones0.py

rem create mlf file containing transcript of wav files, and generate label with led script
py scripts/mlf.py
HLEd -A -D -T 1 -l * -d generated/dict_used -i generated/phones/phones0.mlf train/mkphones0.led generated/words.mlf
HLEd -A -D -T 1 -l * -d generated/dict_used -i generated/phones/phones1.mlf train/mkphones1.led generated/words.mlf

py scripts/scp.py
HCopy -A -D -T 1 -C configurations/wav_config -S generated/codetrain.scp
mkdir hmms
mkdir hmms\hmm0
HCompV -A -D -T 1 -C configurations/config -f 0.01 -m -S generated/train.scp -M hmms/hmm0 train/proto
py scripts/hmmdefs.py
py scripts/macros.py
mkdir hmms\hmm1
mkdir hmms\hmm2
mkdir hmms\hmm3
mkdir hmms\hmm4
mkdir hmms\hmm5
mkdir hmms\hmm6
mkdir hmms\hmm7
mkdir hmms\hmm8
mkdir hmms\hmm9
HERest -A -D -T 1 -C configurations/config -I generated/phones/phones0.mlf -t 250.0 150.0 1000.0 -S generated/train.scp -H hmms/hmm0/macros -H hmms/hmm0/hmmdefs -M hmms/hmm1 generated/monophones0
HERest -A -D -T 1 -C configurations/config -I generated/phones/phones0.mlf -t 250.0 150.0 1000.0 -S generated/train.scp -H hmms/hmm1/macros -H hmms/hmm1/hmmdefs -M hmms/hmm2 generated/monophones0
HERest -A -D -T 1 -C configurations/config -I generated/phones/phones0.mlf -t 250.0 150.0 1000.0 -S generated/train.scp -H hmms/hmm2/macros -H hmms/hmm2/hmmdefs -M hmms/hmm3 generated/monophones0
copy hmms\hmm3\macros hmms\hmm4\macros
py scripts/sp_modeling.py
HHEd -A -D -T 1 -H hmms/hmm4/macros -H hmms/hmm4/hmmdefs -M hmms/hmm5 train/sil.hed generated/monophones1
HERest -A -D -T 1 -C configurations/config  -I generated/phones/phones1.mlf -t 250.0 150.0 3000.0 -S generated/train.scp -H hmms/hmm5/macros -H hmms/hmm5/hmmdefs -M hmms/hmm6 generated/monophones1
HERest -A -D -T 1 -C configurations/config  -I generated/phones/phones1.mlf -t 250.0 150.0 3000.0 -S generated/train.scp -H hmms/hmm6/macros -H hmms/hmm6/hmmdefs -M hmms/hmm7 generated/monophones1

rem align utterances and reestimate parameter
HVite -A -D -T 1 -l * -o SWT -b SENT-END -C configurations/config -H hmms/hmm7/macros -H hmms/hmm7/hmmdefs -i generated/aligned.mlf -m -t 250.0 150.0 1000.0 -y lab -a -I generated/words.mlf -S generated/train.scp generated/dict_used generated/monophones1> logs/HVite_log
HERest -A -D -T 1 -C configurations/config -I generated/aligned.mlf -t 250.0 150.0 3000.0 -S generated/train.scp -H hmms/hmm7/macros -H hmms/hmm7/hmmdefs -M hmms/hmm8 generated/monophones1
HERest -A -D -T 1 -C configurations/config -I generated/aligned.mlf -t 250.0 150.0 3000.0 -S generated/train.scp -H hmms/hmm8/macros -H hmms/hmm8/hmmdefs -M hmms/hmm9 generated/monophones1

rem create list of triphones with HLEd, clone HMM Models with HHEd (using mktri.hed as script), and reestimate parameter of HMM Models with HERest into hmm11
HLEd -A -D -T 1 -n generated/triphones1 -l * -i generated/wintri.mlf train/mktri.led generated/aligned.mlf
py scripts/mktri.py
mkdir hmms\hmm10
mkdir hmms\hmm11
mkdir hmms\hmm12
HHEd -A -D -T 1 -H hmms/hmm9/macros -H hmms/hmm9/hmmdefs -M hmms/hmm10 generated/mktri.hed generated/monophones1 
HERest  -A -D -T 1 -C configurations/config -I generated/wintri.mlf -t 250.0 150.0 3000.0 -S generated/train.scp -H hmms/hmm10/macros -H hmms/hmm10/hmmdefs -M hmms/hmm11 generated/triphones1
HERest  -A -D -T 1 -C configurations/config -I generated/wintri.mlf -t 250.0 150.0 3000.0 -s generated/hmm12stats -S generated/train.scp -H hmms/hmm11/macros -H hmms/hmm11/hmmdefs -M hmms/hmm12 generated/triphones1 

rem output triphones version of dictionary entry, remove duplicate triphones
HDMan -A -D -T 1 -b sp -n generated/fulllist0 -g train/maketriphones.ded -l generated/hdmanflog generated/dict-tri train/lexicon/dict
py scripts/fixfulllist.py

rem generate tree.hed using python, and retrain
py scripts/mkclscript.py
mkdir hmms\hmm13
mkdir hmms\hmm14
mkdir hmms\hmm15
HHEd -A -D -T 1 -H hmms/hmm12/macros -H hmms/hmm12/hmmdefs -M hmms/hmm13 generated/tree.hed generated/triphones1
HERest  -A -D -T 1 -C configurations/config -I generated/wintri.mlf -t 250.0 150.0 3000.0 -S generated/train.scp -H hmms/hmm13/macros -H hmms/hmm13/hmmdefs -M hmms/hmm14 generated/tiedlist
HERest  -A -D -T 1 -C configurations/config -I generated/wintri.mlf -t 250.0 150.0 3000.0 -S generated/train.scp -H hmms/hmm14/macros -H hmms/hmm14/hmmdefs -M hmms/hmm15 generated/tiedlist


rem testing
REM HSGen -l -n 200 generated/wdnet generated/dict_used > generated/testprompts
REM py scripts/testrefmlf.py
REM HVite -A -D -T 1 -H hmms/hmm15/macros -H hmms/hmm15/hmmdefs -S test.scp -l '*' -i generated/recout.mlf -w generated/wdnet -p 0.0 -s 5.0 generated/dict_used generated/tiedlist
REM HResults -I generated/testref.mlf generated/tiedlist generated/recout.mlf