# 1=wall,0=path,5=start,6=end
# for explored 8 = true
# for ideal_path 999 is the path

import numpy as np
import copy
import tkinter as tk

#Default maze
maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

blank_maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

example_maze = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 6, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
        [0, 5, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]]

traversed = copy.deepcopy(maze)
fcosts = copy.deepcopy(maze)
came_from = copy.deepcopy(maze)
explored = copy.deepcopy(maze)
ideal_path = copy.deepcopy(maze)

solvable = False
goal = None
start = None
checked = False

mode = "barrier"
position = [0, 0]


def is_solvable():
    global maze, goal, start, checked
    checked = True
    for y1 in range(len(maze)):
        for x1 in range(len(maze[0])):
            if maze[y1][x1] == 6:
                goal = [x1, y1]

    for y2 in range(len(maze)):
        for x2 in range(len(maze[0])):
            if maze[y2][x2] == 5:
                start = [x2, y2]
                traverse_maze(x2, y2)
                if solvable:
                    return True
                return False


# add diagonal to this
def traverse_maze(x, y):
    global maze, traversed, solvable, goal
    if traversed[y][x] != 5 and traversed[y][x] != 6:
        traversed[y][x] = 2
    if x == goal[0] and y == goal[1]:
        solvable = True
        return
    if x > 0 and traversed[y][x - 1] in (0, 6):
        traverse_maze(x - 1, y)
    if x < len(maze[0]) - 1 and traversed[y][x + 1] in (0, 6):
        traverse_maze(x + 1, y)
    if y < len(maze) - 1 and traversed[y + 1][x] in (0, 6):
        traverse_maze(x, y + 1)
    if y > 0 and traversed[y - 1][x] in (0, 6):
        traverse_maze(x, y - 1)

    if x > 0 and y < len(maze) - 1 and traversed[y + 1][x - 1] in (0, 6):
        traverse_maze(x - 1, y + 1)
    if x < len(maze[0]) - 1 and y < len(maze) -1 and traversed[y + 1][x + 1] in (0, 6):
        traverse_maze(x + 1, y + 1)
    if x > 0 and y > 0 and traversed[y - 1][x - 1] in (0, 6):
        traverse_maze(x - 1, y - 1)
    if x < len(maze[0]) - 1 and y > 0 and traversed[y - 1][x + 1] in (0, 6):
        traverse_maze(x + 1, y - 1)


def distance(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx > dy:
        diagonal = dy
        straight = dx - dy
    else:
        diagonal = dx
        straight = dy - dx
    return 14 * diagonal + 10 * straight


# distance from start
def gcost(x, y):
    global start
    return distance(x, y, start[0], start[1])


# distance from end
def hcost(x, y):
    global goal
    return distance(x, y, goal[0], goal[1])


def fcost(x, y):
    return gcost(x, y) + hcost(x, y)


def calculate_surroundings(x0, y0):
    global fcosts, came_from, explored, maze
    for y in range(-1, 2):
        for x in range(-1, 2):
            if 0 <= x + x0 < len(maze[0]) and 0 <= y + y0 < len(maze):
                if (not (x == y == 0)) and maze[y0 + y][x0 + x] != 1 and maze[y0 + y][x0 + x] != 5:
                    if 9 < fcost(x0 + x, y0 + y) < fcosts[y0 + y][x0 + x] or explored[y0 + y][x0 + x] != 8:
                        fcosts[y0 + y][x0 + x] = fcost(x0 + x, y0 + y)
                        if x == -1 and y == -1:
                            came_from[y0 + y][x0 + x] = 1
                        if x == 0 and y == -1:
                            came_from[y0 + y][x0 + x] = 2
                        if x == 1 and y == -1:
                            came_from[y0 + y][x0 + x] = 3
                        if x == 1 and y == 0:
                            came_from[y0 + y][x0 + x] = 4
                        if x == 1 and y == 1:
                            came_from[y0 + y][x0 + x] = 5
                        if x == 0 and y == 1:
                            came_from[y0 + y][x0 + x] = 6
                        if x == -1 and y == 1:
                            came_from[y0 + y][x0 + x] = 7
                        if x == -1 and y == 0:
                            came_from[y0 + y][x0 + x] = 8
    explored[y0][x0] = 8


def path():
    global maze, goal, start, fcosts, ideal_path, came_from, explored
    path_found = False
    path_traced = False
    if is_solvable():
        calculate_surroundings(start[0], start[1])
        smallest_fcost = [99999999, 0, 0]
        while not path_found:
            for y in range(len(maze)):
                for x in range(len(maze[0])):
                    if 9 < fcosts[y][x] < smallest_fcost[0] and explored[y][x] != 8:
                        smallest_fcost = [fcost(x, y), x, y]
            calculate_surroundings(smallest_fcost[1], smallest_fcost[2])
            if maze[smallest_fcost[2]][smallest_fcost[1]] == 6:
                path_found = True
                position = [goal[1], goal[0]]  # y,x
                while not path_traced:
                    cycle = 0
                    if maze[position[0]][position[1]] == 5:
                        path_traced = True
                    if maze[position[0]][position[1]] != 6:
                        ideal_path[position[0]][position[1]] = 999
                    if came_from[position[0]][position[1]] == 1 and cycle == 0:
                        position[1] += 1
                        position[0] += 1
                        cycle = 1
                    if came_from[position[0]][position[1]] == 2 and cycle == 0:
                        position[0] += 1
                        cycle = 1
                    if came_from[position[0]][position[1]] == 3 and cycle == 0:
                        position[1] -= 1
                        position[0] += 1
                        cycle = 1
                    if came_from[position[0]][position[1]] == 4 and cycle == 0:
                        position[1] -= 1
                        cycle = 1
                    if came_from[position[0]][position[1]] == 5 and cycle == 0:
                        position[1] -= 1
                        position[0] -= 1
                        cycle = 1
                    if came_from[position[0]][position[1]] == 6 and cycle == 0:
                        position[0] -= 1
                        cycle = 1
                    if came_from[position[0]][position[1]] == 7 and cycle == 0:
                        position[1] += 1
                        position[0] -= 1
                        cycle = 1
                    if came_from[position[0]][position[1]] == 8 and cycle == 0:
                        position[1] += 1
                        cycle = 1
            smallest_fcost = [99999999, 0, 0]
    else:
        print("Maze is not solvable")


window = tk.Tk()
window.title("Maze Solver")


def load_window():
    try:
        pass
        #window.delete("all")
    finally:
        text1 = tk.Label(window, text="Maze\nSolver", font=("Helvetica", 50))
        text1.place(x=1670, y=50)

        blank = tk.Label(window, width="8", height="4", bg="gray94")
        blank.grid(row=5, column=26)

        barriers = tk.Label(window, width="26", height="4", bg="black")
        barriers.grid(row=5, column=27)

        endpoint = tk.Label(window, width="26", height="4", bg="red")
        endpoint.grid(row=7, column=27)

        start = tk.Label(window, width="26", height="4", bg="green")
        start.grid(row=9, column=27)

        example = tk.Label(window, width="26", height="4", bg="orange")
        example.grid(row=11, column=27)

        clear = tk.Label(window, width="26", height="4", bg="purple")
        clear.grid(row=13, column=27)

        text2 = tk.Label(window, text="Barriers", font=("Helvetica", 26), foreground="white", background="black")
        text2.place(x=1705, y=340)

        text3 = tk.Label(window, text="End", font=("Helvetica", 26), foreground="white", background="red")
        text3.place(x=1735, y=470)

        text4 = tk.Label(window, text="Start", font=("Helvetica", 26), foreground="white", background="green")
        text4.place(x=1729, y=602)

        text5 = tk.Label(window, text="Example", font=("Helvetica", 26), foreground="white", background="orange")
        text5.place(x=1704, y=735)

        text6 = tk.Label(window, text="Clear", font=("Helvetica", 26), foreground="white", background="purple")
        text6.place(x=1724, y=867)

        if not solvable and checked:
            errortext = tk.Label(window, text="No Solution", font=("Helvetica", 26), foreground="red")
            errortext.place(x=1685, y=200)

        for y in range(16):
            for x in range(26):
                if maze[y][x] == 0:
                    color = "white"
                if maze[y][x] == 1:
                    color = "black"
                if maze[y][x] == 6:
                    color = "red"
                if ideal_path[y][x] == 999:
                    color = "blue"
                if maze[y][x] == 5:
                    color = "green"
                label = tk.Label(window, width="8", height="4", bg=color, relief="solid")
                label.grid(row=y, column=x)

        window.bind("<Button-1>", click)

        window.mainloop()


def motion(event):
    global position
    position[0] = window.winfo_pointerx() - window.winfo_rootx()
    position[1] = window.winfo_pointery() - window.winfo_rooty()


window.bind("<Motion>", motion)


def click(event):
    global maze, mode, position, example_maze, blank_maze
    print(position)
    non_changing = False
    if 1675 < position[0] < 1860 and 330 < position[1] < 395:
        mode = "barrier"
        print(1)
    elif 1675 < position[0] < 1860 and 460 < position[1] < 525:
        mode = "end"
        print(2)
    elif 1675 < position[0] < 1860 and 617 < position[1] < 680:
        mode = "start"
        print(3)
    elif 1675 < position[0] < 1860 and 730 < position[1] < 790:
        maze = copy.deepcopy(example_maze)
        non_changing = True
        print(4)
    elif 1675 < position[0] < 1860 and 855 < position[1] < 920:
        maze = copy.deepcopy(blank_maze)
        non_changing = True
        print(5)
    if 0 < position[0] < 1610 and 0 < position[1] < 1050 or non_changing:
        global traversed, fcosts, came_from, explored, ideal_path, solvable, goal, start
        traversed = copy.deepcopy(maze)
        fcosts = copy.deepcopy(maze)
        came_from = copy.deepcopy(maze)
        explored = copy.deepcopy(maze)
        ideal_path = copy.deepcopy(maze)
        solvable = False
        goal = None
        start = None

        if not non_changing:
            grid_position = [position[0] // 62, position[1] // 65]
            print("grid pos " + str(grid_position))

            if mode == "barrier" and maze[grid_position[1]][grid_position[0]] != 5 and maze[grid_position[1]][grid_position[0]] != 6:
                print(maze[grid_position[1]][grid_position[0]])
                if maze[grid_position[1]][grid_position[0]] == 0:
                    maze[grid_position[1]][grid_position[0]] = 1
                else:
                    maze[grid_position[1]][grid_position[0]] = 0
            elif mode == "start" and maze[grid_position[1]][grid_position[0]] != 5 and maze[grid_position[1]][grid_position[0]] != 6:
                for y1 in range(len(maze)):
                    for x1 in range(len(maze[0])):
                        if maze[y1][x1] == 5:
                            maze[y1][x1] = 0
                maze[grid_position[1]][grid_position[0]] = 5
            elif mode == "end" and maze[grid_position[1]][grid_position[0]] != 5 and maze[grid_position[1]][grid_position[0]] != 6:
                for y1 in range(len(maze)):
                    for x1 in range(len(maze[0])):
                        if maze[y1][x1] == 6:
                            maze[y1][x1] = 0
                maze[grid_position[1]][grid_position[0]] = 6
        path()
        load_window()
        for y in range(16):
            for x in range(26):
                if ideal_path[y][x] == 999:
                    color = "blue"
                label = tk.Label(window, width="8", height="4", bg=color, relief="solid")
                label.grid(row=y, column=x)


load_window()