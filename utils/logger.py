import logging
import os.path
from datetime import datetime

def get_logger():
    logger_info = logging.getLogger("autotest")
    # 已有处理器直接返回，避免重复添加
    if logger_info.handlers:
        return logger_info

    logger_info.setLevel(logging.INFO)
    # 项目根目录log文件夹
    base_path = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(base_path, "logs")
    os.makedirs(log_dir,exist_ok=True)
    # 日志文件名按时间
    log_file = os.path.join(log_dir, f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')

    #定义日志格式
    log_format= logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    #文件输出
    file_handler = logging.FileHandler(log_file,encoding="utf-8")
    file_handler.setFormatter(log_format)

    #控制台输出
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_format)

    logger_info.addHandler(file_handler)
    logger_info.addHandler(stream_handler)
    return logger_info

logging_info = get_logger()


