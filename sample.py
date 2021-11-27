import pandas as pd

data = pd.read_csv('C:/Users/ye303/Desktop/소프트웨어보안프로젝트/3조_prototype/menu_contents.csv', encoding = 'utf-8')

filter = data['캠퍼스 '] == '서울캠퍼스'
data2 = data[filter]
print(data2)