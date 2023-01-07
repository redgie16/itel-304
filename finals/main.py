from kivy.config import Config
Config.set("graphics", "resizable", False)
from kivy.app import App
from kivy.clock import Clock
from datetime import datetime
import pytz
from time import strftime
from kivy.core.window import Window

Window.size = (400, 500)

class ClockApp(App):

    sw_started = False
    sw_seconds = 0

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, tick):
        self.root.ids.time.text = strftime("[size=60][font=arialbd]%I[/font]:%M %p [/size] \n %a, %b %d, %Y")
        #print(tick)

        if self.sw_started:
            self.sw_seconds += tick

        m, s = divmod(self.sw_seconds, 60)

        self.root.ids.stopwatch.text = ("%02d:%02d.[size=40]%02d[/size]" % (int(m), int(s), int(s * 100 % 100)))
    
        correct_time = strftime('[size=30]%I:%M %p[/size]')
        self.root.ids.tz.text = '[size=22]Manila[/size]'
        self.root.ids.tz1.text = correct_time

        home = pytz.timezone('Asia/Tokyo')
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        self.root.ids.tz2.text = 'Tokyo     ' + current_time

        home = pytz.timezone('Asia/Seoul')
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        self.root.ids.tz3.text = 'Seoul    ' + current_time

        home = pytz.timezone('Australia/Sydney')
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        self.root.ids.tz4.text = 'Sydney     ' + current_time

        home = pytz.timezone('America/New_York')
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        self.root.ids.tz5.text = 'New York     ' + current_time

        home = pytz.timezone('Europe/London')
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        self.root.ids.tz6.text = 'London     ' + current_time

    def start_stop(self):
        self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False

        self.sw_seconds = 0

if __name__ == "__main__":
    ClockApp().run()
