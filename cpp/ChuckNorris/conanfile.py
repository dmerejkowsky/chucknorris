from conans import ConanFile, CMake


class ChucknorrisConan(ConanFile):
    name = "ChuckNorris"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/dmerejkowsky/cpp-mobile-example"
    description = "Chuck Norris does not need a description"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False", "sqlite3:pic=True"
    generators = "cmake", "json"
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    requires = "sqlite3/3.21.0@dmerej/test"

    def configure(self):
        # TODO: ask theo why
        # taken fro sqlite3 recipe
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        cmade_definitions = {}
        if self.options.shared:
            cmade_definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.configure(defs=cmade_definitions)
        cmake.build(args=["--", "-v"])

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["chucknorris"]
