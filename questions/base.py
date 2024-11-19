from dataclasses import dataclass
from typing import Callable

import numpy as np

WIDTH = 80
COLWIDTH = 20
MARGIN = 10


def sep(width: int = WIDTH):
    print(f"\n{'-' * width}\n")


def print_x(x: np.ndarray) -> str:
    return "\n".join([" ".join([str(y) for y in x[i, :]]) for i in range(x.shape[0])])


def join(
    x: list[str],
    y: list[str],
    border: str = " ",
    width: int = COLWIDTH,
    margin: int = MARGIN,
) -> str:
    n = min(len(x), len(y))
    lines = []
    m = " " * margin
    for i in range(n):
        pad_x = " " * (width - len(x[i]))
        pad_y = " " * (width - len(y[i]))
        z = f"{m}{x[i]}{pad_x}{border}{m}{y[i]}{pad_y}"
        lines.append(z)
    if len(x) > len(y):
        for i in range(n, len(x)):
            pad_x = " " * (width - len(x[i]))
            pad_y = " " * width
            z = f"{m}{x[i]}{pad_x}{border}{m}{pad_y}"
            lines.append(z)
    else:
        for i in range(n, len(y)):
            pad_x = " " * width
            pad_y = " " * (width - len(y[i]))
            z = f"{m}{pad_x}{border}{m}{y[i]}{pad_y}"
            lines.append(z)

    return "\n".join(lines)


@dataclass()
class Question:
    i: int  # index
    t: str  # title
    s: str  # summary
    f: Callable  # f(X, Y) = Z
    X: np.ndarray  # Input X
    Y: np.ndarray  # Input Y

    # Answers
    a: np.ndarray
    b: np.ndarray
    c: np.ndarray
    d: np.ndarray
    correct: str

    def verify(self):
        print(self.f(self.X, self.Y))

    def print(self):
        sep()
        print(f"      {self.t}\n")
        print(f"        {self.s}")
        sep()
        print(
            join(
                f"X: {self.X.shape}\n\n{print_x(self.X)}\n".split("\n"),
                f"Y: {self.Y.shape}\n\n{print_x(self.Y)}\n".split("\n"),
                border="     ",
            )
        )
        sep()
        print(
            join(
                f"(a): {self.a.shape}\n\n{print_x(self.a)}\n\n".split("\n"),
                f"(b): {self.b.shape}\n\n{print_x(self.b)}\n\n".split("\n"),
                border="     ",
            )
        )
        print(
            join(
                f"(c): {self.c.shape}\n\n{print_x(self.c)}\n\n".split("\n"),
                f"(d): {self.d.shape}\n\n{print_x(self.d)}\n\n".split("\n"),
                border="     ",
            )
        )
        print(join(str("(e):\n\n None of the above \n\n").split("\n"), ["", ""]))
        sep()
