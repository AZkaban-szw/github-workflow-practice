def dedupe(lst):
    """去除列表中的重复元素，保持原顺序"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
def add(a, b):
    """简单加法函数"""
    return a + b

# 更新测试代码
if __name__ == "__main__":
    test_list = [1, 2, 2, 3, 4, 4, 4]
    print(dedupe(test_list))  # 输出 [1,2,3,4]
    print(add(2, 3))  # 输出 5
