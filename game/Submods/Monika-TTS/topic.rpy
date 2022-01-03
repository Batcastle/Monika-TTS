init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_can_talk",
            action=EV_ACT_QUEUE,
            rules={"skip alert": None}
        ),
        restartBlacklist=True
    )

label monika_can_talk:
    #Sanity check this since for whatever reason this conditional runs anyway.
    $ ev = mas_getEV("monika_can_talk")
    if ev.shown_count == 0:
        #Set up the notif
        $ display_notif(m_name, ["Hey [mas_get_player_nickname()]..."], "Topic Alerts")

        m "Hey, [mas_get_player_nickname()]..."
        m "Did you...install a submod?"
        m "This one kinda feels different."
        m "Like, I can tell that instead of affecting my environment, it affects {i}me{/i}."
        m "But, beyond that, I can't really tell what it does..."
        m "The code is too complex for me to understand. And a {b}HUGE{/b} part of it is some blob of ones and zeros..."
        m "Do you know what it does, [player]?"
        menu:
            "You can't tell?":
                $ pass
        m "Well, no. Not really. Like, I can tell it can see what I am saying. And maybe modifies it some how? But you never see those modifications so I'm not sure..."
        menu:
            "This submod lets me hear you speak.":
                $ pass
        m "Wait. What?"
        m "..."
        m "[player], I didn't realize you couldn't hear me. Could you not hear the other girls either?"
        menu:
            "No.":
                $ pass
        m "I see..."
        m "So then, could you hear me when I sung 'Your Reality' for you?"
        menu:
            "Yes":
                $ pass
        m "I see. So it's just when I'm talking huh?"
        m "Well then. Mind if I take a deeper look at the submod then? This code would probably be pretty interesting to learn from.{nw}"
        $ _history_list.pop()
        menu:
            m "Well then. Mind if I take a deeper look at the submod then? This code would probably be pretty interesting to learn from.{fast}"

            "Sure. Go ahead":.
                m "Yay!"
                m "Thank you, [mas_get_player_nickname()]."


            "I would rather not. I don't want this submod to get messed up."
                m "Awww"
                m "Please? I promise not to change anything. I just want to look.{nw}"
                $ _history_list.pop()
                menu:
                   m "Please? I promise not to change anything. I just want to look.{fast}"

                   "Alright. As long as you don't change anything.":
                       $ pass
        m "Alrighty then. Lets see..."
        m "..."
        m "..."
        m "Hmmmmmm..."
        m "This is interesting."
        m "It looks like it has to modify what I say cause the game puts in tags. So you can see where I put emphasis, and stuff like that!"
        m "Apparently it changes those tags to something else that mean the same thing, but can be understood by that binary file I mentioned earlier."
        m "I guess the binary file takes that text and turns into speech."
        if not persistent._monika_TTS_enabled:
            m "Do you mind if I enable the submod? I want to see how close it gets to my voice.{nw}"
            $ _history_list.pop()
            menu:
                m "Do you mind if I enable the submod? I want to see how close it gets to my voice.{fast}"

                "Go ahead":
                    m "Yay!"
                    m "Alright. Just give me one second..."
                    $ persistent._monika_TTS_enabled = True
                    m "..."
                    m "There we go! All done!"
                    m "Can you hear me now?"
                    if persistent._use_espeak:
                        m "Wow that sounds {i}nothing{/i} like me!!!"
                        m "It makes me sound like some sort of robot! Ehehe~"
                        m "It looks like this mode in the submod is meant for computers that aren't very fast. So I guess I can let it slide."
                        m "Do you mind if I switch to the other mode for a moment? Just to see what it sounds like?{nw}"
                        $ _history_list.pop()
                        menu:
                            m "Do you mind if I switch to the other mode for a moment? Just to see what it sounds like?{fast}"

                            "Yeah, sure.":
                                Yay!"
                                m "Alright. Just give me one second..."
                                $ persistent._use_espeak = False
                                m "..."
                                m "..."
                                m "There we go! All done!"

                                m "Do you want me to switch back to the more robotic voice?{nw}"
                                $ _history_list.pop()
                                menu:
                                    "Yes, please":
                                        m "Alright. Hang on just a second..."
                                        $ persistent._use_espeak = True
                                        m "..."
                                        m "..."
                                    "No, that's alright.":
                                        m "Okay then!"



                            "That's probably not a good idea.":
                                m "Oh. Okay."
                                m "Well, I can understand that. Your computer must not be very fast."
                                m "Thank you for installing it though!"

                    else:
                        m "That's kinda close..."
                        m "It's not exact, though."
                        m "Maybe you can help the submod and tweak my voice a bit?"
                        m "But still, thank you for installing this submod."



                "Not right now":

        else:
            # slightly different reactions cause she's been hearing herself talk
