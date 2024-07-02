from caj2pdf import caj2pdf
from pdfminer.high_level import extract_text
import os,re
import glob

#定义你下载的一堆caj文件目录(最后剩下的是无法转化的caj)
caj_path = "/root/caj2txt/caj"
#可以被解析成pdf的caj文件目录
pdf_path = "/root/caj2txt/pdf"
#可以从pdf输出为txt的目录
output_path = "/root/caj2txt/txt"
#不能被转化txt的pdf目录(原因最可能是caj是扫描件，pdf也是图片形式)
error_path = "/root/caj2txt/error"

def batch_convert_to_text(caj_path):
    # 获取指定文件夹下所有的 .caj 文件路径
    caj_files = glob.glob(os.path.join(caj_path, "*.caj"))
    for caj_file in caj_files:
        # 转换为 PDF
        try:
            caj2pdf.convert_to_pdf(caj_file)
        except:
            pass
def pdf_to_text(pdf_path, output_path):
    # 读取生成pdf位置
    pdf_files = glob.glob(os.path.join(pdf_path, "*.pdf"))
    for pdf in pdf_files:
        # 构建输出文件路径，将PDF扩展名改为txt
        txt_output_path = os.path.join(output_path, re.sub(r'\.pdf$', '.txt', os.path.basename(pdf)))
        # PDF 转换为文本并保存
        try:
            text = extract_text(pdf)
        except:
            error_path_full = os.path.join(error_path, os.path.basename(pdf))
            os.rename(pdf, error_path_full)
            print(f'Error processing {pdf}')
            print(f'Moved {pdf} to {error_path_full}')
            
        with open(txt_output_path, 'w', encoding='utf-8') as f:
            f.write(text)




#开关caj转pdf
#batch_convert_to_text(caj_path)


#原作者把输出封装了当前目录
#因本人编程不是很好，只会用GPT拉屎，为了目录结构整洁，统一在最后将同一目录（./caj）下pdf移动到./pdf目录下,./txt文件不变
#源文件夹路径
source_folder = caj_path
#目标文件夹路径
destination_folder = './pdf'
#遍历源文件夹中的文件
for filename in os.listdir(source_folder):
#    如果文件是以.pdf结尾的文件，则移动到目标文件夹
   if filename.endswith('.pdf'):
       source_path = os.path.join(source_folder, filename)
       source_base = os.path.splitext(filename)[0]
       destination_path = os.path.join(destination_folder, filename)
       os.rename(source_path, destination_path)
       print(f'Moved {filename} to {destination_folder}')
       caj_filename = f"{source_base}.caj"
       caj_path = os.path.join(source_folder, caj_filename)
        # 如果同名的.caj文件存在，则删除
       if os.path.exists(caj_path):
           os.remove(caj_path)
           print(f'Deleted {caj_filename}')
       
# 开关pdf转txt
pdf_to_text(pdf_path, output_path)
