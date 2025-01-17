def bubble_sort(arr, matrix):

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                # Swap matrix data to match the key array
                for z in range(1, len(matrix)):
                    (matrix[z][i], matrix[z][i + 1]) = (matrix[z][i + 1], matrix[z][i])
