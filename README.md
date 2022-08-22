<div align="center">

# nonebot-plugin-course
### ✨*基于Nonebot2的课表查询插件*✨
</div>
<div align="center">
<img src="https://img.shields.io/badge/python-3.8.10-green" alt="python"> <img src="https://img.shields.io/badge/license-MIT-blue" alt="license">
</div>

## 💡写在前面

特别感谢[hamo](https://github.com/hamo-reid)的[*nonebot_plugin_PicMenu*](https://github.com/hamo-reid/nonebot_plugin_PicMenu)提供的图片生成工具img_tool和很多思路

算是菜鸡写的第一个完整的工程项目，代码似乎十分屎山，之后有空再重构，所以有什么改进建议或者在使用时遇到bug，欢迎狠狠地提Issue

## 🔔功能
 
* 📖完整课表
* 📙本周课表
* 🧾下周课表
* 🔍查询指定周数课表
* 🕑查询当前在上什么课，今天还有没有课
* 📆支持设定周数
* 📌添加课表过程简单，与主流课表app流程无太大区别

    #### 🎯To_do

    ⬜︎ 如果今天没课了，跨天或跨周查询离现在最近的一节课还有多久（课少的时候看着很赏心悦目

    ⬜︎ 相同课的表格合并

    ⬜︎ 优化添加课程时的逻辑与繁琐度

    ⬜︎ 保姆式式开箱即用
    <!-- ☑︎ -->

    ### 暂时不会考虑添加的功能
    - 用响应器添加课表：因为一周内的课十分的多，多的时候会添加5×13次，而这都需要一次一次地在聊天框输入后发送，在群组里也十分地刷屏。

## 💿如何使用
### 下载
#### 方法一


#### 方法二
- Step1
    ```
    pip install nonebot_plugin_course
    ```
- Step2
  在`pyproject.toml`里的`plugins = []`添加`"nonebot_plugin_course"`

### 初次使用
1. 上一步完成以后启动一次bot，会自动在根目录的`/data`文件夹(即`bot.py`所在文件夹)下生成一个`course_config`的的文件夹
   
2. 打开里面的`config.json`文件，将"default"字段的值改为任意字体的路径，字体格式为[PIL.ImageFont.truetype](https://pillow.readthedocs.io/en/stable/reference/ImageFont.html?highlight=truetype#PIL.ImageFont.truetype)所支持的字体，比如将第一行改为`"default": "simhei.ttf"`

3. 保存json文件后就可以快乐地添加课表了

# (待续)
