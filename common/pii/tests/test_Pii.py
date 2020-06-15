from absl.testing import flagsaver
from common.pii import Pii


class TestPiiWrappers:

    @flagsaver.flagsaver(collect_pii=False)
    def test_redacted_when_pii_off(self):
        assert Pii.String("test") == "[redacted]"
        assert Pii.String("") == "[redacted]"
        assert Pii.Int(1337) == -1
        assert Pii.Int(-1) == -1
        assert Pii.StringSequence(['a', 'b', 'c']) == (
                "[redacted]", "[redacted]", "[redacted]")
        assert Pii.StringSequence([]) == tuple()

    @flagsaver.flagsaver(collect_pii=True)
    def test_redacted_when_pii_on(self):
        assert Pii.String("test") == "test"
        assert Pii.String("") == ""
        assert Pii.Int(1337) == 1337
        assert Pii.Int(-1) == -1
        assert Pii.StringSequence(['a', 'b', 'c']) == ("a", "b", "c")
        assert Pii.StringSequence([]) == tuple()
