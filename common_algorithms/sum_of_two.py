"""Sum Of Two In A List

Given a list of integral numbers, positive or negative, including 0, and another number, we call
'target', check if the target can be created as the sum of two numbers from the list.

The list shall be sorted in ascending order, before doing the check.

Start with the naive solution (i.e. check all possible combinations), and at least one faster
approach.
"""
from itertools import combinations
from numbers import Integral
from typing import Iterable


class SumOfTwo:

    def __init__(self, numbers: Iterable[Integral], target: Integral) -> None:
        self.numbers = sorted(numbers)
        self.target = target

    def __str__(self):
        return 'check if {} is in {}'.format(self.target, self.numbers)

    def naive(self) -> bool:
        """This solution has worst case time complexity of O(n^2)."""
        for c in combinations(self.numbers, 2):
            if self.target == sum(c):
                return True
        return False

    def memoizing(self) -> bool:
        """Strategy: we remember number minus target for each number seen.
        If the number we see is already in the differences memory, we have found one solution.
        Since the first solution we find do the trick, we are done. If we do not find a
        solution, and there are no numbers left, we know we are done with target not feasible.

        This solution has worst case time complexity of O(n), and may worst case double the
        memory usage, because of the memo set.
        """
        memory = set()
        for x in self.numbers:
            if x in memory:
                return True
            else:
                memory.add(self.target - x)
        return False

    def iterative(self) -> bool:
        """Strategy: since the numbers are sorted in ascending order, we can start with the
        least and the biggest element ([0] and [-1]). If the sum of both is below the target, we
        take the next higher value from the lower end of the numbers list. If the sum is
        above, we take the next lower from the high end of our list. If we directly hit the
        point, we return true. If we do not find a sum-of-two match, we return false.

        The worst case time complexity of this approach is O(n).

        This approach requires more code than the others, and may be ost difficult to
        understand.
        """
        numbers = self.numbers
        target = self.target
        low = 0
        high = len(numbers) - 1
        while low < high:
            x = numbers[low] + numbers[high]
            if target == x:
                return True
            else:
                low += 1 if target > x else 0
                high -= 1 if target < x else 0
        return False


if __name__ == '__main__':
    """Quick test."""
    numbers = [-2, 3, 4, 11, 2, 7]
    target = 0
    checker = SumOfTwo(numbers, target)
    print(checker, '--- naive answer =', checker.naive())
    print(checker, '--- answer with memo =', checker.memoizing())
    print(checker, '--- iterative answer =', checker.iterative())

# last line of code
