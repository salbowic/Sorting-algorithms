# Import funkcji wykonujących wybrane algorytmy sortowania i unittest module 
from sorting_algorithms import *
import unittest


#Test algorytmów

class TestCalc(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([55,66,33,2,7,6,3,86,54]), [2, 3, 6, 7, 33, 54, 55, 66, 86])
        self.assertEqual(bubble_sort(['Python','python','Algebra','Całka','java']), ['Algebra','Całka','Python','java','python'])

    def test_quick_sort(self):
        array = [55,66,33,2,7,6,3,86,54]
        array_length = len(array)

        array_words = ['Python','python','Algebra','Całka','java']
        array_words_length = len(array_words)
        
        self.assertEqual(quick_sort(array, 0, array_length - 1), [2, 3, 6, 7, 33, 54, 55, 66, 86])
        self.assertEqual(quick_sort(array_words, 0, array_words_length - 1), ['Algebra','Całka','Python','java','python'])
  

    def test_merge_sort(self):
        self.assertEqual(merge_sort([55,66,33,2,7,6,3,86,54]), [2, 3, 6, 7, 33, 54, 55, 66, 86])
        self.assertEqual(merge_sort(['Python','python','Algebra','Całka','java']), ['Algebra','Całka','Python','java','python'])

    def test_selection_sort(self):
        self.assertEqual(selection_sort([55,66,33,2,7,6,3,86,54]), [2, 3, 6, 7, 33, 54, 55, 66, 86])
        self.assertEqual(selection_sort(['Python','python','Algebra','Całka','java']), ['Algebra','Całka','Python','java','python'])


if __name__ == '__main__':
    unittest.main()
