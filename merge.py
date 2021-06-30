import pandas as pd

xls1=r'160动集车配件.xls'
xls2=r'2021年成都车辆成交厂家物资明细表.xls'

df1 = pd.read_excel(xls1)
df2 = pd.read_excel(xls2)

df1.columns=['序号', '项目名称', '物资编码', '物资名称', '规格型号', '图号', '材质', '计量单位',
       '厂家或品牌', '数量', '供货期限', '到货地点', '不含税单价', '税率（%）', '不含税总金额', '备注']

df2["物资编码"]=df2["物资编码"].astype(str)
df1["物资编码"]=df1["物资编码"].astype(str)

res1=pd.merge(df1,df2[['物资编码','成交价（元）','成交厂家']],how='left',on=['物资编码'])
res2=pd.merge(df1,df2[['物资编码','成交价（元）','成交厂家','规格型号']],how='left',on=['规格型号'])

vendor = [res1["成交厂家"][i] if res1["成交厂家"][i] else res2["成交厂家"][i] for i in range(len(res2["成交厂家"]))]
price = [res2["成交价（元）"][i] if res2["成交价（元）"][i] else res1["成交价（元）"][i] for i in range(len(res2["成交价（元）"]))]

df1["成交厂家"]=vendor
df1["成交价（元）"]=price
# df1["厂家或品牌"]=df1["成交厂家"]
df1.to_excel('160动集车配件询价结果.xlsx',index=False)