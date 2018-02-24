cmake_minimum_required(VERSION 3.10)

project(ChuckNorris)

add_library(chucknorris
  include/chucknorris.hpp
  src/chucknorris.cpp
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
