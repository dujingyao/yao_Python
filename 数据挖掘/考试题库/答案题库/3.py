'''
加载鸢尾花数据集，按7:3划分训练集和测试集，使用KNN分类器（n_neighbors=5）进行分类。输出测试集的准确率、精确率、召回率和F1分数（使用加权平均）。同时尝试不同的k值（1,3,5,7,9），找出最优的k值并输出。
要求：
使用 StandardScaler 对特征进行标准化
输出每个k值对应的准确率
最终输出最优k值和对应的评估指标
'''
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# import load_datasets # 【考场解开此注释，导入老师的脚本】

# 1. 加载数据
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
# X, y = load_datasets.get_iris() # 【考场使用此行替代上面两行】

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. 防泄露标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test) # 绝对不能 fit

# 3. 循环找最佳 K
best_k = -1
best_acc = 0.0

for k in [1, 3, 5, 7, 9]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    
    y_pred_temp = knn.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred_temp)
    print(f"k={k}, 准确率: {acc:.4f}")
    
    # 记录最高分
    if acc > best_acc:
        best_acc = acc
        best_k = k

# 4. 用最佳 K 输出全部指标
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(X_train_scaled, y_train)
y_pred_best = best_knn.predict(X_test_scaled)

print(f"\n最优 k 值为: {best_k}")
print(f"精确率: {precision_score(y_test, y_pred_best, average='weighted'):.4f}")
print(f"召回率: {recall_score(y_test, y_pred_best, average='weighted'):.4f}")
print(f"F1分数: {f1_score(y_test, y_pred_best, average='weighted'):.4f}")