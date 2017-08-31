import sublime, sublime_plugin
from .helper import Task

class DecreasePriorityCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		view = self.view
		sel = self.view.sel()

		for selection in sel:
			line_offset = 0
			lines = view.lines(selection)
			for line in lines:
				adjusted_line = sublime.Region(line.a + line_offset, line.b + line_offset)
				task = Task(view.substr(adjusted_line))
				if not task.completed:
					if task.priority:
						task.priority -= 1
					else:
						task.priority_letter = "A"
					view.replace(edit, adjusted_line, task.string)
					line_offset += task.offset