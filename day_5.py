"""
This adheres a solution of Day 5 puzzle
- https://adventofcode.com/2023/day/5
"""

from sys import argv


# ideally, follow this stream to find seed's location:
# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location


def get_src_pos(dest_pos: int, dest: int, src: int, length: int) -> int:
    return src + (dest_pos - dest) if dest <= dest_pos < dest + length else -1


seeds, *maps = open(argv[1]).read().split('\n\n')
seeds = [int(s) for s in seeds.split()[1:]]

print("seeds=", seeds)

for line in maps:
    src_to_dest, _, *ranges = line.split()
    # src, dest = re.search(r'^(\w+)-to-(\w+)', line)
    print(src_to_dest + "=", ranges)

answer = 0
print(f"[Total Score Is: {answer}]")
