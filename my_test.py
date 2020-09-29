#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json
import pandas as pd
import time

def get_stt_df(filename,side):
	
	# prepare dataframe
	index = ['','','','']
	columns = ['start','end','text','side']
	df = pd.DataFrame(index=index, columns=columns)
	df = df.dropna()
	
	# read file
	wf = wave.open(filename, "rb")
	if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
		print ("Audio file must be WAV format mono PCM.")
		exit (1)
		
	# read model
	model = Model("model")
	rec = KaldiRecognizer(model, wf.getframerate())

	# recognizing
	current_frame = 0

	while True:	
		data = wf.readframes(4000)	
		if len(data) == 0:
			break
		if rec.AcceptWaveform(data):
			accept = json.loads(rec.Result())
			if accept['text'] !='':
				accept_start = accept['result'][0]['start']
				accept_text = accept['text']
				df.loc[current_frame] = [accept_start,'end',accept_text,side]
				print(current_frame)
				current_frame+=1	
				#if current_frame>3: # debug
				#	break
	
	return df

start_time = time.time()

# recognize
df_a = get_stt_df('call_l.wav','>>')
df_b = get_stt_df('call_r.wav','<<')

# merge and sort
df_c = pd.concat([df_a, df_b]).sort_values('start')
result = ''
for i in range (0,len(df_c)):
    row = df_c.iloc()[i]
    result += row.side+' '+row.text+'\n'

# save to file
with open('result.txt','w') as file:
	file.write(result)

file.close()

end_time = time.time()

print(end_time - start_time)
