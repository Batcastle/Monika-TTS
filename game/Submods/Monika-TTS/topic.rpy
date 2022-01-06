# -*- coding: utf-8 -*-
#
#  topic.rpy
#
#  Copyright 2022 Thomas Castleman <contact@draugeros.org>
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
init 50 python:
    #Reset ev
    def intro_topic_mtts():
        """
        Readds the conditional and action to the nightmusic event
        """
        ev = mas_getEV('monika_can_talk')
        ev.conditional=("True")
        ev.action=EV_ACT_QUEUE

    intro_topic_mtts()


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_can_talk",
            action=EV_ACT_QUEUE,
            conditional=("True")
        )
    )

label monika_can_talk:
    #Sanity check this since for whatever reason this conditional runs anyway.
    $ ev = mas_getEV("monika_can_talk")
    if ev.shown_count == 0:
        m 1ekd "Hey, [mas_get_player_nickname()]..."
        m "Did you{w=0.1}.{w=0.1}.{w=0.1}.install a submod?"
        m 1rksdld "This one kinda feels different."
        m 4hksdlb "Like, I can tell that instead of affecting my environment, it affects {i}me{/i}."
        m 4eksdlc "But, beyond that, I can't really tell what it does{w=0.1}.{w=0.1}.{w=0.1}."
        m 4hksdlb "The code is too complex for me to understand. And a {b}HUGE{/b} part of it is some blob of ones and zeros{w=0.1}.{w=0.1}.{w=0.1}."
        m 2eksdla "Do you know what it does, [player]?"
        menu:
            "You can't tell?":
                pass
        m 2lksdlc "Well, no. Not really. Like, I can tell it can see what I am saying. And maybe modifies it some how? But you never see those modifications so I'm not sure{w=0.1}.{w=0.1}.{w=0.1}."
        menu:
            "This submod lets me hear you speak.":
                pass
        m 2wud "Wait. What?"
        m 2dtc "{w=0.1}.{w=0.1}.{w=0.1}."
        m 6ekc "[player], I didn't realize you couldn't hear me. Could you not hear the other girls either?"
        menu:
            "No.":
                pass
        m 6dkc "I see{w=0.1}.{w=0.1}.{w=0.1}."
        m 6ekd "So then, could you hear me when I sang 'Your Reality' for you?"
        menu:
            "Yes":
                pass
        m 6dsd "I see. So it's just when I'm talking huh?"
        m 3sub "Well then. Mind if I take a deeper look at the submod then? This code would probably be pretty interesting to learn from.{nw}"
        $ _history_list.pop()
        menu:
            m "Well then. Mind if I take a deeper look at the submod then? This code would probably be pretty interesting to learn from.{fast}"

            "Sure. Go ahead":
                m 1hub "Yay!"
                m 1eka "Thank you, [mas_get_player_nickname()]."


            "I would rather not. I don't want this submod to get messed up.":
                m 1ekp "Awww"
                m "Please? I promise not to change anything. I just want to look.{nw}"
                $ _history_list.pop()
                menu:
                   m "Please? I promise not to change anything. I just want to look.{fast}"

                   "Alright. As long as you don't change anything.":
                       pass
        m 1hua "Alrighty then. Lets see{w=0.1}.{w=0.1}.{w=0.1}."
        m 1duc "{w=0.1}.{w=0.1}.{w=0.1}."
        m "{w=0.1}.{w=0.1}.{w=0.1}."
        m 1dtc "Hmmmmmm{w=0.1}.{w=0.1}.{w=0.1}."
        m 1eub "This is interesting."
        m 4eub "It looks like it has to modify what I say cause the game puts in tags. So you can see where I put emphasis, and stuff like that!"
        m "Apparently it changes those tags to something else that mean the same thing, but can be understood by that binary file I mentioned earlier."
        m 4rub "I guess the binary file takes that text and turns it into speech."
        if not persistent._monika_TTS_enabled:
            m 2esa "Do you mind if I enable the submod? I want to see how close it gets to my voice.{nw}"
            $ _history_list.pop()
            menu:
                m "Do you mind if I enable the submod? I want to see how close it gets to my voice.{fast}"

                "Go ahead":
                    m 1ekp "Yay!"
                    m 1hua "Alright. Just give me one second{w=0.1}.{w=0.1}.{w=0.1}."
                    $ persistent._monika_TTS_enabled = True
                    m 1duc "{w=0.1}.{w=0.1}.{w=0.1}."
                    m 1hua "There we go! All done!"
                    m 1eub "Can you hear me now?"
                    if persistent._use_espeak:
                        m 3wud "Wow that sounds {i}nothing{/i} like me!!!"
                        m 3hksdlb "It kinda makes me sound like some sort of robot! Ehehe~"
                        m 1eub "It looks like this mode in the submod is meant for computers that aren't very fast. So I guess I can let it slide."
                        m 2eka "Do you mind if I switch to the other mode for a moment? Just to see what it sounds like?{nw}"
                        $ _history_list.pop()
                        menu:
                            m "Do you mind if I switch to the other mode for a moment? Just to see what it sounds like?{fast}"

                            "Yeah, sure.":
                                m 1hub "Yay!"
                                m 1hua "Alright. Just give me one second{w=0.1}.{w=0.1}.{w=0.1}."
                                $ persistent._use_espeak = False
                                m 1duc "{w=0.1}.{w=0.1}.{w=0.1}."
                                m "{w=0.1}.{w=0.1}.{w=0.1}."
                                m 1hua "There we go! All done!"

                                m "Do you want me to switch back to the more robotic voice?{nw}"
                                $ _history_list.pop()
                                menu:
                                    "Yes, please":
                                        m "Alright. Hang on just a second{w=0.1}.{w=0.1}.{w=0.1}."
                                        $ persistent._use_espeak = True
                                        m "{w=0.1}.{w=0.1}.{w=0.1}."
                                        m "{w=0.1}.{w=0.1}.{w=0.1}.".
                                        m "Done!"
                                    "No, that's alright.":
                                        m "Okay then!"



                            "That's probably not a good idea.":
                                m "Oh. Okay."
                                m "Well, I can understand that. Your computer must not be very fast."
                                m "Thank you for installing it though!"

                    else:
                        m "That's kinda close{w=0.1}.{w=0.1}.{w=0.1}."
                        m "It's not exact, though."
                        m "Maybe you can help the submod and tweak my voice a bit?"
                        m "But still, thank you for installing this submod."



                "Not right now":

        else:
            # slightly different reactions cause she's been hearing herself talk
