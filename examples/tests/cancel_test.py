from avocado import Test
from avocado.utils.process import run
from avocado.utils.software_manager.manager import SoftwareManager


class CancelTest(Test):

    """
    Example tests that cancel the current test from inside the test.
    """

    def setUp(self):
        sm = SoftwareManager()
        self.pkgs = sm.list_all(software_components=False)

    @unittest.skipUnless("iperf-2.0.8-6.fc25.x86_64" not in self.pkgs)
    def test_iperf_condition1(self):
        self.cancel("iperf is not installed or wrong version")
        self.assertIn("pthreads", run("iperf -v", ignore_status=True).stderr_text)

    @unittest.skipUnless("iperf-2.0.8-6.fc25.x86_64" in self.pkgs)
    def test_iperf_condition2(self):
        self.assertIn("pthreads", run("iperf -v", ignore_status=True).stderr_text)

    # def test_iperf(self):
    #     if "iperf-2.0.8-6.fc25.x86_64" not in self.pkgs:
    #         self.cancel("iperf is not installed or wrong version")
    #     self.assertIn("pthreads", run("iperf -v", ignore_status=True).stderr_text)

    @unittest.skipUnless("gcc-6.3.1-1.fc25.x86_64" not in self.pkgs)
    def test_gcc_condition1(self):
        self.cancel("gcc is not installed or wrong version")
        self.assertIn(
            "enable-gnu-indirect-function",
            run("gcc -v", ignore_status=True).stderr_text,
        )

    @unittest.skipUnless("gcc-6.3.1-1.fc25.x86_64" in self.pkgs)
    def test_gcc_condition2(self):
        self.assertIn(
            "enable-gnu-indirect-function",
            run("gcc -v", ignore_status=True).stderr_text,
        )

    # def test_gcc(self):
    #     if "gcc-6.3.1-1.fc25.x86_64" not in self.pkgs:
    #         self.cancel("gcc is not installed or wrong version")
    #     self.assertIn(
    #         "enable-gnu-indirect-function",
    #         run("gcc -v", ignore_status=True).stderr_text,
    #     )
