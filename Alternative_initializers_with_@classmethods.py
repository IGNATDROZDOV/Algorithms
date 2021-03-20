class Person:
	def __init__(self, name):
		self.__name = name

	@property #readonly
	def name(self):
		return self.__name

	@classmethod
	def init_from_file(cls, path):
		with open(path) as f:
			name = f.read().strip()
		return cls(name)

	@classmethod
	def init_from_object(cls, obj):
		if hasattr(obj, 'name'):
			name = getattr(obj, 'name')
			return cls(name)
		return cls #return class as object