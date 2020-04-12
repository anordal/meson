import os
import subprocess
from typing import Optional

def _get_vc_spiritual_symlink():
    return os.path.join(os.environ['HOME'], '.vcpkg', 'vcpkg.path.txt')

'''
Returns vcpkg root or None if the user does not have vcpkg.
'''
def get_vcroot() -> Optional[str]:
    try:
        with open(_get_vc_spiritual_symlink(), 'rb') as readlink:
            return readlink.read()
    except FileNotFoundError:
        return None

def install(vcroot, graftdir, pkg) -> None:
    vcpkg = os.path.join(vcroot, b'vcpkg')
    subprocess.check_call([vcpkg, '--vcpkg-root', graftdir, 'install', pkg])













'''
If it's so important to install to the build directory, vcpkg has to be transplanted.
'''
def graft_vcpkg(src, dst) -> None:
    os.makedirs(dst)
    open(os.path.join(dst, '.vcpkg-root'), 'a').close()
    for subdir in ['triplets', 'scripts', 'ports']:
        os.symlink(os.path.join(src, subdir), os.path.join(dst, subdir))
