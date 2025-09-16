def bubble_sort(arr):
    n = len(arr)
    print(f"Input values = {arr}")
    iteration = 0

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            print(f"Items compared: [{arr[j]}, {arr[j+1]}]", end=" ➔ ")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"swapped {arr}")
            else:
                print("not swapped")
        iteration += 1
        print(f"Iteration #{iteration} {arr}")
        if not swapped:
            break

    print(f"Output values = {arr}")



user_input = input("Enter numbers separated by spaces: ")
arr = list(map(int, user_input.split()))
bubble_sort(arr)
