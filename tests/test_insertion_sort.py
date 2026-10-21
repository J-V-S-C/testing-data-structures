from src.insertion_sort import insertion_sort


def test_unsorted():
    list = [3, 995, 213, 65]
    assert insertion_sort(list) == [3, 65, 213, 995]

def test_sorted():
    list = [3, 65 , 213, 995]
    assert insertion_sort(list) == [3, 65, 213, 995]

def test_negative():
    list = [-3, -995, -213, -65]
    assert insertion_sort(list) == [-995, -213, -65, -3]

def test_mixed_numbers():
    list = [3, -995, 213, -65]
    assert insertion_sort(list) == [-995, -65, 3, 213]

def test_empty():
    list = []
    assert insertion_sort(list) == []

def test_single_element():
    list = [42]
    assert insertion_sort(list) == [42]

def test_duplicate_elements():
    list = [5, 5, 3, 5, 3, 4, 4] 
    assert insertion_sort(list) == [3, 3, 4, 4, 5, 5, 5]

def test_identical_elements():
    list = [7, 7, 7, 7]
    assert insertion_sort(list) == [7, 7, 7, 7]

def test_large_randon():
    import random
    list = random.sample(range(1, 1000), 100)
    assert insertion_sort(list) == sorted(list)