# def kalkulyator():
#     print("Oddiy kalkulyator! (+, -, *, /)")
#
#     while True:
#
#         amal = input("Amalni tanlang (+, -, *, /) yoki 'exit' yozib chiqib ketish: ")
#
#         if amal == 'exit':
#             print("Kalkulyatordan chiqildi. 😊")
#             break
#
#
#         son1 = float(input("Birinchi sonni kiriting: "))
#         son2 = float(input("Ikkinchi sonni kiriting: "))
#
#
#         if amal == '+':
#             natija = son1 + son2
#         elif amal == '-':
#             natija = son1 - son2
#         elif amal == '*':
#             natija = son1 * son2
#         elif amal == '/':
#             if son2 != 0:
#                 natija = son1 / son2
#             else:
#                 print("Nolga bo‘lish mumkin emas!")
#                 continue
#         else:
#             print("Noto‘g‘ri amal tanlandi!")
#             continue
#
#         print(f"Natija: {natija}\n")
#
#
# kalkulyator()







import tkinter as tk

def tugma_bosildi(qiymat):
    """Tugma bosilganda uning qiymatini kirish maydonchasiga qo'shadi."""
    hozirgi_qiymat = kirish_maydoni.get()
    kirish_maydoni.delete(0, tk.END)
    kirish_maydoni.insert(0, hozirgi_qiymat + qiymat)

def tozalash():
    """Kirish maydonchasini tozalaydi."""
    kirish_maydoni.delete(0, tk.END)

def hisobla():
    """Kirish maydonchasidagi ifodani hisoblaydi va natijani chiqaradi."""
    try:
        natija = eval(kirish_maydoni.get())
        kirish_maydoni.delete(0, tk.END)
        kirish_maydoni.insert(0, str(natija))
    except Exception as xato:
        kirish_maydoni.delete(0, tk.END)
        kirish_maydoni.insert(0, "Xatolik")

# Tkinter oynasini yaratish
oyna = tk.Tk()
oyna.title("Intelect Kalkulyator ")

# Kalkulyator natijalarini ko'rsatish uchun kirish maydoni
kirish_maydoni = tk.Entry(oyna, width=20, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
kirish_maydoni.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Tugmalar ro'yxati: har bir element (matn, qator, ustun)
tugmalar = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# Tugmalarni yaratish va joylashtirish
for (matn, qator, ustun) in tugmalar:
    if matn == '=':
        # "=" tugmasi: hisoblash funksiyasi bilan
        tugma = tk.Button(oyna, text=matn, width=20, height=2, font=("Arial", 18), command=hisobla)
        tugma.grid(row=qator, column=ustun, columnspan=4, padx=5, pady=5)
    elif matn == 'C':
        # "C" tugmasi: kirish maydonchasini tozalash uchun
        tugma = tk.Button(oyna, text=matn, width=5, height=2, font=("Arial", 18), command=tozalash)
        tugma.grid(row=qator, column=ustun, padx=5, pady=5)
    else:
        # Boshqa tugmalar: ularning bosilishi qiymatni qo'shadi
        tugma = tk.Button(oyna, text=matn, width=5, height=2, font=("Arial", 18),
                          command=lambda qiymat=matn: tugma_bosildi(qiymat))
        tugma.grid(row=qator, column=ustun, padx=5, pady=5)

# Oyna asosiy siklini ishga tushirish
oyna.mainloop()

