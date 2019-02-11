import pandas as pd

"""
假设现在我们有一组从2006年到2016年1000部最流行的电影数据，我们想知道
这些电影数据中评分的平均分，导演的人数等信息，我们应该怎么获取？
DataFrame 也有平均值mean，中值median，最大值/最小值索引argmax/argmin，最大值/最小值max/min
"""

file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
print(df.loc[:, "Actors"])  # 可以看到演员表，不同演员之间以逗号分隔
print(df.info())

# 获取电影的平均评分
print(df["Rating"].mean())

# 获取导演的人数
print(df["Director"].tolist())
print(len(set(df["Director"].tolist())))  # 转换为set，构造无序不重复元素集，找出不重复的导演人数
print(len(df["Director"].unique()))

# 获取演员的人数
temp_actor_list = df["Actors"].str.split(", ").tolist()
actors_list = [i for j in temp_actor_list for i in j]  # 嵌套的循环，遍历每一个演员，并展开成一个列表
#  actors_list = np.array(temp_actor_list).flatten()  # flatten展开，依然是嵌套的列表，不能使用
actors_num = len(set(actors_list))
print(actors_num)