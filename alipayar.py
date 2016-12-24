# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter
import os,sys

position = {
    '750*1335':{'left':205,'top':638,'width':340} # 对应iPhone6的截图图片的 坐标点
}

def handlerImg(path,savepath=''):

    filename=path[path.rfind('/')+1:]
    extension=path[path.rfind('.')+1:]

    #读取图像
    im = Image.open(path)
    w=im.width
    h=im.height

    global position
    pos=position.get(str(w)+'*'+str(h))
    if pos==None:
        pos=position.get('750*1335')

    left=pos['left']
    top=pos['top']
    width=pos['width']
    #从截图中裁出线索图片
    pic=im.crop((left,top,left+width,top+width))

    # 高度偏移值
    # 这些规则完全是从图片中找出来的，不一定完全正确，凭感觉，只是为了提高准确率
    exc=2;
    for index in range(0,27):
        if index%6==0:
            exc=exc+1;
        copyandpaste(pic,exc+index*12,width)

    if ''==savepath:
        pic.show()
    else:
        pic.save(savepath+'/'+filename,extension)

def copyandpaste(pic,start,width):
    destpos=7
    hight=3
    tmp=pic.crop((0,start+(destpos-hight),width,start+destpos))
    pic.paste(tmp,(0,start+destpos,width,start+destpos+hight))
    tmp=pic.crop((0,start+destpos+destpos,width,start+destpos+destpos+destpos-hight))
    pic.paste(tmp,(0,start+destpos+hight,width,start+destpos+destpos))

def input():
    if (len(sys.argv))<2:
        print '错误：请输入图片路径\npython alipayar.py [filepath]'
        return;
    else:
        path1=sys.argv[1] # 原路径
        if os.path.isdir(path1):
            if len(sys.argv)<3:
                print '错误：请输入两个目录\npython alipayar.py [inputpath] [outputpath]'
                return
            else:
                path2=sys.argv[2] # 输入目录
                for file in os.listdir(path1):
                    path = os.path.join(path1, file).lower()
                    if path.endswith('png'):
                        handlerImg(path,path2)
        else:
            handlerImg(sys.argv[1])

if __name__ == '__main__':
    input()
