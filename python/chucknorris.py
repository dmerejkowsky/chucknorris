from _chucknorris import lib, ffi

def c_to_str(c_data):
    return ffi.string(c_data).decode()

c_version = lib.chuck_norris_version()
print(c_to_str(c_version))
chuck_norris = lib.chuck_norris_init()
c_fact = lib.chuck_norris_get_fact(chuck_norris)
print(c_to_str(c_fact))
lib.chuck_norris_deinit(chuck_norris)
