import urllib.request as request
import urllib.parse as parse
import string
import re
import os
import urllib.error as error
import codecs
print("""+++++++++++++++++++++++  version: python3  +++++++++++++++++=++++""")

dirpath = 'C:\\MISC\\temp\\'

def parse_img_link(tagline):
    links = list()
    # 提取图片链接
    imgtags = re.compile('<img([^>]*)>')
    imglist = imgtags.findall(tagline)

    for img in imglist:
        #print(img)
        origsrc = re.compile(r'data-original=\"(.+?)\"')
        match = origsrc.search(img)
        if match is None:
            continue
        link = match.groups()[0]
        pattern = re.compile(r'^https://.*.jpg$')
        if pattern.match(link):
            links.append(link)
    return links          
    
def zhihu_get_jpg(url):
    if len(url)==0:
        return
    
    count = 0
    all_links = list()

    # 构造保存路径
    dirname = 'question\\'+ url[url.rindex('/')+1:]
    new_path = os.path.join(dirpath, dirname)
    if not os.path.isdir(new_path):
        os.makedirs(new_path)

    # 读取页面源文件
    #m = request.urlopen(url).read()
    #page = m.decode('utf8','ignore')

    # 载入本地的html文本
    with codecs.open(dirpath+'zhihu.txt', 'r', 'utf-8', 'ignore') as page_source:
        lines = page_source.readlines()
        print(str(len(lines)) + ' Total Lines')

    for line in lines:
        tmplist = parse_img_link(line)
        if len(tmplist) > 0:
            all_links += tmplist

    print(str(len(all_links)) + ' image links found')

    # 去除重复链接
    links = list(set(all_links))
    links.sort(key = all_links.index)
    
    print(str(len(links))+" images to be download")

    for link in links:
        try:
            image_data = request.urlopen(link).read()
            image_path = dirpath + dirname +'\\'+str(count)+'.jpg'
            print('[%(count)03d] %(link)s ====>> %(image_path)s' %{"count":count, "link":link, "image_path":image_path})
            count += 1
            with open(image_path, 'wb') as image_file:
                image_file.write(image_data)
                image_file.close()
        except error.URLError as e:
                print('Download failed')
##        
        
if __name__ == "__main__":
    url = "http://www.zhihu.com/question/39833238"
    zhihu_get_jpg(url)
    
