#include <chucknorris.h>
#include <cstring>

#include <ChuckNorris.hpp>

struct chuck_norris {
  ChuckNorris* ck;
};

chuck_norris_t* chuck_norris_init()
{
  auto ck = new ChuckNorris();
  return reinterpret_cast<chuck_norris*>(ck);
}

const char* chuck_norris_get_fact(chuck_norris_t* chuck_norris)
{
  auto ck = reinterpret_cast<ChuckNorris*>(chuck_norris);
  std::string fact = ck->getFact();
  const char* result = fact.c_str();
  return result;
  //const char* result = strdup(fact.c_str());
  //return result;
}

void chuck_norris_deinit(chuck_norris_t* chuck_norris)
{
  auto ck = reinterpret_cast<ChuckNorris*>(chuck_norris);
  delete ck;
}
