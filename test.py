import pandas as pd
import numpy as np

data = [['孙兰昌', '男', '1996']]
columns = ['姓名', '性别', '生日']

df = pd.DataFrame(data=data, columns=columns)
print(df)
