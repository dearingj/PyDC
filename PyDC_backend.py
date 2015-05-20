#!/usr/bin/python3
#This file is the back-end for the GUI and CLI programs.

class DCTranslator:
	species = [ "", "D|Dragons", "H|Humanoids", "A|Amphibians", "B|Birds", "C|Crustaceans", "S|Dinosaurs", "E|Extraterrestrials", "F|Fish", "I|Insects", "L|Legends", "M|Mammals", "M|Molluscs", "Y|Mythical", "P|Plants", "R|Reptiles", "Q|Spirits", "U|Undead", "~|Shape Changers" ]
	subSpecies = [
		[], #Unknown
		[ "", "a|Amphiteres", "c|Draconids", "d|Dragonettes", "e|Eastern Dragons", "f|Faerie Dragons", "h|Hydra", "i|Dimar", "l|Dracolich", "p|Pernese Dragons", "r|Turtle Dragons", "s|Serpents", "t|Tarrasques", "u|Pseudodragons", "v|Wyverns", "w|Western Dragons", "y|Wyrms" ], #Dragons
		[ "", "a|Apes", "d|Dwarves", "e|Elves", "f|Fairies", "i|Giants", "g|Gnomes", "h|Hobbits", "k|Kender", "y|Nymphs", "t|Troll", "w|Wolfman", "?|Unknown" ], #Humanoids
		[ "", "f|Frog", "n|Newts", "s|Salamanders", "t|Toads" ], #Amphibians
		[ "", "c|Crows", "e|Eagles", "h|Hawks", "p|Phoenix", "r|Ravens" ], #Birds
		[ "", "c|Crabs", "l|Lobsters", "s|Shrimps" ], #Crustaceans
		[ "", "a|Allosaurs", "c|Triceratops", "p|Apatosaurs", "s|Stegosaurs", "t|Tyrannosaurs", "v|Velociraptors" ], #Dinosaurs
		[ "", "d|Daleks", "t|Tribbles" ], #Extraterrestrials
		[ "", "h|Sea horses", "f|Freshwater fish", "s|Sharks" ], #Fish
		[ "", "a|Ants", "b|Beetles", "f|Flies", "l|Locusts", "m|Moths", "u|Butterflies" ], #Insects
		[ "", "r|Gargoyles", "l|Gremlins", "g|Griffins or Gryphons", "n|Manticores", "m|Merfolk", "f|Salamanders", "s|Sprites", "t|Treants & Treefolk", "u|Unicorns" ], #Legends
		[ "", "a|Avians/Bats", "b|Bears", "c|Canines", "f|Felines", "h|Horses", "m|Monkeys", "p|Polecats", "r|Rodents", "w|Whales/Cetaceans" ], #Mammals
		[ "", "c|Cuttlefish", "l|Limpets", "o|Octopuses", "y|Oysters", "s|Snails" ], #Molluscs
		[ "", "c|Centaurs", "y|Cyclopses", "g|Golems", "h|Hellhounds", "m|Minotaurs", "p|Pegasi", "t|Satyrs", "s|Sphinxes" ], #Mythical
		[ "", "c|Cacti", "f|Fungi", "t|Trees" ], #Plants
		[ "", "a|Alligators/Crocodiles", "c|Chameleons", "g|Geckos", "k|Komodo Dragons", "l|Lizards", "n|Skinks", "s|Snakes", "t|Turtles" ], #Reptiles
		[ "", "a|Angels", "d|Devils/Demons", "g|Ghosts", "i|Imps", "p|Poltergeists", "s|Spectres", "w|Will-o-the-wisps" ], #Spirits
		[ "", "g|Ghouls", "v|Vampires", "z|Zombies" ], #Undead
		[], #Shape changers
	]
	subSubSpecies = [
		[], #Unknown
		[ [], [], [], [], [], [], [], [], [], [], [], [
			"", "s|Sea Serpents", "f|Fire Serpents" #Serpents
		], [], [], [], [], [] ], #Dragons
		[ [], [], [], [
			"", "w|Wood Elves" #Elves
		], [], [], [], [], [], [], [], [], [] ], #Humanoids
		[ [], [], [], [], [] ], #Amphibians
		[ [], [], [], [], [], [] ], #Birds
		[ [], [], [], [] ], #Crustaceans
		[ [], [], [], [], [], [], [] ], #Dinosaurs
		[ [], [], [] ], #Extraterrestrials
		[ [], [], [
			"", "g|Goldfish", "t|Trout" #Freshwater fish
		], [] ], #Fish
		[ [], [], [], [], [], [], [] ], #Insects
		[ [], [], [], [], [], [], [], [], [], [] ], #Legends
		[ [], [], [], [
			"", "d|Domestic dogs", "f|Foxes", "w|Wolves" #Canines
		], [
			"", "b|Black panthers", "c|Cheetahs", "d|Domestic cats", "p|Leopard", "l|Lions", "x|Lynxes", "a|Panthers", "u|Pumas", "t|Tigers" #Felines
		], [], [
			"", "g|Gibbons" #Monkeys
		], [
			"", "f|Ferrets", "m|Mink" #Polecats
		], [
			"", "g|Gerbils", "h|Hamsters", "m|Mice", "r|Rats", "s|Squirrels" #Rodents
		], [
			"", "d|Dolphins", "k|Killer Whales", "p|Porpoises" #Cetaceans
		] ], #Mammals
		[ [], [], [], [], [], [] ], #Molluscs
		[ [], [], [], [], [], [], [], [], [] ], #Mythical
		[ [], [], [], [
			"", "a|Ash", "e|Elm", "o|Oak" #Trees
		] ], #Plants
		[ [], [], [], [], [], [], [
			"", "f|Fire Skinks" #Skinks
		], [], [] ], #Reptiles
		[ [], [], [], [], [], [], [], [] ], #Spirits
		[ [], [], [], [] ], #Undead
		[ [] ], #Shape changers
	]
	
	subSubSubSpecies = [
		[], #Unknown
		[], #Dragons
		[], #Humanoids
		[], #Amphibians
		[], #Birds
		[], #Crustaceans
		[], #Dinosaurs
		[], #Extraterrestrials
		[], #Fish
		[], #Insects
		[], #Legends
		[
			[], #Blank
			[], #Bats
			[], #Bears
			[], #Canines
			[
				[], #Blank
				[], #Black panthers
				[], #Cheetahs
				[], #Domestic cats
				[
					"", "s|Snow leopards"
				], #Leopards
				[], #Lions
				[], #Lynxes
				[], #Panthers
				[], #Pumas
				[] #Tigers
			], #Felines
			[], #Horses
			[], #Monkeys
			[], #Polecats
			[], #Rodents
			[] #Cetaceans
		], #Mammals
		[], #Molluscs
		[], #Mythical
		[], #Plants
		[], #Reptiles
		[], #Spirits
		[], #Undead
		[], #Shape changers
	]
	
	gender = [ "", "f|Female", "h|Hermaphrodite", "m|Male", "n|Neuter", "p|Pseudo-hermaphrodite", "~|Variable", "?|Unknown" ]
	
	lengthMagnitude = [ "+++!|Celestial", "+++|Mistaken for mountain ranges", "++|Can't see own tail on a foggy day", "+|Godzilla-sized", "|Draco-sized", "-|Human-sized", "--|Dog-sized", "---|Pocket Dragon-sized", "---!|Microscopic", "~|Variable", "^|One-Dragon-sized" ]
	
	lengthUnit = [ "i|inches", "f|feet", "y|yards", "c|centimeters", "m|meters", "k|kilometers" ]
	
	lengthMod = [ "a|Arms", "l|Legs", "n|Head and neck", "t|Tail", "w|Wingspan" ]
	
	width = [ "", "+++!|I am Athelind! My belly is now several galaxies wide... while I'm only a few hundred feet long!", "+++|Planets have been known to crack in half with my arrival!", "++|My digestion of food has been known to cause earthquakes.", "+|I move by rolling. Flying has always been an effort for me.", "|What can I say... I'm normal, except for a few feasts here or there.", "-|I'm slightly on the slim side", "--|Ever heard of serpentine?", "---|Whoah! Whaddaya mean I look like a long string with wings?", "---!|I'm one-dimensional - all length and no width or depth. Just one long super-string!", "~|Variable - My girth depends on what I've just eaten!" ]
	
	weightUnit = [ "c|long hundredweight avoirdupois", "g|grams", "k|kilograms", "l|pounds avoirdupois", "o|ounces avoirdupois", "s|stones avoirdupois", "t|tons avoirdupois OR metric tons" ]
	
	weightMagnitude = [ "+++!|Black hole", "+++|Massive", "++|Obese", "+|Over-weight", "|Normal", "-|Under-weight", "--|Buoyant", "---|Feather-weight", "---!|Weightless" ]
	
	def decode( self, coded ):
		"Accepts a single string as the argument. Processes it. Returns true if processing worked or false if there was an error."
		if( type( coded ) is not str ):
			return False
		
		coded = coded.strip()
		
		print( coded )
		return True
	
	def encode( self, version, speciesNum, subSpeciesNum, subSubSpeciesNum, subSubSubSpeciesNum, genderNum, lengthType, lengthNum, lengthUnitNum, lengthModifiers, widthNum, weightType, weightNum, weightUnitNum ):
		"Accepts several arguments. Processes them into a string. Invalid arguments are ignored."
		
		result = "DC"
		if( version == 2 ):
			
			#DC version
			result += str( version )
			result += "."
			
			#Species, Subspecies, Subsubspecies, Subsubsubspecies
			if( speciesNum >= 0 ):
				result += self.species[ speciesNum ][ :1 ]
				if( subSpeciesNum >= 0 ):
					result += self.subSpecies[ speciesNum ][subSpeciesNum][ :1 ]
					if( subSubSpeciesNum >= 0 ):
						result += self.subSubSpecies[ speciesNum ][ subSpeciesNum ][ subSubSpeciesNum ][ :1 ]
						if( subSubSubSpeciesNum >= 0 ):
							result += self.subSubSubSpecies[ speciesNum ][ subSpeciesNum ][ subSubSpeciesNum ][ subSubSubSpeciesNum ][ :1 ]
			
			#Gender
			if( self.gender[ genderNum ] != "" ):
				result += " G"
				result += self.gender[ genderNum ][ :1 ]
			
			#Length
			if( lengthType != 0 ): #0 is 'Unspecified'
				result += " L"
				if( lengthType == 1 ): #Order of Magnitude
					result += self.lengthMagnitude[ lengthNum ][ :self.lengthMagnitude[ lengthNum ].find( "|" ) ]
				else: #Exact measure
					result += str( lengthNum )
					result += self.lengthUnit[ lengthUnitNum ][ :self.lengthUnit[ lengthUnitNum ].find( "|" ) ]
				
				for lm in lengthModifiers:
					if( len( lm ) == 2 ):
						result += str( lm[ 0 ] )
						result += self.lengthMod[ lm[ 1 ] ][ :self.lengthMod[ lm[ 1 ] ].find( "|" ) ]
			
			#Width
			if( self.width[ widthNum ] != "" ):
				result += " W"
				result += self.width[ widthNum ][ :self.width[ widthNum ].find( "|" ) ]
			
			#Weight
			if( weightType != 0 ):
				result += " T"
				if( weightType == 1 ): #Order of Magnitude
					result += self.weightMagnitude[ weightNum ][ :self.weightMagnitude[ weightNum ].find( "|" ) ]
				else: #Exact measure
					result += str( weightNum )
					result += self.weightUnit[ weightUnitNum ][ :self.weightUnit[ weightUnitNum ].find( "|" ) ]
			
		elif( version > 2 ):
			result += str( version )
			result += "."
		
		return result
