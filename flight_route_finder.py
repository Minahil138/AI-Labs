
flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": []
}


def ucs_cheapest_route(graph, start, goal):
    queue = [(0, [start])]
    visited = []
    explored = 0

    while queue:
        queue.sort(key=lambda item: item[0])
        cost, path = queue.pop(0)
        city = path[-1]

        if city in visited:
            continue

        visited.append(city)
        explored = explored + 1

        print("Exploring path:", path, "| Cost:", cost)

        if city == goal:
            return path, cost, explored

        for next_city, price in graph.get(city, []):
            if next_city not in visited:
                new_path = path + [next_city]
                new_cost = cost + price
                queue.append((new_cost, new_path))

    return None, None, explored


route, total_cost, explored_count = ucs_cheapest_route(
    flights, "Islamabad", "Quetta"
)

if route:
    print("Cheapest route:", route)
    print("Total ticket cost:", total_cost)
    print("Total routes explored:", explored_count)
else:
    print("No route found.")
