cmake_minimum_required(VERSION 3.10)
include(GenerateExportHeader)

project(ChuckNorris)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_POSITION_INDEPENDENT_CODE TRUE)
set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_C_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN 1)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(chucknorris
  include/ChuckNorris.hpp
  include/chucknorris.h
  src/ChuckNorris.cpp
  src/c_wrapper.cpp
)

generate_export_header(chucknorris)

target_link_libraries(chucknorris
    CONAN_PKG::sqlite3
)

target_include_directories(
  chucknorris
  PUBLIC
    "include"
    ${CMAKE_CURRENT_BINARY_DIR}
)

add_executable(cpp_demo
  src/main.cpp
)

target_link_libraries(cpp_demo chucknorris)

add_executable(c_demo
  src/main.c
)

target_link_libraries(c_demo chucknorris)
