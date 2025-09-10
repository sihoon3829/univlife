#2_24

#딕셔너리 생성하기
dict_1 = {'name': '홍길동', 'birth': 1990, 'addr': 'KR'}
print(dict_1)
print(dict_1['birth'])

#키와 값 추가하기
dict_1['weight'] =60.5
dict_1['family'] = ['아빠', '엄마', '여동생']
print(dict_1)

#여러 키와 값을 동시에 추가하기
dict_1.update({'weight':67.8,'hobby': ['게임', '독서']})
print(dict_1)

#딕셔너리 값 변경하기
dict_1['hodby'] = ['축구','등산']
print(dict_1)

#데이터 삭제하기
del dict_1['weight']
del dict_1['birth']
del dict_1['addr']
print(dict_1)