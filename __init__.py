#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
conway's game of life
======================

Specification
---------------

    The universe of the Game of Life is an infinite two-dimensional orthogonal
    grid of square cells, each of which is in one of two possible states,
    alive or dead.

    Every cell interacts with its eight neighbours, which are the cells that
    are horizontally, vertically, or diagonally adjacent.

    At each step in time, the following transitions occur:

    - Any live cell with fewer than two live neighbours dies,
      as if caused by under-population.

    - Any live cell with two or three live neighbours lives on
      to the next generation.

    - Any live cell with more than three live neighbours dies,
      as if by overcrowding.

    - Any dead cell with exactly three live neighbours becomes a live cell,
      as if by reproduction.

    The initial pattern constitutes the **seed** of the system.

    The first generation is created by applying the above rules simultaneously
    to every cell in the seed—births and deaths occur simultaneously,
    and the discrete moment at which this happens
    is sometimes called a tick
    (in other words, each generation is a pure function of the preceding one).

    The rules continue to be applied repeatedly to create further generations.

    -- https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

    Implementation
    ----------------

    Sliding evaluative ruleset
        if 1 and len(neigborset) < 2            --> 0, '<2'
        elif 1 and len(neigborset) in (2,3)     --> 1, '=2'|'=3'
        elif 1 and len(neighborset) > 3         --> 0, '>3'

        if 0 and len(neighborset) > 3           --> 1, '>3'

    Multidimensional *infinite* matrix
        env=defaultdict(0)
        env[(x,y)]

    Neighbor cell count
        cell (x,y)

        ----- | ----- | -----
        ----- | (x,y) | -----
        ----- | ----- | -----

        (-1, -1) | (0, -1) | (1, -1)
        ---------|---------|--------
        (-1,  0) | (0,  0) | (1,  0)
        ---------|---------|--------
        (-1,  1) | (0,  1) | (1,  1)

        (-1, -1)
        ( 0, -1)
        ( 1, -1)

        (-1,  0)
        ( 0,  0) *
        ( 1,  0)

        (-1, 1)
        ( 0, 1)
        ( 1, 1)

    morning
    --------
    define:infinite
     - origin? signed ints!?
     - display clipping || wrap around
     - growth bounds
       - max = h+2,w+2 (+1 all around) ?
       - min = 0,0
     - toroidal array approximations? radians?

"""

from collections import namedtuple, OrderedDict
import itertools
import copy
import random
import sys
import logging
from environments import still, to_dict

try:
    import cStringIO as StringIO
except ImportError:
    try:
        import StringIO as StringIO
    except ImportError:
        from io import StringIO

class Action(namedtuple('Action', ('new_state', 'alive_count', 'reason'))):
    pass

class Point(namedtuple('Point', ('x', 'y'))):
    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)


class Env(OrderedDict):
    DEFAULT_VALUE = 0
    TRANSFORMS_TABLE =  [Point(-1, -1), Point(0, -1), Point(1, -1),
                         Point(-1,  0),               Point(1,  0),
                         Point(-1,  1), Point(0,  1), Point(1,  1)]

    RULES = (
            (
                (0, 0, '=0'), # 0
                (0, 0, '=1'), # 1
                (0, 0, '=2'), # 2

                (1, 1, '=3'), # 3

                (0, 0, '=4'), # 4
                (0, 0, '=5'), # 5
                (0, 0, '=6'), # 6
                (0, 0, '=7'), # 7
                (0, 0, '=8'), # 8
            ),
            (
                (0, -1, '<2'), # 0
                (0, -1, '<2'), # 1

                (1,  0, '=2'), # 2
                (1,  0, '=3'), # 3

                (0, -1, '>3'), # 4
                (0, -1, '>3'), # 5
                (0, -1, '>3'), # 6
                (0, -1, '>3'), # 7
                (0, -1, '>3'), # 8
            ),

    )

    iterkeys = OrderedDict.iterkeys
    itervalues = OrderedDict.itervalues
    iteritems = OrderedDict.iteritems

    def __init__(self, data=None, *args, **kwargs):
        self._alive_count = kwargs.pop("alive_count", None)
        self._width = kwargs.pop("width", 10)
        self._height = kwargs.pop("height", 10)
        self._xmin = 0
        self._xmax = self._width
        self._ymin = 0
        self._ymax = self._height

        r = OrderedDict.__init__(self, *args, **kwargs)
        self.update(data) # TODO
        return r

    def __getitem__(self, k):
        try:
            return OrderedDict.__getitem__(self, Point(*k))
        except KeyError:
            return Env.DEFAULT_VALUE

    def __setitem__(self, k, v):
        return OrderedDict.__setitem__(self, Point(*k), v)

    @staticmethod
    def _TRANSFORMS_TABLE():
        """
        build list of neighbor subscript transforms

        #[Out]# [(-1, -1), (0, -1), (1, -1),
        #        (-1,  0),          (1,  0),
        #        (-1,  1), (0,  1), (1,  1)]
        """
        transforms=tuple(Point(*x[::-1]) for x in
                            itertools.product((-1, 0, 1), (-1, 0, 1))
                        )
        # ((3x3 = 9) - 1) / 2 = 4
        transforms.pop(4)
        return transforms

    # static
    def get_neighbor_subscripts(env, pos):
        """
        :param point: (x,y) 2-tuple
        :type point: tuple
        """
        return ((pos+t) for t in Env.TRANSFORMS_TABLE)


    def neighbor_count(env, pos):
        """
        :param env: environment structure ("universe")
        :type env: defaultdict
        # TODO: require integer tuple indices
        :param pos: (x,y) position tuple
        :type pos: tuple

        :returns: number of neighbor cells
        :rtype: int
        """
        return sum(env[p] for p in env.get_neighbor_subscripts(Point(*pos)))

    @classmethod
    def get_default_env(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @classmethod
    def _get_random_env(cls, *args, **kwargs):
        random.seed(kwargs.get('seed',10))
        height=kwargs.get("height")
        width=kwargs.get("width")
        env = Env(*args,
                data=(((x,y,), random.randint(0,1)) for (x,y) in
                    itertools.product(xrange(height), xrange(width))),
                **kwargs)

        for pos in itertools.product(xrange(height), xrange(width)):
            env[pos] = random.randint(0,1)
        return env

    @classmethod
    def _get_named_env(cls, name):
        from .environments import to_dict
        env = Env()
        try:
            env_classpath = ( ".environments.still.%s" % name )
            named_env = __import__(env_classpath)
        except ImportError:
            raise
        env.update(to_dict(named_env))
        return env

    @property
    def alive_count(env):
        #TODO: state
        if env._alive_count is None:
            env._alive_count = sum(env.itervalues()) # !
        return env._alive_count

    @alive_count.setter
    def set_alive_count(env, value):
        env._alive_count = value


    def shift_alive_count(env, delta):
        logging.debug("alive count %d changed by %d"
                        % (env.alive_count, delta))
        env._alive_count += delta

    def process_cell(env, pos):
        """
        :param env: environment
        :type env: hasattr(__getitem__)
        :param pos: (x,y) position tuple
        :type pos: tuple

        :returns: (new_state, alive_count, reason)
        :rtype: tuple

        """
        ncount = env.neighbor_count(pos)

        return Action(*Env.RULES[env[pos]][ncount])

        raise Exception('unhandled case: %s [ %d ] has %d neighbors' % (
                                            pos, env[pos], ncount))


    def __str__(self):
        return Env.to_file(self, StringIO.StringIO()).getvalue()

    def to_file(self,
            outp=sys.stdout,
            width=None,
            height=None,
            header=None):
        width=width or self._width
        height=height or self._height
        if header is not None:
            print(header, file=outp)
        print('_-'*width, file=outp)
        for y in xrange(height):
            for x in xrange(width):
                print(self[(x,y)] and 'X' or ' ', end=' ', file=outp)
            print('', file=outp)
        print('_-'*width, file=outp)
        print(header, file=outp)
        return outp


    def conway(env, step_limit=None, output=sys.stdout):
        """
        conway sim main function
        """

        def _conway(env=env, step_limit=step_limit, output=output):
            yield (copy.copy(env))
            if env.alive_count <= 0:
                logging.debug("K0NTORZZZ")
                return

            # t for 'timestep' (superstep, but s is for superman)
            for t in (step_limit and xrange(step_limit) or itertools.count()):
                print(t)
                env.to_file(output)
                _env = copy.copy(env)

                for pos in env:
                    act = env.process_cell(pos)
                    logging.debug("%s is now %s because ncount %s"
                                    % (pos, act.new_state, act.reason))
                    _env[pos] = act.new_state
                    _env._ymin = min(_env._ymin, pos.y)
                    _env._ymax = max(_env._ymax, pos.y)
                    _env._xmin = min(_env._xmin, pos.x)
                    _env._xmax = max(_env._xmax, pos.x)
                    _env.shift_alive_count(act.alive_count)

                yield (_env)

                # TODO: detect consecutive lack of alive_count_delta over
                # previous N steps ( sum(N-item FIFO queue) == 0 )
                if _env.alive_count <= 0:
                    logging.error("K0NTORZZZ")
                    return
                env = _env

            logging.debug("timed out")
            return
        return list(_conway(env, step_limit, output))

import unittest
class Test_conway(unittest.TestCase):
    def test_null_env(self):
        seed=10
        print("RANDOM SEED: %d" % seed)
        Env.conway(
            Env._get_random_env(
                seed=seed,
                width=10,
                height=10),
            step_limit=12)

    def test_still(self):
        for pattern in still.__ALL__:
            print(pattern)
            current_pattern = getattr(still, pattern)
            env = Env()
            env.update(to_dict(current_pattern))
            Env.conway(env, step_limit=3)

def main():
    import optparse
    import logging

    prs = optparse.OptionParser(usage="./%prog : args")

    prs.add_option('-e','--environment',
                    dest='environment',
                    action='append',
                    default=[])
    prs.add_option('-s', '--steps',
                    dest='steps',
                    action='store',
                    default=0,
                    type=int
                    )

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',)
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',)
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',)

    (opts, args) = prs.parse_args()

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        import sys
        sys.argv = [sys.argv[0]] + args
        import unittest
        exit(unittest.main())

    # load environment

    if opts.environment:
        pass

    else:
        env = Env._get_random_env(width=32,height=32)
    Env.conway(env, step_limit=opts.steps)

if __name__ == "__main__":
    main()
