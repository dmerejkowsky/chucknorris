#include <chucknorris.h>
#include <stdlib.h>
#include <stdio.h>


int main()
{
  chuck_norris_t* ck;
  const char* fact = chuck_norris_get_fact(ck);
  printf("%s\n", fact);
  /*free(fact);*/
  chuck_norris_deinit(ck);
  return 0;
}
