from file_util import read_csv_file
import pandas as pd
import show_tables

data = read_csv_file("./SuicideChina.csv")

# 筛选出死亡的记录
died_df = data[data['Died'] == 'yes']

# # 按年份统计死亡人数
# yearly_death_count = died_df.groupby('Year').size().reset_index(name='Death_Count')
#
# show_tables.show_bar(yearly_death_count)
#
# # 统计自杀性别和人数关系
# sex_death_count = data[data['Died'] == 'yes'].groupby('Sex').size().reset_index(name='Death_Count')
#
# show_tables.show_pie_chart(sex_death_count)
#
# # 统计自杀职业和人数关系
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



# 2. 按年份统计死亡人数
yearly_death_count = died_df.groupby('Year').size().reset_index(name='Death_Count')
show_tables.show_bar(yearly_death_count)

# 3. 统计自杀性别和人数关系
sex_death_count = died_df.groupby('Sex').size().reset_index(name='Death_Count')
show_tables.show_pie_chart(sex_death_count)

# 4. 统计自杀职业和人数关系
occupation_death_count = died_df.groupby('Occupation').size().reset_index(name='Death_Count')
show_tables.show_line_chart(occupation_death_count)

# 5. 获取每种方法的自杀人数
method_death_count = died_df.groupby('method').size().reset_index(name='Death_Count')
show_tables.show_area_chart(method_death_count)

# 6. 按年龄段统计自杀人数
age_bins = [0, 20, 40, 60, 80, 100]
age_labels = ['0-20', '21-40', '41-60', '61-80', '81+']
died_df['AgeGroup'] = pd.cut(died_df['Age'], bins=age_bins, labels=age_labels, right=False)
age_group_death_count = died_df.groupby('AgeGroup').size().reset_index(name='Death_Count')
show_tables.show_age_group_bar(age_group_death_count)

# 7. 按教育水平统计自杀人数
education_death_count = died_df.groupby('Education').size().reset_index(name='Death_Count')
show_tables.show_education_bar(education_death_count)

# 8. 按月份统计自杀人数
monthly_death_count = died_df.groupby('Month').size().reset_index(name='Death_Count')
show_tables.show_monthly_line_chart(monthly_death_count)

# 9. 城市与农村自杀人数对比
urban_rural_death_count = died_df.groupby('Urban').size().reset_index(name='Death_Count')
show_tables.show_urban_rural_pie_chart(urban_rural_death_count)