# INSTALLATION:
# Installing this submod is fairly straightforward, but also highly involved.
# Essentially, it goes as follows:
# 1) Download this file (voice.rpy) into the game directory.
# 2) Save https://raw.githubusercontent.com/python/cpython/2.7/Lib/Queue.py to the game/python-packages/ directory.
# 3) Download the wheel (whl) file for pyttsx3 2.7 (Newer versions don't seem to work) from [https://pypi.org/project/pyttsx3/2.7/#files] and save it somewhere accessible.
# 4) Open this file in an archive editor (whl files are .zips internally, so chainging the file extention to .zip is a
# way to do it without addidional software on Windows).
# 5) Within this archive, there should be a directory called pyttsx3. Extract this directory to game/python-packages/pyttsx3.
# 6) This is the fun part: you have to find the valid voices for your system. If you find valid options for Windows or Mac,
# please let me know so I can add them here (you can find me via the MASC Discord on the GitHub page of the mod, mention said
# solution in the #submod-discussion channel and ping me there. At the moment, I use Linux which means I use espeak for
# the actual voice, however this would represent a minority of users.
# 6a) Windows: N/A, see above
# 6b) Mac: N/A, see above
# 6c) Linux: Install espeak via your package manager, then set the voice down below to "en-us+f2". (Note: you
# can run `espeak -ven-us+f2 "Can you hear me?"` for a preview, and if you find a better voice it should work just as well.)
# 7) Try it out! Open MAS, and see what happens. If everything went well, you should hear the voice of Monika greeting you.
# If this doesn't happen, reach out to me as previously noted so I can fix the issue.
# Enjoy Monika's newfound voice!

init python in mas_tts:
    import subprocess
    from Queue import Queue
    from threading import Thread
    import store
    import os
    import sys
    import re
    import time
    q = Queue()
    
    base_dir = os.getcwd() # this script runs too early for the built in basedir var to work. We need our own.
    
    
    def get_wrapped_say(func):
        def new_say(who, what, interact=True, *args, **kwargs):
            if store.persistent._monika_TTS_enabled:
                speaktext = renpy.substitute(what)
                #Remove any tags that would sound bad but aren't important
                #Regex causes an instant crash for some reason
                if (("{fast}" not in speaktext) or ("chu" not in speaktext.lower())):
                    # Implement emphasis
                    speaktext = speaktext.replace("{i}", "<emphasis>").replace("{b}", "<emphasis>")
                    speaktext = speaktext.replace("{/i}", "</emphasis>").replace("{/b}", "</emphasis>")
                    speaktext = speaktext.replace("~", "").replace("<3", "")
                    speaktext = re.split("{|}", speaktext) # we need to parse out wait calls
                    # Implement pauses
                    for each in enumerate(speaktext):
                        if speaktext[each[0]][:2] == "w=":
                            wait = float(speaktext[each[0]][2:]) * 1.1
                            speaktext[each[0]] = "<break time=%s/>" % (wait) 
                    speaktext = "".join([each for each in speaktext if not each.startswith("nw")])
                    q.put((speaktext, interact))
            func(who, what, interact=interact, *args, **kwargs)
            if store.persistent._monika_TTS_enabled:
                if ((not speaktext.endswith("{fast}")) or ("chu" in speaktext.lower())):
                    q.join()
        return new_say
        
    
    def say_loop():
        while True:
            if ((store.persistent._use_espeak) and (store.persistent._espeak_support)):
                voice = "en-us+f4"
            else:
                voice = base_dir + "/game/Submods/Monika-TTS/Utilities/voices/cmu_us_ljm.flitevox" # SET THE VOICE HERE
            if not store.persistent._monika_TTS_enabled:
                # if not enabled, use as little CPU time as possible
                time.sleep(3)
                continue
            say(q.get(), voice)
            q.task_done()
            time.sleep(0.01)
    
    def say(text, voice):
        mimic_command = base_dir + "/game/Submods/Monika-TTS/Utilities/mimic"
        
        if "win" in sys.platform:
            mimic_command = mimic_command + ".exe" # redirect to Windows executable on Windows
            
        # use espeak when instructed
        if ((store.persistent._use_espeak) and (store.persistent._espeak_support)):
            command = ["espeak", "-v" + voice, "-m", text[0]]
        else:
            command = [mimic_command, "-voice", voice, "-t", text[0], "-ssml"]
        # put the speech in the background so menus don't lag, but in the foreground for normal conversations
        try:
            if text[1]:
                subprocess.check_call(command)
            else:
                subprocess.Popen(command)
        except (subprocess.CalledProcessError, OSError):
            print("WARNING: espeak or mimic threw error or is not installed.")
            print("WARNING: please install espeak or mimic in order to get Text-To-Speech functionality")
        del voice, command
        
    
    t = Thread(target=say_loop)
    t.daemon = True
    t.start()
    renpy.say = get_wrapped_say(renpy.say)
