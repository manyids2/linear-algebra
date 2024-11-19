import numpy as np

from base import Question

question = Question(
    i=1,
    t="X @ Y = Z",
    s="Multiplication ( left <- lying down ; right -> standing up )",
    f=np.dot,
    X=np.ones((1, 4), dtype=int),
    Y=np.ones((4, 3), dtype=int),
    a=1 * np.ones((1, 3), dtype=int),
    b=1 * np.ones((1, 3), dtype=int),
    c=3 * np.ones((1, 3), dtype=int),
    d=2 * np.ones((1, 3), dtype=int),
    correct="c",
)
question.X[0, 0] = 0
question.Y[0, 0] = 5
question.Y[0, 1] = 6
question.Y[0, 2] = 7
question.b[:, 0] = 0
question.d[:, 0] = 1
question.print()

print(f"{question.correct=}")
question.verify()
