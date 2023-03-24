#!/bin/sh

# 判断当前目录是否为 lazyconfig
if [ ! -d lazyconfig ]; then
    echo "not in lazyconfig"
    exit 1
fi

# 判断是否存在 setup.py 文件
if [ ! -f setup.py ]; then
    echo "setup.py not found"
    exit 1
fi

# 如果 build 目录存在，则删除
if [ -d build ]; then
    echo "rm -rf build"
    rm -rf build
fi

# 如果 pip list 中存在 lazyconfig, 则卸载
if [ -n "$(pip list | grep lazyconfig)" ]; then
    echo "pip uninstall lazyconfig"
    pip uninstall lazyconfig
fi

# pip 安装 lazyconfig
echo "pip install ."
pip install .

# # 判断是否存在 readme.md 文件
# if [ ! -f readme.md ]; then
#     echo "readme.md not found"
#     exit 1
# fi
