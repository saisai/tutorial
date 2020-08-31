from itertools import product

def cartesian_product(arr1, arr2):

    # return the list of all the computed tuple
    # using the product() method
    return list(product(arr1, arr2))


if __name__ == '__main__':
    arr1 = [1, 2, 3]
    arr2 = [5, 6, 7]
    print(cartesian_product(arr1, arr2))

    # https://www.geeksforgeeks.org/python-itertools-product/
