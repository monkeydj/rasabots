"""
This adheres a solution of Day 6 puzzle
- https://adventofcode.com/2023/day/6
"""


def charge(time: int, distance: int):
    pass


times, distances = open("data.in").read().split("\n")
records = list(zip(times.split()[1:], distances.split()[1:]))

for time, distance in records:
    print(f"record: {time} ms / {distance} mm")

answer = 0
print(f"[Total Score Is: {answer}]")
