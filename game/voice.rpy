#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  voice.py
#
#  Copyright 2021 Thomas Castleman <contact@draugeros.org>
#
#  Heavily Based upon Simple Text-To-Speech by @zombiepigdragon on GitHub: https://gist.github.com/zombiepigdragon/c68f556a5ccc2f99b32a9e8b87913997
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

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
            bypass = True
            if store.persistent._monika_TTS_enabled:
                speaktext = renpy.substitute(what)
                #Remove any tags that would sound bad but aren't important
                #Regex causes an instant crash for some reason
                if (("{fast}" not in speaktext) or ("chu" not in speaktext.lower())):
                    # Implement emphasis
                    speaktext = speaktext.replace("{i}", "<emphasis>").replace("{b}", "<emphasis>")
                    speaktext = speaktext.replace("{/i}", "</emphasis>").replace("{/b}", "</emphasis>")
                    speaktext = speaktext.replace("~", "").replace("<3", "")
                    speaktext = speaktext.replace("{/cps}", "")
                    # we want to get the text speed for a future feature. So,
                    # we need to parse it out, while preserving the NUMBER in
                    # another var
                    speaktext = speaktext.split("{cps")
                    # doing the above will leave an equals sign at the beginging
                    # of a string that was preceded by {cps=<number}
                    default_speed = store.preferences.text_cps
                    for each in enumerate(speaktext):
                        if len(speaktext[each[0]]) < 1:
                            continue
                        if speaktext[each[0]][0] == "=":
                            speaktext[each[0]] = list(speaktext[each[0]])
                            for each1 in enumerate(speaktext[each[0]]):
                                if speaktext[each[0]][each1[0]] == "}":
                                    bracket = each1[0]
                                    break
                            speed = float("".join(speaktext[each[0]][1:bracket]))
                            speaktext[each[0]] = speaktext[each[0]][bracket + 1:]
                            speaktext[each[0]] = "".join(speaktext[each[0]])
                    speaktext = "".join(speaktext)
                    # old CPS speed is in default_speed
                    # new CPS speed is in speed
                    # We need to figure out a relationship between speech speed and CPS speed that can be used to scale speech speed
                    speaktext = re.split("{|}", speaktext) # we need to parse out wait calls
                    # Implement pauses
                    for each in enumerate(speaktext):
                        if speaktext[each[0]][:2] == "w=":
                            wait = float(speaktext[each[0]][2:]) * 1.1
                            speaktext[each[0]] = "<break time=%s/>" % (wait)
                    if "fast" not in speaktext:
                        speaktext = "".join([each for each in speaktext if not each.startswith("nw")])
                        if ((isinstance(speaktext, (str, unicode))) and ("chu" not in speaktext.lower())):
                            q.put((speaktext, interact))
                    else:
                        bypass = True
            func(who, what, interact=interact, *args, **kwargs)
            if store.persistent._monika_TTS_enabled:
                if not bypass:
                    try:
                        if ((isinstance(speaktext, (str, unicode))) and ("chu" not in speaktext.lower())):
                            q.join()
                    except AttributeError:
                        pass
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
