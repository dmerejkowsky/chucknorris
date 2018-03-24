#include <chucknorris.h>
#include <cstring>

#include <ChuckNorris.hpp>


chuck_norris_t* chuck_norris_init()
{
  return new ChuckNorris();
}

char* chuck_norris_get_fact(chuck_norris_t* chuck_norris)
{
  std::string fact = chuck_norris->getFact();
  char* result = strdup(fact.c_str());
  return result;
}

void chuck_norris_deinit(chuck_norris_t* chuck_norris)
{
  delete chuck_norris;
}
