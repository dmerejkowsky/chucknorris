cmake_minimum_required(VERSION 3.10)

project(ChuckNorris)
set(CMAKE_CXX_STANDARD 11)


include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(chucknorris
  include/chucknorris.hpp
  src/chucknorris.cpp
)

target_link_libraries(chucknorris
  PRIVATE
    CONAN_PKG::sqlite3
)

target_include_directories(
  chucknorris
  PUBLIC
    "include"
)

add_executable(demo
  src/main.cpp
)

target_link_libraries(demo chucknorris)
