c = int(input("Enter maximum storage capacity: "))
N = int(input("Enter number of containers: "))
weights = []

for i in range(N):
    weight = int(input(f"Enter weight of container {i + 1}: ")) # Take inputs for all containers
    weights.append(weight)

total = sum(weights)
print(f"Total Shipment Weight: {total}")
print(f"Average Container Weight: {total / N}")
print(f"Heaviest Container: {max(weights)}")
print(f"Lightest Container: {min(weights)}")
print(f"Classification: {"Heavy" if total >= 200 else "Light"}")
print(f"Port Capacity: {c}")
print(f"Status: {"Shipment can be unloaded" if total <= c else "Shipment exceeds port capacity"}")
