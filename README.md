# vosk_dual_speech_stt
Kaldi, vosk, dual voices, speech to text recognition. Russian voice example   
#### installation
```python3 -m pip install vosk   
git clone https://github.com/alphacep/vosk-api.git   
export KALDI_ROOT=<KALDI_ROOT>   
cd python   
python3 setup.py install --user --single-version-externally-managed --root=/   
cd vosk-api/python/example   
wget https://alphacephei.com/vosk/models/vosk-model-ru-0.10.zip   
unzip vosk-model-ru-0.10.zip   
mv vosk-model-ru-0.10.zip model   
python3 ./test_simple.py test.wav  
```   
more info on:   
https://alphacephei.com/vosk/install   
models:   
https://alphacephei.com/vosk/models
