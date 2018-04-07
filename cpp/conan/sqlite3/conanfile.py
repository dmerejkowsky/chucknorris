#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class ConanSqlite3(ConanFile):
    name = "sqlite3"
    version = "3.21.0"
    year = "2017"
    sha1 = "ebe33c20d37a715db95288010c1009cd560f2452"
    description = "Self-contained, serverless, in-process SQL database engine."
    url = "http://github.com/bincrafters/conan-sqlite3"
    homepage = "https://www.sqlite.org"
    license = "Public Domain"
    generators = "cmake"
    settings = "os", "compiler", "arch", "build_type"
    exports = ["LICENSE.md"]
    exports_sources = "CMakeLists.txt", "FindSQLite3.cmake", "test.cpp"
    options = {"shared": [True, False], "enable_json1": [True, False]}
    default_options = "shared=False", "enable_json1=False"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        base_url = "https://dmerej.info/pub/" + self.year
        archive_name = "sqlite-amalgamation-" + self.version.replace(".","") + "000"
        archive_ext = "zip"
        download_url = "{0}/{1}.{2}".format(base_url, archive_name, archive_ext)
        self.output.info("Attempting download of sources from: " + download_url)
        tools.get(download_url, sha1=self.sha1)
        os.rename(archive_name, "sources")

    def build(self):
        cmake = CMake(self)

        cmake.definitions["ENABLE_JSON1"] = self.options.enable_json1
        cmake.verbose = True
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("FindSQLite3.cmake", ".", ".")
        self.copy("*.h", dst="include", src="sources")
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)
        self.copy(pattern="*.pdb", dst="lib", keep_path=False)
        self.copy(pattern="*.so", dst="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['sqlite3']
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
            self.cpp_info.libs.append("dl")
