from tkinter import *
root = Tk()

root.title("% Calculation")
root.geometry("600x600")

pa_grade_3_label = Label(root)
pa_grade_5_label = Label(root)
pa_grade_10_label = Label(root)

class grade_3():
    
    def __init__(self, lang_arts, maths):
        self.lang_arts = lang_arts
        self.maths = maths
        
    def percentage(self):
        total_marks = self.lang_arts + self.maths
        tm_with_100 = total_marks * 100
        grade_3_pa = tm_with_100 / 200
        pa_grade_3_label["text"] = grade_3_pa
        
class grade_5():
    
    def __init__(self, lang_arts, maths, sst):
        self.lang_arts = lang_arts
        self.maths = maths
        self.sst = sst
        
    def percentage(self):
        total_marks = self.lang_arts + self.maths + self.sst
        tm_with_100 = total_marks * 100
        grade_5_pa = tm_with_100 / 300
        pa_grade_5_label["text"] = grade_5_pa
        
class grade_10():
    
    def __init__(self, lang_arts, maths, sst, foreign_lang):
        self.lang_arts = lang_arts
        self.maths = maths
        self.sst = sst
        self.foreign_lang = foreign_lang
        
    def percentage(self):
        total_marks = self.lang_arts + self.maths + self.sst + self.foreign_lang
        tm_with_100 = total_marks * 100
        grade_10_pa = tm_with_100 / 400
        pa_grade_10_label["text"] = grade_10_pa
        
obj_grade_3 = grade_3(40, 50)
grade_3_btn = Button(root, text = "Grade - 3", command = obj_grade_3.percentage)
grade_3_btn.pack(padx = 20, pady = 20)
pa_grade_3_label.pack(padx = 20, pady = 20)

obj_grade_5 = grade_5(40, 50, 70)
grade_5_btn = Button(root, text = "Grade - 5", command = obj_grade_5.percentage)
grade_5_btn.pack(padx = 20, pady = 20)
pa_grade_5_label.pack(padx = 20, pady = 20)

obj_grade_10 = grade_10(40, 50, 70, 90)
grade_10_btn = Button(root, text = "Grade - 10", command = obj_grade_10.percentage)
grade_10_btn.pack(padx = 20, pady = 20)
pa_grade_10_label.pack(padx = 20, pady = 20)

root.mainloop()