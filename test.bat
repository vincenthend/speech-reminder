echo ========================================================
echo "                   Closed Testing                     "
echo ========================================================
HVite -A -D -T 1 -C configurations/config -H hmms/hmm15/macros -H hmms/hmm15/hmmdefs -S generated/train.scp -l '*' -i generated/closed_test_result.mlf -w generated/wdnet -p 0.0 -s 5.0 generated/dict_used generated/tiedlist
HResults -I generated/words.mlf generated/tiedlist generated/closed_test_result.mlf

echo ========================================================
echo "                    Open Testing                      "
echo ========================================================

rem testing, generate words, create transcript, create list of codefiles, mfcc, viterby, cek result
REM HSGen -l -n 200 generated/wdnet generated/dict_used > generated/testprompts
py scripts/testing_transcript.py
mkdir test\mfcc
py scripts/testing_scp.py
HCopy -A -D -T 1 -C configurations/wav_config -S generated/open_test_codetrain.scp
HVite -A -D -T 1 -C configurations/config -H hmms/hmm15/macros -H hmms/hmm15/hmmdefs -S generated/open_test_train.scp -l '*' -i generated/open_test_result.mlf -w generated/wdnet -p 0.0 -s 5.0 generated/dict_used generated/tiedlist
HResults -I generated/open_test_transcript.mlf generated/tiedlist generated/open_test_result.mlf
