import sublime, sublime_plugin, re

class ComplineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view

        targetLine = view.line(view.sel()[0].begin())
        targetContent = view.substr(targetLine).lstrip()
        count = {targetContent: 0}
        for line in view.lines(sublime.Region(0, view.size())):
            lineContent = view.substr(line).lstrip()
            if lineContent.startswith(targetContent):
                key = lineContent.strip()
                count[key] = count.get(key, 0) + 1
        candidates = [x for x, y in sorted(count.items(), key=lambda (x, y): -y)]

        def on_done(index):
            view.replace(edit, targetLine, candidates[index])
        sublime.active_window().show_quick_panel(candidates, on_done)
