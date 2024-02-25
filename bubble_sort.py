arr = [1, 2, 3, 4, 5]

n = len(arr)
steps = 0

for i in range(n):
    swapped = False

    for j in range(n - 1 - i):
        steps += 1

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

        if not swapped:
            break

print(f'Steps: {steps}')

string = 'aabb'

for letter in string:
    string.count(letter)
