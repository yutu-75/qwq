import logging
import subprocess
from datetime import datetime
from threading import Thread

from superset.service_management.redis_client import cache

logger = logging.getLogger(__name__)

TIMEOUT = 3 * 24 * 60 * 60


def run_command():
    start_time = datetime.now()
    start_time_string = start_time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        cache.set('update_frontend_code_status', 2, timeout=60 * 15)

        # 执行 shell 脚本
        script = r"/home/app/test.sh"  # 替换为你的实际脚本路径
        process = subprocess.run(
            ["sh", script],
            capture_output=True,
            text=True
        )

        if process.returncode == 0:
            result = process.stdout
            cache.set('update_frontend_code_status', 1, timeout=TIMEOUT)

        else:
            result = process.stderr
            cache.set('update_frontend_code_status', 0, timeout=TIMEOUT)
        run_time = datetime.now() - start_time
        text_str = f"""
        npm run build 开始时间:\n{start_time_string}\n\n\n
        npm run build 耗时:\n{run_time}\n\n\n
   
        """ + f"npm run build 成功信息:\n{result}\n\n\n" \
            if process.returncode == 0 \
            else f"npm run build 失败信息:\n{result}\n\n\n"
        cache.set(
            'update_frontend_code_message',text_str,
            timeout=TIMEOUT
        )

        logger.info(f'{start_time_string} update_frontend_code_message: >>>>>{result}')
    except Exception as e:
        cache.set('update_frontend_code_status', 0, timeout=TIMEOUT)

        run_time = datetime.now() - start_time
        text_str = f"""
        npm run build 开始时间:{start_time_string}\n\n\n
        npm run build 运行耗时:{run_time}\n\n\n
        npm run build 失败信息:{e}\n\n\n
        """
        cache.set('update_frontend_code_message', text_str,
                  timeout=TIMEOUT)
        logger.error(f'{start_time_string} execute_command error: >>>>>{e}')


def execute_command():
    # 创建线程并执行命令
    thread = Thread(target=run_command, args=())
    thread.start()
