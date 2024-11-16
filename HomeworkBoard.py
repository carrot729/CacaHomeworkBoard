import datetime
import json
import os
import logging

# 默认配置设置，包括模板路径、作业路径和备份后缀
DEFAULT_CONFIG = {
    "template": ".\\template",
    "homework": "{0}\\Desktop\\homework".format(os.environ['USERPROFILE']),
    "suffix": ".docx"
}

# 设置文件名
CONFIG_FILE_NAME = 'HomeworkBoard.setting.caca.json'
LOG_FILE_NAME = 'HomeworkBoard.log.caca.txt'
# 初始化配置和日志记录器
config = {}
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler(LOG_FILE_NAME)
#handler = logging.Handler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
def welcome() -> None:
    """显示欢迎信息"""
    print('''
*************************************
 ######     ###     ######     ###    
##    ##   ## ##   ##    ##   ## ##   
##        ##   ##  ##        ##   ##  
##       ##     ## ##       ##     ## 
##       ######### ##       ######### 
##    ## ##     ## ##    ## ##     ## 
 ######  ##     ##  ######  ##     ## 
*************************************
    ''')
    print('Welcome to CacaHomeworkBoard.')

def read_config() -> None:
    """读取设置文件"""
    global config
    logger.info('Reading config file')
    with open(CONFIG_FILE_NAME, "r") as f:
        config = json.loads(f.read())

def write_config() -> None:
    """初始化设置文件"""
    global config
    logger.info('Initialing config file')
    config = DEFAULT_CONFIG
    with open(CONFIG_FILE_NAME, "w") as f:
        f.write(json.dumps(DEFAULT_CONFIG, sort_keys=True, indent=4, separators=(',', ': ')))

def copy_file(src: str, dst: str) -> None:
    """
    拷贝函数
    :param src: Source file path
    :param dst: Destination file path
    """
    try:
        with open(src, 'rb') as src_file, open(dst, 'wb') as dst_file:
            dst_file.write(src_file.read())
    except FileNotFoundError:
        logger.error(f"File not found: {src}")
        exit(1)
    except PermissionError:
        logger.error(f"Permission denied: {src}")
        exit(1)
    except Exception as e:
        logger.error(f"Error copying file: {e}")
        exit(1)

def make_backup(homework: str, backup: str) -> None:
    """
    制作备份
    :param homework: homework file
    :param backup: backup file
    """
    if os.path.exists(backup):
        print('CacaHomeworkBoard was used today, do you want to OVERWRITE it (y/N):', end='')
        if input().strip().lower() not in ['y', 'yes']:
            exit(0)
    if not os.path.exists('backup'):
        os.mkdir('backup')
    logger.info('Making backup')
    copy_file(homework, backup)

def make_homework(homework: str, template: str) -> None:
    """
    刷新作业板
    :param homework: homework file
    :param template: template file
    """
    logger.info('Making homework')
    copy_file(template, homework)

def main():
    """主函数"""
    global config
    welcome()
    if os.path.exists(CONFIG_FILE_NAME):
        read_config()
    else:
        write_config()
    make_backup(config['homework']+config['suffix'], os.path.join('backup', f'{datetime.date.today()}{config["suffix"]}'))
    make_homework(config['homework']+config['suffix'], config['template']+config['suffix'])

if __name__ == '__main__':
    main()
