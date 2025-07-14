from book import Book
from member import Member
from library import Library
from curses import wrapper




def main(stdscr):
   stdscr.clear()
   stdscr.refresh()
   stdscr.getch()



def admin_login():
    pass

def member_login():
    pass

if __name__ == "__main__":
    wrapper(main)