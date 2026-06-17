import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# 1. 加载数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# 2. 自定义训练集和测试集比例（例如 80%训练，20%测试）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 建立SVM模型
svm = SVC(kernel='rbf', random_state=42)
svm.fit(X_train, y_train)

# 4. 预测
y_pred = svm.predict(X_test)

# 5. 根据混淆矩阵输出准确率、召回率、查准率和F1 Score
cm = confusion_matrix(y_test, y_pred)
# 准确率 (Accuracy): 所有预测正确的样本 / 总样本数
accuracy = np.trace(cm) / np.sum(cm)

print("混淆矩阵:\n", cm)
print(f"\n整体准确率(Accuracy): {accuracy:.4f}\n")

# 计算各类的Precision, Recall, F1
precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average=None)

for i, class_name in enumerate(target_names):
    print(f"类别: {class_name} ({i})")
    print(f"  查准率(Precision) : {precision[i]:.4f}")
    print(f"  召回率(Recall)    : {recall[i]:.4f}")
    print(f"  F1-Score          : {f1[i]:.4f}\n")

# 可视化混淆矩阵
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=target_names, yticklabels=target_names)
plt.title("SVM 混淆矩阵")
plt.xlabel("预测值")
plt.ylabel("真实值")
plt.show()