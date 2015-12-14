import ctypes
import pygmplib as gmp

print 'gmp version: ', gmp.gmp_version.value

integ1 = ctypes.pointer( gmp.__mpz_struct() )
integ2 = ctypes.pointer( gmp.__mpz_struct() )

gmp.gmpz_init_set_ui( integ1, ctypes.c_ulong( 1900 ) )
print 'integ1 : ', gmp.gmpz_get_si( integ1 )
gmp.gmpz_init_set_ui( integ2, ctypes.c_ulong( 77 ) )
print 'integ2 : ', gmp.gmpz_get_si( integ2 )

gmp.gmpz_add( integ1, integ1, integ2 )

print 'integ1 : ', gmp.gmpz_get_si( integ1 )

