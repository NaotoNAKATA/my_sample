
from docx import Document
from docx.shared import Cm

file_name = 'test.docx'

doc = Document()

p = doc.add_paragraph('新しい段落')
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True

doc.add_page_break()

bmp = 'サンプル.bmp'
doc.add_picture( bmp , width=Cm(6.3) )


doc.save(file_name)
