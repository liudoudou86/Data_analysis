# -*- encoding=utf8 -*-

import pandas as pd


def data():
	data = pd.DataFrame(pd.read_excel('before.xlsx'))
	data_order = (data.set_index(['NO','日期','平台','单号','状态','解决方案','数量','快递公司','订单编号'])
	            .stack()
				.str.split(' ', expand=True)
				.stack()
				.reset_index(drop=False)
				)
	data_order.to_excel('after_1st.xlsx') # 需要删除多余列
	
def info():
	info = pd.DataFrame(pd.read_excel('after_1st.xlsx'))
	info_order = (info.set_index(['NO','日期','平台','单号','状态','解决方案','数量','快递公司','订单编号'])
	            .stack()
				.str.split('*', expand=True)
				.reset_index(drop=False)
				)
	info_order.to_excel('after_2nd.xlsx') # 需要删除多余列
	
if __name__ == '__main__':
	info()