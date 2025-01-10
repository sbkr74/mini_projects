import curses

def main(stdscr):
    curses.curs_set(1)  # Enable cursor
    stdscr.clear()

    # Get terminal size
    height, width = stdscr.getmaxyx()

    # Create windows for input and output
    output_win = stdscr.subwin(height - 3, width, 0, 0)
    input_win = stdscr.subwin(3, width, height - 3, 0)
    
    output_win.scrollok(True)
    input_win.addstr(0, 0, "Input: ")
    
    # Input loop
    while True:
        # Display output
        output_win.addstr(f"Output line at {curses.LINES - 3}\n")
        output_win.refresh()

        # Get input from user
        input_win.clear()
        input_win.addstr(0, 0, "Input: ")
        curses.echo()
        user_input = input_win.getstr(0, 7).decode('utf-8')

        if user_input.lower() == "quit":
            break
        
        # Process input
        output_win.addstr(f"You entered: {user_input}\n")

curses.wrapper(main)
