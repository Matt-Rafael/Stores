# 负责将新导出的文件归档
import os
from datetime import datetime
import shutil

# 负责移除以前导出的数据文件
def remove_excels(export_path):
    for fname in os.listdir(export_path):
        if fname.endswith("task.xlsm"):
            os.remove(os.path.join(export_path, fname))

def archive_excels(export_path):
    # 首先创建一个文件夹
    now = datetime.now()
    dirname = "%s_%s_%s_%s" % (now.year, now.month, now.day, now.hour)
    target_dir = os.path.join(export_path, dirname)
    if os.path.exists(target_dir):
        os.remove(target_dir)
    os.mkdir(target_dir)
    # 将导出的数据文件移动到目标文件夹
    for fname in os.listdir(export_path):
        if fname.endswith("task.xlsm"):
            shutil.move(os.path.join(export_path, fname), os.path.join(target_dir, fname))


