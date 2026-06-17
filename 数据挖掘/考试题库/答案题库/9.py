'''
9、加载乳腺癌数据集，按7:3划分训练集和测试集。分别构建逻辑回归、决策树（criterion='entropy'）、SVM（kernel='rbf'）三个基分类器，然后使用软投票（soft voting）将它们集成。输出每个基分类器及投票集成器的准确率、精确率、召回率，并绘制柱状图进行对比。
要求：
所有模型使用相同的随机种子（42）
柱状图标题为 "各模型性能对比"
三个评估指标使用不同颜色的柱子分组显示
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
# import load_datasets

plt.rcParams['font.sans-serif'] = ['SimHei']

from sklearn.datasets import load_breast_cancer
X, y = load_breast_cancer(return_X_y=True)
# X, y = load_datasets.get_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 定义模型，SVM 必须配概率！
clf1 = LogisticRegression(random_state=42)
clf2 = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf3 = SVC(kernel='rbf', probability=True, random_state=42) 
voting_clf = VotingClassifier(estimators=[('lr', clf1), ('dt', clf2), ('svm', clf3)], voting='soft')

models = {'逻辑回归': clf1, '决策树': clf2, 'SVM': clf3, '软投票': voting_clf}
metrics = {'Acc': [], 'Pre': [], 'Rec': []}

# 循环批改卷子
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    metrics['Acc'].append(accuracy_score(y_test, y_pred))
    metrics['Pre'].append(precision_score(y_test, y_pred))
    metrics['Rec'].append(recall_score(y_test, y_pred))

# 极简对称画图法
x = np.arange(4)
w = 0.25

plt.figure(figsize=(10, 6))
plt.bar(x - w, metrics['Acc'], width=w, label='准确率')
plt.bar(x,     metrics['Pre'], width=w, label='精确率')
plt.bar(x + w, metrics['Rec'], width=w, label='召回率')

plt.xticks(x, list(models.keys()))
plt.title("各模型性能对比")
plt.legend()
plt.show()