#include <chucknorris.h>
#include <stdlib.h>
#include <stdio.h>


int main()
{
  chuck_norris_t* ck = chuck_norris_init();
  const char* fact = chuck_norris_get_fact(ck);
  printf("%s\n", fact);
  chuck_norris_deinit(ck);
  return 0;
}
