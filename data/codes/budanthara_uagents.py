# -*- coding: utf-8 -*-
from random import randint 
class UserAgents: def __init__(self): self.user_agents = [ "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, \          like Gecko) Version/4.0 Mobile Safari/534.30",
 def user_agent(self): return self.user_agents[randint(0, len(self.user_agents)-1)]