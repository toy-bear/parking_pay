from asyncio.windows_events import NULL
import code
from tkinter.tix import COLUMN
from distutils.cmd import Command
from re import X
from textwrap import fill
from uu import Error
import paddlehub as hub
import sqlite3
import math
import time
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from  sqlite3 import Error
import qrcode
import tkinter . messagebox
class Utils():
    # 获取 13 位的时间戳
    def getCurrentDateLong(self):
        current_timestamp = int(round(time.time()))  # 获取当前时间的时间戳（精确到毫秒）
        return current_timestamp
class CameraApp:
    def __init__(self): 

         # 创建界面         
        self.window = tk.Tk()  # 创建一个窗口对象
        self.window.iconbitmap('login.ico')
        self.window.title("toy-bear停车收费系统")  # 设置窗口标题
        w = self.window.winfo_screenwidth()# 读取屏幕宽度
        h = self.window.winfo_screenheight()# 读取屏幕高度
        self.window.geometry("%dx%d" %(w,h))  # 设置全屏窗口 
        self.window.config(bg='#87CEEB')
    
# 创建一个主目录菜单，也被称为顶级菜单
        main_menu = tk.Menu (self.window)
        data_menu = tk.Menu(main_menu,tearoff = False)
        cap_menu = tk.Menu(main_menu,tearoff = False)
#新增命令菜单项，使用 add_command() 实现
        main_menu.add_cascade (label="摄像头",menu=cap_menu)
        cap_menu.add_command(label="打开",command=self.opencap)
        cap_menu.add_command(label="关闭",command= self.closecap)
        main_menu.add_command (label="进场识别",command=self.take_photo_in)
        main_menu.add_command (label="出场识别",command=self.take_photo_out)
        main_menu.add_command (label="进场图片",command=self.load_image)
        main_menu.add_command (label="会员充值",command=self.pay_vip)
        main_menu.add_cascade (label="数据库",menu=data_menu)
        data_menu.add_command(label='查看记录',command=self.getdatabase,accelerator='Ctrl+O')
        data_menu.add_command(label='清除记录',command=self.cleandatabase,accelerator='Ctrl+C')                      
        main_menu.add_command (label="帮助",command=self.getdatabase)
        main_menu.add_command (label="退出",command=self.window.quit)
#显示菜单
        self.window.config (menu=main_menu)
        
        self.menu_lable = tk.Label(self.window,text = "序号",width=3,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable.place(relx=0.36,rely=0.01)
        self.menu_lable1 = tk.Label(self.window ,text = "车 牌 号",width=8,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable1.place(relx=0.38,rely=0.01)
        self.menu_lable2 = tk.Label(self.window ,text = "进   场   时   间",width=15,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable2.place(relx=0.44,rely=0.01)
        self.menu_lable3 = tk.Label(self.window ,text = "出   场   时   间",width=15,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable3.place(relx=0.53,rely=0.01)
        self.menu_lable4 = tk.Label(self.window ,text = "收费时长",width=8,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable4.place(relx=0.63,rely=0.01)
        self.menu_lable5 = tk.Label(self.window ,text = "会员",width=6,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable5.place(relx=0.68,rely=0.01)
        self.menu_lable6 = tk.Label(self.window ,text = "会员开始",width=8,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable6.place(relx=0.71,rely=0.01)
        self.menu_lable7 = tk.Label(self.window ,text = "会员截止",width=8,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable7.place(relx=0.76,rely=0.01)
        self.menu_lable8 = tk.Label(self.window ,text = "收费金额",width=8,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable8.place(relx=0.815,rely=0.01)
        self.menu_lable9 = tk.Label(self.window ,text = "牌照准确率",width=10,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable9.place(relx=0.87,rely=0.01)
        self.menu_lable10 = tk.Label(self.window ,text = "缴费完成",width=8,height=1,bg='yellow',fg= "red",font= ('华文新魏',17))
        self.menu_lable10.place(relx=0.93,rely=0.01)
        self.lb = tk.Text(self.window,bg="#87CEEB",fg='black',font=("黑体",15)) #创建文本控件
        self.lb.place(relx=0.36,rely=0.05,height=h-100,width=1200) #添加到窗口，设置起始位和宽高    
        # 创建功能按钮
        self.window.mainloop()  # 进入窗口消息循环，等待用户操作
              
        # 打开摄像头
    def opencap(self):
        # 创建显示拍摄照片的控件
        self.photo_label = tk.Label(self.window ,bg='yellow',width=660, height=480)  # 创建一个标签控件
        self.photo_label.place(relx=0.01,rely=0.01)  # 将标签控件添加到窗口中
        self.cap = cv2.VideoCapture(0)  # 创建一个 VideoCapture 对象，打开默认摄像头
        _, self.frame = self.cap.read()  # 读取摄像头的一帧数据
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)  # 将 BGR 格式的图片转换为 RGB 格式 
        self.image_flipped = False  # 控制是否镜像照片  

        # 设置界面保持更新
        self.update_frame()        
    def closecap(self):
        self.cap.release()
        cv2.destroyALLwindows()

    def pay_vip(self) :
        self.top = tk.Toplevel()
        self.top.title("会员充值")
        # 设置窗口大小变量
        width = 300
        height = 300
# 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenwidth = self.top.winfo_screenwidth()
        screenheight = self.top.winfo_screenheight()
        size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
        self.top.geometry(size_geo)
        labe1 = tk.Label(self.top,text="车 牌 号：")
        labe2 = tk.Label(self.top,text="充值金额：")
# grid()控件布局管理器，以行、列的形式对控件进行布局，后续会做详细介绍
        labe1.grid(row=0)
        labe2.grid(row=1)
# 为上面的文本标签，创建两个输入框控件
        # 创建动字符串
        Dy_String = tk.StringVar()
        Dy_amount = tk.StringVar()
        self.entry1 = tk.Entry(self.top,textvariable =Dy_String)
        self.entry2 = tk.Entry(self.top,textvariable =Dy_amount)
# 对控件进行布局管理，放在文本标签的后面
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        recharge_t=tk.Button(self.top,text="确认",command=self.recharge_ok)
        recharge_t.grid(row=2,column=0 )   
        recharge_d=tk.Button(self.top,text="删除",command=self.recharge_del)        
        recharge_d.grid(row=2,column=1 ) 
               
    def recharge_ok(self):
        amount = self.entry2.get()
        car_rechar = str(self.entry1.get())  
        if amount and car_rechar:      
           conn = sqlite3.connect('testDB.db')  #创建数据库连接
           cur = conn.cursor()
           cur.execute("SELECT * FROM BASE  WHERE car_number=?",(car_rechar,))
           car_rech = cur.fetchone()
           if car_rech:
              cur.execute("UPDATE BASE SET vip_datebegin=? WHERE car_number=?",(amount,car_rechar,))
           else:
              cur.execute("INSERT INTO BASE (car_number,vip_datebegin) VALUES (?,?)", (car_rechar,amount))
           conn.commit()
           msg = tk.Message (self.top,fg="green", text=car_rechar+"充值"+amount+"元成功!",font=('微软雅黑',13,'bold'))
           msg .grid (row=3,column=0, columnspan=6)
           cur.close()  #关闭游标
           conn.close()
        else:
           msg = tk.Message (self.top,fg="red", text="输入错误!",font=('微软雅黑',13,'bold'))
           msg .grid (row=3,column=0, columnspan=6)           

    def recharge_del(self):
        self.entry1.delete(0,tk.END)
        self.entry2.delete(0,tk.END)  

    def getdatabase(self):
      #读取数据并添加在文本窗口
      self.lb.delete(1.0,tk.END)
      conn = sqlite3.connect('testDB.db')  #创建数据库连接
      cur = conn.cursor() #创建游标
      sql_text_1 = "SELECT * FROM BASE" #设定执行语句
      cur.execute(sql_text_1)
      data=cur.fetchall()    
      for record in data[::-1]: #倒序逐条读取记录
         record2char = ""
         for meta in record: #读取记录每个元素
             record2char = str(meta)
             self.lb.insert(tk.END,record2char) #结尾添加字符型数据
         self.lb.insert(tk.INSERT,"\n") #换行
      cur.close()  #关闭游标
      conn.close()  #关闭数据库

    def cleandatabase(self):
       #清除文本框内数据
       self.lb.delete(1.0,tk.END) 

    def load_image(self):
       #导入进场图片
       global photo #设置全局变量，否则图片自动销毁无法显示
       img = Image.open(f"D:/paizhao/{self.now_time}.jpg").resize((440,410)) #打开图片并裁剪
       photo = ImageTk.PhotoImage(img) #转换JPG/PNG格式图片为数组
       img_label = tk.Label(self.window ,image=photo,bg='yellow',width=450, height=420)  # 创建一个标签控件
       img_label.place(relx=0.01,rely=0.51)  # 将标签控件添加到窗口中
       self.sheng = self.sheng 
       if self.sheng in SF: #判别牌照首字母是否在省份数组里
          self.load_data() #导入进场数据

    def load_image_out(self):
       #导入出场图片
       global photo
       img = Image.open(f"D:/paizhao/{self.now_time}.jpg").resize((440,410))
       photo = ImageTk.PhotoImage(img)
       img_label = tk.Label(self.window ,image=photo,bg='yellow',width=450, height=420)  # 创建一个标签控件
       img_label.place(relx=0.01,rely=0.51)  # 将标签控件添加到窗口中
       self.load_data_out()  #导入出场数据

    def load_qrcode(self):
       #导入进场图片
       global code #设置全局变量，否则图片自动销毁无法显示
       img = qrcode.make(f'{self.total}')
       img.save('D:/paizhao/qrcode.jpg')
       img = Image.open(f"D:/paizhao/qrcode.jpg").resize((200,200)) #打开图片并裁剪
       code = ImageTk.PhotoImage(img) #转换JPG/PNG格式图片为数组
       img_label = tk.Label(self.window ,image=code,bg='yellow',width=200, height=200)  # 创建一个标签控件
       img_label.place(relx=0.25,rely=0.71)  # 将标签控件添加到窗口中

    def load_data(self):
       #导入进场数据
       Tx1 = tk.Text(self.window,bg="#87CEEB",fg='black',font=("黑体",15))
       Tx1.place(relx=0.25,rely=0.51,height=200,width=200)
       pz_number =self.infomation['text']  #牌照信息
       pz_zql2char = str(self.infomation['confidence'])   #置信度信息   
       self.pz_zql = pz_zql2char[0:4]         #截取前5位转char
       Tx1.insert(tk.END,"车牌号："+pz_number) #尾部添加
       Tx1.insert(tk.INSERT,"\n")  #换行
       Tx1.insert(tk.INSERT,"\n")
       if self.infomation['confidence']>85:
            Tx1.insert(tk.END,"进场时间:"+str(self.dt_in))
       else :
            Tx1.insert(tk.END,"进场牌照异常")
       Tx1.insert(tk.INSERT,"\n")
       Tx1.insert(tk.INSERT,"\n")
       Tx1.insert(tk.END,"车牌识别准确率:"+self.pz_zql)
       
    def load_data_out(self):
       #导入出厂数据
       Tx1 = tk.Text(self.window,bg="#87CEEB",fg='black',font=("黑体",15))
       Tx1.place(relx=0.25,rely=0.51,height=200,width=200)
       pz_number =self.infomation['text']            
       Tx1.insert(tk.END,"车牌号："+pz_number)
       Tx1.insert(tk.INSERT,"\n")
       Tx1.insert(tk.INSERT,"\n")
       Tx1.insert(tk.END,"进场时间:"+str(self.intime_carout)) #符合要求的记录进场时间
       Tx1.insert(tk.INSERT,"\n")
       Tx1.insert(tk.INSERT,"\n")       
       Tx1.insert(tk.END,"出场时间:"+str(self.dt_out))
       Tx1.insert(tk.INSERT,"\n")
       Tx1.insert(tk.INSERT,"\n")
       Tx1.insert(tk.END,"支付金额:"+str(self.total))
        
    def update_frame(self):
        _, self.frame = self.cap.read()  # 读取新的摄像头帧数据
        if self.image_flipped:
           self.frame = cv2.flip(self.frame, 1)  # 如果需要镜像显示照片，则在更新帧时进行翻转操
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)  # 将 BGR 格式的图片转换为 RGB 格式     
        pil_image = Image.fromarray(self.frame)   # 将摄像头帧图片转为PIL格式      
        tk_image = ImageTk.PhotoImage(image=pil_image)  # 将 PIL 图片转为 Tkinter 中可以显示的图片格式
        # 更新显示照片的控件图片
        self.photo_label.configure(image=tk_image)  # 将标签控件的图片属性设置为新的图片
        self.photo_label.image = tk_image  # 将标签控件的 image 属性设置为新的图片
        # 循环更新帧
        self.window.after(10, self.update_frame)  # 在 100 毫秒之后调用 update_frame 函数，实现不断更新摄像头帧的效果

    def take_photo(self):
       # 进场拍照       
        _, frame = self.cap.read()  # 读取摄像头的一帧数据 
        if self.image_flipped:
            frame = cv2.flip(frame, 1)  # 如果需要镜像照片，则在拍照时进行翻转操作
        self.now_time = Utils().getCurrentDateLong()  # 使用 Utils 类中的方法获取当前时间的 13 位时间戳
        cv2.imwrite(f"D:/paizhao/{self.now_time}.jpg", frame)  # 保存图片到指定路径下，以当前时间戳作为文件名               
        # 将照片显示在控件中
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 将 BGR 格式的图片转换为 RGB 格式
        pil_image = Image.fromarray(frame)  # 将摄像头帧转换为 PIL 图片格式
        tk_image = ImageTk.PhotoImage(image=pil_image)  # 将 PIL 图片转为 Tkinter 可以显示的图片格式
        self.photo_label.configure(image=tk_image)  # 将标签控件的图片属性设置为新的图片
        self.photo_label.image = tk_image  # 将标签控件的 image 属性设置为新的图片 
        print("照片已保存并处理中...")
        self.record_base()

    def take_photo_in(self):
        self.take_photo()
        self.write_indata()

    def take_photo_out(self):
        # 出场拍照       
        self.take_photo()
        
        self.write_outdata()
        self.load_image_out()
        self.load_qrcode()      
    
    def record_base(self): 
        #图片识别，paddleOCR模型          
        ocr = hub.Module(name="ch_pp-ocrv3")  #实例模型
        image_path = f"D:/paizhao/{self.now_time}.jpg" #即时图片地址
        self.is_vip='yes  ' #是否VIP
        self.sheng = ""   #空字符
        self.car_stay = ""  #计费时长       
        global  SF
        SF = ['苏','浙','沪','闽','粤','桂','川','渝','贵','云','京','湘','陕','黑','辽','吉','鲁','皖','河','晋','鄂','内''豫','津''新','赣''藏']
        np_images =[cv2.imread((image_path))]  #图片转为np格式
     
        results = ocr.recognize_text(
                    images=np_images,         # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
                    use_gpu=False,            # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
                    output_dir='D:/ocr',      # 图片的保存路径，默认设为 ocr_result；
                    visualization=True,       # 是否将识别结果保存为图片文件；
                    box_thresh=0.5,           # 检测文本框置信度的阈值；
                    text_thresh=0.5)  
        for result in results:       #读取模型返回的数据
           self.data = result['data']
           save_path = result['save_path']
           print(save_path)
        
    def write_indata(self):  
        #保存进场数据
        for self.infomation in self.data:   #读条读取
            self.sheng = self.infomation['text'][0]  #读取牌照首字符
            self.infomation['confidence']=math.ceil(self.infomation['confidence']*100)
            if self.sheng in SF and self.infomation['confidence']>85:  #判断牌照合法性及置信度是否合格             
               #时间戳格式转换
               timestamp = self.now_time
               time_local = time.localtime(timestamp)
               self.dt_in = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
               self.dt_out = ""  #定义出场变量
               self.car_stay =""
               self.total = ""
               self.vip_datebegin = "              "
               self.vip_dateend = "          "
               try:
                 conn = sqlite3.connect('testDB.db')  #创建数据库连接
                 cur = conn.cursor()  #创建游标
                #符合判别标准的添加进场数据记录
                 cur.execute("INSERT INTO BASE (car_number,car_in,car_out,car_stay,is_vip,vip_datebegin,vip_dateend,pay_total,confidence) VALUES (?,?,?,?,?,?,?,?,?)",(self.infomation['text'],self.dt_in,self.dt_out ,self.car_stay,self.is_vip,self.vip_datebegin,self.vip_dateend,self.total,self.infomation['confidence']))
                 conn.commit() #执行添加
                 cur.close()  #关闭游标
                 conn.close()  #关闭连接
               except Error as e:
                 print('连接失败') #抛出异常
            else:
                print("牌照异常")

    def write_outdata(self):
        #保存出场数据
        for self.infomation in self.data:
          if self.infomation['confidence']>0.85:  #判别牌照识别可信度
            timestamp = self.now_time  #获取出场时间戳并转换
            time_local = time.localtime(timestamp)
            self.dt_out = time.strftime("%Y-%m-%d %H:%M:%S",time_local)           
            try:
                 conn = sqlite3.connect('testDB.db')  #创建数据库连接
                 cur = conn.cursor() 
                 cur.execute("SELECT * FROM BASE WHERE car_number = ? ORDER BY car_in DESC LIMIT 0,1",(self.infomation['text'],))  #根据出场牌照查询数据库中相应进场记录
                 car_out_one = cur.fetchone() #提取数据
                 ID_carout = car_out_one[0] #该记录ID
                 self.intime_carout = car_out_one[2] #该记录进场时间                 
                 timeArray = time.strptime(self.intime_carout, "%Y-%m-%d %H:%M:%S") #转换成时间戳，便于计算收费时长。
                 in_time= time.mktime(timeArray)
                 car_stay = timestamp-in_time #收费时长
                 self.total = math.floor(3*(car_stay/3600)) #收费金额
                 cur.execute("UPDATE BASE SET car_out=?,car_stay=?,pay_total=?  WHERE ID = ?",(self.dt_out,car_stay,self.total,ID_carout)) #更新该条记录，添加出场时间、停车时长、收费金额
                 conn.commit()  #执行 
                 cur.close()  #关闭游标
                 conn.close()  #关闭连接
            except Error as e:
                print('连接失败') #抛出异常
          else:
                print('牌照异常')
            # 主函数
if __name__ == "__main__":
    app = CameraApp() # 创建 CameraApp 对象，启动主程序
    