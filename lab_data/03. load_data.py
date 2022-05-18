import pandas as pd
# 데이터 관리 용도
# 데이터 처리의 용의한 페키지
data = pd.read_csv('../data/titles.cvs')
print(data)

titles = data['title'].values
print(titles)
