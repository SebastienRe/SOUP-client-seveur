import time
import vlc
from vlc import MediaPlayer

# Créer une instance VLC
instance = vlc.Instance()

# Créer un nouveau lecteur média
player = instance.media_player_new()

output = 'sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100}:http{mux=raw,dst=:12345/}'

# Créer un nouveau média
media = instance.media_new('musiques/2-Murder at Midnight-Powerwolf.mp3', output)

# Définir le média pour le lecteur
player.set_media(media)

# Jouer le média
player.play()

time.sleep(100)



