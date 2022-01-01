# Monika-TTS
Text-To-Speech Submod for Monika After Story!

This submod is based off of @zombiepigdragon's [Simple Text-To-Speech](https://gist.github.com/zombiepigdragon/c68f556a5ccc2f99b32a9e8b87913997). But, expands on it by switching to use the [Mimic Text-To-Speech Engine](https://github.com/MycroftAI/mimic1) by default (it does keep eSpeak support on Linux though). It also has the ability to be disabled or enabled at will in the submod settings menu, supports the Submod Updater Plugin, and more.

## Support
### Linux
Monika Text-To-Speech is primarily developed and tested on and for Linux. When it comes to support, Linux is a first class citizen with regards to Monika Text-To-Speech.

### MacOS
Monika Text-To-Speech SHOULD work just fine on MacOS, thanks to it's similarities to Linux. It does require it's own Text-To-Speech engine binary file though, so that increases the size of the submod.

Early testing on MacOS in a virtual machine indicates some clipping may be present near the beginning of audio. This may or may not have been a result of the virtual machine environment.

Feedback is greatly appreciated on MacOS.

### Windows
Windows is a weird beast. With using back slashes instead of forward slashes in file paths, to having it's own audio-backend, to the lack of built-in Python support, Windows has it out for this submod.

That being said, Monika Text-To-Speech has been tested on Windows and is known working. However, please know that:
 * It sometimes takes a while for speech to be played on Windows.
 * a command prompt will temporarily pop up when speech is being played.

Both these bugs are being investigated.

### Other operating systems
Other operating systems have not been tested or developed for. While we are open to supporting BSD distros in the future, that would require contributors who are familiar with BSD to contribute. Mimic may not even run on BSD distros. As such, at current time, Monika Text-To-Speech does not support BSD distros.

There are no plans to support any other OSs in the future, this includes but is not limited to Haiku OS, React OS, and Temple OS.

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
