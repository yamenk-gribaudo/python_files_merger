import subprocess
from genbadge import Badge
import python_files_merger

# Version
version = Badge(left_txt="version",
                right_txt=python_files_merger.__version__, color="violet")
version.write_to("badges/version.svg", use_shields=False)

# License
license_ = Badge(left_txt="license",
                 right_txt="MIT", color="blue")
license_.write_to("badges/license.svg", use_shields=False)

# Tests
subprocess.check_call(
    "pytest --junitxml=reports/junit/junit.xml --html=reports/junit/report.html && \
        genbadge tests -o badges/tests.svg", shell=True)

# Coverage
subprocess.call(
    "coverage run --source=python_files_merger -m unittest discover && coverage report && coverage html && coverage xml -o reports/coverage/coverage.xml && genbadge coverage -o badges/coverage.svg", shell=True)
