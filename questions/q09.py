import numpy as np

from base import Question

question = Question(
    i=1,
    t="X @ Y = Z",
    s="Multiplication ( left <- lying down ; right -> standing up )",
    f=np.dot,
    X=np.ones((5, 2), dtype=int),
    Y=np.ones((2, 3), dtype=int),
    a=1 * np.ones((5, 3), dtype=int),
    b=1 * np.ones((3, 5), dtype=int),
    c=2 * np.ones((5, 3), dtype=int),
    d=2 * np.ones((3, 5), dtype=int),
    correct="c",
)
question.X[0, :] = 0
question.a[0, :] = 0
question.b[:, 0] = 0
question.c[0, :] = 0
question.d[:, 0] = 0
question.print()

print(f"{question.correct=}")
question.verify()
