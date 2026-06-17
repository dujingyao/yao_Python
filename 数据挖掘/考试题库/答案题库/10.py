'''
10、加载手写数字数据集（digits），将所有类别为0的样本视为正常样本，其他类别为异常样本。使用隔离森林（Isolation Forest）算法进行异常检测（设置污染率为0.1）。输出检测结果的准确率、召回率、精确率，并绘制异常分数的分布直方图。
要求：
随机种子固定为42
直方图标题为 "异常分数分布"
在直方图上用垂直线标注异常阈值
输出混淆矩阵
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
# import load_datasets

plt.rcParams['font.sans-serif'] = ['SimHei']

from sklearn.datasets import load_digits
X, y_orig = load_digits(return_X_y=True)
# X, y_orig = load_datasets.get_digits()

# 1. 考卷答案标准：0变0(正常)，其它变1(异常)
y_true = np.where(y_orig == 0, 0, 1)

# 2. 预测 (无监督瞎砍)
iso = IsolationForest(contamination=0.1, random_state=42)
iso.fit(X)
y_pred_iso = iso.predict(X)

# 3. 强行翻译忍者的语言：1(正常)变0，-1(异常)变1
y_pred = np.where(y_pred_iso == 1, 0, 1)

print(f"准确率: {accuracy_score(y_true, y_pred):.4f}")
print(f"精确率: {precision_score(y_true, y_pred):.4f}")
print(f"召回率: {recall_score(y_true, y_pred):.4f}")
print("混淆矩阵:\n", confusion_matrix(y_true, y_pred))

# 4. 提取安全分数画直方图
scores = iso.decision_function(X)
plt.figure(figsize=(8, 6))
plt.hist(scores, bins=50)

# 在倒数 10% 的位置画红杠
threshold = np.percentile(scores, 10) 
plt.axvline(threshold, color='red', linestyle='--', label='异常阈值')

plt.title("异常分数分布")
plt.legend()
plt.show()