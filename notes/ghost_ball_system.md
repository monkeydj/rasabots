## Ghost ball extended
https://youtu.be/jmI1ZiuOqUs?si=rtvaqUtwHjzHnTog

**Prerequisite**
- towards same short cushion
- effect 0

**Formulation**

| Variable | Description |
| ----------- | ----------- |
| `lc` | long diamonds of cue ball |
| `lo` | long diamonds of object ball |
| `so` | short diamonds between cue ball and object ball |
| `fo` | extended long diamonds of ghost ball |
| `s` | striking diamonds on short cushion (counted from cue ball) |

Basic calculation is $so / fo = s / lc$, therefore $s = (so * lc) / fo$

but $fo = lc + lo$ so it becomes

$$ 
s = (so * lc) / (lc + lo) \\
s = (so * lc) / lc + (so * lc) / lo \\
\therefore s = so + (so * lc) / lo 
$$
