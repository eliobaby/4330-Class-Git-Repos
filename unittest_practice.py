import unittest
import numpy as np

def bubble_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

class TestBubbleSort(unittest.TestCase):
    # Positive Case
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([2, 4, 1, 3]), [1, 2, 3, 4])
        self.assertEqual(bubble_sort([1.3, 2.5, 4.2, 3.1]), [1.3, 2.5, 3.1, 4.2])
        self.assertEqual(bubble_sort([-9.5, 15.7, -9.666, -9.667]), [-9.667, -9.666, -9.5, 15.7])

    # Negative Case
    def test_bubble_sort_invalid_input(self):
        with self.assertRaises(TypeError):
            bubble_sort("Hello World")
        with self.assertRaises(TypeError):
            bubble_sort(0)
        with self.assertRaises(TypeError):
            bubble_sort([1, "a", 2, "b"])

    # Performance Case
    def test_bubble_sort_large_array(self):
        large_array = np.random.randint(0, 1000, 1000).tolist()  # Large array of 1000 random integers
        sorted_array = sorted(large_array)
        self.assertEqual(bubble_sort(large_array), sorted_array)

    # Boundary Cases
    def test_bubble_sort_edge_cases(self):
        self.assertEqual(bubble_sort([]), [])  # Empty array
        self.assertEqual(bubble_sort([1]), [1])  # Single-element array
        self.assertEqual(bubble_sort([2, 2, 2, 2]), [2, 2, 2, 2])  # Array with all elements the same
        self.assertEqual(bubble_sort([4, 4, 5, 3, 3, 5]), [3, 3, 4, 4, 5, 5])  # Array with duplicate elements
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  # Reverse array
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Presorted array

    # Idempotency Case
    def test_bubble_sort_idempotency(self):
        arr1 = [2, 4, 1, 3]
        arr2 = [2, 4, 1, 3]
        self.assertEqual(bubble_sort(arr1), bubble_sort(arr2))

if __name__ == '__main__':
    unittest.main()
