from os import walk
from os.path import join as join_paths

B_RTL = """<div dir="rtl">"""
E_RTL = """</div>"""

def check_rtl(checking_file):
    handler = open(checking_file,"r")
    file_content = handler.read()
    handler.close()
    if file_content.strip().startswith(B_RTL):
        print(f"{checking_file} is ok!")
        return 
    else:
        handler = open(checking_file,"w")
        modified_content =f"{B_RTL}\n{file_content}\n{E_RTL}\n"
        handler.write(modified_content)
        handler.close()
        print(f"mission completed!{checking_file} modified successfully!!!!=)")

for dirpath, _ , fnames in walk("./"):
    for f in fnames:
        if f.endswith(".md"):
            file_path =(join_paths(dirpath, f))
            check_rtl(file_path)


    
    
 
    

    
            