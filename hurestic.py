import random

class Branch:
    """Represents a branch of City Bank in the map."""
    def __init__(self, branch_id, name, geo_location):
        self.branch_id = branch_id
        self.name = name
        self.geo_location = geo_location
        self.neighbors = []
        
class Map:
    """Represents a map of City Bank branches."""
    def __init__(self):
        # Adjacent Branch List
        self.adj_list = {}

    def add_branch(self, branch_id, name, geo_location):
        # Create a new branch add it to the adjacent branch list
        branch = Branch(branch_id, name, geo_location)
        self.adj_list[branch_id] = branch

    def add_edge(self, branch_id1, branch_id2, distance):
        fuel_cost = random.randint(1, 10)  # Random fuel cost between 1 and 10
        # Add the edge between branch_id1 and branch_id2
        self.adj_list[branch_id1].neighbors.append((branch_id2, distance, fuel_cost))
        self.adj_list[branch_id2].neighbors.append((branch_id1, distance, fuel_cost))

    def tsp_nearest_neighbor(self, start_branch_id):
        """Heuristic for solving the TSP problem using nearest neighbor."""
        unvisited = set(self.adj_list.keys())
        current_branch_id = start_branch_id
        path = [self.adj_list[current_branch_id]]
        total_distance = 0
        total_fuel_cost = 0

        unvisited.remove(current_branch_id)

        while unvisited:
            nearest_neighbor_id = None
            nearest_neighbor_distance = float('inf')
            nearest_neighbor_fuel_cost = 0

            for neighbor_id, distance, fuel_cost in self.adj_list[current_branch_id].neighbors:
                if distance < nearest_neighbor_distance and neighbor_id in unvisited:
                    nearest_neighbor_id = neighbor_id
                    nearest_neighbor_distance = distance
                    nearest_neighbor_fuel_cost = fuel_cost

            current_branch_id = nearest_neighbor_id
            path.append(self.adj_list[current_branch_id])
            unvisited.remove(current_branch_id)

            total_distance += nearest_neighbor_distance
            total_fuel_cost += nearest_neighbor_fuel_cost

        path.append(f"Total Distance: {total_distance}")
        path.append(f"Total Fuel Cost: {total_fuel_cost}")

        return path


def main():
    # Create a map of City Bank branches
    g = Map()
    g.add_branch(1, "Uttara Branch", {"lat": 23.8728568, "long": 90.3984184})
    g.add_branch(2, "City Bank Airport", {"lat": 23.8513998, "long": 90.3944536})
    g.add_branch(3, "City Bank Nikunja", {"lat": 23.8330429, "long": 90.4092871})
    g.add_branch(4, "City Bank Beside Uttara Diagnostic", {"lat": 23.8679743, "long": 90.3840879})
    g.add_branch(5, "City Bank Mirpur 12", {"lat": 23.8248293, "long": 90.3551134})
    g.add_branch(6, "City Bank Le Meridien", {"lat": 23.827149, "long": 90.4106238})
    g.add_branch(7, "City Bank Shaheed Sarani", {"lat": 23.8629078, "long": 90.3816318})
    g.add_branch(8, "City Bank Narayanganj", {"lat": 23.8673789, "long": 90.429412})
    g.add_branch(9, "City Bank Pallabi", {"lat": 23.8248938, "long": 90.3549467})
    g.add_branch(10, "City Bank JFP", {"lat": 23.813316, "long": 90.4147498})

    # Add random distances between branches and fuel costs
    for i in range(1, 11):
        for j in range(i + 1, 11):
            distance = random.randint(1, 10)
            g.add_edge(i, j, distance)

    start_branch_id = 1  # Start from City Bank Uttara
    tsp_path = g.tsp_nearest_neighbor(start_branch_id)

    print("Huerestic Path:")
    for item in tsp_path:
        if isinstance(item, str):
            print(item)
        else:
            print(item.name, item.geo_location)

if __name__ == '__main__':
    main()
