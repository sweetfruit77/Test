# JSON making 샘플

import json
student = {
    'id':2002324,
    'name':'홍길동',
    'history':[
        {'date':'2018-03-11','lang':'java'},
        {'date':'2018-07-23','lang':'pyhton'},
    ]
}
#JSON making
jsonString = json.dumps(student,ensure_ascii=False,indent=4)
print(jsonString)
print(type(jsonString))