'''
12、加载乳腺癌数据集，按7:3划分训练集和测试集，使用高斯朴素贝叶斯（GaussianNB）进行分类。输出测试集准确率，绘制混淆矩阵热力图，并生成分类报告（精确率、召回率、F1分数）。将分类报告以表格形式打印输出。
要求：
混淆矩阵热力图使用 seaborn.heatmap
热力图标题为 "朴素贝叶斯分类混淆矩阵"
在热力图上标注每个格子的具体数值
分类报告输出包含每个类别的精确率、召回率、F1分数
'''
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# import load_datasets

plt.rcParams['font.sans-serif'] = ['SimHei']

from sklearn.datasets import load_breast_cancer
X, y = load_breast_cancer(return_X_y=True)
# X, y = load_datasets.get_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 贝叶斯极其简单，没有乱七八糟的参数
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)

print(f"准确率: {accuracy_score(y_test, y_pred):.4f}")
print("分类报告:\n", classification_report(y_test, y_pred))

# 算混淆矩阵并画热力图
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
# annot=True 让格子里显示具体数字，fmt='d' 保证是整数格式
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')

plt.title("朴素贝叶斯分类混淆矩阵")
plt.show()