from caj2pdf import caj2pdf
from pdfminer.high_level import extract_text
import os,re
import glob

#定义你下载的一堆caj文件目录
caj_path = "/home/ubuntu/caj2txt/caj"

#定义你的txt输出目录
output_path = "/home/ubuntu/caj2txt/txt"

def batch_convert_to_text(caj_path):
    # 获取指定文件夹下所有的 .caj 文件路径
    caj_files = glob.glob(os.path.join(caj_path, "*.caj"))
    for caj_file in caj_files:
        # 转换为 PDF
        caj2pdf.convert_to_pdf(caj_file)

import os
import glob
import re
from pdfminer.high_level import extract_text

def pdf_to_text(caj_path, output_path):
    # 读取生成pdf位置
    pdf_files = glob.glob(os.path.join(caj_path, "*.pdf"))
    for pdf in pdf_files:
        # 构建输出文件路径，将PDF扩展名改为txt
        txt_output_path = os.path.join(output_path, re.sub(r'\.pdf$', '.txt', os.path.basename(pdf)))
        # PDF 转换为文本并保存
        text = extract_text(pdf)
        with open(txt_output_path, 'w', encoding='utf-8') as f:
            f.write(text)


#开关caj转pdf
#batch_convert_to_text(caj_path)

# 开关pdf转txt
#pdf_to_text(caj_path, output_path)

# 上一个作者把输出封装了当前目录，因本人编程不是很好，只会用GPT拉屎，为了目录结构整洁，统一在最后将同一目录（./caj）下pdf移动到./pdf目录下,./txt文件不变




