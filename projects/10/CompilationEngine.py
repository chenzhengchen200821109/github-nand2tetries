import JackTokenizer


class CE:

	def __init__(self):
		self.tokenDict = { '(':'(', ')':')', '[':'[', ']':']' }
		self.output
		self.keyword_pre = '<keyword>'
		self.keyword_post = '</keyword>'

	def CompileClass(self):

	def CompileClassVarDec(self, token):
		if token in ['static', 'field']:
			self.output.write( self.keyword_pre + token + self.keyword_post )
			nextToken = self.getToken()
		else:
			print('error')


	def CompileType(self, token):
		if token in ['int', 'char', 'boolean']:
			self.output.write( self.keyword_pre + token + self.keyword_post )
		elif JackTokenizer().isIdentifier( token ) == True:
			self.output.write( self.keyword_pre + token + self.keyword_post )
		else:
			print('error')








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


	"Get the next token from the sequnce of tokens"
	def getToken(self, seq):


class isClass:

	#def __init__(self):

	def isClass(self, token):
		if token == 'class':
			return True
		else:
			return False

	def isClassVarDec(self, token):
		if token in [ 'static', 'field' ]:
			return True
		else:
			return False

	def isType(self, token):
		if token in [ 'int', 'char', 'boolean' ]:
			return True
		elif JackTokenizer().isIdentifier( token ) == True:
			return True
		else:
			return False

	def isSubroutineDec(self, token):
		if token in [ 'constructor', 'function', 'method' ]:
			return True
		else:
			return False

	def isParameterList(self, token):
		next = self.getToken()
		if self.isType( token ) and JackTokenizer().isIdentifier( next ):
			return True
		else:
			return False

	def isSubroutineBody(self, token):
		next = self,getToken()
		if token == '{' and self.isVarDec( next ):
			return True
		else:
			return False

	def isVarDec(self, token):
		if token == 'var':
			return True
		else:
			return False

	def isClassName(self, token):
		if JackTokenizer().isIdentifier( token ):
			return True
		else:
			return False

	def isSubroutineName(self, token):
		if JackTokenizer().isIdentifier( token ):
			return True
		else:
			return False

	def isVarName(self, token):
		if JackTokenizer().isIdentifier( token ):
			return True
		else:
			return False

class isStatement:

	def isLetStatement(self, token):
		if token == 'let':
			return True
		else:
			return False

	def isIfStatement(self, token):
		if token == 'if':
			return True
		else:
			return False

	def isWhileStatement(self, token):
		if token == 'while':
			return True
		else:
			return False

	def isDoStatement(self, token):
		if token == 'do':
			return True
		else:
			return False

	def isReturnStatement(self, token):
		if token == 'return':
			return True
		else:
			return False


class isExpression:

	def isExpression(self, token):
		if isExpression().isTerm( token ):
			return True
		else:
			return False

	def isTerm(self, token):
		if JackTokenizer().isIntVal( token ):
			return True
		elif JackTokenizer().isStrVal( token ):
			return True
		elif token in [ 'true', 'false', 'null', 'this' ]:
			return True
		elif isClass().isVarName( token ):
			return True
		elif self.isSubroutineCall( token ):
			return True
		elif token in [ '-', '~' ]:
			return True
		elif token == '(':
			return True
		else:
			return False

	def isSubroutineCall(self, token):
		if isClass().isSubroutineName( token ):
			return True
		elif isClass().isClassName( token ):
			return True
		elif isClass().isVarName( token ):
			return True
		else:
			return False

	def isExpressionList(self, token):
		if isExpression().isExpression( token ):
			return True
		else:
			return False

	def isOp(self, token):
		if token in [ '+', '-', '/', '&', '|', '<', '>', '=' ]:
			return True
		else:
			return False










