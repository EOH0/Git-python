if __name__ == "__main__":
    maze = [
        "1111111111",
        "1111101111",
        "1111111111",
        "1111111111",
        "1011111111", 
        "1111111111",
        "1111111111",
        "1111111011",
        "1111111111",
        "1111111111"
    ]
    
    for i in range(len(maze)):
        maze[i] = list(maze[i])

    print(maze)

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            maze[i][j] = int(maze[i][j])
    
    for i in range(1, len(maze)):
        for j in range(1, len(maze[i])):
            if maze[i][j] == 1:
                maze[i][j] = min(int(maze[i-1][j]), int(maze[i][j - 1]), int(maze[i - 1][j - 1]))
    maxVal = 0
    for line in maze:
        maxVal = max(maxVal, max(line))
    
    print(maxVal)