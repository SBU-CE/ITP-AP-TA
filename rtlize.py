#!/usr/bin/env python

from os import walk
from os.path import join as join_paths

B_RTL = """<div dir="rtl">"""
E_RTL = """</div>"""


def check_rtl(checking_file):
    handler = open(checking_file, mode="r", encoding="utf-8")
    file_content = handler.read()
    handler.close()
    if file_content.strip().startswith(B_RTL):
        print(f"{checking_file} is ok!")
        return

    handler = open(checking_file, mode="w", encoding="utf-8")
    modified_content = f"{B_RTL}\n\n{file_content}\n{E_RTL}\n"
    handler.write(modified_content)
    handler.close()
    print(f"mission completed!{checking_file} modified successfully!!!!=)")


def main():
    for dirpath, _, file_names in walk("./"):
        for file_name in file_names:
            if file_name.endswith(".md"):
                file_path = (join_paths(dirpath, file_name))
                check_rtl(file_path)


if __name__ == "__main__":
    main()

