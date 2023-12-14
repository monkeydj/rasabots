"""
This adheres a solution of Day 5 puzzle
- https://adventofcode.com/2023/day/5
"""

from sys import argv


def find_dest_pos(src_pos: int, dest: int, src: int, length: int) -> int:
    return dest + (src_pos - src) if src <= src_pos < src + length else src_pos


seeds, *maps = open(argv[1]).read().split('\n\n')
positions = [int(s) for s in seeds.split()[1:]]

print("seeds=", positions)

# ideally, it just follow downstream to find seed's location:
# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location
for categories_map in maps:
    src_to_dest, _, *ranges = categories_map.split()
    # ? if the maps are not in order of downstream

    for i in range(0, len(ranges), 3):
        src, dest, length = [int(n) for n in ranges[i:(i + 3)]]
        positions = [find_dest_pos(p, src, dest, length) for p in positions]

        print(src_to_dest + "=", positions, "/ map=", [src, dest, length])

answer = min(positions)
print(f"[Total Score Is: {answer}]")
