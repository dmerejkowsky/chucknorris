import os
import sys
import json

import path
from cffi import FFI
ffibuilder = FFI()


cpp_build_path = path.Path("../cpp/build/default").abspath()
libs = []

libchucknorris_path = cpp_build_path.joinpath("lib/libchucknorris.a")
libs.append(libchucknorris_path)

conan_info = json.loads(cpp_build_path.joinpath("conaninfo.json").text())
for dep in conan_info["dependencies"]:
    for lib_name in dep["libs"]:
        lib_filename = "lib%s.a" % lib_name
        for lib_path in dep["lib_paths"]:
            candidate = path.Path(lib_path).joinpath(lib_filename)
            if candidate.exists():
                libs.append(candidate)

ffibuilder.set_source(
    "_chucknorris",
    """
    #include <chucknorris.h>

    """,
    extra_objects=libs,
    include_dirs=["../cpp/include"],
)

ffibuilder.cdef("""
const char* chuck_norris_version(void);

typedef struct ChuckNorris chuck_norris_t;
chuck_norris_t* chuck_norris_init(void);
const char* chuck_norris_get_fact(chuck_norris_t*);
void chuck_norris_deinit(chuck_norris_t*);
""")


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
