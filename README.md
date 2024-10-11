# auto_star
自动点击github_star

# 运行代码部分
# 需要手动改定的部分
# 1. 需要点击的坐标，使用如下代码得到
 document.addEventListener('click', function(event) {  
    const x = event.clientX;  // 获取相对于视口的X坐标  
    const y = event.clientY;  // 获取相对于视口的Y坐标  
    
     console.log(`X坐标: ${x}, Y坐标: ${y}`);   });
# 该代码需要先在页面右击鼠标，点击检查，然后点击console打开控制台页面，需要输入allow paste允许粘贴之后，复制代码运行，代码会报错，不用管
# 然后关闭刚刚的控制台，点击star，再打开控制台，会输出star位置的坐标，请你记录下来坐标，在auto_star函数的ac.move_to(ele_or_loc=(1379,132),duration=0.85).click()这一行把坐标修改。
# 2.修改github——link为自己的link
# 3. 修改chrome_path为自己的chrome path
# 注意！！！！不要放大页面，修改页面，保持默认设置
