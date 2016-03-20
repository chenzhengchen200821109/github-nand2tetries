class SymbolTable():

	def __init__(self):
		self._classScope = None
		self._subroutineScope = None
		self._key = [ 'name', 'type', 'kind', '#' ]
		self._value = None
		self._classCount = 0

	# Starts a new subroutine scope
	def startSubroutine(self):

	# Defines a new identifier of a given name, type, and kind and 
	# assigns it a running index. STATIC and FIELD identifiers have
	# a class scope, while ARG and VAR identifier have a subroutine 
	# scope
	def Define(self, name, type, kind):
		if kind in [ 'STATIC', 'FIELD' ]:
			pair = { 'name': name, }
			self._classScope.update

	# Returns the number of variables of the given kind already defined
	# in the current scope
	def VarCount(self, kind):

	# Returns the kind of the named identifier in the current scope.
	# If the identifier is unknown in the current scope, returns None.
	def KindOf(self, name):

	# Returns the type of the named identifier in the current scope.
	def TypeOf(self, name):

	# Returns the index assigned to the named identifier.
	def IndexOf(self, name):


class _
		
