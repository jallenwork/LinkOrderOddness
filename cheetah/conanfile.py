from conans import ConanFile

class cheetahConan(ConanFile):
    name = "cheetah"
    version = "2.0.0"
    description = "An intermediate library with one public dependency and at least one transitive dependency,\
                   who's unit test calls the transitive dependency explicitly as a build_requires."
    settings = "os", "compiler", "build_type", "arch"
    generators = "txt"
    requires = "gazelle/[*]@user/testing"
    build_requires =  "gtest/[*]@build/prod", "grass/[*]@user/testing"
    build_policy = "missing"

    def build(self):
        pass

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.libs = ["cheetah"]
