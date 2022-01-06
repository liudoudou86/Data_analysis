# -*- encoding=utf8 -*-

import pandas as pd

data = pd.DataFrame(pd.read_excel('before.xlsx'))
d = (data.set_index(['No.','平台']) # 以哪两列为索引
         .stack() # 将除索引列的其他列堆成行
         .str.split(' ',expand=True) # 以空格为切割为多个单元格
         .stack() # 再次堆行
         .str.split('*',expand=True) # 以*号为切割为多个单元格
         .unstack(-2)) # 索引倒数第二列成为新的列
d.to_excel('after.xlsx') # 输出到新的文档