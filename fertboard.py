import tkinter as tk

class GuitarFretboard(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.markers = [[] for _ in range(6)]  # 为每根弦初始化标记列表
        self.bind("<Button-1>", self.on_click)  # 绑定点击事件
        self.draw_fretboard()  # 绘制指板

    def draw_fretboard(self):
        fret_width = 20  # 品格宽度
        fret_height = 120  # 品格高度
        string_spacing = 20  # 弦间距
        fret_spacing = 30  # 品间距

        # 绘制品
        for i in range(1, 14):
            self.create_line(i * fret_spacing, string_spacing, i * fret_spacing, fret_height)

        # 绘制弦
        for i in range(6):
            self.create_line(fret_spacing, string_spacing + i * string_spacing,
                             13 * fret_spacing, string_spacing + i * string_spacing)

        # 绘制弦枕
        self.create_line(fret_spacing - 5, string_spacing - 5, fret_spacing - 5, fret_height + 5, width=2)

        # 绘制品记号（品上的圆点）
        fret_markers = [3, 5, 7, 9]  # 有单一记号的品
        for fret in fret_markers:
            x = fret * fret_spacing + fret_spacing / 2
            y = (fret_height + string_spacing) / 2
            self.create_oval(x-5, y-5, x+5, y+5, fill="black")

        # 绘制第12品上的双记号
        x = 12 * fret_spacing + fret_spacing / 2
        y1 = fret_height / 2.3
        y2 = 2 * fret_height / 2.7
        self.create_oval(x-5, y1-5, x+5, y1+5, fill="black")
        self.create_oval(x-5, y2-5, x+5, y2+5, fill="black")

    def on_click(self, event):
        x, y = event.x, event.y
        string = (y - 10) // 20  # 调整以更好地对齐
        fret = (x - 15) // 30
        if 0 <= string < 6 and 0 <= fret < 12:
            self.highlight_fret(string, fret)
            print(f"Clicked on string {string + 1}, fret {fret + 1}")

    def highlight_fret(self, string, fret):
        fret_spacing = 30
        string_spacing = 20
        x = fret * fret_spacing + fret_spacing / 2
        y = string * string_spacing + 20  # 调整y使其在弦上
        
        # 清除同一弦上的任何现有标记
        if self.markers[string]:
            self.delete(self.markers[string][0])
            self.markers[string] = []

        # 创建新标记
        marker = self.create_oval(x-5, y-5, x+5, y+5, fill="red")
        self.markers[string].append(marker)  # 记录新标记

    def clear_markers(self):
        for string_markers in self.markers:
            for marker in string_markers:
                self.delete(marker)
        self.markers = [[] for _ in range(6)]  # 重置标记列表

root = tk.Tk()
root.title("Guitar Fretboard")
fretboard = GuitarFretboard(root, width=390, height=180)
fretboard.pack()
clear_button = tk.Button(root, text="Clear", command=fretboard.clear_markers)
clear_button.pack(pady=10)
root.mainloop()
