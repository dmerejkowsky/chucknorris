import json

import path
from cffi import FFI
ffibuilder = FFI()

ffibuilder.set_source(
    "_chucknorris",
    """
    #include <chucknorris.h>
    """,
    include_dirs = ["../rust/target/c/"],
    extra_objects=["../rust/target/debug/libchucknorris.so"],
)

ffibuilder.cdef("""
typedef struct ChuckNorris ChuckNorris;

void chuck_norris_deinit(const ChuckNorris *ptr);

char *chuck_norris_get_fact(const ChuckNorris *ptr);

const ChuckNorris *chuck_norris_init(void);
""")
