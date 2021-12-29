# Monika-TTS
Text-To-Speech Submod for Monika After Story!

This submod is based off of @zombiepigdragon's [Simple Text-To-Speech](https://gist.github.com/zombiepigdragon/c68f556a5ccc2f99b32a9e8b87913997). But, expands on it by switching to use the [Mimic Text-To-Speech Engine](https://github.com/MycroftAI/mimic1) by default (it does keep eSpeak support on Linux though). It also has the ability to be disabled or enabled at will in the submod settings menu, supports the Submod Updater Plugin, and more.

## Support
This submod is designed to be capabale of supporting Windows, Mac OS, and Linux. Unfortunetly, I do not have a Mac in order to compile the Text-To-Speech engine on. Because of that, this submod **will not work on Mac OS**. It WILL work on Windows and Linux. 

Windows users, please know that every time Monika speaks a command prompt will temporarily pop up. We are investigating WHY this happens still and are trying to find a fix.

## Installation
1. Navigate to the releases page
2. Download the Monika-TTS.zip file for the latest release
3. Extract the Monika-TTS.zip file you just downloaded
4. **Merge** the game folder you extracted with the game folder in your Monika After Story installation
5. Restart Monika After Story (Talk > Goodbye > "I'm going to restart")
6. Profit $$$


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
