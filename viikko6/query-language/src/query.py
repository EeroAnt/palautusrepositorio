from matchers import All, And

class QueryBuilder:
	def __init__(self, query_object = All(), operator = And):
		self.query_object = query_object
		self.operator = operator

	def build(self):
		return self.query_object
	
	def playsIn(self, team):
		from matchers import PlaysIn
		return QueryBuilder(self.operator(self.query_object,PlaysIn(team)))

	def hasAtLeast(self, value, attr):
		from matchers import HasAtLeast
		return QueryBuilder(self.operator(self.query_object,HasAtLeast(value,attr)))

	def hasFewerThan(self, value, attr):
		from matchers import HasFewerThan
		return QueryBuilder(self.operator(self.query_object,HasFewerThan(value,attr)))

	def oneOf(self, *queries):
		from matchers import Or
		return QueryBuilder(self.operator(self.query_object,Or(*queries)),Or())

# class PlaysInQuery:
# 	def __init__(self, query_object = All(), team=""):
# 		from matchers import PlaysIn
# 		self.query_object = And(query_object, PlaysIn(team))
# 		self.team = team
	
# 	def build(self):
# 		return self.query_object
	
# 	def test(self, player):
# 		return player.team == self.team

# class HasAtLeastQuery:
# 	def __init__(self, query_object = All(), value=0, attr=""):
# 		from matchers import HasAtLeast
# 		self.query_object = And(query_object, HasAtLeast(value, attr))
# 		self.value = value
# 		self.attr = attr
	
# 	def build(self):
# 		return self.query_object
	
# 	def test(self, player):
# 		player_value = getattr(player, self.attr)
# 		return player_value >= self.value