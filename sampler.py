# What to do!
# Each function below has an instruction on what it should do, and in
# some cases some doctests to illustrate what it should do  but no implementation. Add the implementation,
# you can use any libraries you like (if you've received this test via replit add libraries through
# replit, if not you should provide a requirements.txt / poetry file or similar). If you'd
# like to structure your solution with more than just one function (multiple functions,
# classes etc) feel free to do so. These snippets are small, but please treat them like
# "real" code :) (comments if appropriate, attention to edge cases etc)

import doctest
from pathlib import Path
from dataclasses import dataclass
import datetime

# ---- 1.
# Write a function that accepts two Paths and returns the portion of the first Path that is not
# common with the second, which is to say portion of the first path starting from where the two
# paths diverged.
# p.s. bonus points for thinking of a better name for this function and its parameters
def relative_to_common_base(path1: Path, path2: Path) -> Path:
    """
    >>> relative_to_common_base(Path('/home/daniel/git/ws/py311/test.yaml'), Path('/home/daniel/git/slippers'))
    PosixPath('ws/py311/test.yaml')
    """
    raise NotImplementedError()

# ---- 2.
# Write a function that accepts a string as the first parameter, and a
# list of strings as the second parameter, and returns a string from the
# list that is "most like" the first string. There are some examples of
# what "most like" is below, but the choice of algorithm is yours.
def closest_word(word: str, possibilities: list[str]):
    """
    >>> closest_word('potato', ['potato', 'pumpkin'])
    'potato'
    >>> closest_word('arakeat', ['zzzzzzzz', 'parakeet'])
    'parakeet'
    """
    raise NotImplementedError()


# ---- 3.
# Pretend there is a vehicle traveling along a path. The path is represented
# by a list of x, y points and a timestamp at that point. The vehicle travels
# in straight lines between those points and passes through each point at
# the corresponding timestamp. Given this list of points and timestamps,
# and a time seconds (relative to the first timestamp), write a function
# that returns the instantaneous speed at that timestamp. For simplicity
# return the speed as a string rounded and zero-padded to 2dp.
@dataclass
class PointInTime:
    x: float
    y: float
    ts: datetime.datetime


def speed_at_time(at_time: float | int, path: list[PointInTime]) -> str:
    """
    >>> now = datetime.datetime.now()
    >>> speed_at_time(10, [PointInTime(x=0, y=0, ts=now), PointInTime(x=0, y=10, ts=now + datetime.timedelta(seconds=20))])
    '0.50'
    """
    raise NotImplementedError()


if __name__ == '__main__':
    doctest.testmod(verbose=True, exclude_empty=True)
