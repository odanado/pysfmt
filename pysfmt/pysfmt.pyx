from libc.stdlib cimport malloc, free
from libc.stdint cimport uint32_t

cimport pysfmt

cdef class SFMT:
    cdef sfmt_t *_thisptr

    def __cinit__(self, uint32_t seed):
        self._thisptr = <sfmt_t*>malloc(sizeof(sfmt_t))

        pysfmt.sfmt_init_gen_rand(self._thisptr, seed)

    def __dealloc__(self):
        if self._thisptr != NULL:
            free(self._thisptr)

    def genrand_uint64(self):
        return pysfmt.sfmt_genrand_uint64(self._thisptr)

    def genrand_real1(self):
        return pysfmt.sfmt_genrand_real1(self._thisptr)

    def genrand_real2(self):
        return pysfmt.sfmt_genrand_real2(self._thisptr)

    def genrand_real3(self):
        return pysfmt.sfmt_genrand_real3(self._thisptr)

    def genrand_res53(self):
        return pysfmt.sfmt_genrand_res53(self._thisptr)

    def genrand_res53_mix(self):
        return pysfmt.sfmt_genrand_res53_mix(self._thisptr)
