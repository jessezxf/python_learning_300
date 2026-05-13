"""
Date:2026/5/13 15:19
Author:Jesse

Python入门习题第93练：验证密码
需求：定义一个函数，验证密码是否符合规范：
1.长度位于6-20之间
2.必须包含至少1个小写字母
3.必须包含至少1个大写字母
4.必须包含至少1个数字
5.必须包含至少1个特殊字符
"""
import re

def verify_password(password):
    """
    验证密码是否符合规范
    :param password: 要验证的密码
    :return: 返回两个元素的元组，第一个元素为布尔值（true表示密码规范，false表示密码不规范）。
    第二个元素是字符串，若密码不规范，则提供具体原因；若规范，则为None
    """
    # 1.长度位于6 - 20之间
    if not 6<= len(password) <= 20:
        return False, "密码长度位于6-20之间"

    # 2.必须包含至少1个小写字母
    if not re.findall(r'[a-z]', password):
        return False, "密码必须包含至少1个小写字母"

    # 3.必须包含至少1个大写字母
    if not re.findall(r'[A-Z]', password):
        return False, "密码必须包含至少1个大写字母"

    # 4.必须包含至少1个数字
    if not re.findall(r'[0-9]', password):
        return False, "密码必须包含至少1个数字字符"

    # 5.必须包含至少1个特殊字符
    if not re.findall(r'[\W]', password):   #\W表示非字母、非数字、非下划线,\w表示字母、数字、下划线
        return False, "密码必须包含至少1个特殊字符"

    return True, None

print("Hello98998##", verify_password("Hello98998##"))
print("Hello98998", verify_password("Hello98998"))
print("Hellosdfs", verify_password("Hellosdfs"))







