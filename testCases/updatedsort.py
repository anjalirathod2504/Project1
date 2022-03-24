import copy

def bubble_sort_v1(container: object) -> object:
    # setting up variables
   
    container = list(copy.copy(container))
    length = len(container)

    while length:

        for i in range(len(container) - 1):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]

        length -= 1

    return container


'''
data = [-2, 45, 0, 11, -9]
print(bubble_sort_v1(data))

data = (-2, 45, 0, 11, -3925)
print(bubble_sort_v1(data))
print(type(data))

# failed
data = [-2, 45, (0, 11), -9]
#print(bubble_sort_v1(data))

'''