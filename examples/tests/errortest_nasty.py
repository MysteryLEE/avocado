from avocado import Test


class NastyException(Exception):

    """Please never use something like this!!!"""

    def __init__(self, msg):  # pylint: disable=W0231
        self.msg = msg

    def __str__(self):
        return self.msg


class FailTest(Test):

    """
    Very nasty exception test

    :avocado: tags=failure_expected
    """

    # @staticmethod
    def test(self):
        """
        Avocado should report this as TestError.
        """
        self.assertRaises(NastyException, msg="Nasty-string-like-exception\u017e")
