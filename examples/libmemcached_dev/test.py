import ctypes
import pymemcached as mmc

print 'memcached version: ', mmc.memcached_lib_version()

memc = mmc.memcached_create(None)
servers = mmc.memcached_servers_parse( "localhost:11211" )
mmc.memcached_server_push(memc, servers);
mmc.memcached_server_list_free(servers);

key = "1"
value = "Python is better!"

result = mmc.memcached_add( memc, key, len(key), value, len(value), 0, 0);
print "key/value (%s/%s ) was stored?: " % ( key, value ) + mmc.memcached_strerror(memc, result);

result = mmc.memcached_delete( memc, key, len(key), 0);
print "key/value (%s/%s ) was deleted?: " % ( key, value ) + mmc.memcached_strerror(memc, result);

for key in 'abcdefghijklmnopqrstuvwxyz':
    value_length = ctypes.c_size_t()
    flags = ctypes.c_ulong()
    result = mmc.memcached_return()
    value = mmc.memcached_get( memc, key, len(key), ctypes.byref( value_length ), ctypes.byref( flags ), ctypes.byref( result ) )
    print 'key/value (%s/%s)' % ( key, value )
    print   mmc.memcached_strerror(memc, result);

