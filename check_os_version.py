# Check the distribution name along with the OS version number.

#!/usr/bin/env python3

import distro
print(distro.linux_distribution())
print(distro.id())
print(distro.version())
print(distro.name())

# Example:
# $ ./check_os_version.py
# DeprecationWarning: distro.linux_distribution() is deprecated. It should only be used as a compatibility shim with Python's platform.linux_distribution(). Please use distro.id(), distro.version() and distro.name() instead.
#   print(distro.linux_distribution())
# ('Fedora Linux', '36', '')
