
maze = {
    "Entrance": ["Hall1", "Hall2"],
    "Hall1": ["Room1"],
    "Hall2": ["Room2", "Trap"],
    "Room1": [],
    "Room2": ["Exit"],
    "Trap": [],
    "Exit": [],
    "SecretRoom":[]
}


def dfs_can_reach(maze, start, exit_room):
    visited = []

    def dfs(room):
        if room in visited:
            return False

        visited.append(room)

        if room == exit_room:
            return True

        for next_room in maze[room]:
            if dfs(next_room):
                return True

        return False

    result = dfs(start)
    print("Visit order:", visited)
    return result


print(
    "Can reach Exit from Entrance?",
    dfs_can_reach(maze, "Entrance", "Exit")
)
