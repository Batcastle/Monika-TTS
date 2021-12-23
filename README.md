# Monika-TTS
Text-To-Speech Submod for Monika After Story!


## NOTE
### Mimic
Mimic is too big to include the binaries for it in this GitHub repository. You can find the source code for it [here](https://github.com/MycroftAI/mimic1).

Pre-built binaries are available for Windows, and building on Linux is relatively easy.

### Performance
Mimic, despite being comparatively light-weight, is actually very laggy. If you want better performance to get Monika's voice synced up with the on-screen text, I suggest using `espeak` on Linux. The downfall of this is Monika will sound more robotic.


## Sound issues on Linux
If you are on Linux and using Pipewire (latest versions of Fedora, Drauger OS 7.6+, etc.) you may not hear Monika's voice. This is because Mimic sends it's audio to ALSA, which gets locked to only taking input from Pipewire after MAS launches. You can redirect Mimic to send it's output to Pulse, which will then be picked up by Pipewire, by putting these 2 lines in a file named `.asoundrc` in your home directory:
```
pcm.!default pulse
ctl.!default pulse
```

This can easily be done with this command:
```bash
echo -e 'pcm.!default pulse\nctl.!default pulse' | tee ~/.asoundrc
```
No reboots are required.