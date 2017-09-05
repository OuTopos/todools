import sublime, sublime_plugin
from .helper import Task

class IncreasePriorityCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		view = self.view
		sel = self.view.sel()

		for selection in sel:
			keep_selection = True
			if selection.a == selection.b:
				keep_selection = False
			line_offset = 0
			lines = view.lines(selection)
			for line in lines:
				if line.a != line.b and not keep_selection:
					keep_selection = True
				adjusted_line = sublime.Region(line.a + line_offset, line.b + line_offset)
				task = Task(view.substr(adjusted_line))
				if not task.completed:
					if task.priority:
						task.priority += 1
					else:
						task.priority_letter = "A"
					view.replace(edit, adjusted_line, task.string)
					line_offset += task.offset
			if not keep_selection:
				sel.clear()
				sel.add(sublime.Region(view.line(selection).b, view.line(selection).b))