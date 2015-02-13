from __future__ import absolute_import

import logging
import os
import subprocess
import sys

import sublime
import sublime_plugin

VERSION = "0.1.0"

SETTINGS_KEY = "ransack_finder"
RANSACK_PATH_KEY = "agent_ransack_path"

# Logging (send to the sublime console)
stderr_hdlr = logging.StreamHandler(sys.stderr)
stderr_hdlr.setFormatter(logging.Formatter("%(name)s: %(levelname)s: %(message)s"))
log = logging.getLogger(SETTINGS_KEY)
log.handlers = [stderr_hdlr]
log.setLevel(logging.ERROR)


def get_settings(key, view):
    settings = None

    if view:
        settings = view.settings()

    if settings and settings.has(SETTINGS_KEY) and key in settings.get(SETTINGS_KEY):
        # Get project-specific setting
        results = settings.get(SETTINGS_KEY)[key]
    else:
        # Get user-specific or default setting
        settings = sublime.load_settings('%s.sublime-settings' % SETTINGS_KEY)
        results = settings.get(key)
    return results


def get_selected_text(view):
    for region in view.sel():
        if not region.empty():
            return view.substr(region)
    else:
        return ''


class RsFindInCurrentFolderCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        file_name = view.file_name()

        ransack_path = get_settings(RANSACK_PATH_KEY, view)
        if not os.path.exists(ransack_path):
            log.error('"%s" does not exist. Please check "%s" in the settings.',
                      ransack_path,
                      RANSACK_PATH_KEY)
            return

        args = [ransack_path,
                '-f', '',
                '-c', get_selected_text(view),
                '-d', os.path.dirname(file_name)]

        subprocess.Popen(args)
