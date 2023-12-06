from conan import ConanFile
from conan.tools.files import update_conandata, copy, chdir, mkdir, collect_libs, download
from conan.tools.layout import basic_layout
from conan.tools.env import Environment
from conan.tools.env import VirtualRunEnv

import os, sys
import sysconfig
from io import StringIO


class NugetConan(ConanFile):
    name = "nuget"
    version = "6.8.0"
    license = "bsd"
    url = "https://www.nuget.org"
    settings = "os"
    description="Nuget for windows. Useful as a build_require."
    package_type = "application"

    def validate(self):
        if self.settings.os != "Windows":
            raise ConanInvalidConfiguration("Only windows supported for nuget")


    def generate(self):
        env = Environment()
        return env

    def layout(self):
        basic_layout(self)

    def build(self):
        download(self, "https://dist.nuget.org/win-x86-commandline/v%s/nuget.exe" % (self.version), os.path.join(self.build_folder, "nuget.exe"))

    def package(self):
        copy(self, "*.exe", src=self.build_folder, dst=os.path.join(self.package_folder, "bin"), keep_path=True)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))