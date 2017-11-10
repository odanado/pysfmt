from libc.stdint cimport uint32_t, uint64_t

cdef extern from 'SFMT.h':
    ctypedef struct sfmt_t:
        pass

    void sfmt_fill_array32(sfmt_t * sfmt, uint32_t * array, int size)
    void sfmt_fill_array64(sfmt_t * sfmt, uint64_t * array, int size)
    void sfmt_init_gen_rand(sfmt_t* sfmt, uint32_t seed)
    void sfmt_init_by_array(sfmt_t * sfmt, uint32_t * init_key, int key_length)
    const char * sfmt_get_idstring(sfmt_t * sfmt)
    int sfmt_get_min_array_size32(sfmt_t * sfmt)
    int sfmt_get_min_array_size64(sfmt_t * sfmt)
    void sfmt_gen_rand_all(sfmt_t * sfmt)

    uint64_t sfmt_genrand_uint64(sfmt_t * sfmt)
    double sfmt_genrand_real1(sfmt_t * sfmt)
    double sfmt_genrand_real2(sfmt_t * sfmt)
    double sfmt_genrand_real3(sfmt_t * sfmt)
    double sfmt_genrand_res53(sfmt_t * sfmt)
    double sfmt_genrand_res53_mix(sfmt_t * sfmt)
