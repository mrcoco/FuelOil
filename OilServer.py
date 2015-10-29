import os
import sublime
import sublime_plugin

class OilServerCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        oil_path = self.view.window().folders()[0] + "/oil"
        if os.path.isfile("%s" % oil_path):
            sublime.message_dialog(oil_path)
        else:
            sublime.message_dialog("Not found oil")
