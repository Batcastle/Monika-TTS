#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  mtts_utils.rpy
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
init -1 python:
    tt_mtts_desc = (
        "Enable this to allow Monika to speak."
    )
    tt_mtts_espeak = (
        "Provides lower-latency Text-To-Speech, at the cost of sounding more robotic"
    )
    tt_mtts_mimic = (
        "Provides more realistc Text-To-Speech, at the cost of higher latency."
    )


#Our settings + Status pane
screen monika_tts_settings():
    $ submods_screen_tt = store.renpy.get_screen("submods", "screens").scope["tooltip"]
    vbox:
        box_wrap False
        xfill True
        xmaximum 1000

        hbox:
            style_prefix "check"
            box_wrap False
            textbutton _("Enabled"):
                action ToggleField(persistent, "_monika_TTS_enabled")
                selected persistent._monika_TTS_enabled
                hovered SetField(submods_screen_tt, "value", tt_mtts_desc)
                unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)

            python:
                persistent._espeak_support = False
                if sys.platform.startswith('linux'):
                    # Enable support for espeak on Linux, if it's in the $PATH
                    try:
                        # check for command, send output to /dev/null
                        # also a return code of 0 is success in Linux, but it's boolean subclass is False, so use a not statment
                        if not subprocess.check_call(["which", "espeak"], stdout=open("/dev/null", "w")):
                            persistent._espeak_support = True
                    except subprocess.CalledProcessError:
                        print("It looks like you are using Linux, but don't have espeak installed.")
                        print("You might want to install espeak to get better performance on lower-end systems.")
                        persistent._espeak_support = False
                else:
                    # not on Linux, no espeak
                    persistent._espeak_support = False


            if bool(persistent._espeak_support):
                style_prefix "check"
                box_wrap False
                if bool(persistent._use_espeak):
                    textbutton _("espeak"):
                        action ToggleField(persistent, "_use_espeak")
                        selected persistent._use_espeak
                        hovered SetField(submods_screen_tt, "value", tt_mtts_espeak)
                        unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)
                else:
                    textbutton _("Mimic"):
                        action ToggleField(persistent, "_use_espeak")
                        selected persistent._use_espeak
                        hovered SetField(submods_screen_tt, "value", tt_mtts_mimic)
                        unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)



default persistent._monika_TTS_enabled = True
default persistent._use_espeak = False
