import sublime, sublime_plugin

class CompleteTaskCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		sel = self.view.sel()

		revert_all = True

		for selection in sel:
			line_offset = 0
			lines = view.lines(selection)
			for line in lines:
				adjusted_line = sublime.Region(line.a + line_offset, line.b + line_offset)
				if view.substr(adjusted_line)[:2] != "x ":
					revert_all = False
					line_offset += view.insert(edit, adjusted_line.a, "x ")

		if revert_all:

			for selection in sel:
				line_offset = 0
				lines = view.lines(selection)
				for line in lines:
					adjusted_line = sublime.Region(line.a + line_offset, line.b + line_offset)
					erase_region = sublime.Region(adjusted_line.a, adjusted_line.a + 2)
					view.erase(edit, erase_region)
					line_offset -= 2