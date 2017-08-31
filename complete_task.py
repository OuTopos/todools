import sublime, sublime_plugin
from .helper import Task

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
				task = Task(view.substr(adjusted_line))
				if not task.completed:
					revert_all = False
					task.set_completed()
					view.replace(edit, adjusted_line, task.string)
					line_offset += task.offset

		if revert_all:

			for selection in sel:
				line_offset = 0
				lines = view.lines(selection)
				for line in lines:
					adjusted_line = sublime.Region(line.a + line_offset, line.b + line_offset)
					task = Task(view.substr(adjusted_line))
					task.set_completed(False)
					view.replace(edit, adjusted_line, task.string)
					line_offset += task.offset