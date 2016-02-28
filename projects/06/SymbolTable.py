# Keeps a correspondence between symbolic labels and numeric address

class SymbolTable():

	def __init__(self):
		self.dict = {
						'SP': str( bin( 0x0000 )[2:].zfill(16) ),
					   'LCL': str( bin( 0X0001 )[2:].zfill(16) ),
					   'ARG': str( bin( 0X0002 )[2:].zfill(16) ),
					  'THIS': str( bin( 0X0003 )[2:].zfill(16) ),
					  'THAT': str( bin( 0X0004 )[2:].zfill(16) ),
					'SCREEN': str( bin( 0X4000 )[2:].zfill(16) ),
					   'KBD': str( bin( 0X6000 )[2:].zfill(16) )
					   }
		self.a = '0'
		self.count = 16

	def addEntry(self, symbol):
		if( self.contains( symbol ) == True):
			return self.dict
		else:
			if( self.isdigit( symbol ) == True ):
				address = self.a + str( bin( int( symbol ) )[2:].zfill(15) )
				self.dict[ symbol ] = address
				return self.dict
			else:
				""" address = self.a + str( bin( random.randint(16, 1000) )[2:].zfill(15) )
				self.dict[ symbol ] = address
				return self.dict """
				self.count = self.count + 1
				if( self.count >= 16 and self.count <= 1000 ):
					address = self.a + str( bin( self.count ))[2:].zfill(15)
					self.dict[ symbol ] = address
					return self.dict
				else:
					print("Error! Too many user-defined variables")

	def contains(self, symbol):
		if( self.dict.has_key( symbol ) == True ):
			return True
		return False

	def GetAddress(self, symbol):
		return self.dict.get( symbol )

	def isdigit(self, symbol):
		if( symbol.isdigit() == True):
			return True
		else:
			return False
