#JackTokenizer: Removes all comments and  white space from the input stream and breaks it into Jack-language tokens,
#as specified by the Jack grammar.
import re

class JackTokenizer:
	
	def __init__(self, inputFile):

		self.keyWordList = [ 'class', 
				'constructor',
				'function',
				'method',
				'field',
				'static',
				'var',
				'int', 
				'char',
				'boolean',
				'void',
				'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return' ]
		#self.letterList = re.compile(r'[a-zA-Z]')
		self.symbolList = [ '{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~' ] 
		self.constantList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		#self.constantList = re.compile(r'[0-9]')
		self.letterList = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', 
				'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ] 

		self.sourceFile = open(inputFile, 'r')
		self.sequenceList = list()

		self.accept_state_int = 0

		self.tokenList = list()
		self.partsList = list()

	#def hasMoreTokens(self):

	#def advance(self):

	# remove exactly rthe number of characters in font of a string.
	def _preMove(self, seq, chars):
		length1 = len( chars )
		length2 = len( seq )
		return seq[length1:length2]

	def _getToken(self, seq):
		length = len( seq )
		for i in range(1, length+1):
			temp = seq[0:i]
			if self.tokenType( temp ) in [ 'T_KEYWORD', 'T_SYMBOL', 'T_IDENTIFIER', 'T_INTEGER' ]:
				pass
			else:
				i = i-1
				break
		return seq[0:i]

	def _getTokens(self, seq):
		while True:
			temp = self._getToken( seq )
			self.tokenList.append( temp )
			seq = self._preMove( seq, temp )
			if seq == '':
				break;
		return self.tokenList

	def _getAllParts(self):
		for part in self.getAllSequence():
			temp = part.split(' ')
			for p in temp:
				if p == '':
					pass
				else:
					self.partsList.append( p )
		return self.partsList

	def getAllTokens(self):
		for part in self._getAllParts():
			self._getTokens( part )
		return self.tokenList


	
	def getAllSequence(self):
		lines = self.sourceFile.readlines()
		for element in lines:
			temp = element.rstrip('\n').lstrip('\t').lstrip(' ')
			self.sequenceList.append( temp )
		return self.sequenceList


	def tokenType(self, seq):
		if self.isKeyWord( seq ) == True:
			return 'T_KEYWORD'
		elif self.isSymbol( seq ) == True:
			return 'T_SYMBOL'
		elif self.isIdentifier( seq ) == True:
			return 'T_IDENTIFIER'
		elif self.isIntVal( seq ) == True:
			return 'T_INTEGER'
		else:
			return 'T_UNDEFINE'

		
	def isKeyWord(self, seq): 
		if  seq in self.keyWordList:
			return True
		else:
			return False

	def isSymbol(self, seq):
		"Returns the character which is the current token. Should be called only when tokenType() is SYMBOL"
		length = len( seq )
		if length == 1:
			if seq in self.symbolList:
				return True
			else:
				return False
		elif length == 2:
			if seq in [ '==', '<=', '>=' ]:
				return True
			else:
				return False
		else:
			return False
		
	# DFA mode for variables
	def isIdentifier(self, seq):
		length = len( seq )
		if length == 0:
			return False
		elif length == 1:
			if seq[0] in self.letterList:
				return True
			else:
				False
		else:
			if seq[0] in self.letterList:
				for i in range(1, length):
					if seq[i] in self.letterList or seq[i] in self.constantList:
						continue
					else:
						return False
				return True
			else:
				return False
	 
	# DFA model for integer value
	def isIntVal(self, seq):
	 	length = len( seq )
	 	for i in range(length):
	 		if seq[i] in self.constantList:
	 			continue
	 		else:
	 			return False
	 	return True





