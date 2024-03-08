import re
import json
from ie2instruction.eval.extracter.extracter import Extracter


class KGExtracter(Extracter):
    def __init__(self, language="zh", NAN="NAN", prefix="输入中包含的关系三元组是：\n", Reject="No relation triples found."):
        super().__init__(language, NAN, prefix, Reject)
    

    def post_process(self, result):   
        try:      
            rst = json.loads(result)
        except json.decoder.JSONDecodeError:
            print("json decode error", result)
            return False, []
        if type(rst) != dict:
            print("type(rst) != dict", result)
            return False, []
        new_record = []
        for key, values in rst.items():  # entity_type
            if type(key) != str or type(values) != dict:
                print("type(key) != str or type(values) != dict", result)
                continue
            for key1, values1 in values.items():   # entity, attributes
                if type(key1) != str or type(values1) != dict:
                    print("type(key1) != str or type(values1) != dict", result)
                    continue
                for key2, values2 in values1.items(): # key, value
                    if type(values2) == list:
                        for iit in values2:
                            new_record.append((key1, key2, iit))
                    elif type(values2) == str:
                        new_record.append((key1, key2, values2))
        return True, new_record

