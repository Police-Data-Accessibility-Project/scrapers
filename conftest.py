import pytest
import sys

from absl import flags


# This needs to happen once before we can use absl flags.
# Normally, this is taken care of by the app.run(main)
# call in our programs, but pytest complicates that a bit.
@pytest.fixture(scope="session", autouse=True)
def absl_flags():
    flags.FLAGS(sys.argv)
    return flags.FLAGS
