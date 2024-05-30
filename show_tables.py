from matplotlib import pyplot as plt

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 确保负号显示正常

import numpy as np
##展示自杀人数跟年份关系
def show_bar(yearly_death_count):
    # 提取年份和死亡人数
    years = yearly_death_count['Year'].astype(str)
    death_counts = yearly_death_count['Death_Count']

    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(years, death_counts, color='skyblue')
    plt.xlabel('year')
    plt.ylabel('people_count')
    plt.title('Relationship_By_Year_People_count')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # 在每个柱顶端添加标签
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, int(yval), ha='center', va='bottom')

    plt.show()

def show_pie_chart(sex_death_count):
    """
    展示自杀性别和人数关系的饼图。

    参数:
    sex_death_count (pd.DataFrame): 包含性别和死亡人数的DataFrame。
    """
    # 提取性别和死亡人数
    labels = sex_death_count['Sex']
    sizes = sex_death_count['Death_Count']

    # 绘制饼图
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue'])
    plt.title('The relationship between gender and number of suicides')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def show_line_chart(occupation_death_count):
    """
    展示自杀人数和职业关系的折线图。

    参数:
    occupation_death_count (pd.DataFrame): 包含职业和死亡人数的DataFrame。
    """
    # 提取职业和死亡人数
    occupations = occupation_death_count['Occupation']
    death_counts = occupation_death_count['Death_Count']

    # 绘制折线图
    plt.figure(figsize=(12, 6))
    plt.plot(occupations, death_counts, marker='o', linestyle='-', color='b')
    plt.xlabel('职业')
    plt.ylabel('人数')
    plt.title('自杀人数和职业关系')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def show_area_chart(method_death_count):
    """
    展示自杀人数和方法关系的面积图。

    参数:
    method_death_count (pd.DataFrame): 包含方法和自杀人数的DataFrame。
    """
    # 提取方法和自杀人数
    methods = method_death_count['method']
    death_counts = method_death_count['Death_Count']

    # 绘制面积图
    plt.figure(figsize=(12, 6))
    plt.fill_between(methods, death_counts, color='skyblue', alpha=0.4)
    plt.plot(methods, death_counts, marker='o', linestyle='-', color='b')
    plt.xlabel('自杀方法', fontsize=12)
    plt.ylabel('人数', fontsize=12)
    plt.title('自杀人数和方法关系', fontsize=15)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def show_age_group_bar(age_group_death_count):
    """
    展示按年龄段统计的自杀人数柱状图。

    参数:
    age_group_death_count (pd.DataFrame): 包含年龄段和自杀人数的DataFrame。
    """
    # 提取年龄段和死亡人数
    age_groups = age_group_death_count['AgeGroup']
    death_counts = age_group_death_count['Death_Count']

    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(age_groups, death_counts, color='lightgreen')
    plt.xlabel('年龄段')
    plt.ylabel('人数')
    plt.title('按年龄段统计的自杀人数')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # 在每个柱顶端添加标签
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, int(yval), ha='center', va='bottom')

    plt.show()


def show_education_bar(education_death_count):
    """
    展示教育水平与自杀人数关系的柱状图。

    参数:
    education_death_count (pd.DataFrame): 包含教育水平和自杀人数的DataFrame。
    """
    # 提取教育水平和死亡人数
    education_levels = education_death_count['Education']
    death_counts = education_death_count['Death_Count']

    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(education_levels, death_counts, color='orange')
    plt.xlabel('教育水平')
    plt.ylabel('人数')
    plt.title('教育水平与自杀人数关系')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # 在每个柱顶端添加标签
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, int(yval), ha='center', va='bottom')

    plt.show()


def show_monthly_line_chart(monthly_death_count):
    """
    展示按月份统计的自杀人数折线图。

    参数:
    monthly_death_count (pd.DataFrame): 包含月份和自杀人数的DataFrame。
    """
    # 提取月份和死亡人数
    months = monthly_death_count['Month'].astype(str)
    death_counts = monthly_death_count['Death_Count']

    # 绘制折线图
    plt.figure(figsize=(10, 6))
    plt.plot(months, death_counts, marker='o', linestyle='-', color='purple')
    plt.xlabel('月份')
    plt.ylabel('人数')
    plt.title('按月份统计的自杀人数')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def show_urban_rural_pie_chart(urban_rural_death_count):
    """
    展示城市与农村自杀人数对比的饼图。

    参数:
    urban_rural_death_count (pd.DataFrame): 包含地区类型（城市/农村）和自杀人数的DataFrame。
    """
    # 提取地区类型和死亡人数
    labels = urban_rural_death_count['Urban']
    sizes = urban_rural_death_count['Death_Count']

    # 绘制饼图
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue'])
    plt.title('城市与农村自杀人数对比')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
