import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from hijridate import Gregorian, Hijri
from datetime import datetime
import pyglet
from names import *
import os
import sys

# Singleton for managing GUI
class GUIManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(GUIManager, cls).__new__(cls)
        return cls._instance
    
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def __init__(self):
        pyglet.font.add_file(self.resource_path('fonts\\IBMPlexSansArabic-Regular.ttf'))
        pyglet.font.add_file(self.resource_path('fonts\\Montserrat-VariableFont_wght.ttf'))

        self.root = tk.Tk()
        self.style = ttk.Style()
        
        self.root.geometry("550x600")
        self.root.iconbitmap(self.resource_path("images\\ico.ico"))
        self.root.configure(background='white')
        self.style.configure('TLabelframe', background="white") 
        self.style.configure('TLabelframe.Label', background="white")
        self.style.configure('TRadiobutton', background="white")
        self.style.configure('TLabel', background="white", bd=0, highlightthickness=0, relief='flat')
        self.style.configure('TFrame', background="white")
        self.style.configure('TPhotoImage', highlightthickness=0)

        # Language Buttons Frame
        self.language_frame = tk.Frame(self.root)
        self.language_frame.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)  # Positioned on the top right
        self.language_frame.configure(background='white')

        # Language Buttons
        self.english_button = tk.Button(self.language_frame, text="English", command=self.set_language_english)
        self.english_button.pack(side=tk.RIGHT, padx=5)

        self.korean_button = tk.Button(self.language_frame, text="한국어", command=self.set_language_korean)
        self.korean_button.pack(side=tk.RIGHT, padx=5)

        self.arabic_button = tk.Button(self.language_frame, text="عربي", command=self.set_language_arabic)
        self.arabic_button.pack(side=tk.RIGHT, padx=5)
        self.arabic_button.invoke() #Default language Arabic

        # Bottom Frame
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(side=tk.BOTTOM, ipadx=10, ipady=10, fill=tk.X)  # Positioned on the bottom
        self.bottom_frame.configure(background='white')

        # Image Placeholder and Title
        self.logo = tk.PhotoImage(file=self.resource_path('images\\llogo.png'))
        logo_label = tk.Label(self.bottom_frame, image=self.logo, relief='ridge', bd=0, highlightthickness=0)
        logo_label.pack(side="right", anchor=tk.SE, pady=10, padx=10)

        self.title_label = tk.Label(self.root, text="محول التاريخ الهجري", font=("IBM Plex Sans Arabic", 30, 'bold'))
        self.title_label.pack(pady=(0, 0))
        self.title_label.configure(background='white')

        # Frame for radio buttons
        self.radio_frame = ttk.LabelFrame(self.root, text="التقويم", labelanchor='ne' ,padding=10)
        self.radio_frame.pack(pady=10, padx=50, anchor=tk.CENTER)
        

        # Radio Buttons
        self.selected_option = tk.StringVar()
        self.hijriButton = ttk.Radiobutton(self.radio_frame, text="هجري", variable=self.selected_option, value="hijri", command=self.on_option_change)
        self.hijriButton.pack(side=tk.RIGHT, anchor=tk.E, padx=10)
        self.gregorianButton = ttk.Radiobutton(self.radio_frame, text="غريغوري", variable=self.selected_option, value="gregorian", command=self.on_option_change)
        self.gregorianButton.pack(side=tk.RIGHT, anchor=tk.E, padx=10)

         # Frame for date input fields
        self.date_input_frame = tk.Frame(self.root, bg='white', bd=0, highlightthickness=0, relief='ridge')
        self.date_input_frame.pack(pady=20)

        # Year Input
        self.year_label = tk.Label(self.date_input_frame, text="عام", bg='white', font=("IBM Plex Sans Arabic", 14, 'bold'))
        
        self.year_label.grid_forget()
        self.year_entry = tk.Entry(self.date_input_frame, width=10, font=(10), justify='center')
        
        self.year_entry.grid_forget()
        # Month Input

        # String variable to store selected month name
        self.selected_month = tk.StringVar()

        

        # Dropdown menu for months
        self.month_label = tk.Label(self.date_input_frame, text="الشهر", bg='white', font=("IBM Plex Sans Arabic", 14, 'bold'))
        self.month_label.grid_forget()

        self.month_dropdown = ttk.Combobox(self.date_input_frame, width=10, font=(10))
        self.month_dropdown.set('الشهر')
        self.month_dropdown.configure(justify='center')

        # Day Input
        self.day_label = tk.Label(self.date_input_frame, text="اليوم", bg='white',font=("IBM Plex Sans Arabic", 14, 'bold'))
        self.day_label.grid_forget()

        self.day_entry = ttk.Combobox(self.date_input_frame, values=list(range(1, 32)), width=5, font=(10))
        self.day_entry.set('اليوم')
        self.day_entry.configure(justify='center')
        self.day_entry.grid_forget()

        # Convert Button
        self.convert_button = tk.Button(self.date_input_frame, text="حول", command=self.display_selected_date, state=tk.DISABLED, font=("IBM Plex Sans Arabic", 10, 'bold'), width=10)
        self.convert_button.grid_forget()

        # Info Button
        self.info_button = tk.Button(self.bottom_frame, text="معلومات", command=self.display_info)
        self.info_button.pack(side="left", fill='x', anchor=tk.SW, pady=10, padx=10)

        self.lang= 'ar'

    
    def on_option_change(self):
        for widget in self.date_input_frame.winfo_children():
            widget.forget()

        self.display_label.config(text='')
        self.display_label_year.config(text='')
        self.year_entry.delete(0, 'end')
        if self.lang=="ar":
            self.month_dropdown.set('الشهر')
            self.day_entry.set('اليوم')
        elif self.lang=="en":
            self.month_dropdown.set('Month')
            self.day_entry.set('Day')
        elif self.lang=="kr":
            self.month_dropdown.set('월')
            self.day_entry.set('날')

        
        if self.lang=="ar":
            self.year_label.grid(row=0, column=3)
            self.year_entry.grid(row=1, column=3, padx=10)
            self.month_label.grid(row=0, column=2)
            self.month_dropdown.grid(row=1, column=2, padx=10)
            self.day_label.grid(row=0, column=1)
            self.day_entry.grid(row=1, column=1, padx=10)
            self.convert_button.grid(row=1, column=0, padx=10)
            self.display_label.pack(pady=10, padx=(10,40), side=tk.RIGHT)
            self.display_label.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='right')
            self.display_label_year.pack(pady=10, padx=10, side=tk.RIGHT)
            self.display_label_year.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='right')

            if self.selected_option.get() == "hijri":
                self.month_dropdown.configure(values=hijri_ar)
            elif self.selected_option.get() == "gregorian":
                self.month_dropdown.configure(values=months_ar)

            
        elif self.lang=="en":
            self.year_label.grid(row=0, column=0)
            self.year_entry.grid(row=1, column=0, padx=10)
            self.month_label.grid(row=0, column=1)
            self.month_dropdown.grid(row=1, column=1, padx=10)
            self.day_label.grid(row=0, column=2)
            self.day_entry.grid(row=1, column=2, padx=10)
            self.convert_button.grid(row=1, column=3, padx=10)
            self.display_label.pack(pady=10, padx=(40,10), side=tk.LEFT)
            self.display_label.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='left')
            self.display_label_year.pack(pady=10, padx=10, side=tk.LEFT)
            self.display_label_year.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='left')

            if self.selected_option.get() == "hijri":
                self.month_dropdown.configure(values=hijri_en)
            elif self.selected_option.get() == "gregorian":
                self.month_dropdown.configure(values=months_en)

        elif self.lang=="kr":
            self.year_label.grid(row=0, column=0)
            self.year_entry.grid(row=1, column=0, padx=10)
            self.month_label.grid(row=0, column=1)
            self.month_dropdown.grid(row=1, column=1, padx=10)
            self.day_label.grid(row=0, column=2)
            self.day_entry.grid(row=1, column=2, padx=10)
            self.convert_button.grid(row=1, column=3, padx=10)
            self.display_label.pack(pady=10, padx=(40,10), side=tk.LEFT)
            self.display_label.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='left')
            self.display_label_year.pack(pady=10, padx=10, side=tk.LEFT)
            self.display_label_year.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='left')

            if self.selected_option.get() == "hijri":
                self.month_dropdown.configure(values=hijri_kr)
            elif self.selected_option.get() == "gregorian":
                self.month_dropdown.configure(values=months_kr)

        self.convert_button.config(state=tk.NORMAL)

    def is_valid_date(self, year, month, day):
        try:
            datetime(int(year), int(month), int(day))
            return True
        except ValueError:
            return False

    def display_selected_date(self):
        year = self.year_entry.get()
        selected_month_name = self.month_dropdown.get()
        month = self.month_dropdown['values'].index(selected_month_name) + 1
        day = self.day_entry.get()
        
        if not self.is_valid_date(year, month, day):
            if self.lang=="en":
                messagebox.showerror("Error", "Invalid date entered!")
                return
            elif self.lang=="kr":
                messagebox.showerror("에러", "잘못된 날짜 입력!")
                return
            elif self.lang=="ar":
                messagebox.showerror("خطأ", "التاريخ المدخل غير صحيح")
                return
    
        if self.selected_option.get() == "gregorian":
            gregorian_date = datetime.strptime(f"{year}-{month}-{day}", '%Y-%m-%d').date()
            hijri_date = Gregorian(gregorian_date.year, gregorian_date.month, gregorian_date.day).to_hijri()
            hijri_date = datetime.strptime(f"{hijri_date.year}-{hijri_date.month}-{hijri_date.day}", '%Y-%m-%d').date()
            
            gregMonthar = months_ar_text[month-1]
            hijriMonthar = hijri_ar_text[hijri_date.month-1]

            gregMonthen = months_en_text[month-1]
            hijriMonthen = hijri_en_text[hijri_date.month-1]

            gregMonthkr = months_kr_text[month-1]
            hijriMonthkr = hijri_kr_text[hijri_date.month-1]

        else:
            hijri_date = datetime.strptime(f"{year}-{month}-{day}", '%Y-%m-%d').date()
            gregorian_date = Hijri(hijri_date.year, hijri_date.month, hijri_date.day).to_gregorian()
            gregorian_date = datetime.strptime(f"{gregorian_date.year}-{gregorian_date.month}-{gregorian_date.day}", '%Y-%m-%d').date()

            hijriMonthar = hijri_ar_text[month-1]
            gregMonthar = months_ar_text[gregorian_date.month-1]

            hijriMonthen = hijri_en_text[month-1]
            gregMonthen = months_en_text[gregorian_date.month-1]

            hijriMonthkr = hijri_kr_text[month-1]
            gregMonthkr = months_kr_text[gregorian_date.month-1]

        #formatted_gregorian_date = gregorian_date.strftime('%d / %m / %Y')
        #formatted_hijri_date = hijri_date.strftime('%d / %m / %Y')

        p1 = f":التاريخ الهجري"
        p2 = f":التاريخ الغريغوري"

        hijriYear = hijri_date.year
        hijriDay = hijri_date.day
        weekDayar = days_ar[gregorian_date.strftime('%A')]
        weekDaykr = days_kr[gregorian_date.strftime('%A')]
        gregYear = gregorian_date.year
        gregDay = gregorian_date.day

        if self.lang == "ar":
            self.display_label.config(text=f"{p1}\n{p2}", font=("IBM Plex Sans Arabic", 15, 'bold'))
            self.display_label_year.config(text=f"{hijriYear} {weekDayar}، {hijriDay} {hijriMonthar}\n{gregYear} {weekDayar}، {gregDay} {gregMonthar}", font=("IBM Plex Sans Arabic",15))
        elif self.lang == "en":
            self.display_label.config(text="Hijri:\nGregorian:", font=("MONTSERRAT 14 bold"))
            self.display_label_year.config(text=f"{gregorian_date.strftime('%A')}, {hijriDay} {hijriMonthen} {hijriYear}\n{gregorian_date.strftime('%A')}, {gregDay} {gregMonthen} {gregYear}", font=("MONTSERRAT",14))
        elif self.lang == "kr":
            self.display_label.config(text="히즈라력:\n그레고리력:", font=("MONTSERRAT 14 bold"))
            self.display_label_year.config(text=f"{weekDaykr}, {hijriYear}년 {hijriMonthkr} {hijriDay}일\n{weekDaykr}, {gregYear}년 {gregorian_date.month}월 {gregDay}일", font=("MONTSERRAT",14))

    def display_info(self):
        if self.lang == "en":
            messagebox.showinfo("Info", "Developed by Abdulrahman Aldayel \n\nMIT License\nCopyright (c) 2024 Abdulrahman Aldayel")
        elif self.lang == "ar":
            messagebox.showinfo("معلومات", "تطوير عبدالرحمن الدايل \n\nMIT رخصة\nحقوق النشر (c) 2024 Abdulrahman Aldayel")
        elif self.lang == "kr":
            messagebox.showinfo("정보", "압도라만 아다엘에 의해 개발됨\n\nMIT 허가서\n\n저작권 (c) 2024 Abdulrahman Aldayel")
    
    def set_language_arabic(self):
        
        self.root.title("محول التاريخ الهجري") #Window Title
        self.style.configure('TLabelframe.Label', font=("IBM Plex Sans Arabic", 16, 'bold')) #Frame Title
        self.style.configure('TRadiobutton', font=("IBM Plex Sans Arabic", 15)) #Radio Button

        self.title_label.config(text="محول التاريخ الهجري")
        self.title_label.config(font=("IBM Plex Sans Arabic", 30, 'bold'))
        self.title_label.pack(pady=(0, 0))

        self.radio_frame.config(text="التقويم")
        self.radio_frame.config(labelanchor='ne')

        self.hijriButton.config(text="هجري")
        self.gregorianButton.config(text="غريغوري")

        self.convert_button.config(text="حول", font=("IBM Plex Sans Arabic", 10, 'bold'))

        self.info_button.config(text="معلومات")

        self.year_label.config(text="عام")
        self.year_label.config(font=("IBM Plex Sans Arabic", 14, 'bold'))
        self.month_label.config(text="شهر")
        self.month_label.config(font=("IBM Plex Sans Arabic", 14, 'bold'))
        self.day_label.config(text="يوم")
        self.day_label.config(font=("IBM Plex Sans Arabic", 14, 'bold'))


        if self.convert_button['state'] != 'disabled':
            self.year_label.grid(row=0, column=3)
            self.year_entry.grid(row=1, column=3, padx=10)
            self.month_label.grid(row=0, column=2)
            self.month_dropdown.grid(row=1, column=2, padx=10)
            self.day_label.grid(row=0, column=1)
            self.day_entry.grid(row=1, column=1, padx=10)
            self.convert_button.grid(row=1, column=0, padx=10)
            self.display_label.pack(pady=10, padx=(10,40), side=tk.RIGHT)
            self.display_label.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='right')
            self.display_label_year.pack(pady=10, padx=10, side=tk.RIGHT)
            self.display_label_year.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='right')

            if self.selected_option.get() == "hijri":
                nom = self.month_dropdown.get()
                if nom != 'Month' and nom != '월':
                    i = self.month_dropdown['values'].index(nom)
                    self.month_dropdown.configure(values=hijri_ar)
                    self.month_dropdown.set(hijri_ar[i])
                else:
                    self.month_dropdown.configure(values=hijri_ar)
                    self.month_dropdown.set('الشهر')
            elif self.selected_option.get() == "gregorian":
                nom = self.month_dropdown.get()
                if nom != 'Month' and nom != '월':
                    i = self.month_dropdown['values'].index(nom)
                    self.month_dropdown.configure(values=months_ar)
                    self.month_dropdown.set(months_ar[i])
                else:
                    self.month_dropdown.configure(values=months_ar)
                    self.month_dropdown.set('الشهر')
        
        self.lang = "ar"

        if self.day_entry.get() == 'Day' or self.day_entry.get() == '날':
            self.day_entry.set('اليوم')
                

        if self.display_label.cget("text"):
            self.display_selected_date()
        
        

    def set_language_english(self):

        self.root.title("Hijri Date Converter")
        self.style.configure('TLabelframe.Label', font=("MONTSERRAT", 14, 'bold')) #Frame Title
        self.style.configure('TRadiobutton', font=("MONTSERRAT", 13)) #Radio Button

        self.title_label.config(text="Hijri Date Converter")
        self.title_label.config(font=("MONTSERRAT 20 bold"))
        self.title_label.pack(pady=(30, 12))

        self.radio_frame.config(text="Calender")
        self.radio_frame.config(labelanchor='nw')

        self.hijriButton.config(text="Hijri")
        self.gregorianButton.config(text="Gregorian")

        self.convert_button.config(text="Convert")
        self.convert_button.configure(font=("MONTSERRAT", 10, 'bold'))

        self.info_button.config(text="Info")

        self.year_label.config(text="Year")
        self.year_label.config(font=("MONTSERRAT", 12, 'bold'))
        self.month_label.config(text="Month")
        self.month_label.config(font=("MONTSERRAT", 12, 'bold'))
        self.day_label.config(text="Day")
        self.day_label.config(font=("MONTSERRAT", 12, 'bold'))
        
        if self.convert_button['state'] != 'disabled':
            self.year_label.grid(row=0, column=0)
            self.year_entry.grid(row=1, column=0, padx=10)
            self.month_label.grid(row=0, column=1)
            self.month_dropdown.grid(row=1, column=1, padx=10)
            self.day_label.grid(row=0, column=2)
            self.day_entry.grid(row=1, column=2, padx=10)
            self.convert_button.grid(row=1, column=3, padx=10)
            self.display_label.pack(pady=10, padx=(40,10), side=tk.LEFT)
            self.display_label.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='left')
            self.display_label_year.pack(pady=10, padx=10, side=tk.LEFT)
            self.display_label_year.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='left')

            if self.selected_option.get() == "hijri":
                nom = self.month_dropdown.get()
                if nom != 'الشهر' and nom != '월':
                    i = self.month_dropdown['values'].index(nom)
                    self.month_dropdown.configure(values=hijri_en)
                    self.month_dropdown.set(hijri_en[i])
                else:
                    self.month_dropdown.configure(values=hijri_en)
                    self.month_dropdown.set('Month')
            elif self.selected_option.get() == "gregorian":
                nom = self.month_dropdown.get()
                if nom != 'الشهر' and nom != '월':
                    i = self.month_dropdown['values'].index(nom)
                    self.month_dropdown.configure(values=months_en)
                    self.month_dropdown.set(months_en[i])
                else:
                    self.month_dropdown.configure(values=months_en)
                    self.month_dropdown.set('Month')
        
        self.lang = "en"

        if self.day_entry.get() == 'اليوم' or self.day_entry.get() == '날':
            self.day_entry.set('Day')
        
        if self.display_label.cget("text"):
            self.display_selected_date()
        
        

    def set_language_korean(self):
        

        self.root.title("히즈리 날짜 변환기")

        self.title_label.config(text="히즈리 날짜 변환기")
        self.title_label.config(font=("MONTSERRAT 20 bold"))
        self.title_label.pack(pady=(0, 0))

        self.radio_frame.config(text="달력")
        self.radio_frame.config(labelanchor='nw')

        self.hijriButton.config(text="히즈라력")
        self.gregorianButton.config(text="그레고리력")

        self.convert_button.config(text="변환")

        self.info_button.config(text="정보")

        self.year_label.config(text="년")
        self.year_label.config(font=("MONTSERRAT", 14, 'bold'))
        self.month_label.config(text="월")
        self.month_label.config(font=("MONTSERRAT", 14, 'bold'))
        self.day_label.config(text="일")
        self.day_label.config(font=("MONTSERRAT", 14, 'bold'))
        
        if self.convert_button['state'] != 'disabled':
            self.year_label.grid(row=0, column=0)
            self.year_entry.grid(row=1, column=0, padx=10)
            self.month_label.grid(row=0, column=1)
            self.month_dropdown.grid(row=1, column=1, padx=10)
            self.day_label.grid(row=0, column=2)
            self.day_entry.grid(row=1, column=2, padx=10)
            self.convert_button.grid(row=1, column=3, padx=10)
            self.display_label.pack(pady=10, padx=(40,10), side=tk.LEFT)
            self.display_label.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='left')
            self.display_label_year.pack(pady=10, padx=10, side=tk.LEFT)
            self.display_label_year.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='left')

            if self.selected_option.get() == "hijri":
                nom = self.month_dropdown.get()
                if nom != 'الشهر' and nom != 'Month':
                    i = self.month_dropdown['values'].index(nom)
                    self.month_dropdown.configure(values=hijri_kr)
                    self.month_dropdown.set(hijri_kr[i])
                else:
                    self.month_dropdown.configure(values=hijri_kr)
                    self.month_dropdown.set('월')
            elif self.selected_option.get() == "gregorian":
                nom = self.month_dropdown.get()
                if nom != 'الشهر' and nom != 'Month':
                    i = self.month_dropdown['values'].index(nom)
                    self.month_dropdown.configure(values=months_kr)
                    self.month_dropdown.set(months_kr[i])
                else:
                    self.month_dropdown.configure(values=months_kr)
                    self.month_dropdown.set('월')
        
        self.lang = "kr"

        if self.day_entry.get() == 'اليوم' or self.day_entry.get() == 'Day':
            self.day_entry.set('날')
        
        if self.display_label.cget("text"):
            self.display_selected_date()
        
        

    def start(self):
        self.display_label = tk.Label(self.root, text="")
        self.display_label.pack(pady=10, padx=(10,40), side=tk.RIGHT)
        self.display_label.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='right')

        self.display_label_year = tk.Label(self.root, text="")
        self.display_label_year.pack(pady=10, padx=10, side=tk.RIGHT)
        self.display_label_year.configure(background='white', bd=0, highlightthickness=0, relief='ridge', justify='right')

        

        self.root.mainloop()


if __name__ == "__main__":
    GUIManager().start()
