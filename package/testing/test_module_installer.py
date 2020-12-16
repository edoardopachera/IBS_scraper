import subprocess
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname('package')))
from package import module_installer as mi

# Run python3 -m unittest package/testing/test_module_installer.py


class TestInput(unittest.TestCase):

    # smoke test: already installed module
    def test_installed(self):
        module = "pyfiglet"
        try:
            subprocess.check_call([sys.executable,
                                   "-m", "pip", "install",
                                   module])
            mi.modules([module])
        except Exception:
            self.fail("È stato impossibile importare il modulo %s" % (module))
