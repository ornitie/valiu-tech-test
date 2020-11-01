moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, 2]]


class casilla:
    def __init__(self, x, y, distancia):
        self.x = x
        self.y = y
        self.distancia = distancia


def caballo(inicio, objetivo):
    queue = []

    queue.append(casilla(inicio[0], inicio[1], 0))

    visited = set()

    visited.add(tuple([inicio[0], inicio[1]]))

    while(len(queue) > 0):
        next_pos = queue[0]
        queue.pop(0)

        if(next_pos.x == objetivo[0] and next_pos.y == objetivo[1]):
            return next_pos.distancia

        for move in moves:
            x = next_pos.x + move[0]
            y = next_pos.y + move[1]

            if((x, y) not in visited):
                visited.add(tuple([x, y]))
                queue.append(casilla(x, y, next_pos.distancia + 1))


if __name__ == "__main__":
    knightpos = [-5, -5]
    targetpos = [5, 5]
    caballo(knightpos, targetpos)
