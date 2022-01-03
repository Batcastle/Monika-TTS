#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  header.rpy
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
init -990 python in mas_submod_utils:
    h_submod = Submod(
        author="Batcastle",
        name="Monika Text To Speech",
        description="Give Monika a voice!",
        version="0.3.6",
        settings_pane="monika_tts_settings"
    )

init -989 python in mtts_utils:
    import store
    import os
    import stat
    import sys

    base_dir = os.getcwd()

    #Register the updater if needed
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Monika Text To Speech",
            user_name="Batcastle",
            repository_name="Monika-TTS",
            tag_formatter=lambda x: x[x.index('v') + 1:],
            update_dir=base_dir + "/game",
            attachment_id=0,
            redirected_files="game"
        )

    # some other work that needs to be done.
    # make sure Mimic is set as executable
    base_path = "/game/Submods/Monika-TTS/Utilities/mimic"
    if "win" in sys.platform:
        base_path.replace("/", "\\")
    path = base_dir + base_path
    if "win" in sys.platform:
        path = path + ".exe"
    elif sys.platform.startswith("linux"):
        path = path + ".bin"
    # if not Linux or Windows, we're on MacOS
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)
