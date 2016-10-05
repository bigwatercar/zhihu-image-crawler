# zhihu-image-crawler
知乎图片抓取小工具

先打开知乎话题页面，然后在控制台执行下面代码：

```Javascript
function getmore() {  	
  var e = $(".zg-btn-white.zu-button-more"); 	
  if (e.length!=0) { 		
      setTimeout('getmore()', 2000); 		
      e[0].click(); 		 	
      } 
} 
getmore()  	 	
```
执行后，会自动地点击“更多”，将通过Ajax加载的内容全部加载。

### 完成后，保存页面到html文件，用这段python程序解析html即可下载所有的图片。
