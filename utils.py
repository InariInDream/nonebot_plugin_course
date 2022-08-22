import time
import importlib
from PIL import Image
from pathlib import Path
import datetime
import json

from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot import logger
from pydantic import error_wrappers

from .template import DefaultTemplate, PicTemplate

"""
代码逻辑：存入数据（字典）→ 读取数据 → 填充表格 → 生成图片
"""


class DataManager(object):
    def __init__(self):
        """
        说明:初始化
        """
        self.course_data = {}

    def load_class_info(self):
        """
        说明:加载课程信息
        :return:
        """
        def load_from_json(_json_path: Path):
            """
            说明:加载json文件
            :param _json_path:
            :return:
            """
            self.course_data = json.loads(_json_path.read_text(encoding='utf-8'))

        try:
            load_from_json(Path.cwd() / 'data' / 'course_config' / 'config.json')
            logger.success(f'课表数据加载成功')
        except json.JSONDecodeError as e:
            logger.opt(colors=True).error(f'<y>课表</y> 课表数据加载失败 <c>(from json)</c>\n'
                                          f'<y>json解析失败</y>: {e}')
        except error_wrappers.ValidationError as e:
            logger.opt(colors=True).error(f'<y>课表</y> 课表数据加载失败 <c>(from json)</c>\n'
                                          f'<y>json缺少必要键值对</y>: \n'
                                          f'{e}')
        return self.course_data


class TemplateManager(object):
    def __init__(self):
        self.template_container = {'default': DefaultTemplate}  # 模板装载对象
        self.templates_path = Path.cwd() / 'menu_config' / 'template'  # 模板路径
        self.load_templates()

    def load_templates(self):  # 从文件加载模板
        template_list = [template for template in self.templates_path.glob('*.py')]
        template_name_list = [template.stem for template in self.templates_path.glob('*.py')]
        for template_name, template_path in zip(template_name_list, template_list):
            template_spec = importlib.util.spec_from_file_location(template_name, template_path)
            template = importlib.util.module_from_spec(template_spec)
            template_spec.loader.exec_module(template)
            self.template_container.update({template_name: template.DefaultTemplate})

    def select_template(self, template_name: str) -> PicTemplate:  # 选择模板
        if template_name in self.template_container:
            return self.template_container[template_name]
        else:
            raise KeyError(f'There is no template named {template_name}')


def get_weekday():
    """
    获取今天是周几
    :return: int
    """
    return datetime.datetime.now().weekday() + 1


class CourseManager(object):
    """
    说明:课表管理类
    """
    def __init__(self):
        self.cwd = Path.cwd()
        self.config_folder_make()
        self.data_manager = DataManager()
        self.template_manager = TemplateManager()
        # 上下课时间
        self.exact_time = {
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
        }

    def config_folder_make(self):
        """
        说明:创建配置文件夹
        :return:
        """
        if not (self.cwd / 'data' / 'course_config').exists():
            (self.cwd / 'data' / 'course_config').mkdir()
        if not (self.cwd / 'data' / 'course_config' / 'fonts').exists():
            (self.cwd / 'data' / 'course_config' / 'fonts').mkdir()
        if not (self.cwd / 'data' / 'course_config' / 'templates').exists():
            (self.cwd / 'data' / 'course_config' / 'templates').mkdir()
        if not (self.cwd / 'data' / 'course_config' / 'menus').exists():
            (self.cwd / 'data' / 'course_config' / 'menus').mkdir()
        if not (self.cwd / 'data' / 'course_config' / 'config.json').exists():
            with (self.cwd / 'data' / 'course_config' / 'config.json').open('w', encoding='utf-8') as fp:
                fp.write(json.dumps({'default': 'font_path'}))

    def generate_timetable_image(self, event: GroupMessageEvent, week=None) -> Image:
        """
        说明:生成完整课表图片
        :param event:
        :param week:
        :return:
        """
        self.init_user_data(event)
        if self.init_user_data(event) == -1:
            return f"暂时还没有你的数据哦，请联系超管创建一个你的课表吧"
        user_id = str(event.user_id)
        data = self.data_manager.course_data[user_id]
        template = self.template_manager.select_template('default')
        return template().generate_main_menu(data, event=event, current_week=week)

    def generate_week_image(self, event: GroupMessageEvent, week) -> Image:
        """
        生成当前周数的课表
        :param event:
        :param week:
        :return:
        """
        self.init_user_data(event)
        if self.init_user_data(event) == -1:
            return f"暂时还没有你的数据哦，请联系超管创建一个你的课表吧"
        user_id = str(event.user_id)
        data = self.data_manager.course_data[user_id]
        template = self.template_manager.select_template('default')
        return template().generate_main_menu(data, event=event, current_week=week)

    def init_user_data(self, event: GroupMessageEvent):
        """
        说明:初始化用户数据
        :param event:
        :return:
        """
        user_id = str(event.user_id)
        self.data_manager.course_data = self.data_manager.load_class_info()
        if user_id not in self.data_manager.course_data:
            self.blank_struct(event)
            return -1
        else:
            self.data_manager.course_data[user_id] = self.data_manager.load_class_info()[user_id]

    def save(self):
        """
        保存数据
        :return:
        """
        with (self.cwd / 'data' / 'course_config' / 'config.json').open('w', encoding='utf-8') as fp:
            json.dump(self.data_manager.course_data, fp, indent=4)

    def blank_struct(self, event: GroupMessageEvent):
        """
        新建user的空白课表结构存在json里
        :return:
        """
        user_id = str(event.user_id)
        course_info = {"name": "",
                       "teacher": "",
                       "classroom": "",
                       "week": []}

        # 新用户的周数默认初始化为1
        self.data_manager.course_data[user_id] = {'week': 1}
        for i in range(7):
            i += 1
            self.data_manager.course_data[user_id][str(i)] = {}
            for j in range(13):
                j += 1
                self.data_manager.course_data[user_id][str(i)][str(j)] = []
                self.data_manager.course_data[user_id][str(i)][str(j)].append(course_info)

        self.save()

    def auto_update_week(self):
        """
        更新周数
        :return:
        """
        self.data_manager.course_data = self.data_manager.load_class_info()
        tmp_data = self.data_manager.course_data
        users_list = []
        for user_id in tmp_data:
            try:
                if user_id['week']:
                    users_list.append(user_id)
            except KeyError:
                pass
        # py里面似乎没有for(auto)的语法，所以这里先添加了一次用户名单，再挨个更新周数
        for user in users_list:
            self.data_manager.course_data[str(user)]['week'] += 1
        self.save()

    def set_week(self, event, week: int):
        """
        设置周数
        :param event:
        :param week: int
        :return:
        """
        self.init_user_data(event)
        user_id = str(event.user_id)
        self.data_manager.course_data[user_id]['week'] = week
        self.save()

    def get_week(self, event):
        """
        获取周数
        :param event
        :return: int
        """
        self.init_user_data(event)
        user_id = str(event.user_id)
        return self.data_manager.course_data[user_id]['week']

    def now_course(self, event):
        """
        获取当前课程及最近的一节课(今日范围内)
        :param event:
        :return:
        """
        # 获取当前周数
        current_week = self.get_week(event)

        # 获取当前是周几
        current_weekday = get_weekday()

        # 获取当前格式化时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg = ""

        # 取前十位到日期
        current_day = now_time[:10]

        # 当前时间戳
        current_time_stamp = int(time.mktime(time.strptime(now_time, '%Y-%m-%d %H:%M:%S')))
        today_data = self.data_manager.course_data[str(event.user_id)][str(current_weekday)]
        is_in_class = 0
        next_class = 0
        for i in range(1, 14):
            # 今日上下课时间
            course_start_time = f"{current_day} {self.exact_time[str(i)]['start']}"  # 注意有空格
            course_end_time = f"{current_day} {self.exact_time[str(i)]['end']}"

            # 今日上下课时间的时间戳
            course_start_time_stamp = int(time.mktime(time.strptime(course_start_time, '%Y-%m-%d %H:%M')))
            course_end_time_stamp = int(time.mktime(time.strptime(course_end_time, '%Y-%m-%d %H:%M')))
            for course in today_data[str(i)]:
                if course_start_time_stamp <= current_time_stamp <= course_end_time_stamp\
                        and current_week in course['week']:
                    msg += f"当前您正在上第{i}节课,为{course['name']},地点为{course['classroom']}\n"
                    is_in_class = 1
                    break
            for course in today_data[str(i)]:
                if current_time_stamp < course_start_time_stamp and current_week in course['week']:
                    msg += f"今天的下一节课为{course['name']},地点为{course['classroom']}\n,上课时间为{self.exact_time[str(i)]['start']},请注意不要迟到\n"
                    next_class = 1
                    break
            if is_in_class == 1 and next_class == 1:
                break

        if is_in_class == 0:
            msg = f"当前没有正在上的课\n" + msg

        if next_class == 0:
            msg = msg + f"今天剩下没有课了哦\n"
        weekday_info = ""
        if current_weekday == 1:
            weekday_info = "星期一"
        elif current_weekday == 2:
            weekday_info = "星期二"
        elif current_weekday == 3:
            weekday_info = "星期三"
        elif current_weekday == 4:
            weekday_info = "星期四"
        elif current_weekday == 5:
            weekday_info = "星期五"
        elif current_weekday == 6:
            weekday_info = "星期六"
        elif current_weekday == 7:
            weekday_info = "星期日"
        tmp = f"当前时间为{now_time},第{current_week}周{weekday_info}\n"
        msg = tmp + msg
        return msg


# 实例化
course_manager = CourseManager()
