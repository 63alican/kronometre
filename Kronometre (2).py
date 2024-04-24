import tkinter as tk

def geri_say():
    global dk,sn
    if dk==0 and sn == 0:
        label.config(text="Süre bitmiştir")
    else:
        if sn == 0:
            dk -=1
            sn = 59
        else:
            sn -=1
        root.after(1000,geri_say)
    label1.config(text="{:02d} . {:02d}".format(dk,sn))
def baslat():
    global dk,sn
    dk = int(dk_entry.get())
    sn = int(sn_entry.get())
    geri_say()
    label1.config(text="{:02d} . {:02d}".format(dk,sn))

root = tk.Tk()
root.title("Geri Sayım")

label1 =tk.Label(root,text="00.00", font=("Arial",48))
label1.pack()
label = tk.Label(root,text="",font=("Arial",48))
label.pack()

label_dakika = tk.Label(root,text="Dakika:")
label_dakika.pack()

dk_entry = tk.Entry(root)
dk_entry.pack()

label_saniye = tk.Label(root,text="Saniye:")
label_saniye.pack()

sn_entry = tk.Entry(root)
sn_entry.pack()

baslat_button = tk.Button(root,text="Başlat", command=baslat)
baslat_button.pack()

root.mainloop()