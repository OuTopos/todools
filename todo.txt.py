import re, time

pattern = re.compile("(?:(x)\s)?(?:\(([A-Z])\)\s)?(?:([0-9]{4}-[0-9]{2}-[0-9]{2})\s)?(?:([0-9]{4}-[0-9]{2}-[0-9]{2})\s)?(.*)")
priorities = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
asd = -41
le = 40

print(str(asd % le))

class Task():
	def __init__(self, string):
		self.string = string
		
	def add_creation_date(self):
		if not self.creation_date:
			self.creation_date = time.strftime("%Y-%m-%d")
	@property
	def priority_letter(self):
		if isinstance(self.priority, int):
			priority = len(priorities) - self.priority % len(priorities)
		else:
			return None

	@property
	def string(self):
		#sane_pri = self.priority % len(priorities)
		#print(str(self.priority) + " % " + str(len(priorities)) + " = " + str(sane_pri))
		#print(str(len(priorities)) + " - " + str(sane_pri) + " = " + str(len(priorities) - sane_pri))
		#print(str(sane_pri) + " = " + priorities[len(priorities) - sane_pri:(len(priorities) - sane_pri)+1])
		task = "x " if self.completed else ""
		task += "(" + self.priority_letter + ") " if self.priority_letter else ""
		task += self.completion_date + " " if self.completion_date else ""
		task += self.creation_date + " " if self.creation_date else ""
		task += self.description if self.description else ""

		return task

	@string.setter
	def string(self, value):
		self.match = re.search(pattern, str(value))
		self.completed = self.match.group(1) == "x"
		self.priority = len(priorities) - priorities.find(self.match.group(2)) if not self.match.group(2) == None else None
		print(self.priority)
		self.completion_date = self.match.group(3) if self.match.group(4) else None
		self.creation_date = self.match.group(4) if self.match.group(4) else self.match.group(3)
		self.description = self.match.group(5)


test = Task("x (A) 2000-08-22 2017-08-22 sdsd +poop sdasd @asdasdad")
print("1st " + test.string)
print("1st " + test.match.group(0))
test.completed = True
test.priority += 1
print("2nd " + test.string)

test2 = Task("asdsad asdfasdf asdf 5434534 asfasf")
test2.add_creation_date()
print(test2.string)