# Auto-play-XUEXITONG
自动播放学习通视频
=
简介
--
基于python，通过selenium+webdriver实现自动播放学习通中的课程视频，可连续播放无需操作。  
由于是浏览器自动操作，有绝对的安全性，不存在异常学习的风险。  
目前项目正处于初期，功能较为单一，自动化不够全面。需手动输入要播放的课程章节和小节。 
之后会不断优化代码。达到完全自动。  
目前可以自动连续播放所指定章节的小节，但不能识别视频是否已完成，不能播放小节内的多个视频。  
本人为初学者，如有错误和建议请及时指出。   
**代码需本地化修改！**  


安装要求
--
1、安装chrome浏览器  
2、下载chromedriver，用于自动操作浏览器。下载地址http://chromedriver.storage.googleapis.com/index.html 注意下载浏览器版本相对应的chromedriver    
3、python安装第三方库selenium  


使用步骤
--
1、在**path**中填入chromedriver的位置，格式实例r'D:\pycharm\new\chromedriver.exe'  
2、在url中填入课程**url**，通常以https://mooc1.chaoxing.com/mycourse/ 开头  
3、分别在**account**、**password**中填入自己的账号密码  
4、在学习通中查看未播放的课程，使用play_one()和play()  play_one()需填入 (章节，小节)；play()需填入(章节，开始的小节，**结束小节+1**)。程序会显示当前播放的视频章节和小节，时长以及预计结束时间  

注意事项
--
1、请注意selenium版本，chromedriver版本，不配会则会报错  
2、有概率会出现程序识别课程时长为0：00，导致不播放就跳转到下一个视频。重新运行一般可以解决。  
3、在程序运行时，不要在其他地方登录学习通观看课程，否则会触发异常学习。可以切出浏览器做别的事，也可最大化浏览器来观看，但尽量不要点浏览器的内容，特别是不要将视频全屏播放。  
4、所选的章节和小节中必须都是视频内容  
5、小节多个视频暂无无法全部自动播放，之后会解决。  
