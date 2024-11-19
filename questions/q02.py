import numpy as np

from base import Question

question = Question(
    i=2,
    t="X @ Y = Z",
    s="Multiplication ( left <- lying down ; right -> standing up )",
    f=np.dot,
    X=np.ones((3, 1), dtype=int),
    Y=np.ones((1, 3), dtype=int),
    a=1 * np.ones((1, 1), dtype=int),
    b=3 * np.ones((3, 1), dtype=int),
    c=1 * np.ones((3, 3), dtype=int),
    d=3 * np.ones((3, 3), dtype=int),
    correct="c",
)
question.print()

print(f"{question.correct=}")
question.verify()
