import doctest
import io
import sys
import numpy as np

<<<<<<< HEAD
"""
This is a helper function that you can use to add simple unit tests
to your exercise.

This uses https://docs.python.org/3/library/doctest.html.
"""


def test(f):
    """Run unit tests defined in a function's docstring (doctests)"""
=======

def test(f):
    # The `globs` defines the variables, functions and packages allowed in the docstring.
>>>>>>> upstream/master
    tests = doctest.DocTestFinder().find(f)
    assert len(tests) <= 1
    for test in tests:
        # We redirect stdout to a string, so we can tell if the tests worked out or not
        orig_stdout = sys.stdout
        sys.stdout = io.StringIO()

<<<<<<< HEAD
        orig_rng_state = np.random.get_state()

        try:
            np.random.seed(1)
=======
        try:
>>>>>>> upstream/master
            results: doctest.TestResults = doctest.DocTestRunner().run(test)
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = orig_stdout
<<<<<<< HEAD
            np.random.set_state(orig_rng_state)
=======
>>>>>>> upstream/master

        if results.failed > 0:
            print(f"❌ The are some issues with your implementation of `{f.__name__}`:")
            print(output, end="")
            print(
                "**********************************************************************"
            )
        elif results.attempted > 0:
<<<<<<< HEAD
            print(f"✅ Your `{f.__name__}` passes some basic tests.")
=======
            print(f"✅ Your `{f.__name__}` passed {results.attempted} tests.")
>>>>>>> upstream/master
        else:
            print(f"Could not find any tests for {f.__name__}")
