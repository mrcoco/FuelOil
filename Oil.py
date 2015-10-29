import os
import subprocess
import sublime
import sublime_plugin

class OilCommand(sublime_plugin.TextCommand):

    def get_oil_path(self):
        return os.path.join(self.view.window().folders()[0], "oil")

    def run(self, edit):
        oil_path = self.get_oil_path()
        if os.path.isfile("%s" % oil_path):
            self.cmd = "php " + oil_path
            self.view.window().show_input_panel('oil command: ', '', self.on_done, None, None)
        else:
            sublime.message_dialog("Not found oil")

    def on_done(self, input_cmd):
        res = subprocess.check_output(self.cmd + " " + input_cmd, shell=True, universal_newlines=True)
        sublime.message_dialog(str(res))
