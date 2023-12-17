"""
This adheres a solution of Day 6 puzzle Part Two
- https://adventofcode.com/2023/day/6#part2
"""


def outrun(time: int, distance: int) -> int:
    beats, speed = 0, 0
    # speed increases by one millimeter per millisecond
    # speed = 0 or eq time cannot make a run, thus don't beat it
    while speed < time:
        speed += 1
        if speed * (time - speed) > distance:
            beats += 1

    return beats


def rekern(input_line: str) -> str:
    return int(input_line.replace(" ", "").split(":")[1])


times, distances = open("data.in").read().split("\n")
time, distance = (rekern(times), rekern(distances))

print(f"record: {time} ms / {distance} mm")

answer = outrun(int(time), int(distance))
# another interesting solution:
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/6_binary_search.py#L21

print(f"[Total Score Is: {answer}]")
