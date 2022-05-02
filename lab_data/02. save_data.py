import pandas as pd
import os

# 만약 data 폴더가 없다면
if not os.path.exists('../data'):
    # 폴더를 만들어 준다
    os.mkdir('../data')

titles = ['제목 1', '제목 2', '제목 3']

# 엑셀과 유사하게 되어있음
data = pd.DataFrame({'title': titles})
# 한글이 포함되어 있다면 인코딩이 필요.!
data.to_csv('../data/titles.cvs', encoding='utf-8')
