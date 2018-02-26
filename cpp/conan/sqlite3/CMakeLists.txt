project(cmake_wrapper)

set(CMAKE_POSITION_INDEPENDENT_CODE TRUE)
include(conanbuildinfo.cmake)
conan_basic_setup()

if (WIN32 AND MSVC AND BUILD_SHARED_LIBS)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif(MSVC AND BUILD_SHARED_LIBS)

add_library(sqlite3 sources/sqlite3.c)
target_include_directories(sqlite3 PUBLIC "sources")

# Add some options from https://sqlite.org/compile.html
option(ENABLE_JSON1 "Enable JSON SQL functions")
if(ENABLE_JSON1)
    target_compile_definitions(sqlite3 PRIVATE SQLITE_ENABLE_JSON1)
endif()

add_executable(cpp_test
    test.cpp
)

target_link_libraries(cpp_test
    sqlite3
)
