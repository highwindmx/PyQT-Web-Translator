# PyQT-Web-Translator
借用几大网页翻译做个简单的词典

## 先上图
<img src="https://raw.githubusercontent.com/highwindmx/PyQT-Web-Translator/master/Demo/Snipaste_2018-05-19_23-05-20.png" width=600>

## 下一步

看看能不能对几个开源的离线词典做个解析

#### 如果用pyinstaller编译后出现如下错误

``` 
This application failed to start because it could not find or load the Qt platform plugin "windows"
in "".
Reinstalling the application may fix this problem.
``` 

#### 解决方法非常简单
比如编译好的路径是： ..path..\dist\MD_WEB_Translator（也就是可执行文件的根目录），那么就把..path..\dist\MD_WEB_Translator\PyQt5\Qt\plugins\路径下的 platforms 文件夹 直接复制到..path..\dist\MD_WEB_Translator（可执行文件根目录）下，再双击试试，就OK啦。
