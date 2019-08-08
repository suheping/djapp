#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

c_dir = os.getcwd()
print('当前路径为：' + c_dir)
conf_dir = os.path.join(c_dir,'conf')
print('配置文件的路径为：' + conf_dir)
data_dir = os.path.join(c_dir,'data')
print('用例文件的路径为：'+ data_dir)
reprot_dir = os.path.join(c_dir,'report')
print('报告文件路径为：'+ reprot_dir)
case_dir = os.path.join(c_dir,'testcase')
print('testcase路径为：'+ case_dir)

api_datafile = ''
api_reportfile = ''
process_datafile = ''
process_reportfile = ''

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
