import time
import tkinter as tk

def start_timer():
    # 获取用户输入的专注时间（以分钟为单位）
    focus_time_minutes = int(entry.get())
    focus_time_seconds = focus_time_minutes * 60

    # 禁用开始按钮和输入框，以防止用户在计时期间更改设置
    start_button.config(state=tk.DISABLED)
    entry.config(state=tk.DISABLED)

    # 计时循环
    for remaining_time in range(focus_time_seconds, 0, -1):
        minutes, seconds = divmod(remaining_time, 60)
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        root.update()
        time.sleep(1)

    # 恢复开始按钮和输入框的状态
    start_button.config(state=tk.NORMAL)
    entry.config(state=tk.NORMAL)
    timer_label.config(text="00:00")

# 创建主窗口
root = tk.Tk()
root.title("专注时钟")

# 创建并布置窗口组件
tk.Label(root, text="专注时间（分钟）:").pack(pady=10)
entry = tk.Entry(root, width=5)
entry.pack(pady=10)
entry.insert(0, "25")

start_button = tk.Button(root, text="开始专注", command=start_timer)
start_button.pack(pady=10)

timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

# 启动主事件循环
root.mainloop()
