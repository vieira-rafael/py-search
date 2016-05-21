# -*- coding: utf-8 -*-
import cyj
parser = cyj.cyj()assert parser << '{"ab":"test","c":[1,2,{"x":["y","f","w",[6,7,8,10]]},4],"s":{"y":["llll",1,false,true]}}' == Trueprint parser.root_info()
print parser >> ('c',2)
for i in parser.root_info()["keys"]: print parser( ( str(i), ) )

