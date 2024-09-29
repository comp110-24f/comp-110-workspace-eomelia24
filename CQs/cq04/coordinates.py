"""CQ04 Coordinates: Give coordinates of two strings."""


__author__ = "730574218"


def get_coords(xs: str, ys: str) -> None:
    """Find all combinations of coordinates from two strings."""
    xs_idx: int = 0 # xs and ys each need their own index variable.
    ys_idx: int = 0
    while xs_idx < len(xs):
        while ys_idx < len(ys):
            print("(" + xs[xs_idx] + "+" + ys[ys_idx] + ")")
            ys_idx += 1
        xs_idx += 1
        ys_idx = 0 # ys_idx has to be reset to zero to go through each character again.
