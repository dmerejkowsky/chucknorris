#pragma once

#ifdef __cplusplus
extern "C" {
#endif

const char* chuck_norris_version();
typedef struct ChuckNorris chuck_norris_t;
chuck_norris_t* chuck_norris_init(void);
char* chuck_norris_get_fact(chuck_norris_t*);
void chuck_norris_deinit(chuck_norris_t*);

#ifdef __cplusplus
}
#endif
