"""
This adheres a solution of Day 6 puzzle
- https://adventofcode.com/2023/day/6
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


times, distances = open("data.in").read().split("\n")
records = list(zip(times.split()[1:], distances.split()[1:]))

answer = 0
for time, distance in records:
    print(f"record: {time} ms / {distance} mm")

    beat_it = outrun(int(time), int(distance))
    if beat_it:
        answer = (answer or 1) * beat_it

print(f"[Total Score Is: {answer}]")
