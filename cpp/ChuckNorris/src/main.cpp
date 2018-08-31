#include <iostream>

#include <ChuckNorris.hpp>

int main()
{
  std::cout << "Running ChuckNorris version: " << ChuckNorris::version() << std::endl;
  ChuckNorris chuckNorris;
  std::string fact = chuckNorris.getFact();
  std::cout << fact << std::endl;
  return 0;
}
