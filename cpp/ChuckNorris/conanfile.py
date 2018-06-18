from conans import ConanFile, CMake


class ChucknorrisConan(ConanFile):
    name = "ChuckNorris"
    version = "0.2"
    license = "MIT"
    url = "https://github.com/dmerejkowsky/cpp-mobile-example"
    description = "Chuck Norris does not need a description"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake", "json"
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    requires = "sqlite3/3.21.0@dmerej/test"
    keep_imports = True

    def build(self):
        cmake = CMake(self)
        cmake_definitions = {}
        if self.options.shared:
            cmake_definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.configure(defs=cmake_definitions)
        cmake.build(args=["--", "-v"])

    def imports(self):
        self.copy("*libc++_shared.so", dst="lib", keep_path=False)

    def package(self):
        self.copy("bin/cpp_demo", dst="bin", keep_path=False)
        self.copy("lib/libchucknorris.so", dst="lib", keep_path=False)
        self.copy("lib/libc++_shared.so", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["chucknorris"]
