"""Implement solutions to the Traversable Path problem.

A path shall be represented by a list of positive integers (or 0), where a 0 means:
no further advance, or stop. A positive integer means: advance one step, or more steps,
up to the number given. We start at step 0. Let's call such an advancement a jump.

A step can be seen as the index into the list that represents the path. We start at index 0
representing step 0, and advance until we reach a point beyond the last index.

Path example: [1, 3, 0, 0, 1]

A path is traversable, if there is at least one sequence of jumps through the path, that leads
at least one step after its end.

A path is not traversable, when there is no jump sequence available that leads beyond its end.
"""


def is_traversable_path(path: list[int]) -> bool:
    """path must be a list of non-negative integers, including 0"""
    advancement = 0
    for step, max_advance in enumerate(path):
        if max_advance < 0:
            raise ValueError('advancements may not be negative')
        if step > advancement:
            break
        advancement = max(advancement, step + max_advance)
    return advancement >= len(path)


# last line of code
