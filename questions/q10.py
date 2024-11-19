import numpy as np

from base import Question

question = Question(
    i=1,
    t="X @ Y = Z",
    s="Multiplication ( left <- lying down ; right -> standing up )",
    f=np.dot,
    X=np.ones((4, 2), dtype=int),
    Y=np.ones((2, 3), dtype=int),
    a=2 * np.ones((4, 3), dtype=int),
    b=2 * np.ones((4, 3), dtype=int),
    c=2 * np.ones((4, 3), dtype=int),
    d=2 * np.ones((4, 3), dtype=int),
    correct="c",
)
question.X[0, 0] = 0
question.a[0, :] = 0
question.b[:, 0] = 0
question.c[0, :] = 1
question.d[:, 0] = 1
question.print()

print(f"{question.correct=}")
question.verify()
