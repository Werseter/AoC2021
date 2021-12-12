from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(unsafe_hash=True)
class Node:
    name: str
    neighbours: set[Node] = field(default_factory=set, hash=False, repr=False)


def generate_routes(route: tuple[Node, ...], visited_small: set[Node]) -> set[tuple[Node, ...]]:
    new_routes = set()
    for subnode in ([x for x in route[-1].neighbours if x.name != 'start'] if route[-1].name != 'end' else []):
        if subnode.name.islower() and subnode in visited_small:
            continue
        new_routes.update(generate_routes(route + (subnode,),
                                          visited_small | ({subnode} if subnode.name.islower() else set())))
    return new_routes or ({route} if route[-1].name == 'end' else set())


with open('input.txt') as fp:
    data = [x.strip().partition('-')[::2] for x in fp.readlines()]
nodes: dict[str, Node] = {}
for a, b in data:
    nodes[a] = nodes.get(a) or Node(a)
    nodes[b] = nodes.get(b) or Node(b)
    nodes[a].neighbours.add(nodes[b])
    nodes[b].neighbours.add(nodes[a])
routes = generate_routes((nodes['start'],), set())
print(len(routes))
