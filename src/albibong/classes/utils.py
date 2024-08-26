import os
import platform
from importlib.metadata import version
from uuid import UUID

from scapy.all import conf, get_if_addr

FILENAME = os.path.join(os.path.expanduser("~"), "Albibong/Debug/user_spec.txt")
os.makedirs(os.path.dirname(FILENAME), exist_ok=True)


class Utils:

    @staticmethod
    def convert_int_arr_to_uuid(arr):
        b = bytes(arr)
        return UUID(bytes=b)

    @staticmethod
    def get_user_specifications(install_source: str):
        os_ver = f"{platform.system()} {platform.release()}"
        python_ver = platform.python_version()
        albibong_ver = version("albibong")
        interfaces = f"{conf.iface} ({get_if_addr(conf.iface)})"

        text = f"\n===\n\nAlbibong Ver        : {albibong_ver}\nPython Ver          : {python_ver}\nOS Ver              : {os_ver}\nInstallation Source : {install_source}\nInterfaces          : {interfaces}\n\n===\n"
        print(text)
        with open(FILENAME, "w+") as file:
            file.write(text)
