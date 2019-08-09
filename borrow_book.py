# coding=utf-8

book_list = []  # 图书馆所有书

unborrowed_book = []  # 可借阅的书

borrowed_book = []  # 已经借出去的书


def add():  # 添加书

    global book_list

    global unborrowed_book

    book_name = raw_input(u"请输入要添加的书名：")

    book_list.append(book_name)

    unborrowed_book.append(book_name)

    print u"添加书成功"


def borrow_book():  # 借书

    global unborrowed_book

    global borrowed_book

    while 1:

        book_name = raw_input(u"请输入要借的书名：")

        if book_name in unborrowed_book:

            unborrowed_book.remove(book_name)

            borrowed_book.append(book_name)

            print u"借书成功"

            break

        else:

            print u"抱歉，您要借的书不存在!"

            continue_back = raw_input(u"继续借书请输入：c 返回主菜单请输入：b ：")

            if continue_back.lower() == "c":

                continue

            elif continue_back.lower() == "b":

                break

            else:

                print u"输入数据无效"


def return_book():  # 还书

    global borrowed_book

    global unborrowed_book

    while 1:

        book_name = raw_input(u"请输入要还的书名：")

        if book_name in borrowed_book:

            borrowed_book.remove(book_name)

            unborrowed_book.append(book_name)

            print u"还书成功"

            break

        else:

            print u"您输入的书名不是此图书馆的"

            continue_back = raw_input(u"继续还书请输入：c 返回主菜单请输入：b ：")

            if continue_back.lower() == "c":

                continue

            elif continue_back.lower() == "b":

                break

            else:

                print u"输入数据无效"


menu_info = '''

添加书--请输入：1

借书--请输入：2

查看可借阅的书--请输入：3

查看借出去的书--请输入：4

还书--请输入：5

查看所有书--请输入：6

退出--请输入：q

'''

import sys

print menu_info.decode("utf-8")

while True:

    command = raw_input(u"请输入您要做的操作选项：")

    if command == "1":

        add()

    elif command == "2":

        borrow_book()

    elif command == "3":

        if unborrowed_book == []:

            print u"抱歉，没有可以借的书了!"

        else:

            print u"可借阅的书：", unborrowed_book

    elif command == "4":

        if borrowed_book == []:

            print u"没有借出去的书！"

        else:

            print u"借出去的书：", borrowed_book

    elif command == "5":

        return_book()

    elif command == "6":

        if book_list == []:

            print u"图书馆还没有书，赶快去添加吧！"

        else:

            print u"图书馆所有的书：", book_list

    elif command == "q":

        sys.exit()

    else:

        print u"输入数据无效！"

