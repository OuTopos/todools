import sublime, sublime_plugin

priorities = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class ReducePriorityCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		view = self.view
		sel = self.view.sel()
		print("NOOO!??!?!")

		revert_all = True
		for selection in sel:
			line_offset = 0
			lines = view.lines(selection)
			for line in lines:
				adjusted_line = sublime.Region(line.a + line_offset, line.b + line_offset)
				if view.substr(adjusted_line)[:2] != "x ":
					print("not x")
					print(view.substr(adjusted_line)[0:1] + view.substr(adjusted_line)[2:3])
					if view.substr(adjusted_line)[0:1] + view.substr(adjusted_line)[2:3] == "()":
						print("HAS PRIO" + view.substr(adjusted_line)[1:2])
						prio = int(priorities.find(view.substr(adjusted_line)[1:2]))
						prio += 1
						view.replace(edit, sublime.Region(adjusted_line.a + 1, adjusted_line.a + 2), priorities[prio:prio + 1])