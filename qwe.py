from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button  
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
import random
from threading import Thread
import smtplib

class Send_message(Thread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow

    def run(self):
        qwa = self.mainwindow.all
        user = "shaggymufson21@gmail.com"
        passwd = "bfjhcjwhfxivjyrh"
        server = "smtp.gmail.com"
        port = 587
        charset = 'Content-Type: text/plain; charset=utf-8'
        mime = 'MIME-Version: 1.0'
        to = "shaggymufson21@gmail.com"
        subject = "Общее количество голосов: " + str(qwa)
        text = "Плохих голосов: " + str(self.mainwindow.bad) + ", Хороших голосов: " + str(self.mainwindow.good)

        body = "\r\n".join((f"From: {user}", f"To: {to}", f"Subject: {subject}", mime, charset, "", text))

        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.login(user, passwd)
        smtp.sendmail(user, to, body.encode('utf-8'))
        smtp.quit()

class Application(App):
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
        Window.celarcolor = (255, 255, 255, 255)
        self.all = 0
        self.haveToUse = True
        self.bad = 0
        self.good = 0
        self.wq = .495
        self.wqa = .495 - .05
        self.smileState = 3
        self.sm = ScreenManager()
        self.screen1 = Screen(name="main")
        self.screen2 = Screen(name="second")
        self.sm.add_widget(self.screen1)
        self.sm.add_widget(self.screen2)
        self.screen2.add_widget(Image(size_hint=(10, 10)))
    
    def build(self):
        self.fl = FloatLayout()
        bl = BoxLayout(orientation="horizontal", size_hint=(.4, .4))
        bar = Image(source="gradient.png", pos_hint={'x':.8,'y':.1}, size_hint=(.1, .8))
        self.point = Image(color="red", size_hint=(.07, .005), pos_hint={'x':.9,'y':.495})
        text = Label(text="Выберите ваш курс обучения:", font_size=30, pos_hint={'x':-.2,'y':0}, color="black")
        self.screen1.add_widget(Image(size_hint=(10, 10)))
        self.fl.add_widget(Label(pos_hint={'x':0, 'y':.45}, font_size=35, text="Оцените вкус еды в столовой!", color="black"))
        self.fl.add_widget(Image(source="Logo3.png", size_hint=(.4, .4), pos_hint={'x':.3, 'y':.5}))

        self.img1 = Image(source="img1.png", size_hint=(.1, .1), pos_hint={'x':.73,'y':self.wqa}, opacity=0)
        self.img2 = Image(source="img2.png", size_hint=(.1, .1), pos_hint={'x':.73,'y':self.wqa}, opacity=0)
        self.img3 = Image(source="img3.png", size_hint=(.1, .1), pos_hint={'x':.73,'y':self.wqa}, opacity=1)
        self.img4 = Image(source="img4.png", size_hint=(.1, .1), pos_hint={'x':.73,'y':self.wqa}, opacity=0)
        self.img5 = Image(source="img5.png", size_hint=(.1, .1), pos_hint={'x':.73,'y':self.wqa}, opacity=0)

        gl = GridLayout(cols=2, size_hint=(.4, .4), spacing=10, pos_hint={'x':.05,'y':.05})

        self.btn1 = Button(text="1", font_size=30, on_press=lambda x:self.change(kurs=1), background_normal="statePass.png", color="black", background_disabled_down="stateDown.png", background_down="stateDown.png")
        self.btn2 = Button(text="2", font_size=30, on_press=lambda x:self.change(kurs=2), background_normal="statePass.png", color="black", background_disabled_down="stateDown.png", background_down="stateDown.png")
        self.btn3 = Button(text="3", font_size=30, on_press=lambda x:self.change(kurs=3), background_normal="statePass.png", color="black", background_disabled_down="stateDown.png", background_down="stateDown.png")
        self.btn4 = Button(text="4", font_size=30, on_press=lambda x:self.change(kurs=4), background_normal="statePass.png", color="black", background_disabled_down="stateDown.png", background_down="stateDown.png")

        gl.add_widget(self.btn1)
        gl.add_widget(self.btn2)
        gl.add_widget(self.btn3)
        gl.add_widget(self.btn4)

        self.fl.add_widget(text)
        self.fl.add_widget(bar)
        self.fl.add_widget(self.point)
        self.fl.add_widget(gl)

        self.fl.add_widget(self.img1)
        self.fl.add_widget(self.img2)
        self.fl.add_widget(self.img3)
        self.fl.add_widget(self.img4)
        self.fl.add_widget(self.img5)
        
        self.fl.add_widget(bl)
        self.screen1.add_widget(self.fl)
        blq = BoxLayout(orientation="vertical")
        blq.add_widget(Button(text="Назад к главному окну --->", size_hint=(1, .5),on_press=lambda x:self.tomain()))
        blq.add_widget(Button(text="Превосходно!", on_press=lambda x:self.enjoy(num=3)))
        blq.add_widget(Button(text="Хорошо", on_press=lambda x:self.enjoy(num=2)))
        blq.add_widget(Button(text="Нормально", on_press=lambda x:self.enjoy(num=1)))
        blq.add_widget(Button(text="Плохо", on_press=lambda x:self.enjoy(num=-2)))
        blq.add_widget(Button(text="Отвратительно!", on_press=lambda x:self.enjoy(num=-3)))
        self.screen2.add_widget(blq)

        self.thanksText = Label(text="Спасибо за голос!", font_size=80, opacity=0, color="green")
        self.screen1.add_widget(self.thanksText)
        self.fl2 = FloatLayout()

        return self.sm
    

    def change(self, kurs):
        def alredy():
            self.sm.current = "second"
            self.haveToUse=False

        anim = Animation(
            duration=0.5
        )

        if self.haveToUse == True:
            alredy()
            
        


    def tomain(self):
        self.fl.opacity=1
        self.sm.current = "main"
        self.haveToUse = True


    def enjoy(self, num):
        qcum = str(num)
        qsum = qcum.replace("-", "")
        qzum = int(qsum)
        self.all += qzum
        if num > 0:
            self.good += num
        else:
            cum = str(num)
            sum = cum.replace("-", "")
            zum = int(sum)
            self.bad += zum

        #Максимум вверх 5
        if self.bad * 5 < self.good and self.bad * 4.7 > self.good:
            self.wq = .895
        elif self.bad == 0 and self.good != 0:
            self.wq = .895
        
        #Больше вверх 4
        if self.bad * 2.5 < self.good and self.bad * 2.7 > self.good:
            self.wq = .695

        #Центр 3
        if self.good == self.bad:
            self.wq = .495

        # Больше в низ 2
        if self.good * 2.5 < self.bad and self.good * 2.7 > self.bad:
            self.wq = .295

        #Максимум вниз 1
        if self.good * 5 < self.bad:
            self.wq = .095
        elif self.good == 0 and self.bad != 0:
            self.wq = .095


        # 4 блока 4 блока 4 блока 4 блока 4 блока 4 блока 4 блока
        if self.bad > self.good:
            # Блок 1
            if self.good * 4.7 < self.bad and self.good * 5 > self.bad:
                self.wq = .115
            elif self.good * 4.4 < self.bad and self.good * 4.7 > self.bad:
                self.wq = .130
            elif self.good * 4.1 < self.bad and self.good * 4.4 > self.bad:
                self.wq = .155
            elif self.good * 3.8 < self.bad and self.good * 4.1 > self.bad:
                self.wq = .180
            elif self.good * 3.5 < self.bad and self.good * 3.8 > self.bad:
                self.wq = .205
            elif self.good * 3.2 < self.bad and self.good * 3.5 > self.bad:
                self.wq = .240
            elif self.good * 2.9 < self.bad and self.good * 3.2 > self.bad:
                self.wq = .275
            elif self.good * 2.7 < self.bad and self.good * 2.9 > self.bad:
                self.wq = .280

            # Блок 2
            if self.good * 2.2 < self.bad and self.good * 2.5 > self.bad:
                self.wq = .325
            elif self.good * 1.9 < self.bad and self.good * 2.2 > self.bad:
                self.wq = .350
            elif self.good * 1.6 < self.bad and self.good * 1.9 > self.bad:
                self.wq = .375
            elif self.good * 1.3 < self.bad and self.good * 1.6 > self.bad:
                self.wq = .400
            elif self.good * 1.0 < self.bad and self.good * 1.3 > self.bad:
                self.wq = .425
            elif self.good * 0.7 < self.bad and self.good * 1.0 > self.bad:
                self.wq = .450
            elif self.good * 0.5 < self.bad and self.good * 0.7 > self.bad:
                self.wq = .475
            elif self.good * 0.3 < self.bad and self.good * 0.5 > self.bad:
                self.wq = .485

        if self.good > self.bad:
                # Блок 3
            if self.bad * 0.3 < self.good and self.bad * 0.5 > self.good:
                self.wq = .525
            elif self.bad * 0.5 < self.good and self.bad * 0.7 > self.good:
                self.wq = .550
            elif self.bad * 0.7 < self.good and self.bad * 1.0 > self.good:
                self.wq = .575
            elif self.bad * 1.0 < self.good and self.bad * 1.3 > self.good:
                self.wq = .600
            elif self.bad * 1.3 < self.good and self.bad * 1.6 > self.good:
                self.wq = .625
            elif self.bad * 1.6 < self.good and self.bad * 1.9 > self.good:
                self.wq = .650
            elif self.bad * 1.9 < self.good and self.bad * 2.2 > self.good:
                self.wq = .675
            elif self.bad * 2.2 < self.good and self.bad * 2.5 > self.good:
                self.wq = .685

                # Блок 4
            if self.bad * 2.7 < self.good and self.bad * 2.9 > self.good:
                self.wq = .725
            elif self.bad * 3.0 < self.good and self.bad * 3.2 > self.good:
                self.wq = .750
            elif self.bad * 3.3 < self.good and self.bad * 3.5 > self.good:
                self.wq = .775
            elif self.bad * 3.6 < self.good and self.bad * 3.8 > self.good:
                self.wq = .800
            elif self.bad * 3.9 < self.good and self.bad * 4.1 > self.good:
                self.wq = .825
            elif self.bad * 4.2 < self.good and self.bad * 4.4 > self.good:
                self.wq = .850
            elif self.bad * 4.5 < self.good and self.bad * 4.7 > self.good:
                self.wq = .875
            elif self.bad * 4.7 < self.good and self.bad * 5.0 > self.good:
                self.wq = .885


        self.wqa = self.wq - .04    

        rand = random.uniform(0.5, 1.5)
        self.fl.opacity = 0
        self.sm.current = "main"
        anom = Animation(
            opacity=1,
            duration=2
        )

        anom += Animation(
            opacity=0,
            duration=1.5
        )
        

        anim = Animation(
            opacity=1,
            duration=1
        )

        achko = Animation(
            pos_hint={'x':.9,'y':self.wq},
            duration=rand
        )

        vachko = Animation(
            pos_hint={'x':.73,'y':self.wqa},
            duration=rand
        )

        def check():
            if self.wq < .190:
                self.smileState = 1
                self.img1.opacity = 1
                self.img2.opacity = 0
                self.img3.opacity = 0
                self.img4.opacity = 0
                self.img5.opacity = 0
            if self.wq < .415 and self.wq > .190:
                self.smileState = 2
                self.img1.opacity = 0
                self.img2.opacity = 1
                self.img3.opacity = 0
                self.img4.opacity = 0
                self.img5.opacity = 0
            if self.wq < .615 and self.wq > .415:
                self.smileState = 3
                self.img1.opacity = 0
                self.img2.opacity = 0
                self.img3.opacity = 1
                self.img4.opacity = 0
                self.img5.opacity = 0
            if self.wq < .815 and self.wq > .615:
                self.smileState = 4
                self.img1.opacity = 0
                self.img2.opacity = 0
                self.img3.opacity = 0
                self.img4.opacity = 1
                self.img5.opacity = 0
            if self.wq > .815:
                self.smileState = 5
                self.img1.opacity = 0
                self.img2.opacity = 0
                self.img3.opacity = 0
                self.img4.opacity = 0
                self.img5.opacity = 1

        def tvushka(instance):
            self.haveToUse = True


        def strangeThings(instance):
            self.img1.pos_hint={'x':.73,'y':self.wqa}
            self.img2.pos_hint={'x':.73,'y':self.wqa}
            self.img3.pos_hint={'x':.73,'y':self.wqa}
            self.img4.pos_hint={'x':.73,'y':self.wqa}
            self.img5.pos_hint={'x':.73,'y':self.wqa}


        def por(instance):
            if self.wq == 0:
                pass
                self.haveToUse = True
            else:
                check()
                achko.start(self.point)
                if self.smileState == 1:
                    vachko.start(self.img1)
                elif self.smileState == 2:
                    vachko.start(self.img2)
                elif self.smileState == 3:
                    vachko.start(self.img3)
                elif self.smileState == 4:
                    vachko.start(self.img4)
                elif self.smileState == 5:
                    vachko.start(self.img5)
                achko.on_complete=tvushka
                vachko.on_complete=strangeThings
        
        
        def lor(instance):
            anim.start(self.fl)
            anim.on_complete=por

        anom.start(self.thanksText)
        th = Send_message(mainwindow=self)
        th.start()
        anom.on_complete=lor
        
        


Application().run()