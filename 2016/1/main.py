import os
from collections import deque


def manhattan_dist(p, q):
    return abs(p['x'] - q['x']) + abs(p['y'] - q['y'])

def blocks_away(pos):
    return manhattan_dist({ 'x':0, 'y':0 }, pos)

def travel(path, part2=False):
    pos = { 'x':0, 'y':0 }
    compass = deque(['N', 'E', 'S', 'W'])

    if part2:
        visited = {(0, 0)}

    for step in path.split(', '):
        # extract parts of string
        lr = step[0]
        blocks = int(step[1:])

        # turn
        if lr == 'R':
            compass.rotate(-1)
        elif lr == 'L':
            compass.rotate(1)

        dir = compass[0]

        # increment by 1 so we can track each visited grid point for part 2
        for i in range(blocks):
            if dir == 'N':
                pos['y'] += 1
            elif dir == 'E':
                pos['x'] += 1
            elif dir == 'S':
                pos['y'] -= 1
            elif dir == 'W':
                pos['x'] -= 1

            if part2:
                visiting = (pos['x'], pos['y'])

                # part 2, return the current pos if we've been here before
                if visiting in visited:
                    return pos
                else:
                    visited.add(visiting)

    return pos


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        path = f.readline().strip()

    print(f'Part 1 Solution: {blocks_away(travel(path))}')
    print(f'Part 2 Solution: {blocks_away(travel(path, True))}')