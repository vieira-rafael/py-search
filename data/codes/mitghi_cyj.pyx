from libc.stdio cimport printffrom libc.stdlib cimport freecimport cyJSONimport types
cJSON_False = 0cJSON_True = 1cJSON_NULL = 2cJSON_Number = 3cJSON_String = 4cJSON_Array = 5cJSON_Object = 6cJSON_IsReference = 256cJSON_StringIsConst = 512
GLOBAL_TYPE = { 0 : "bool", 1 : "bool", 2 :  None, 3 : "num", 4 : "str", 5 : "list", 6 : "dict"}
class cyJSON_Invalid_JSON(Exception): pass
class cyJSON_Element_Error(Exception): pass
class cyJSON_Index_Error(Exception): pass
class cyJSON_Key_Error(Exception): pass
class cyJSON_Panic(Exception): pass
cdef class cyj: cdef cyJSON.cJSON *root cdef bint debug def __cinit__(self,bint debug=False): self.root = NULL self.debug = debug  def __dealloc__(self): if self.root is not NULL:			cyJSON.cJSON_Delete(self.root)  cdef bint _loads(self, str input): if self.root is not NULL: cyJSON.cJSON_Delete(self.root)  cdef char *out self.root = cyJSON.cJSON_Parse(input) if self.root is NULL:			printf("[-]Error: \n\tSTART\n\t\t%s .\n\tEND\n",cyJSON.cJSON_GetErrorPtr()) return False 
 return True  cpdef bint loads(self, str input,bint check=True): if check:input = input.replace('\'','\"')  return self._loads(input)	
 cdef list _keys(self,cyJSON.cJSON *base=NULL): cdef unsigned int i cdef cyJSON.cJSON *subitem = NULL cdef list result = []  if base is NULL: base = self.root
 if base.type == cJSON_Object: for i in range(<int>cyJSON.cJSON_GetArraySize(base)):				subitem = cyJSON.cJSON_GetArrayItem(base,i) if self.debug: printf(" sub: %d ( base:%d ) ",subitem.type,base.type)				result.append(<bytes>subitem.string.decode('UTF-8'))  return result
 cpdef bint modify(self): #TODO pass
 cdef bint _haskey(self, str item, cyJSON.cJSON *base=NULL): cdef unsigned int i cdef cyJSON.cJSON *subitem = NULL
 if base is NULL: base = self.root if cyJSON.cJSON_HasObjectItem(base,item): return True
 return False  cpdef bint haskey(self, str item): self._check_root() return self._haskey(item)  cpdef object get_type(self,str item): cdef cyJSON.cJSON *subitem = NULL cdef object result = None
 if cyJSON.cJSON_HasObjectItem(self.root,item):			subitem = cyJSON.cJSON_GetObjectItem(self.root,item) if subitem is not NULL:				result = GLOBAL_TYPE[subitem.type] return result
 cdef dict __get_info(self, cyJSON.cJSON *base): cdef cyJSON.cJSON *temp = NULL cdef dict result = {}
		result["size"] = <int>cyJSON.cJSON_GetArraySize(base)		result["keys"] = self._keys(base)		result["types"] = [] for i in range(cyJSON.cJSON_GetArraySize(base)):			temp = cyJSON.cJSON_GetArrayItem(base,i) if temp is not NULL:				result["types"].append(GLOBAL_TYPE[temp.type])
 return result
 cpdef object root_info(self): return self.__get_info(self.root)  cpdef object get(self, object item,bint raw=False,bint info=False): self._check_root() cdef cyJSON.cJSON *base = NULL cdef cyJSON.cJSON *temp = NULL cdef object result = None
 if raw:			base = <cyJSON.cJSON *>self._get_raw(item) if base is NULL: raise cyJSON_Panic("root is invalid.") if base != self.root: if info: return self.__get_info(base) else: return self._proc_item(base)				 elif base == self.root: return result  return self._get(item)  cdef object _get(self,object item): cdef cyJSON.cJSON *subitem = NULL cdef bint _has_key = self._haskey(item,self.root) cdef object result = None
 if _has_key:			subitem = cyJSON.cJSON_GetObjectItem(self.root,item) if subitem is not NULL:				result = self._proc_item(subitem)  return result
 cdef cyJSON.cJSON* _get_raw(self, tuple item, cyJSON.cJSON *base=NULL) except NULL: cdef cyJSON.cJSON *subitem = NULL cdef object i = None
 if base is NULL: base = self.root  for i in item: if self.debug: print i, type(i) if type(i) == types.StringType or type(i) == types.UnicodeType: if <bint>self._haskey(i,base) == True:					base = cyJSON.cJSON_GetObjectItem(base,i) else: raise cyJSON_Key_Error("Invalid key: {}".format(i)) elif type(i) == types.IntType: if base.type == cJSON_Array: if i >= 0 and i < cyJSON.cJSON_GetArraySize(base):						base = cyJSON.cJSON_GetArrayItem(base,i) else: raise cyJSON_Index_Error("Invalid index on {} object: {}".format(str(GLOBAL_TYPE[base.type]),str(i))) elif base.type == cJSON_Object: if <bint>cyJSON.cJSON_HasObjectItem(base,i) == True:						base = cyJSON.cJSON_GetObjectItem(base,i) else: raise cyJSON_Index_Error("Invalid index on {} object: {}".format(str(GLOBAL_TYPE[base.type]),str(i)))				
 return base
#	cpdef object get_raw(self,object item):#		self._check_root()#   cdef cyJSON.cJSON *base = NULL#		base = self._get_raw(item)#   return self._proc_item(base)
 cdef __get_string(self, cyJSON.cJSON *item): return <bytes>item.valuestring.decode("UTF-8")
 cdef __get_num(self, cyJSON.cJSON *item): return <int>item.valueint  cdef __get_bool(self, cyJSON.cJSON *item): if item.type == 0: return False elif item.type == 1: return True
 cdef __get_list(self, cyJSON.cJSON *item): cdef cyJSON.cJSON *temp = NULL cdef list result = []
 for i in range(cyJSON.cJSON_GetArraySize(item)):			temp = cyJSON.cJSON_GetArrayItem(item,i) if temp is not NULL:				result.append( self._proc_item(temp) )
 return result
 cdef __get_object(self, cyJSON.cJSON *item): cdef cyJSON.cJSON *temp = NULL cdef dict result = {}
 for i in range(cyJSON.cJSON_GetArraySize(item)):			temp = cyJSON.cJSON_GetArrayItem(item,i) if temp is not NULL:				result[ <bytes>temp.string.encode("UTF-8") ] = self._proc_item(temp)
 return result
 cdef _proc_item(self, cyJSON.cJSON *item): cdef object result = None if item.type == cJSON_String: return self.__get_string(item)  elif item.type == cJSON_False: return self.__get_bool(item)  elif item.type == cJSON_Array: return self.__get_list(item)
 elif item.type == cJSON_Number: return self.__get_num(item)
 elif item.type == cJSON_Object: return self.__get_object(item)
 cpdef object get_root(self): self._check_root() return self._proc_item(self.root)  cpdef list get_keys(self): self._check_root() return self._keys()
 cpdef void print_json(self): self._check_root() 		printf("%s",cyJSON.cJSON_Print(self.root))
 cpdef void _check_root(self): if self.root is NULL: raise Exception("JSON is not loaded or invalid. You are on your own.")
 cpdef bint delete(self, str item): self._check_root() if cyJSON.cJSON_HasObjectItem(self.root,item):			cyJSON.cJSON_DeleteItemFromObject(self.root,item)
 def __lshift__(self, item): return self.loads(item,check=True)
 def __rshift__(self, item): return self.get(item,raw=True,info=True)
 def __call__(self,item,*args,**kwargs): return self.get(item,raw=True,*args,**kwargs)