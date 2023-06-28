a = {"이름": "소연", "나이": 20, "직업": "래퍼"}
b = {"이름": "민니", "나이": 18, "직업": "가수"}

print(a['나이'])

for key in a.keys():
    print(key)

for value in a.values():
    print(value)

gangsa = [{"이름":"김도언","나이":20,"직업":"강사","일일퀴즈성적":[10,20,30]},
{"이름":"이예원", "나이":21, "직업": "멘토", "일일퀴즈성적":[9,19,19]}]
gangsa_add_info={"회사":"이스트소프트", "강의기수":"2기"}

for i in gangsa:
    i.update(gangsa_add_info)

print(gangsa)