#pragma once

#ifdef __cplusplus
extern "C" {
#endif


typedef struct chuck_norris chuck_norris_t;
char* chuck_norris_version(void);
const char* chuck_norris_get_fact(chuck_norris_t*);
void chuck_norris_deinit(chuck_norris_t*);

#ifdef __cplusplus
}
#endif
