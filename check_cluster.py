import time
from redis.sentinel import Sentinel

sentinel = Sentinel([('192.168.11.35', 26379),('192.168.11.37', 26379),('192.168.11.37', 26379)], socket_timeout=0.1)
for i in range(1,1000):
  print "ciclo " + str(i)
  try:
    print "master: " + str(sentinel.discover_master('mymaster'))
    print "slave/s: " + str(sentinel.discover_slaves('mymaster'))

    master = sentinel.master_for('mymaster', socket_timeout=0.1)
    slave = sentinel.slave_for('mymaster', socket_timeout=0.1)
  except:
    print "sentinel eligiendo a un master"

  clave = "clave" + str(i)
  valor = "valor" + str(i)

  try:
    print "master.set " + clave + " " + valor 
    master.set(clave, valor)

    print "master.get " + clave + " = " + str(master.get(clave))

    print "master.set " + clave + " = " + str(slave.get(clave))

    print "master.delete " + clave
    master.delete(clave)
  except:
    print "cluster en modo solo lectura"

  print ""
  time.sleep(1)
