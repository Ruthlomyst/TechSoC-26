def input_grid():
    i_pop = 0
    with open("PS_1//input.txt", "r") as f:
        first_line =  f.readline().strip()
        R, C = int(first_line[0]), int(first_line[2])
        G = int(f.readline())

        # Defining the grid
        grid = [[] * C for r in range(R)]

        # Taking input from grid.txt file and copying into grid
        for r, line in enumerate(f.readlines()):
                    for char in line.strip():
                        grid[r].append(char)
        
                        # Counting initial population
                        if char == "#":
                            i_pop += 1

    """
    for r in range(R):
        for c in range(C):
            print(f"For row {r+1}, column {c+1}")
            char = input("Enter character: ")
            if char == ".":
                grid[r].append(".")
            elif char == "#":
                grid[r].append("#")
                i_pop += 1

    print(f"Initial popuation: {i_pop}")
    """
    return R, C, G, grid, i_pop


def neighbours_list(grid, r, c, R, C):
    n_list = []
    offsets = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for offset in offsets:
        coord_of_neigh_r = r + offset[0] # changing row based on offset
        coord_of_neigh_c = c + offset[1] # changing col based on offset

        # Effectively checking if coord_.._r and coord_.._c are not going out of bounds
        if (coord_of_neigh_r >= 0 and coord_of_neigh_r < R) and (coord_of_neigh_c >= 0 and coord_of_neigh_c < C):
            # and if they are not, then the coordinates belong to neighbour
            n_list.append(grid[coord_of_neigh_r][coord_of_neigh_c])

    return n_list


def writing_output(grid, population): # writing output to o_grid.txt file
    with open("o_grid.txt", "w+") as f:
            f.write(f"Initial population: {population[0]}\n")
            f.write(f"Final population: {population[-1]}\n")
            f.write(f"Peak population: {max(population)}\n")
            f.write(f"Final grid: \n")
            for line in grid:
                for char in line:
                    f.write(char)
    
                f.write("\n")
    exit()


R, C, G, grid, i_pop = input_grid()

while G > 0:
    grid_copy = [list(row) for row in grid]
    population = [i_pop]
    pop = 0
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            # Making a list of neighbours to count "#" and "."
            n_lst = neighbours_list(grid, i, j, R, C)

            alive = 0
            for n in n_lst:
                if n == "#":
                    alive += 1

            # Conditions for Game of Life
            if c == "#" and (alive > 3 or alive < 2):
                grid_copy[i][j] = "."
            if c == "." and alive == 3:
                grid_copy[i][j] = "#"

    # Counting population in the new grid
    for l in grid_copy:
        for m in l:
            if m == "#":
                pop += 1
    population.append(pop)

    # Again copying back into grid
    grid = [list(row) for row in grid_copy]
    G -= 1

    # sending final grid for output
    if G == 0:
        writing_output(grid, population)
