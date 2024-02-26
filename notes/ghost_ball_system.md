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
| `fo` | extended long diamonds of ghost ball (over to the other side of mirroring cushion) |
| `s` | striking diamonds on short cushion (counted from cue ball) |

Basic calculation is $so / fo = s / lc$, therefore $s = (so * lc) / fo$

but $fo = lc + lo$ so it becomes

$$ 
s = (so * lc) / (lc + lo) \\
s = (so * lc) / lc + (so * lc) / lo \\
\therefore s = so + (so * lc) / lo 
$$

Instructions (simplified) are follow
1. Count number of diamonds to object ball `lo`
2. Add up with number of diamonds to cue ball `lc`
3. Find the fraction number `lc / lo`
4. Count number of diamonds (on the other cushion) to cue ball `so`
5. ...