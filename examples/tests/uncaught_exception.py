from avocado import Test


class ErrorTest(Test):

    """
    Example test that raises generic exception

    :avocado: tags=failure_expected
    """


    def test(self):
        """
        This should end with ERROR.
        """
        self.assertRaises(Exception, msg="This is a generic exception")
