class CE:

	def __init__(self):
		self.tokenDict = { '(':'(', ')':')', '[':'[', ']':']' }

	def CompileClass(self):

	def CompileClassVarDec(self):

	def CompileSubroutine(self):

	def CompileParameterList(self):

	def compileVarDec(self):

	def compileStatements(self):

	def compileDo(self):

	def compileLet(self):

	def compileWhile(self):

	def compileReturn(self):

	def compileIf(self):

	def compileExpression(self):

	def compileTerm(self):

	def compileExpressionList(self):

	def match(self, target, expect):
		if expect == self.tokenDict[target]:
			"Get the next token"
			self.getToken() 
		else:
			print('Unmatched error')

	def 






