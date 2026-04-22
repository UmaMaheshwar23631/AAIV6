import math

def minimax(depth, nodeIndex, isMax, values, height):
    
    # Leaf node condition
    if depth == height:
        return values[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )

# Driver code
values = [3, 5, 2, 9]

height = math.log(len(values), 2)
height = int(height)

result = minimax(0, 0, True, values, height)

print("Leaf Node Values:", values)
print("Optimal Value:", result)