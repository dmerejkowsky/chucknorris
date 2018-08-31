cmake_minimum_required(VERSION 3.10)

project(ChuckNorris)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_POSITION_INDEPENDENT_CODE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(chucknorris
  include/ChuckNorris.hpp
  include/chucknorris.h
  src/ChuckNorris.cpp
  src/c_wrapper.cpp
)

target_link_libraries(chucknorris
    CONAN_PKG::sqlite3
)

target_include_directories(
  chucknorris
  PUBLIC
    "include"
)

add_executable(cpp_demo
  src/main.cpp
)

target_link_libraries(cpp_demo chucknorris)

add_executable(c_demo
  src/main.c
)

target_link_libraries(c_demo chucknorris)
