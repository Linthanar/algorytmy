import unittest
from Bubble import bubble_sort

class TestBubble(unittest.TestCase):
    
    def test_unorderred_list(self):
        arr = [1,2,1,3,1,2]
        bubble_sort(arr)
        self.assertEqual(arr, [1,1,1,2,2,3])
    def test_bubble_sort(self):
        # Test dla listy posortowanej rosnąco
        arr = [1, 2, 3, 4, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        # Test dla listy posortowanej malejąco
        arr = [5, 4, 3, 2, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        # Test dla listy z powtarzającymi się elementami
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

        # Test dla pustej listy
        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [])

        # Test dla listy z jednym elementem
        arr = [42]
        bubble_sort(arr)
        self.assertEqual(arr, [42])

if __name__ == "__main__":
    unittest.main()


print('----------------------------------------------------')

def test_bubble_sort():
    # Test dla listy nieuporządkowanej
    arr = [5, 2, 8, 1, 6]
    print(bubble_sort(arr))
    assert arr == [1, 2, 5, 6, 8]

    # Test dla listy uporządkowanej malejąco
    arr = [10, 8, 6, 4, 2]
    print(bubble_sort(arr))
    assert arr == [2, 4, 6, 8, 10]

    # Test dla listy z powtarzającymi się elementami na końcu
    arr = [1, 2, 3, 4, 5, 5, 5, 5]
    print(bubble_sort(arr))
    assert arr == [1, 2, 3, 4, 5, 5, 5, 5]

    # Test dla listy z powtarzającymi się elementami na początku
    arr = [5, 5, 5, 5, 1, 2, 3, 4]
    print(bubble_sort(arr))
    assert arr == [1, 2, 3, 4, 5, 5, 5, 5]

    # Test dla listy z wartościami ujemnymi
    arr = [-3, 0, 5, -1, 2]
    print(bubble_sort(arr))
    assert arr == [-3, -1, 0, 2, 5]

    # # Test dla listy z wartością None
    # arr = [None, 2, 5, 1, None, 4]
    # bubble_sort(arr)
    # assert arr == [None, None, 1, 2, 4, 5]

