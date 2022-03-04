# 두 리스트 비교해서 서로 포함안하고 있는 값만 새로 저장
lost=[2,4]
reserve=[1,4,5]
_reserve = [r for r in reserve if r not in lost]
# 1,5