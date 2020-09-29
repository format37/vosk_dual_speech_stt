### Dual speakers, captured from different audio channels, VOSK speech to text
Kaldi, vosk. Russian voice example   
#### Installation
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

#### Running the example code with python
1. Prepare wav autio file, where speaker A and B stored on different channels.   
2. Separate one stereo file to two mono files:   
```
ffmpeg -i call.wav -ar 16000 -af "pan=mono|c0=FL" call_l.wav   
ffmpeg -i call.wav -ar 16000 -af "pan=mono|c0=FR" call_r.wav
```
3. Run example:
```
python3 my_test.py
```

#### More info on:   
https://alphacephei.com/vosk/install   
#### Models:   
https://alphacephei.com/vosk/models
