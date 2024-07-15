import curses

def main(stdscr):
    curses.curs_set(0)  # 隐藏光标
    stdscr.timeout(-1)  # 设置非阻塞读取，这里为了演示改为阻塞模式可设为0
    
    choices = ["加载模组", "编辑语言条目", "保存资源包", "退出"]
    current_choice = 0

    while True:
        stdscr.clear()
        for index, choice in enumerate(choices):
            x = 2
            y = index + 2
            if index == current_choice:
                stdscr.attron(curses.A_REVERSE)  # 选中项高亮
            stdscr.addstr(y, x, choice)
            if index == current_choice:
                stdscr.attroff(curses.A_REVERSE)  # 取消高亮

        key = stdscr.getch()

        if key == curses.KEY_UP and current_choice > 0:
            current_choice -= 1
        elif key == curses.KEY_DOWN and current_choice < len(choices) - 1:
            current_choice += 1
        elif key == ord(' ') or key in [10, 13]:  # 空格键或回车键确认
            if current_choice == len(choices) - 1:  # 如果选择“退出”
                break
            else:
                process_choice(current_choice)  # 这里应调用对应的功能函数

    stdscr.refresh()
    curses.endwin()

def process_choice(choice_index):
    if choice_index == 0:
        print("加载模组功能...")
    elif choice_index == 1:
        print("编辑语言条目功能...")
    elif choice_index == 2:
        print("保存资源包功能...")
    # 实现每个选项对应的逻辑...

if __name__ == "__main__":
    curses.wrapper(main)