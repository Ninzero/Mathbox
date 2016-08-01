# Mathbox

##概述
Mathbox是一款由Portal Research构想并开发的数学辅助计算软件，目前主要设计目为进行一元方程的求解。<br>

    目前程序由python开发，请使用python3打开。（详见后文打开方式章节）
    
##基本思路
由于多数方程的解都可以被表述为`(a*√b+c*√d)/e`(e!=0)的形式(不考虑三角方程及其他特殊方程），故可以使用迭代法获得方程的解。
##目前进展
正在进行可行性试验，我们担心由于多重迭代导致循环次数过多而使得求解变得困难无比。我们正在尝试向`(a*√b)/c`中带入编辑数值来获得近似的最长计算时间。
##文件列表
暂无
##接下来的目标
###将用户输入化为公式
* 举例来说，当用户在命程序中输入`x+√2=5`时，我们需要将该式拆分为 左边：x+√2 右边：5随后，我们需要将√变为sqrt并在正确的位置打上括号。
* 事实上完成上述步骤后，最难的是将这部分内容变为代码的一部分而不是字符串。
* 我们承认暂时没有找到这个问题的解决办法。

###对结果化简
* 根据目前的实验，我们不可避免的会获得一些诸如`（3*√16）/1`的结果。显然，该结果需要化简。
* 我们可以通过判断某变量是否等于1来省去部分内容。
* 然而对于`√27`,`18/21`之类的结果，我们正在探索化简方式，但我们相信可以很快得出方案。

##在可预见的未来内可能实现的功能
###解多元方程组
* 我们所使用的迭代法是理论上的通法，但由于未知数的增多会导致循环次数指数级的增长，多元方程组求解可能会变得不甚现实。

###支持更多方程类型
* 我们希望Mathbox在未来可以求解对数方程（其解通常为大型整数），三角方程（其解通常包括π）及其他类型的方程。

###可以添加模块
* 我们希望可以让用户（开发者）自定义模块，这意味着我们需要一个格式标准和一个主界面。

##打开方式

    请注意这部分python程序打开方式是针对使用Windows的用户编写的，使用*nix系统的用户请自己google一下，谢谢。
    
不幸的是，python的程序运行时不进行编译，这意味着它不会像C一样生成一个`.exe`文件，这同时意味着我们需要安装python才能使用它，不过相信我，这很容易。
###下载python
你可以直接[点击这里](https://www.python.org/ftp/python/3.5.0/python-3.5.0-amd64.exe "64位，版本为3.5.0")下载64位版，或[这里](https://www.python.org/ftp/python/3.5.0/python-3.5.0.exe "32位，版本号3.5.0")下载32位版，也可以前往[python官网](https://www.python.org/downloads/windows/)下载最新版本，如果你选择前往官网下载的话，请务必下载3.5.0及以上版本。

###安装python
下载完后，运行下载的安装包。<br>
请务必勾选`Add Python 3.5 to PATH`，随后，点击`install now`即可。

###运行程序
Python程序以.py作为后缀，若要运行，请按下`win`+`R`键，输入`cmd`即可打开控制台（命令行）。随后，直接键入`python`，打一个空格，再将你想要运行的.py文件拖入命令行窗口，按下`enter`即可。
