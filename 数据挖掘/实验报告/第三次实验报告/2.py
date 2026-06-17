import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# 1. 加载数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 2. 划分数据集（90%训练，10%测试）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# 3. 建立CART决策树模型 (criterion为'gini'即为CART)
clf = DecisionTreeClassifier(criterion='gini', random_state=42)
clf.fit(X_train, y_train)

# 4. 预测与评估
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"CART决策树模型准确率: {accuracy:.4f}")

# 5. 画出决策树模型
plt.figure(figsize=(15, 10))
plot_tree(clf, 
          feature_names=iris.feature_names,  
          class_names=iris.target_names,
          filled=True, 
          rounded=True,
          fontsize=12)
plt.title("CART 决策树模型")
plt.show()