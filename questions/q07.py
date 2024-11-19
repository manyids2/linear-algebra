import numpy as np

from base import Question

question = Question(
    i=1,
    t="X @ Y = Z",
    s="Multiplication ( left <- lying down ; right -> standing up )",
    f=np.dot,
    X=np.ones((3, 2), dtype=int),
    Y=np.ones((2, 3), dtype=int),
    a=1 * np.ones((3, 3), dtype=int),
    b=1 * np.ones((2, 2), dtype=int),
    c=2 * np.ones((3, 3), dtype=int),
    d=1 * np.ones((3, 3), dtype=int),
    correct="c",
)
question.print()

print(f"{question.correct=}")
question.verify()
