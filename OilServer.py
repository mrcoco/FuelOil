import sublime
import sublime_plugin

class OilServerCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        project_data = self.view.window().project_data()
        if project_data:
            project_root = project_data["folders"][0]["path"]
            oil_cmd = "php " + project_root + "/oil server"
            sublime.message_dialog(oil_cmd)
        else:
            sublime.message_dialog("Not set project")
