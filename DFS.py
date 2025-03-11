from pyamaze import maze, agent, COLOR
from tkinter import Button, LEFT

def DFS(m):
    start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfsPath = {}
    while len(frontier) > 0:
        currCell = frontier.pop()
        if currCell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currCell
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath

m = None
a = None
path = None
create_button = None
solve_button = None

def create_maze():
    global m, a, path, create_button, solve_button
    if m and hasattr(m, '_win') and m._win:
        m._win.destroy()
    m = maze(20, 30)
    m.CreateMaze(loopPercent=100)
    path = DFS(m)
    a = agent(m, footprints=True)

    # Hủy nút bấm cũ nếu tồn tại
    if create_button:
        create_button.destroy()
    if solve_button:
        solve_button.destroy()

    # Tạo nút bấm mới
    create_button = Button(m._win, text="Create Maze", command=create_maze)
    create_button.pack(side=LEFT)

    solve_button = Button(m._win, text="Solve Maze", command=solve_maze)
    solve_button.pack(side=LEFT)
    m.enableWASD(a)
    m.run()

def solve_maze():
    global m, a, path
    if m and hasattr(m, '_win') and m._win:
        m.tracePath({a: path})

if __name__ == '__main__':
    create_maze()