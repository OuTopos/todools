import sublime, sublime_plugin, time

class CreateTaskCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		sel = self.view.sel()

		sel.clear()
		sel.add(sublime.Region(0, 0))
		
		task = "(A) " + time.strftime("%Y-%m-%d") + " \n"

		insert_size = view.insert(edit, 0, task)
		first_line_end = sublime.Region(insert_size - 1, insert_size - 1)

		sel.clear()
		sel.add(first_line_end)
