# coding: utf-8

import sys
import os
import re

from contextlib import contextmanager
from io import StringIO
import importlib

import random

import unittest


@contextmanager
def capture_stdout():
    old_out = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_out


class TestFunctions(unittest.TestCase):

    modex = re.compile(r"(\d+)-.*\.py$")

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.modules = 8 * [None]
        dirname = os.path.dirname(__file__)
        for f in os.listdir(dirname):
            m = self.modex.match(f)
            if m is not None:
                self.modules[int(m.group(1))-1] = os.path.join(dirname, f)

    def import_module(self, task):
        mod = self.modules[task-1]
        if mod is None:
            raise ImportError('No module for task {}'.format(task))
        spec = importlib.util.spec_from_file_location(mod[:-3], mod)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def assertBetween(self, x, lo, hi):
        if not (lo <= x <= hi):
            raise AssertionError('{!r} not between {!r} and {!r}'.format(x, lo, hi))

    def test_1_pecentage(self):
        mod = self.import_module(1)
        for A,n,p in ((1000, 3, 5), (20, 5, 2)):
            self.assertAlmostEqual(A * (1 + p/100)**n, mod.interest(A=A, n=n, p=p), 2)

    def test_2_temperature(self):
        mod = self.import_module(2)
        for f in (10., 20., 50., 15.):
            self.assertAlmostEqual(5/9 * (f-32), mod.C(f), 2)

    def test_3_dollars(self):
        mod = self.import_module(3)
        for pln in (10., 20., 50., 15.):
            self.assertAlmostEqual(pln / 3.85, mod.convert_to_usd(pln), 2)

    def test_4_net(self):
        mod = self.import_module(4)
        self.assertAlmostEqual(50 / 1.20, mod.calc_netto(brutto=50, vat=20), 2)
        self.assertAlmostEqual(70 / 1.23, mod.calc_netto(brutto=70), 2)

    def test_5_words(self):
        mod = self.import_module(5)
        words = "Litwo ojczyzno moja ty jesteś jak zdrowie".split(' ')
        self.assertEqual(['moja', 'ty', 'jak'], mod.get_short_words(words))
        self.assertEqual(['ty', 'jak'], mod.get_short_words(words, 4))

    def test_6_message(self):
        mod = self.import_module(6)
        data = dict(name="Don Corleone", role="gangster", movie="The Godfather")
        self.assertEqual("In The Godfather, Don Corleone is a gangster.", mod.message(data))
        data = dict(movie="Kill Bill", role="assassin")
        self.assertIsNone(mod.message(data))

    def test_7_dice(self):
        mod = self.import_module(7)

        for _ in range(100):
            self.assertBetween(mod.dice(1), 1, 6)
            self.assertBetween(mod.dice(2), 2, 12)

        regex = [re.compile(r"\s*{:2}\s*:\s+#*".format(i)) for i in range(2, 13)]
        with capture_stdout() as out:
            mod.print_histogram(500)
        result = out.getvalue().rstrip()
        lines = result.split('\n')
        for l, r in zip(lines, regex):
            self.assertRegex(l, r)
        self.assertEqual(sum(1 for c in result if c == '#'), 500)
