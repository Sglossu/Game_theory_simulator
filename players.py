class Player:
	
	def __init__(self, candy=0, name=""):
		self.candy = candy
		self.name = name
		self.answer = []
		self.num_round = 0

	def __str__(self):
		return self.name


class Cheater(Player):
	
	def __init__(self, name):
		super().__init__(0, name)
		
	def round(self, other):
		self.answer.append(False)
		self.num_round += 1
		return self.answer[self.num_round - 1]


class Cooperative(Player):
	
	def __init__(self, name):
		super().__init__(0, name)
	
	def round(self, other):
		self.answer.append(True)
		self.num_round += 1
		return self.answer[self.num_round - 1]


class Copycat(Player):
	
	def __init__(self, name):
		super().__init__(0, name)
	
	def round(self, other):
		if self.num_round == 0:
			self.answer.append(True)
		else:
			if other.answer[self.num_round-1]:
				self.answer.append(True)
			else:
				self.answer.append(False)
		self.num_round += 1
		return self.answer[self.num_round - 1]


class Grudger(Player):
	
	def __init__(self, name):
		super().__init__(0, name)
		self.trust = True

	def round(self, other):
		if self.num_round == 0:
			self.answer.append(True)
		else:
			if other.answer[self.num_round-1] and not self.trust:
				self.answer.append(True)
			else:
				self.trust = False
				self.answer.append(False)
		self.num_round += 1
		return self.answer[self.num_round - 1]


class Detective(Player):
	
	def __init__(self, name):
		super().__init__(0, name)
		self.trust = True
	
	def round(self, other):
		if 0 <= self.num_round <= 3 and self.num_round != 1:
			if not other.answer[self.num_round-1]:
				self.trust = False
			self.answer.append(True)
		elif self.num_round == 1:
			self.answer.append(False)
			if not other.answer[self.num_round-1]:
				self.trust = False
		else:
			if self.trust:
				self.answer.append(False)
			else:
				if other.answer[self.num_round-1]:
					self.answer.append(True)
				else:
					self.answer.append(False)
		self.num_round += 1
		return self.answer[self.num_round - 1]