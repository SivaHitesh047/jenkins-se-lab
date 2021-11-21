import unittest 
from add_list import add_list_func

class TestAddList(unittest.TestCase):
	def test_add_list_one(self):
		self.assertEqual(sum([1,2,3,4,5], 15)
	
	def test_add_list_two(self):
		self.assertEqual(sum([6,7,8,9]), 30)

	def test_add_list_three(self):
		self.assertEqual(sum([1,3,5,7]), 16)

	def test_add_list_empty(self):
		self.assertEqual(sum([]), 0)

	
if __name__ == "__main__":
	unittest.main()
	
