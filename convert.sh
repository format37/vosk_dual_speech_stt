ffmpeg -i call.wav -ar 16000 -af "pan=mono|c0=FL" call_l.wav
ffmpeg -i call.wav -ar 16000 -af "pan=mono|c0=FR" call_r.wav
