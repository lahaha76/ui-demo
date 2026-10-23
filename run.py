import time
import os
import shutil
import subprocess
import pytest

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    temp_result = os.path.join(base_dir, "allure-results")

    if os.path.exists(temp_result):
        shutil.rmtree(temp_result)

    ts = time.strftime("%Y%m%d_%H%M%S")
    report_name = f"allure_report_{ts}"
    report_dir = os.path.join(base_dir, "reports", report_name)
    os.makedirs(report_dir, exist_ok=True)

    print(f"【调试】原始数据目录：{temp_result}")
    print(f"【调试】报告目录：{report_dir}")

    pytest.main(["tests/test_login.py", "-v", "-s", "--alluredir", temp_result])

    allure_bat = r"D:\gong\test\baogao\allure-2.24.0\allure-2.24.0\bin\allure.bat"
    cmd = [
        allure_bat,
        "generate",
        temp_result,
        "-o",
        report_dir,
        "--clean"
    ]
    print(f"【调试】执行命令：{cmd}")
    try:
        # shell=False，列表传参，规避引号+编码问题
        ret = subprocess.run(cmd, shell=False, capture_output=True, text=True, encoding="utf-8")
        print("stdout：", ret.stdout)
        print("stderr：", ret.stderr)
        print(f"【调试】返回码：{ret.returncode}")

        index_path = os.path.join(report_dir, "index.html")
        if os.path.exists(index_path):
            print(f"✅ 报告成功！ {index_path}")
        else:
            print("❌ 目录存在，无 index.html")
    except Exception as e:
        print("执行异常：", e)
