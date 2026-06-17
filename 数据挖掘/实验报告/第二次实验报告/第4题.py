import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def main():
    dataset = [
        ['牛奶', '面包', '尿布'],
        ['可乐', '面包', '尿布', '啤酒'],
        ['牛奶', '尿布', '啤酒', '鸡蛋'],
        ['面包', '牛奶', '尿布', '啤酒'],
        ['面包', '牛奶', '尿布', '可乐']
    ]
    
    print("----- 经典的购物篮事务数据集 -----")
    for i, transaction in enumerate(dataset):
        print(f"T{i+1}: {transaction}")
        
    # 1. 数据预处理
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df_bool = pd.DataFrame(te_ary, columns=te.columns_)

    # 2. 获取频繁项集
    print("\n[开始获取频繁项集... (min_support=0.4)]")
    frequent_itemsets = apriori(df_bool, min_support=0.4, use_colnames=True)
    
    if frequent_itemsets.empty:
        print("未找到满足最小支持度的频繁项集。")
        return
        
    print("\n---------- 获取到的频繁项集 ----------")
    print(frequent_itemsets.sort_values(by="support", ascending=False).to_string(index=False))

    # 3. 挖掘关联规则 
    print("\n[开始生成关联规则... (min_confidence=0.7)]")
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
    
    if rules.empty:
        print("未找到满足条件的关联规则。")
        return
    
    print("\n---------- 挖掘出的关联规则 ----------")
    # 只提取重要列进行展示
    cols_to_show = ['antecedents', 'consequents', 'support', 'confidence', 'lift']
    rules_show = rules[cols_to_show].sort_values(by='confidence', ascending=False)
    print(rules_show.to_string(index=False))

if __name__ == '__main__':
    main()
