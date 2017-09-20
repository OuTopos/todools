import re, time

pattern = re.compile("(?:(x)\s)?(?:\(([A-Z])\)\s)?(?:([0-9]{4}-[0-9]{2}-[0-9]{2})\s)?(?:([0-9]{4}-[0-9]{2}-[0-9]{2})\s)?(.*)")
priorities = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

class Task():
	def __init__(self, string=""):
		self.string = string
		
	def add_date(self):
		self.creation_date = time.strftime("%Y-%m-%d")

	def set_completed(self, completed=True):
		if completed:
			self.completed = True
			if self.creation_date:
				self.completion_date = time.strftime("%Y-%m-%d")
		else:
			self.completed = False
			self.completion_date = None

	@property
	def offset(self):
		return len(self.string) - self.initial_len

	@property
	def priority_letter(self):
		if isinstance(self.priority, int):
			priority = self.priority % len(priorities)
			return priorities[priority:priority+1]
		else:
			return None

	@priority_letter.setter
	def priority_letter(self, value):
		if isinstance(value, str) and priorities.find(value) > -1:
			self.priority = priorities.find(value)

	@property
	def string(self):
		string = "x " if self.completed else ""
		string += "(" + self.priority_letter + ") " if self.priority_letter else ""
		string += self.completion_date + " " if self.completion_date else ""
		string += self.creation_date + " " if self.creation_date else ""
		string += self.description if self.description else ""
		return string

	@string.setter
	def string(self, value):
		self.initial_len = len(value)
		self.match = re.match(pattern, str(value))
		self.completed = self.match.group(1) == "x"
		self.priority = None
		self.priority_letter = self.match.group(2)
		self.completion_date = self.match.group(3) if self.match.group(4) else None
		self.creation_date = self.match.group(4) if self.match.group(4) else self.match.group(3)
		self.description = self.match.group(5)