<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>
<div align="center">

# nonebot-plugin-course

 ✨*基于Nonebot2的课表查询插件*✨
 
</div>
<div align="center">
<img src="https://img.shields.io/badge/python-3.8.10-green" alt="python"> 
<a href="https://github.com/InariInDream/nonebot_plugin_course/blob/main/LICENSE">
<img src="https://img.shields.io/badge/license-MIT-blue" alt="license"> 
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_course">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_course?color=yellow" alt="pypi">
</a>
<a href="https://github.com/nonebot/nonebot2">
<img src="https://img.shields.io/badge/nonebot-2.0.0b4-orange" alt="nonebot2"> 
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_course">
    <img src="https://img.shields.io/pypi/dm/nonebot_plugin_course" alt="pypi download">
</a>
<a href="https://www.codefactor.io/repository/github/inariindream/nonebot_plugin_course"><img src="https://img.shields.io/codefactor/grade/github/InariInDream/nonebot_plugin_course/main?color=red"></a>

</div>


<!--ts-->
* [nonebot-plugin-course](#nonebot-plugin-course)
   * [<g-emoji class="g-emoji" alias="bulb" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4a1.png">💡</g-emoji>写在前面](#写在前面)
   * [<g-emoji class="g-emoji" alias="star2" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f31f.png">🌟</g-emoji>功能](#功能)
      * [<g-emoji class="g-emoji" alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>TODO](#todo)
      * [<g-emoji class="g-emoji" alias="negative_squared_cross_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/274e.png">❎</g-emoji>暂时不会考虑添加的功能](#暂时不会考虑添加的功能)
   * [<g-emoji class="g-emoji" alias="cd" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4bf.png">💿</g-emoji>如何使用](#如何使用)
      * [下载](#下载)
         * [方法一](#方法一)
         * [方法二](#方法二)
         * [方法三](#方法三)
      * [初次使用](#初次使用)
         * [示例](#示例)
   * [<g-emoji class="g-emoji" alias="exclamation" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2757.png">❗</g-emoji><strong>注意事项</strong>](#注意事项)
   * [<g-emoji class="g-emoji" alias="chart_with_upwards_trend" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4c8.png">📈</g-emoji>功能展示](#功能展示)
      * [指令](#指令)
   * [感谢你看到这里，如果觉得还不错的话给个star吧](#感谢你看到这里如果觉得还不错的话给个star吧)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Tue Aug 23 08:23:18 UTC 2022 -->

<!--te-->




## 💡写在前面

特别感谢[hamo](https://github.com/hamo-reid)的[*nonebot_plugin_PicMenu*](https://github.com/hamo-reid/nonebot_plugin_PicMenu)提供的图片生成工具img_tool和很多思路

算是菜鸡写的第一个完整的工程项目，代码似乎十分屎山，但作为总计写python不到两个月的人来说，我还是较为有成就感的。之后有空再重构，所以有什么改进建议或者在使用时遇到bug，欢迎狠狠地提Issue

## 更新记录

- 2022.8.28:支持不同账号设定不同的上下课时间,现在可在json文件里自动生成的"exact_time"下更改
- 2022.9.9:修复编码问题，此前在json里保存的课程名会出现乱码
- 2022.9.28:修复第13节课不能正常显示的问题（前两周没第13节课都没发现）
- 2022.9.28:新增查询第二天有无早八功能


## 🌟功能
 
* 📖完整课表
* 📙本周课表
* 🧾下周课表
* 🔍查询指定周数课表
* 🕑查询当前在上什么课，今天还有没有课
* 📆支持设定周数
* 📌添加课表过程简单，与主流课表app流程无太大区别

    ### 🎯TODO

    ☑︎ 支持不同账号设定不同的上下课时间，而非一个bot共用一套上下课时间

    ☑︎ 查询明天有无早八，好决定今晚熬不熬夜

    ⬜︎ 如果今天没课了，跨天或跨周查询离现在最近的一节课还有多久（课少的时候看着很赏心悦目

    ⬜︎ 相同课的表格合并

    ⬜︎ 自定义课表表格的行数与列数

    ⬜︎ 这个老师经常点名？在Ta上课前半小时自动提醒我

    
    <!-- ☑︎ -->

    ### ❎暂时不会考虑添加的功能
    - 用对话添加课表：因为一周内的课十分的多，多的时候会添加5×13次，而这都需要一次一次地在聊天框输入后发送，若遇传参问题会增加复杂度，反而本末倒置了。若是在群组里添加也会十分地刷屏。


## 💿如何使用

- 首先部署nonebot，具体可参照[这里](https://v2.nonebot.dev/docs/start/installation)

### 下载
#### 方法一

```
nb plugin install nonebot-plugin-course
```

#### 方法二
- Step1
    ```
    pip install nonebot_plugin_course
    ```
- Step2
  在pyproject.toml里的`plugins = []`添加`"nonebot_plugin_course"`

#### 方法三

在src文件夹下的plugin文件夹里使用`git clone`

### 初次使用
1. 上一步完成以后启动一次bot，会自动在根目录的/data文件夹(即bot.py所在文件夹)下生成一个名为course_config的文件夹

    #### **注意**：请确保自己的bot.py同级的文件夹下有一个名为data的文件夹，若没有请自行创建
    文件结构应为如下所示：
    ```
   └─ YourBotName
     │  .env
     │  .env.dev
     │  .env.prod
     │  .gitignore
     │  bot.py
     │  docker-compose.yml
     │  Dockerfile
     │  pyproject.toml
     │  README.md
     │
     ├─ __pycache__
     ├─ src
     └─ data            # 自创的名为 data 的文件夹
         └─ course_config # （将会由插件自动生成的名为 course_config 的文件夹）
    ```

   
2. 打开里面的config.json文件，将"default"字段的值改为任意字体的路径，字体格式为[PIL.ImageFont.truetype](https://pillow.readthedocs.io/en/stable/reference/ImageFont.html?highlight=truetype#PIL.ImageFont.truetype)所支持的字体，比如将第一行改为`"default": "simhei.ttf"`

3. 保存json文件后就可以快乐地添加课表了

4. 在任意一个群内发送“完整课表”，即可自动初始化当前帐号的课表结构

![](https://github.com/InariInDream/nonebot_plugin_course/blob/main/resources/2022-08-22-23-33-19.png)

![](https://github.com/InariInDream/nonebot_plugin_course/blob/main/resources/2022-08-22-23-11-43.png)

5. 根据自己的课表情况在框内填写即可

#### 示例
```json
"qq号": {
        "week": 1,
        "exact_time": {//自定义用户每节课的上下课时间
            "1": {
                "start": "08:20",
                "end": "09:05"
            },
            "2": {
                "start": "09:10",
                "end": "09:55"
            },
            ...
        },
        "1": { // 周一
            "1": [ // 第一节课
                {
                    "name": "",
                    "teacher": "",
                    "classroom": "",
                    "week": []
                }
            ],
            "2": [ // 第二节课
                {
                    "name": "",
                    "teacher": "",
                    "classroom": "",
                    "week": []
                }
            ],
            "3": [ //注意如果某天的某个位置在不同周有多节课，在列表位置以相同格式复制字典后再填写即可
                {
                    "name": "数字图像处理基础",
                    "teacher": "虞旦",
                    "classroom": "物流113",
                    "week": [
                        8
                    ]
                },
                {
                    "name": "数字图像处理基础",
                    "teacher": "王晓兰",
                    "classroom": "物流113",
                    "week": [ // 周数需一个一个填，暂不支持如"3-13"的形式填写
                        9,
                        10,
                        11,
                        12,
                        13,
                        15,
                        16
                    ]
                }
            ],
            ...
        },
        "2":{ // 周二
            ...
        },
        ...
}
```

## ❗**注意事项**

1. **不同学校的上课时间有所不同**，默认设定的时间仅代表作者的学校。因此，请**务必**确认utils.py里默认初始化的上下课时间是否与使用者的一致
    ```py
    self.data_manager.course_data[user_id] = {'week': 1,
                                                  'exact_time': {
                                                      "1": {"start": "08:20", "end": "09:05"},
                                                      "2": {"start": "09:10", "end": "09:55"},
                                                      "3": {"start": "10:15", "end": "11:00"},
                                                      "4": {"start": "11:05", "end": "11:50"},
                                                      "5": {"start": "11:55", "end": "12:25"},
                                                      "6": {"start": "12:30", "end": "13:00"},
                                                      "7": {"start": "13:10", "end": "13:55"},
                                                      "8": {"start": "14:00", "end": "14:45"},
                                                      "9": {"start": "15:05", "end": "15:50"},
                                                      "10": {"start": "15:55", "end": "16:40"},
                                                      "11": {"start": "18:00", "end": "18:45"},
                                                      "12": {"start": "18:50", "end": "19:35"},
                                                      "13": {"start": "19:40", "end": "20:25"},
                                                  },
                                                  }
    ```

2. 如果某一节课在不同周有不同的教室，建议在填写`classroom`的时候就以原始形式填写
   ```
   "classroom": "2-3:3B403,4-6:2A401"
   ```
   因为除了“完整课表”以外的查询命令，都会返回查询者的当前周数。(若在填写时以字典形式存每周对应的教室反而会增加填写难度和出错率。)

## 📈功能展示

### 指令

- **本周课表**：查看这周的课表
- **完整课表**：查看完整的课表
- **下周课表**：查看下周的课表
- **查看课表** + **周数**：查询指定周的课表
- **设置周数** + **周数**：设定当前是第几周
- **上课**：查询当前是否有课，及今天的下一节课是什么，还有多久上
- **明日早八**：查询明天是否有早八


![](https://github.com/InariInDream/nonebot_plugin_course/blob/main/resources/2022-08-22-23-20-19.png)

![](https://github.com/InariInDream/nonebot_plugin_course/blob/main/resources/2022-08-22-23-22-17.png)

![](https://github.com/InariInDream/nonebot_plugin_course/blob/main/resources/2022-08-23-11-57-14.png)

![](https://github.com/InariInDream/nonebot_plugin_course/blob/main/resources/UJP%40BUK%25TOA95TWWL97%7D%7DKT.jpg)

![](https://github.com/InariInDream/nonebot_plugin_course/blob/main/resources/2022-08-22-23-23-40.png)




## 感谢你看到这里，如果觉得还不错的话给个star吧


