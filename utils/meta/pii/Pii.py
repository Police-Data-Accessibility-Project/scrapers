from typing import Optional, Generic, TypeVar, Sequence, Tuple

from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_bool("collect_pii", False, "Whether to store PII.")


def PrimitiveWrapper(typename, redacted_value):
    class Pii(typename):
        def __new__(cls, value):
            if not FLAGS.collect_pii:
                value = redacted_value
            return typename.__new__(cls, value)
    return Pii


class String(PrimitiveWrapper(str, "[redacted]")):
    """Safely wraps PII strings."""


class Int(PrimitiveWrapper(int, -1)):
    """Safely wraps PII ints."""


class StringSequence(Tuple[String]):
    """Safely wraps sequences of PII strings."""

    def __new__(cls, values: Sequence[str]):
        return tuple.__new__(cls, (String(v) for v in values))
