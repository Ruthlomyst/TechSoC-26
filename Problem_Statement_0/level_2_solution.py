def sorting(weights):
    print("Containers in sorted order: ")
    for i, weight in enumerate(sorted(weights)): # to get index for every container
        print(f"{i+1}. {weight}")
# sorting([10, 20, 30, 40])

def multi_ship_processing():
    N = int(input("Enter number of containers: "))
    weights = []
    for i in range(N):
        weight = int(input(f"Enter weight of container {i + 1}: ")) # Take inputs for all containers
        weights.append(weight)

    total = sum(weights)
    print(f"\nTotal Shipment Weight: {total}")
    print(f"Classification: {"Heavy" if total >= 200 else "Light"}\n")


# c = int(input("Enter maximum storage capacity: "))
# weights = [50, 120, 80, 45, 30]
# do consider below function, it was commented as it runs otherwise and 
# - may hinder checking out other functions
"""
multi_ship_processing()
ships_processed = 1

while True:
    continue_or_not = input("Input (continue?): ")

    if continue_or_not == "yes":
        multi_ship_processing()
        ships_processed += 1
    elif continue_or_not == "no":
        print(f"Total ships processed: {ships_processed}\n")
        break
    else:
        print("Kindly enter either yes/no\n")
"""

def bar_chart(weights):
    print("Container Weight Bar Chart: \n")
    for i, weight in enumerate(weights):
        print(f"Container {i+1} ({weight}) : {"*" * (weight // 5)}") # so, ***** for 25 weight, // for int division
# bar_chart([50, 120, 80, 45, 30])

def save_report(weights):
    what_say = input("Whether to save shipment report (yes/no): ")
    if what_say == "yes":
        with open("shipment_report.txt", "w+") as f: # opening the file
            total = sum(weights)
            f.write(f"Total Shipment Weight: {total}\n")
            f.write(f"Average Container Weight: {total / len(weights)}\n")
            f.write(f"Heaviest Container: {max(weights)}\n")
            f.write(f"Lightest Container: {min(weights)}\n")
            f.write(f"Classification: {"Heavy" if total >= 200 else "Light"}\n")

        print("Report saved to shipment_report.txt\n")
    elif what_say == "no":
        return
    else:
        print("Kindly input yes/no\n")
        return
# save_report([50, 120, 80, 45, 30])

def read_from_file():
    file = input("Enter filename: ")
    with open(file, "r") as f:
        lines = [int(line.strip()) for line in f] # removing \n from end of line and getting list
        print(f"\nLoaded {lines[0]} containers from {file}")
        weights = lines[1:] # as first line has number of containers
        print(f"Weights: {', '.join([str(weight) for weight in weights])}\n") 
        # converting to str is necessary for join function
        total = sum(weights)
        print(f"Total Shipment Weight: {total}")
        print(f"Average Container Weight: {total / len(weights)}")
        print(f"Heaviest Container: {max(weights)}")
        print(f"Lightest Container: {min(weights)}")
        print(f"Classification: {"Heavy" if total >= 200 else "Light"}")
# read_from_file()

def search(weights):
    find_weight = int(input("Enter weight of container to be found: "))
    if find_weight in weights:
        print("Container found!")
        print(f"Container {weights.index(find_weight) + 1} has weight {find_weight}")
    else:
        print(f"No container found with weight {find_weight}")
# search([50, 80, 50, 30])

def kth_heaviest(weights):
    heavy_weights = sorted(weights, reverse=True)
    i = int(input("kth heaviest for k: "))
    if not (i >= 1):
        print("Invalid input: k must be at least 1.")
        return
    try:
        print(f"The {i}th heaviest container has weight: {heavy_weights[i-1]}")
    except IndexError:
        print(f"Invalid input: Only {len(weights)} containers exist.")
# kth_heaviest([50, 120, 80, 45, 30])
