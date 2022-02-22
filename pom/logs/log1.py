#学习日志
# 几个组件
# 1.loggers:日志器  程序的入口  别的文件想要调用日志
# 2.handlers:处理器  日志信息 显示到哪里  多个
# 3.formatter:格式器 日志信息详细  格式变得准确好看
# 封装日志  日志组件
import logging

def test_log():
    # 日志器  创建日志器
    logger=logging.getLogger()
    # 设置级别  从哪个级别开始
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        # 指定日志信息显示在哪里 哪个组件 控制台  文本文件  处理器
        # 创建处理器  控制台处理器
        sh=logging.StreamHandler()
        # 把日志信息添加到控制台
        logger.addHandler(sh)

        # 把日志信息显示到文本文件  可以的
        # 创建文本处理器  文件放在哪  文件地址
        fh=logging.FileHandler('log3.txt', encoding='utf-8')

        # 日志信息显示在文本文件中    日志信息保存在哪
        logger.addHandler(fh)

        # 缺少哪个步骤  格式
        # 格式器  创建格式器  设置自定义格式
        fmt='%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s'
        formatter=logging.Formatter(fmt)

        # 格式器  创建格式器  设置自定义格式
        fmt1='%(asctime)s %(filename)s %(funcName)s %(message)s'
        formatter1=logging.Formatter(fmt1)
        # 给谁设置格式
        # 给控制台设置格式
        sh.setFormatter(formatter)
        # 给文本文件设置格式
        fh.setFormatter(formatter1)
    return logger