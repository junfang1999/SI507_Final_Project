import csv

with open('npc13.csv', newline='') as f:
	reader = csv.reader(f)
	data = list(reader)



class TreeNode:
	#this class corresponds to the nodes in our binary search tree
	#each node in the binary search tree has a value (corresponding to a congresspersons name)
	#each node in bst has a datum corresponding to the entry in the csv file of the corresponding congressperson
	#each node in the bst has a left and right value that corresponds to future nodes in the binary search tree

	def __init__(self, entry=None):
		if entry is None:
			self.value = None
			self.datum = None
		else:
			self.value = entry[0]
			self.datum = entry

		self.left = None
		self.right = None

class BinarySearchTree:

	def __init__(self):
		self.root = None

	def insert(self, entry):
		new_node = TreeNode(entry)

		value = entry[0]

		if self.root is None:

			self.root = new_node
			return

		current_node = self.root

		while True:

			if value < current_node.value:
				if current_node.left is None:
					current_node.left = new_node
					break

				current_node = current_node.left

			else:
				if current_node.right is None:
					current_node.right = new_node
					break
				current_node = current_node.right



	def search(self, value):
		if self.root is None:
			return False, None

		current_node = self.root
		while current_node:
			if value == current_node.value:
				return True, current_node.datum

			elif value < current_node.value:
				current_node = current_node.left
			else:
				current_node = current_node.right

		return False, None



#Now we build our binary search tree for names in our csv file

name_bst = BinarySearchTree()

for datum in data:
	name_bst.insert(datum)



def name_search(name):
	#takes a name as input and returns the congressperson with this exact name.
	#this function uses a binary search tree internally.

	return name_bst.search(name)






def general_search(party = None, gender = None, ethnicity = None, birthday = None, position = None, birthplace = None, constituency = None):

	#takes an optional number of properties and returns all congresspersons satisfying these properties.
	#this code uses the set intersection functionality of python3.
	


	outputs = []

	inputs = [party, gender, ethnicity, birthday, position, birthplace, constituency]

	reqs = [x for x in inputs if x is not None]

	for datum in data:

		if set(reqs).issubset(set(datum)):
			outputs += [datum]

	return outputs




