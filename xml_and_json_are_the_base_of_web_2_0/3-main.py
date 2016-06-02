from car import Car

print "1"
c = Car(name="Rogue", brand="Nissan", nb_doors=5)
#print "c: %s" % c

print "2"
c2 = Car(c.to_hash())
#c2.set_nb_doors(3)
#print "c2: %s" % c2
#print "c: %s" % c

print "3"
Car("toto", 42, title=12)
