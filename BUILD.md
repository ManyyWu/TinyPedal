# Windows 本地构建流程

## 1. 前置条件

- 安装 Git
- 安装 Microsoft Store 安装 Python Install Manager，终端能够运行 `pymanager`。
- 源码位于 `/cygdrive/d/Projects/TinyPedal`。

## 2. 项目路径内安装 Python

```bash
cd /cygdrive/d/Projects/TinyPedal

pymanager list --online 3.10
pymanager install 3.10 --target="./.python"
./.python/python.exe -m ensurepip --upgrade

./.python/python.exe --version
./.python/python.exe -c "import sys, struct; print(sys.executable); print('bits:', struct.calcsize('P') * 8)"
```

确认解释器位于当前项目的 `.python` 内，且输出 `bits: 64`。

## 3. 安装运行依赖和构建工具

```bash
./.python/python.exe -m pip install --upgrade pip
./.python/python.exe -m pip install -r requirements.txt
./.python/python.exe -m pip install py2exe
./.python/python.exe -m pip check
```

## 4. 初始化遥测子模块

```bash
git submodule update --init --recursive
git submodule status
```

## 5. 验证源码运行

```bash
./.python/python.exe run.py
```

也可双击项目内的 `run-local.cmd` 启动源码版。

RF2 的数据读取另需游戏侧安装并启用 `rFactor2SharedMemoryMapPlugin64.dll`。

## 6. 完整打包

退出源码运行的 TinyPedal，在项目根目录执行：

```bash
./.python/python.exe freeze_py2exe.py --clean
```

## 7. 验证打包结果

主要产物：

```text
dist/TinyPedal/
├─ tinypedal.exe
├─ lib/
│  └─ library.zip
├─ platforms/
├─ mediaservice/
├─ images/
└─ docs/
```

# 同步`TinyPedal/TinyPedal`

添加官方仓库：

```bash
cd /cygdrive/d/Projects/TinyPedal

git remote add upstream https://github.com/TinyPedal/TinyPedal.git
git remote -v
```

合并最新代码：

```bash
git submodule sync --recursive
git submodule update --init --recursive
git fetch --no-recurse-submodules upstream
git merge upstream/master
```