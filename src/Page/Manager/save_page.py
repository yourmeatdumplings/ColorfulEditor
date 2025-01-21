from typing import Any

_save_page = {}

def save_init() -> None:  # 初始化
    global _save_page
    _save_page = {}

def set_page(key, value) -> None:
    #定义一个全局变量
    _save_page[key] = value

def get_page(key) -> Any:
    #获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return _save_page[key]
    except KeyError:
        print('读取'+key+'失败\r\n')