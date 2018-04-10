print("This is from Chimps module to import")

test = "This is test by Chimp"

def find_index(to_search, target):
	for i, value in enumerate (to_search):
		if value==target:
			return i

	return -1;