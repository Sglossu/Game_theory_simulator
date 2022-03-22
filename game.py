import players
from collections import Counter
from itertools import combinations


class Game:
	
	def __init__(self, matches=1):
		self.matches = matches
		self.registry = Counter()
		self.answer1 = None
		self.answer2 = None

	def __str__(self):
		return "game"

	def play(self, player1, player2):
		for i in range(self.matches):
			self.answer1 = player1.round(player2)
			self.answer2 = player2.round(player1)
			if self.answer1 is True and self.answer2 is True:
				player1.candy += 2
				player2.candy += 2
			elif self.answer1 is True and self.answer2 is False:
				player1.candy -= 1
				player2.candy += 3
			elif self.answer1 is False and self.answer2 is True:
				player1.candy += 3
				player2.candy -= 1
			elif self.answer1 is False and self.answer2 is False:
				pass
		
		self.registry.update({player1.name: player1.candy})
		self.registry.update({player2.name: player2.candy})
		player1.__init__(player1.name)
		player2.__init__(player2.name)

	def top3(self):
		return self.registry.most_common(3)


if __name__ == '__main__':
	
	game = Game()
	cheater = players.Cheater("cheater")
	coop = players.Cooperative("cooperative")
	copy = players.Copycat("copycat")
	grud = players.Grudger("grudger")
	detect = players.Detective("detective")
	
	# game.play(copy, cheater)
	# game.play(copy, coop)
	# game.play(copy, grud)
	# game.play(copy, detect)
	# game.play(cheater, coop)
	#
	# game.play(cheater, grud)
	# game.play(cheater, detect)
	# game.play(coop, grud)
	# game.play(coop, detect)
	# game.play(grud, detect)
	
	players_lst = (cheater, coop, copy, grud, detect)
	for pl1, pl2 in combinations(players_lst,2):
		game.play(pl1, pl2)
		
	print(game.top3())