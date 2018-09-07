#include <chucknorris.h>
#include <stdlib.h>
#include <stdio.h>


int main()
{
  printf("Using ChuckNorris version %s\n", chuck_norris_version());
  chuck_norris_t* ck = chuck_norris_init();
  char* fact = chuck_norris_get_fact(ck);
  printf("%s\n", fact);
  free(fact);
  chuck_norris_deinit(ck);
  return 0;
}
