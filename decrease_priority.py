import sublime, sublime_plugin

priorities = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class DecreasePriorityCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		view = self.view
		sel = self.view.sel()

		for selection in sel:
			line_offset = 0
			lines = view.lines(selection)
			for line in lines:
				adjusted_line = sublime.Region(line.a + line_offset, line.b + line_offset)
				if view.substr(adjusted_line)[:2] != "x ":
					if view.substr(adjusted_line)[0:1] + view.substr(adjusted_line)[2:3] == "()":
						prio = int(priorities.find(view.substr(adjusted_line)[1:2]))
						prio += 1
						if prio > len(priorities) - 1:
							prio = 0
						view.replace(edit, sublime.Region(adjusted_line.a + 1, adjusted_line.a + 2), priorities[prio:prio + 1])