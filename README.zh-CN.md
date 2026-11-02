# TinyPedal — 模拟赛车遥测悬浮工具

[English](README.md) | 简体中文

TinyPedal 是一款自由、开源的模拟赛车遥测悬浮工具。

项目注重简洁设计、轻量与效率，支持丰富的自定义和数据分析，提供大量可配置的悬浮组件、后台数据模块，以及高级燃油计算器和编辑工具。

目前支持 `Assetto Corsa Competizione`、`Le Mans Ultimate` 和 `rFactor 2`，可在 `Windows` 与 `Linux` 上运行。

[官方版本下载](https://github.com/TinyPedal/TinyPedal/releases) ·
[快速开始](#quick-start) ·
[常见问题](https://github.com/TinyPedal/TinyPedal/wiki/Frequently-Asked-Questions) ·
[用户指南](https://github.com/TinyPedal/TinyPedal/wiki/User-Guide) ·
[Linux 运行说明](#running-on-linux) ·
[许可证](#license)

![预览](https://user-images.githubusercontent.com/21177177/282278970-b806bf02-a83d-4baa-8b45-0ca10f28f775.png)

## 本个人版本

本仓库是基于官方主线维护的个人汉化版本，不是官方中文发行版。上面的官方下载链接指向上游版本，不包含本仓库的汉化修改。

- Widget 和 Module 列表名称显示中文，悬停保留英文名称。
- Config 的选项标签、分组标题及部分操作文字显示中文，选项标签悬停保留英文。
- Config 搜索支持中文标签和英文名称；内部配置键及保存值保持不变。
- 译文集中在 `tinypedal/languages/zh_CN.py`，默认简体中文，尚未提供语言切换界面。
- 部分选项按术语组合翻译，未识别项回退为英文；缺失译文不会自动收集。其他界面和悬浮组件内部文字尚未全面汉化。

个人版本的 Windows 项目内 Python 安装、Cygwin Bash 运行及完整打包步骤见 [BUILD.md](BUILD.md)。下文保留上游 README 的全部主题与通用使用说明；其中 Python 3.8 虚拟环境是上游示例，个人环境使用 Python 3.10。

<a id="requirements"></a>
## 运行要求

### 支持的模拟器

| API | Windows | Linux |
| :--- | :--- | :--- |
| [Assetto Corsa Competizione](#setup-for-assetto-corsa-competizione) | 无需插件 | 需要第三方插件 |
| [Le Mans Ultimate](#setup-for-le-mans-ultimate) | 无需插件 | 需要第三方插件 |
| [rFactor 2](#setup-for-rfactor-2) | rF2SharedMemoryMapPlugin | rF2SharedMemoryMapPlugin（Wine） |

### 显示模式

游戏必须使用无边框（`Borderless`）或窗口（`Windowed`）模式才能显示悬浮组件，不支持独占全屏（`Fullscreen`）。

<a id="setup-for-assetto-corsa-competizione"></a>
### 配置 Assetto Corsa Competizione

#### Windows

- 访问 ACC 内置共享内存 API 无需安装插件。
- 需手动启用 ACC 内置 UDP API，以获取共享内存中没有的补充数据，步骤见下文。

#### Linux

- 可以选择 ACC 内置共享内存 API，但访问它可能需要第三方插件，参见 [讨论 #9](https://github.com/TinyPedal/TinyPedal/issues/9)。
- UDP API 的启用步骤与 Windows 相同。

#### 启用 UDP API

ACC 的车手姓名、圈速、排名等补充信息需要 UDP API。游戏默认关闭此接口，需要手动开启。

1. 在 `Documents/Assetto Corsa Competizione/Config` 中找到 `broadcasting.json`。如果不存在，先启动一次游戏，让游戏生成该文件。
2. 关闭游戏，用文本编辑器打开 `broadcasting.json`。
3. 找到 `"updListenerPort"`，将默认值 `0` 改为 `9000`，保存并关闭文件。
4. 重新启动游戏。

补充说明：

- `broadcasting.json` 中的 `"connectionPassword"` 与 `"commandPassword"` 应留空。
- `"updListenerPort"` 可以使用其他端口，但必须与 TinyPedal API 配置中的 `URL Port` 一致。详见用户指南的 [Assetto Corsa Competizione API](https://github.com/TinyPedal/TinyPedal/wiki/User-Guide#assetto-corsa-competizione-api) 章节。

<a id="setup-for-le-mans-ultimate"></a>
### 配置 Le Mans Ultimate

#### Windows

访问 LMU 内置共享内存 API 无需安装插件，但必须在游戏的 `Settings → Gameplay` 中将 `Enable Plugins` 设为 `ON`。

#### Linux

可以选择 LMU 内置 API，但访问它可能需要第三方插件，参见 [讨论 #9](https://github.com/TinyPedal/TinyPedal/issues/9)。

<a id="setup-for-rfactor-2"></a>
### 配置 rFactor 2

访问 rFactor 2 API 需要 TheIronWolf 的 [rF2 Shared Memory Map Plugin](https://github.com/TheIronWolfModding/rF2SharedMemoryMapPlugin)。

#### Windows

从 [插件下载页面](https://github.com/TheIronWolfModding/rF2SharedMemoryMapPlugin#download) 获取插件。

#### Linux

从 [Wine 插件分支](https://github.com/schlegp/rF2SharedMemoryMapPlugin_Wine/blob/master/build) 获取插件。

#### 安装插件

将 `rFactor2SharedMemoryMapPlugin64.dll` 放入游戏的 `rFactor 2/Bin64/Plugins` 目录。如果没有 `Plugins` 目录，手动创建。

#### 在游戏中启用插件

在游戏 `Settings → Gameplay` 中找到插件设置，开启 `rFactor2SharedMemoryMapPlugin64.dll`，然后重启游戏。

如果游戏未在 `CustomPluginVariables.JSON` 中生成该插件条目，请确认已安装 `VC12（Visual C++ 2013）运行库`，安装程序位于游戏的 `Support/Runtimes` 目录。

<a id="quick-start"></a>
## 快速开始

> [!IMPORTANT]
> 先按照[运行要求](#requirements)安装对应游戏需要的插件。
>
> 不要将 TinyPedal 解压到系统或游戏目录，例如 `Program Files` 或 `rFactor 2`，否则可能无法运行。
>
> 常见问题见 [FAQ](https://github.com/TinyPedal/TinyPedal/wiki/Frequently-Asked-Questions)，详细用法见[用户指南](https://github.com/TinyPedal/TinyPedal/wiki/User-Guide)。Linux 用户请参阅 [Linux 运行说明](#running-on-linux)。

1. 从上游 [Releases](https://github.com/TinyPedal/TinyPedal/releases) 下载官方版本，解压到一个干净目录并运行 `tinypedal.exe`。本个人汉化版请从本仓库源码运行或构建，方法见 [BUILD.md](BUILD.md)。
2. 程序会在系统托盘显示图标；如果看不到，检查隐藏的托盘图标。右键图标可打开菜单。
3. 启动游戏，车辆进入赛道后悬浮组件会出现，离开赛道后自动隐藏。可通过托盘菜单的 `Auto Hide` 开关自动隐藏。
4. 通过托盘菜单的 `Lock Overlay` 锁定或解锁布局。解锁后可拖动悬浮组件。
5. 在主窗口的 `Widget` 页面启用或关闭组件。主窗口隐藏时，右键托盘图标并选择 `Config` 可重新打开。
6. 退出时，选择托盘菜单的 `Quit`，或主窗口 `Overlay → Quit`。

<a id="run-from-source"></a>
## 从源码运行

### 依赖

- [Python](https://www.python.org/) 3.8、3.9 或 3.10（上游支持范围；个人版本目前主要使用 3.10 验证）。
- PySide2。
- psutil。
- [pyACCSharedMemory](https://github.com/TinyPedal/pyACCSharedMemory)。
- [pyLMUSharedMemory](https://github.com/TinyPedal/pyLMUSharedMemory)。
- [pyRfactor2SharedMemory](https://github.com/TinyPedal/pyRfactor2SharedMemory)。

> [!IMPORTANT]
> 安装依赖前先确认 Python 版本。Python 3.10 以上版本可能无法安装 PySide2，需要改用 PySide6。目前 PySide6 通过命令行选项启用，详见[命令行参数](https://github.com/TinyPedal/TinyPedal/wiki/User-Guide#command-line-arguments)。

### 获取源码

> [!NOTE]
> 不建议使用 GitHub 的 `Code → Download ZIP` 获取源码，因为其中不包含必需的子模块文件，也不便于更新或同步。

使用 [Git](https://git-scm.com/) 克隆上游源码及子模块：

```bash
git clone --recursive https://github.com/TinyPedal/TinyPedal.git
```

若需要本个人版本，改用本仓库地址：

```bash
git clone --recursive https://github.com/ManyyWu/TinyPedal.git
```

进入项目目录后更新子模块：

```bash
git submodule update --init --recursive
```

上游 `master` 是开发分支，日常使用可能不够稳定。可切换到指定发行标签，例如原文使用的 `v2.45.0`：

```bash
git checkout tags/v2.45.0
```

切回开发分支：

```bash
git checkout master
```

切换到上游发行标签也会离开当前个人汉化提交；如要保留汉化，请使用自己的分支。

### 建立开发环境

建议使用隔离环境运行与测试，尤其是在系统中安装了多个 Python 版本时。个人版本的项目内安装方案见 [BUILD.md](BUILD.md)。

下面是上游使用 Python 3.8 和内置 `venv` 的示例。先安装所需 Python 版本，再建立[虚拟环境](https://docs.python.org/3/library/venv.html)。也可以使用其他环境管理工具。

Windows 下，上游 PowerShell 示例为：

```powershell
py -3.8 -m venv '.virtualenvs\tinypedal_py38'
.virtualenvs\tinypedal_py38\Scripts\activate.ps1
```

在 Cygwin Bash 中，对应命令为：

```bash
py -3.8 -m venv .virtualenvs/tinypedal_py38
source .virtualenvs/tinypedal_py38/Scripts/activate
```

激活后继续[安装依赖](#install-dependencies)，在该虚拟环境中运行或构建 TinyPedal。后续安装依赖或运行前，也应先激活对应环境。

<a id="install-dependencies"></a>
### 安装依赖

安装额外依赖：

```bash
pip3 install PySide2 psutil
```

在项目根目录启动程序：

```bash
python run.py
```

<a id="build-executable-for-windows"></a>
## 构建 Windows 可执行程序

可通过 [py2exe](https://www.py2exe.org/) 构建可执行程序。

安装 py2exe：

```bash
pip3 install py2exe
```

执行构建：

```bash
python freeze_py2exe.py
```

产物位于 `dist/TinyPedal` 目录。

> [!NOTE]
> 构建脚本要求 py2exe `v0.12.0.0` 或更高版本，不支持 PySide6。

本个人版本的 Cygwin Bash 构建流程见 [BUILD.md](BUILD.md)。分发时需要整个输出目录，不能只复制 EXE。

<a id="running-on-linux"></a>
## 在 Linux 上运行

[从源码运行](#run-from-source)中的流程基本适用于 Linux，但依赖有所不同，此处流程不提供 Linux 可执行文件构建。

配置与数据保存在用户目录，默认位置为：

```bash
$HOME/.config/TinyPedal/
$HOME/.local/share/TinyPedal/
```

所需 Python 包为 `PySide2`、`psutil` 与 `pyxdg`。多数发行版的软件包名称带有前缀，例如 `python3-pyside2`、`python3-psutil`、`python3-pyxdg`。

部分发行版把 PySide2 拆成多个包。如果找不到 `python3-pyside2`，可安装 `python3-pyside2.qtgui`、`python3-pyside2.qtwidgets` 和 `python3-pyside2.qtmultimedia`。

也可使用 pip3 安装，但这会绕过系统包管理器，因此不作为推荐方式：

```bash
pip3 install PySide2 psutil pyxdg
```

启动命令：

```bash
./run.py
```

### 安装到系统

通过 Git 或 Linux 发行包获得可运行的程序后，可使用安装脚本安装或更新。

脚本会创建桌面启动器，并使终端可以通过 `TinyPedal` 命令启动程序。文件安装到 `/usr/local/`，需要相应写权限，例如使用 sudo。脚本不接受参数或选项：

```bash
sudo ./install.sh
```

如果要保存启动参数，例如强制使用 PySide6，可创建 `~/.config/TinyPedal/launcher.conf`，内容为：

```bash
TINYPEDAL_RUN_ARGS="--pyside 6"
```

安装后的启动器和桌面入口会自动读取该文件。这主要用于 PySide2 已被弃用的 ArchLinux。

### 已知问题

- 部分功能在 Linux 上不可用或不受支持，例如全局快捷键（`Global Hotkey`）。
- KDE 下组件未显示在游戏窗口上方：在 `Config → Compatibility` 中启用 `Bypass Window Manager`。
- 桌面合成关闭时组件不透明：在桌面环境中启用窗口管理器合成（`window manager compositing`）。

## 贡献

报告问题、提出功能请求或贡献代码前，请阅读[贡献指南](CONTRIBUTING.md)。

<a id="license"></a>
## 许可证

Copyright (C) 2022-2026 TinyPedal developers

TinyPedal 是自由软件，采用 GNU 通用公共许可证第 3 版或更新版本（GPL-3.0-or-later）。软件按现状提供，不附带任何担保。详见 [LICENSE.txt](LICENSE.txt)。

TinyPedal 图标及 `images` 目录中的图像采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)。

第三方软件许可证及声明位于 `docs/licenses`，详见 [THIRDPARTYNOTICES.txt](docs/licenses/THIRDPARTYNOTICES.txt)。

## 致谢

TinyPedal 是非营利项目，由模拟赛车爱好者与志愿者开发和维护。

开发者与贡献者名单见 [docs/contributors.md](docs/contributors.md)。
