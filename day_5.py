"""
This adheres a solution of Day 5 puzzle
- https://adventofcode.com/2023/day/5
"""

from sys import argv


def find_src_pos(dest_pos: int, src: int, dest: int, length: int) -> int:
    return src + (dest_pos - dest) if dest <= dest_pos < dest + length else dest_pos


seeds, *maps = open(argv[1]).read().split('\n\n')
positions = [int(s) for s in seeds.split()[1:]]

print("seeds=", positions)

# ideally, it just follow downstream to find seed's location:
# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location
for categories_map in maps:
    src_to_dest, _, *ranges = categories_map.split()
    # ? if the maps are not in order of downstream

    for i in range(0, len(ranges), 3):
        src_dest_range = [int(n) for n in ranges[i:(i + 3)]]
        positions = [find_src_pos(p, *src_dest_range) for p in positions]

        print(src_to_dest + "=", positions, "/", src_dest_range)

answer = min(positions)
print(f"[Total Score Is: {answer}]")
