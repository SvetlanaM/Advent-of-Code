from collections import defaultdict
from typing import DefaultDict, Dict

graph = defaultdict(dict)
total = []

def create_graph() -> DefaultDict[str, Dict[str, int]]:
  for line in open("2015/day09/input.txt"):
    city1, city2, distance = line.replace("to", "").replace("=", "").split()
    graph[city1][city2], graph[city2][city1] = [int(distance)] * 2
  return graph

create_graph()

def calculate_path(cities:Dict[str, int], selected_city: str, visited: list[str], calculated_path: int = 0) -> None:
    if set(cities[selected_city]).issubset(visited):
        total.append(calculated_path)
        return

    for city in cities[selected_city]:
      if city not in visited:
          visited.append(selected_city)
          calculate_path(cities, city, visited, calculated_path + cities[selected_city][city])
          visited.pop()

for city in graph:
  calculate_path(graph, city, [])

print("Part 1:", min(total))
print("Part 2:", max(total))
  


