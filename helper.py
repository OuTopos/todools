import re, time

pattern = re.compile("(?:(x)\s)?(?:\(([A-Z])\)\s)?(?:([0-9]{4}-[0-9]{2}-[0-9]{2})\s)?(?:([0-9]{4}-[0-9]{2}-[0-9]{2})\s)?(.*)")
priorities = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Task():
	def __init__(self, string):
		self.string = string
		
	def set_creation_date(self, date=time.strftime("%Y-%m-%d")):
		if date:
			self.creation_date = date
		else:
			None

	def set_completed(self, completed=True):
		if completed:
			self.completed = True
			self.completion_date = time.strftime("%Y-%m-%d")
		else:
			self.completed = False
			self.completion_date = None

	@property
	def priority_letter(self):
		if isinstance(self.priority, int):
			priority = len(priorities) - 1 - self.priority % len(priorities)
			print(priority, priorities[priority:priority+1])
			return priorities[priority:priority+1]
		else:
			return None

	@priority_letter.setter
	def priority_letter(self, value):
		if isinstance(value, str) and priorities.find(value) > -1:
			self.priority = len(priorities) - (priorities.find(value) + 1)


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
		self.match = re.search(pattern, str(value))
		self.completed = self.match.group(1) == "x"
		self.priority = None
		self.priority_letter = self.match.group(2)
		self.completion_date = self.match.group(3) if self.match.group(4) else None
		self.creation_date = self.match.group(4) if self.match.group(4) else self.match.group(3)
		self.description = self.match.group(5)


test = Task("(A) 2000-08-22 sdsd +poop sdasd @asdasdad")
print("1st " + test.string)
print("1st " + test.match.group(0))
test.completed = True
test.priority += 1
print("2nd " + test.string)
test.priority_letter = "U"
test.set_completed(True)
print("3rd " + test.string)

test2 = Task("asdsad asdfasdf asdf 5434534 asfasf")
test2.set_creation_date()
print(test2.string)


al = 20
ran = 21
print(ran % al)