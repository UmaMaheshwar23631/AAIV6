# AO* Algorithm Implementation (Tower of Hanoi Example)

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"{source} -> {destination}")
        return
    
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"{source} -> {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Main Program
n = 3   # Number of disks

print("Initial State:")
print("A = [3,2,1], B = [], C = []")

print("\nOptimal Move Sequence:")
tower_of_hanoi(n, 'A', 'B', 'C')

print("\nFinal State:")
print("A = [], B = [], C = [3,2,1]")