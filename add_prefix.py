import sublime, sublime_plugin, time
import helper

class AddPrefixCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		sel = self.view.sel()

		for selection in sel:
			line_offset = 0
			lines = view.lines(selection)
			for line in lines:
				task = "(A) " + time.strftime("%Y-%m-%d ")
				adjusted_line = sublime.Region(line.a + line_offset, line.b + line_offset)
				#if view.substr(adjusted_line)[:2] != "x ":
				#	revert_all = False
				line_offset += view.insert(edit, adjusted_line.a, task)

		#sel.clear()
		#sel.add(sublime.Region(0, 0))
		
		#task = "(A) " + time.strftime("%Y-%m-%d") + " \n"

		#insert_size = view.insert(edit, 0, task)
		#first_line_end = sublime.Region(insert_size - 1, insert_size - 1)

		#sel.clear()
		#sel.add(first_line_end)
