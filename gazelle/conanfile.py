from conans import ConanFile

class gazelleConan(ConanFile):
    name = "gazelle"
    version = "1.3.0"
    description = "An intermediate library with one public dependency."
    settings = "os", "compiler", "build_type", "arch"
    generators = "txt"
    requires = "grass/[*]@user/testing"
    build_requires =  "gtest/[*]@build/prod"
    build_policy = "missing"

    def build(self):
        pass

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.libs = ["gazelle"]
