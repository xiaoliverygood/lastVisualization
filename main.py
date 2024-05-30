from file_util import read_csv_file

import show_tables

data = read_csv_file("./SuicideChina.csv")

# # 筛选出死亡的记录
# died_df = data[data['Died'] == 'yes']
#
# # 按年份统计死亡人数
# yearly_death_count = died_df.groupby('Year').size().reset_index(name='Death_Count')
#
# show_tables.show_bar(yearly_death_count)

# # 统计自杀性别和人数关系
# sex_death_count = data[data['Died'] == 'yes'].groupby('Sex').size().reset_index(name='Death_Count')
#
# show_tables.show_pie_chart(sex_death_count)

# 统计自杀职业和人数关系
# occupation_death_count = data[data['Died'] == 'yes'].groupby('Occupation').size().reset_index(name='Death_Count')
# print(occupation_death_count)
# # 展示折线图
# show_tables.show_line_chart(occupation_death_count)


# 获取每种方法的自杀人数
if data is not None:
    # 按方法统计自杀人数
    method_death_count = data.groupby('method').size().reset_index(name='Death_Count')
    print(method_death_count)
    # 展示面积图
    show_tables.show_area_chart(method_death_count)
