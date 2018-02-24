#include <sqlite3.h>

#include <iostream>

int main()
{
  std::cout << "hello, world" << std::endl;
  std::cout << "sqlite version: " << sqlite3_libversion() << std::endl;
  return 0;
}
