1，将要编辑的图片放入pic文件夹下面。
2. 按图片顺序在string.txt 下面编辑对应的字体
3. 执行 generateFnt.py   会生成 对应的图片和fnt文件。

QA：若执行之后出现大量图片，则修改 config/configModel.bmfc 文件下面34行，35行（ outWidth=256  outHeight=64） 这是生成图片的大小，若你需要
生成的png太大，bmfont 会默认拆分成很多小图。此时改大尺寸即可。