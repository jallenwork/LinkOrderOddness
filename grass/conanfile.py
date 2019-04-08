from conans import ConanFile

class grassConan(ConanFile):
    name = "grass"
    version = "1.0.1"
    description = "A base library with no public dependencies"
    settings = "os", "compiler", "build_type", "arch"
    generators = "txt"
    build_requires =  "gtest/[*]@build/prod"
    build_policy = "missing"

    def build(self):
        pass

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.libs = ["grass"]
