#pragma once

#include "chucknorris_export.h"
#ifdef __cplusplus
extern "C" {
#endif

typedef struct chuck_norris chuck_norris_t;
CHUCKNORRIS_EXPORT char* chuck_norris_version(void);
CHUCKNORRIS_EXPORT chuck_norris_t* chuck_norris_init(void);
CHUCKNORRIS_EXPORT char* chuck_norris_get_fact(chuck_norris_t*);
CHUCKNORRIS_EXPORT void chuck_norris_deinit(chuck_norris_t*);

#ifdef __cplusplus
}
#endif
