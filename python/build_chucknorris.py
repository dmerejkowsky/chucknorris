import json

import path
from cffi import FFI
ffibuilder = FFI()


cpp_path = path.Path("../cpp/ChuckNorris").abspath()
cpp_build_path = cpp_path.joinpath("build/default")

extra_objects = []
libchucknorris_path = cpp_build_path.joinpath("lib/libchucknorris.a")
extra_objects.append(libchucknorris_path)

include_dirs = []
include_dirs.append(cpp_path.joinpath("include"))
include_dirs.append(cpp_build_path)

libraries = ["stdc++"]

conan_info = json.loads(cpp_build_path.joinpath("conanbuildinfo.json").text())
for dep in conan_info["dependencies"]:
    for lib_name in dep["libs"]:
        lib_filename = "lib%s.a" % lib_name
        for lib_path in dep["lib_paths"]:
            candidate = path.Path(lib_path).joinpath(lib_filename)
            if candidate.exists():
                extra_objects.append(candidate)
            else:
                libraries.append(lib_name)
    for include_path in dep["include_paths"]:
        include_dirs.append(include_path)


ffibuilder.set_source(
    "_chucknorris",
    """
    #include <chucknorris.h>

    """,
    extra_objects=extra_objects,
    include_dirs=include_dirs,
    libraries=libraries,
)

ffibuilder.cdef("""
typedef struct chuck_norris chuck_norris_t;
chuck_norris_t* chuck_norris_init(void);
const char* chuck_norris_get_fact(chuck_norris_t*);
void chuck_norris_deinit(chuck_norris_t*);
""")
