from  inherit import *
p=Parent()
p.parentMethod()

p2=Child()
p2.parentMethod()
p2.childMethod()

p2.getAttr()