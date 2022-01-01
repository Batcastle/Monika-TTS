# Contributing to Monika Text-To-Speech

## Engines
Developers are welcome to implement support for other Text-To-Speech Engines, such as Google Text-To-Speech, 15.ai, or others. However, a new engine must follow the following guidelines:
1. The engine **must** be either:

   a) open-source

     or

   b) proprietary, used with permission from the original developer, at no cost to the end-user or the developers of this submod

2. The engine **must** work offline.
3. The engine needs to support some form of text formatting to indicate pauses, emphasis, etc. [SSML](https://en.wikipedia.org/wiki/Speech_Synthesis_Markup_Language) is the formatting used internally in Monika Text-To-Speech, so please stick to that.
4. The engine should support using different voices. This is especially important for engines that have voices that, by default, are reminiscent of popular voice assistants such as [Google Assistant](https://www.youtube.com/watch?v=5WEt-j7N7N8), [Alexa](https://www.youtube.com/watch?v=7ya8ahjnfnE), [Siri](https://youtu.be/zOJBGZmCZYU?t=7), [Mycroft](https://www.youtube.com/watch?v=71RwUTnGJbI), or [Cortanta](https://www.youtube.com/watch?v=YFweSyEQiv0)

## Voices
If you wish to add a voice to Monika Text-To-Speech, the best way to do so would be to either create a voice for eSpeak, or contact [VocalID](https://vocalid.ai/) about making a new voice for Mimic. Please note that making a voice for Mimic is a large undertaking and requires recording a large amount of audio data.


## Platforms

### Operating Systems
#### Linux
Monika Text-To-Speech is a Linux-first Submod. If a new feature doesn't work on Linux, it won't be added until it does. The exception to this is different Text-To-Speech Engines.

Monika Text-To-Speech primarily supports and is tested against Debian-based distros. But Arch-based, Red Hat-based, and independent distros will also be supported to the best of our ability.

#### Windows
As the majority of the Monika After Story community is on Windows, we are required to support this OS. Unfortunately Windows has some unique quirks, being one of the few remaining DOS-based operating systems left.

#### Mac OS
Mac OS is difficult to support without a Mac of some sort. Developers on Mac are strongly encouraged to contribute!


#### BSD
BSD-based operating systems may be hit-and-miss with DDLC and Ren'Py. As such, we have no intentions of supporting BSD-based operating systems.


#### Other
Other operating systems, including but not limited to: Haiku OS, Temple OS, React OS, and FreeDOS; are not supported.

### CPU Architectures
Monika Text-To-Speech only supports 64-bit x86 CPU architectures. Future support for ARM64 is open for discussion, but requires re-compiling of Mimic binaries.

## Planned Features
There are 2 planned features so far:
 * Add a slider in submod settings to set the default speed of Monika's speech
 * Add a drop down menu to change between different voices on a single engine.

## Coding Style
Please adhere to [PEP8](https://www.python.org/dev/peps/pep-0008/) as closely as possible. This is especially important in Python code blocks. 
