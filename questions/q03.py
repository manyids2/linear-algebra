import numpy as np

from base import Question

question = Question(
    i=1,
    t="X @ Y = Z",
    s="Multiplication ( left <- lying down ; right -> standing up )",
    f=np.dot,
    X=np.ones((1, 3), dtype=int),
    Y=np.ones((3, 1), dtype=int),
    a=1 * np.ones((1, 3), dtype=int),
    b=1 * np.ones((3, 1), dtype=int),
    c=2 * np.ones((1, 1), dtype=int),
    d=1 * np.ones((3, 3), dtype=int),
    correct="c",
)
question.Y[0, 0] = 0
question.b[0, 0] = 0
question.d[0, :] = 0
question.print()

print(f"{question.correct=}")
question.verify()
