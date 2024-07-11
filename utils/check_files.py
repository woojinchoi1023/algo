import os
from collections import defaultdict


def get_file_list():
    file_dict = defaultdict(list)
    for root, dirs, files in os.walk("./"):
        for file in files:
            if file.endswith(".py"):
                date_dir = os.path.basename(root)
                file_dict[date_dir].append(file)
    total_file_cnt = sum(len(files) for files in file_dict.values())
    return file_dict, total_file_cnt


def make_info(file_dict, total_file_cnt):
    info = f"## 문제 \n 총 개수 : {total_file_cnt}개\n"
    for date, files in sorted(file_dict.items()):
        info += f"\n### {date}\n"
        for file in sorted(files):
            file_name = os.path.splitext(file)[0]
            file_path = f"{date}/{file}"
            info += f"- [{file_name}](https://github.com/woojinchoi1023/algo/blob/main/{
                file_path})\n"
    return info


def make_read_me(info):
    return f"""# 알고리즘 공부
문제 풀이<br><br>
{info}
"""


def update_readme():
    file_dict, total_file_cnt = get_file_list()
    info = make_info(file_dict, total_file_cnt)
    readme = make_read_me(info)
    return readme


if __name__ == "__main__":
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
