# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/1.txt 10:06
@Auth ： Dosbo
@Motto: 快乐小杜！加油每一天！！！
"""
import datetime
import sys

import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QMessageBox, QTableWidgetItem, QHeaderView, \
    QAbstractItemView

import ui_main, ui_index, ui_login, ui_reset, ui_register, ui_forget, ui_loss, ui_manage, ui_select, \
    ui_top_up, ui_open_card, ui_change_card_info, ui_change_pwd, ui_select_all, ui_user_info, ui_add_user, \
    ui_loss_and_logout

''' ------------------------------------窗口区------------------------------------'''


class main_window(QMainWindow, ui_main.Ui_main_window):  # 登录之后的主页面
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', '确定退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            close_main_windows()
        else:
            event.ignore()


class index_window(QMainWindow, ui_index.Ui_index_window):  # 最开始的首页
    def __init__(self):
        super(index_window, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', '确定退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            close_index_windows()
        else:
            event.ignore()


class login_window(QMainWindow, ui_login.Ui_login_window):  # 登录页面

    def __init__(self):
        super(login_window, self).__init__()
        self.setupUi(self)


class reset_window(QMainWindow, ui_reset.Ui_reset_window):  # 找回密码界面
    def __init__(self):
        super(reset_window, self).__init__()
        self.setupUi(self)


class register_window(QMainWindow, ui_register.Ui_register_window):  # 注册界面
    def __init__(self):
        super(register_window, self).__init__()
        self.setupUi(self)


class forget_window(QMainWindow, ui_forget.Ui_forget_window):  # 找回密码之前的验证账号界面
    def __init__(self):
        super(forget_window, self).__init__()
        self.setupUi(self)


class loss_window(QMainWindow, ui_loss.Ui_loss_window):  # 挂失界面
    def __init__(self):
        super(loss_window, self).__init__()
        self.setupUi(self)


class select_window(QMainWindow, ui_select.Ui_select_window):  # 查询界面
    def __init__(self):
        super(select_window, self).__init__()
        self.setupUi(self)


class manage_window(QMainWindow, ui_manage.Ui_manage_window):  # 管理员界面
    def __init__(self):
        super(manage_window, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', '确定退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            close_manage_windows()
        else:
            event.ignore()


class open_card_window(QMainWindow, ui_open_card.Ui_open_card_window):  # 开卡界面
    def __init__(self):
        super(open_card_window, self).__init__()
        self.setupUi(self)


class top_up_window(QMainWindow, ui_top_up.Ui_top_up_window):  # 充值界面
    def __init__(self):
        super(top_up_window, self).__init__()
        self.setupUi(self)


class change_card_info_window(QMainWindow, ui_change_card_info.Ui_change_card_info):  # 修改卡信息界面
    def __init__(self):
        super(change_card_info_window, self).__init__()
        self.setupUi(self)


class change_pwd_window(QMainWindow, ui_change_pwd.Ui_change_pwd_window):  # 修改密码界面
    def __init__(self):
        super(change_pwd_window, self).__init__()
        self.setupUi(self)


class select_all_window(QMainWindow, ui_select_all.Ui_select_all_window):  # 查询所有界面
    def __init__(self):
        super(select_all_window, self).__init__()
        self.setupUi(self)


class user_info_window(QMainWindow, ui_user_info.Ui_user_info_window):  # 用户信息界面
    def __init__(self):
        super(user_info_window, self).__init__()
        self.setupUi(self)


class add_user_window(QMainWindow, ui_add_user.Ui_add_user_window):  # 新建用户界面
    def __init__(self):
        super(add_user_window, self).__init__()
        self.setupUi(self)


class loss_and_logout_window(QMainWindow, ui_loss_and_logout.Ui_loss_and_logout_window):  # 挂失并注销界面
    def __init__(self):
        super(loss_and_logout_window, self).__init__()
        self.setupUi(self)


''' ------------------------------------方法区------------------------------------'''


def connect_mysql():  # 连接数据库
    conn = pymysql.connect(host='localhost', user='root', password='root',
                           database='FoodCardMS',
                           charset='utf8')
    return conn


def now_time():  # 获取当前时间
    now = datetime.datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date


# index 界面
def open_login_window():
    login_window.show()


def open_register_window():
    register_window.show()


# login 界面
def click_logging_btn():  # 登录
    conn = connect_mysql()
    cur = conn.cursor()
    sql = f"select name from cardholder_info where sId = '{login_window.username_edit.text()}'"
    cur.execute(sql)
    names = cur.fetchall()
    if len(names) == 0:
        name = login_window.username_edit.text()
    else:
        name = names[0][0]
    if login_judgment() == 3:
        login_window.hide()
        main_window.show()
        index_window.hide()
        main_window.name_label.setText(name)  # 传递用户名
        main_flush(name)
        clear_login_window()
        close_index_windows()

    elif login_judgment() == 1:
        QMessageBox(QMessageBox.Warning, '警告', '用户不存在或用户类别错误！').exec_()
    elif login_judgment() == 2:
        QMessageBox(QMessageBox.Warning, '警告', '密码错误！').exec_()
    elif login_judgment() == 4:
        login_window.hide()
        manage_window.show()
        index_window.hide()
        manage_window.name_label.setText(name)  # 传递用户名
        clear_login_window()
        close_index_windows()
    elif login_judgment() == 5:
        QMessageBox(QMessageBox.Warning, '警告', '不能为空！').exec_()
    cur.close()


def login_judgment():  # 登录判断用户是否存在
    cur = connect_mysql().cursor()
    cur.execute("select * from user_info")
    list_info = cur.fetchall()
    if_login = 0
    for i in list_info:
        if len(login_window.username_edit.text()) == 0:
            if_login = 5
            break
        try:
            int(login_window.username_edit.text())
        except ValueError:
            if_login = 1
            break
        if int(login_window.username_edit.text()) == i[1]:
            if login_window.password_edit.text() == i[2]:
                login_type = login_window.comboBox.currentText()
                if login_type == '管理员':
                    login_type = 0
                elif login_type == '学生':
                    login_type = 1
                elif login_type == '教职工':
                    login_type = 2
                if login_type == i[3]:
                    if login_type == 1 or login_type == 2:
                        if_login = 3  # 主页面
                        break
                    elif login_type == 0:
                        if_login = 4  # 管理员
                        break
                else:
                    if_login = 1
                    break
            else:
                if_login = 2  # 密码错误!
                break
        else:
            if_login = 1  # 用户不存在!
    cur.close()
    return if_login


def clear_login_window():
    login_window.username_edit.clear()
    login_window.password_edit.clear()


def open_forget_window():
    login_window.hide()
    forget_window.show()


# forget 忘记密码界面
def click_finding_btn():
    conn = connect_mysql()
    cur = conn.cursor()
    sql = f"select name,phoneNum from cardholder_info where sId = '{forget_window.sid_edit.text()}'"
    cur.execute(sql)
    info = cur.fetchall()
    if len(info) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '账号不存在！').exec_()
    else:
        if info[0] == (forget_window.username_edit.text(), forget_window.phone_edit.text()):
            forget_window.hide()
            reset_window.show()
            clear_forget_window()
        else:
            QMessageBox(QMessageBox.Warning, '警告', '信息错误！').exec_()
    cur.close()


def clear_forget_window():
    forget_window.sid_edit.clear()
    forget_window.username_edit.clear()
    forget_window.phone_edit.clear()


# reset 重置密码界面
def click_set_btn():
    conn = connect_mysql()
    cur = conn.cursor()
    if len(reset_window.password_edit.text()) != 0 and len(reset_window.check_edit.text()) != 0 and len(
            reset_window.sid_edit.text()) != 0:
        if reset_window.password_edit.text() == reset_window.check_edit.text():
            try:
                sql = f"select user from user_info"
                cur.execute(sql)
                users = cur.fetchall()
                user_list = []
                for i in users[0]:
                    user_list.append(i)
                if int(reset_window.sid_edit.text()) in user_list:
                    sql = f"update user_info set pwd = '{int(reset_window.password_edit.text())}' where user = '{int(reset_window.sid_edit.text())}'"
                    cur.execute(sql)
                    conn.commit()
                    QMessageBox(QMessageBox.Information, '提示', '重置成功！').exec_()
                    reset_window.hide()
                    index_window.show()
                    clear_reset_window()
                else:
                    QMessageBox(QMessageBox.Warning, '警告', '用户不存在！').exec_()
            except pymysql.err.OperationalError:
                QMessageBox(QMessageBox.Warning, '警告', '账号错误！').exec_()
        else:
            QMessageBox(QMessageBox.Warning, '警告', '两次密码不一致！').exec_()
    else:
        QMessageBox(QMessageBox.Warning, '警告', '不能为空！').exec_()

    cur.close()


def clear_reset_window():
    reset_window.sid_edit.clear()
    reset_window.password_edit.clear()
    reset_window.check_edit.clear()


# register 注册界面
def click_register_btn():
    user = register_window.username_edit.text()
    password = register_window.password_edit.text()
    check_pwd = register_window.password_edit_2.text()
    conn = connect_mysql()
    cur = conn.cursor()
    if user == '' or password == '':
        QMessageBox(QMessageBox.Warning, '警告', '用户名或密码不能为空！').exec_()
    else:
        if password == check_pwd:
            cur.execute("select * from user_info")
            list_info = cur.fetchall()
            for i in list_info:
                if int(user) == i[1]:
                    QMessageBox(QMessageBox.Warning, '警告', '该用户已存在！').exec_()
                    break
            else:
                sql = f"insert into user_info(user,pwd,type,cardHolder) values ('{user}', '{password}', 1.txt,0);"
                cur.execute(sql)
                conn.commit()
                QMessageBox(QMessageBox.Information, '提示', '默认用户类型为学生，申请办卡后会自动修改。').exec_()
                cur.execute("select sId from cardholder_info")
                ids = cur.fetchall()
                if user not in ids:
                    QMessageBox(QMessageBox.Information, '提示', '首次注册，请完成办卡。').exec_()
                    # 办卡
                    open_card_after_register()
                    register_window.hide()

                else:
                    register_window.hide()
                    index_window.show()
        else:
            QMessageBox(QMessageBox.Warning, '警告', '两次密码不一致！').exec_()
        cur.close()


def open_card_after_register():
    open_card_window.sid_lab.setText(register_window.username_edit.text())
    open_card_window.show()


def clear_register_window():
    register_window.username_edit.clear()
    register_window.password_edit.clear()
    register_window.password_edit_2.clear()


# main 首页界面
def click_main_back_btn():
    main_window.hide()
    clear_main_window()
    clear_register_window()
    index_window.show()
    close_main_windows()


def main_flush(name):
    conn = connect_mysql()
    cur = conn.cursor()
    sql = f"select cardId from cardholder_info where name = '{name}'"
    cur.execute(sql)
    info = cur.fetchall()
    if len(info) == 0:
        pass
    else:
        cardId = info[0][0]
        sql = f"select balance from card_info where cardId = '{cardId}'"
        cur.execute(sql)
        info_money = cur.fetchall()
        if len(info_money) == 0:
            balance = ''
        else:
            balance = info_money[0][0]
        main_window.name_label.setText(name)
        main_window.balance_label.setText(str(balance))
    cur.close()


def clear_main_window():
    main_window.name_label.clear()
    main_window.balance_label.clear()


def open_change_pwd_window():
    change_pwd_window.show()


def open_open_card_window():
    conn = connect_mysql()
    cur = conn.cursor()
    name = main_window.name_label.text()
    cur.execute(f"select * from cardholder_info where name = '{name}'")
    infos = cur.fetchall()
    if len(infos) == 0:
        open_card_window.show()
    else:
        info = infos[0]
        change_card_info_window.sid_lab.setText(str(info[1]))
        change_card_info_window.name_edit.setText(str(info[2]))
        change_card_info_window.sex_comb.setCurrentText(info[3])
        change_card_info_window.phone_edit.setText(str(info[4]))
        change_card_info_window.address_edit.setText(str(info[5]))
        sql = f"select type from user_info where user = '{info[1]}'"
        cur.execute(sql)
        type_info = cur.fetchone()[0]
        if type_info == 0:
            type_info = '管理员'
        elif type_info == 1:
            type_info = '学生'
        elif type_info == 2:
            type_info = '教职工'
        change_card_info_window.type_comb.setCurrentText(type_info)
        change_card_info_window.show()
    cur.close()


def open_loss_window():
    conn = connect_mysql()
    cur = conn.cursor()
    cur.execute(f"select * from cardholder_info where name = '{main_window.name_label.text()}'")
    infos = cur.fetchall()
    if len(infos) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '请先办卡！').exec_()
    else:
        sid = infos[0][1]
        name = infos[0][2]
        phone = infos[0][4]
        card_id = infos[0][0]
        loss_window.sid_edit.setText(str(sid))
        loss_window.username_edit.setText(name)
        loss_window.phone_edit.setText(str(phone))
        loss_window.cardid_edit.setText(str(card_id))
        loss_window.show()
    cur.close()


def open_select_window():
    conn = connect_mysql()
    cur = conn.cursor()
    cur.execute(f"select * from cardholder_info where name = '{main_window.name_label.text()}'")
    infos = cur.fetchall()
    if len(infos) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '请先办卡！').exec_()
        cur.close()
    else:
        cur.close()
        flush_btn()
        select_window.show()


def open_top_up_window():
    conn = connect_mysql()
    cur = conn.cursor()
    cur.execute(f"select * from cardholder_info where name = '{main_window.name_label.text()}'")
    infos = cur.fetchall()
    if len(infos) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '请先办卡！').exec_()
    else:
        sql = f"select cardId from cardholder_info where name = '{main_window.name_label.text()}'"
        cur.execute(sql)
        cardId = cur.fetchall()[0][0]
        top_up_window.card_edit.setText(str(cardId))
        top_up_window.show()
    cur.close()


# change_pwd界面
def click_change_pwd_set_btn():  # 修改密码
    conn = connect_mysql()
    cur = conn.cursor()
    name = main_window.name_label.text()
    if len(name) == 0:
        name = manage_window.name_label.text()
    old_pwd = change_pwd_window.old_pwd_edit.text()
    new_pwd = change_pwd_window.new_pwd_edit.text()
    new_pwd_check = change_pwd_window.check_new_pwd_edit.text()
    cur.execute(f"select pwd from user_info where (select sId from cardholder_info where "
                f"name = '{name}') = user")
    pwd = cur.fetchall()[0][0]
    if len(old_pwd) == 0 or len(new_pwd) == 0 or len(new_pwd_check) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '不能为空！').exec_()
    elif old_pwd != pwd:
        QMessageBox(QMessageBox.Warning, '警告', '原密码错误！').exec_()
    elif new_pwd != new_pwd_check:
        QMessageBox(QMessageBox.Warning, '警告', '两次密码不一致！').exec_()
    else:
        sql = f"update user_info set pwd = '{new_pwd}' where (select sId from cardholder_info where " \
              f"name = '{name}') = user"
        cur.execute(sql)
        conn.commit()
        QMessageBox(QMessageBox.Information, '提示', '修改成功！').exec_()
        change_pwd_window.hide()
    clear_change_pwd_window()
    cur.close()


def clear_change_pwd_window():
    change_pwd_window.old_pwd_edit.clear()
    change_pwd_window.new_pwd_edit.clear()
    change_pwd_window.check_new_pwd_edit.clear()


# openCard界面
def click_open_card_set_btn():  # 办卡
    conn = connect_mysql()
    cur = conn.cursor()
    sid = register_window.username_edit.text()
    name = open_card_window.name_edit.text()
    sex = open_card_window.sex_comb.currentText()
    type_info = open_card_window.type_comb.currentText()
    if type_info == '学生':
        type_info = 1
    elif type_info == '教职工':
        type_info = 2
    phone = open_card_window.phone_edit.text()
    address = open_card_window.address_edit.toPlainText()
    if len(sid) == 0 or len(name) == 0 or len(phone) == 0 or len(address) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '不能为空！').exec_()
    elif len(phone) != 11:
        QMessageBox(QMessageBox.Warning, '警告', '手机号码错误！').exec_()
    else:
        sql = f"insert into cardholder_info(cardId,sId,name,gender,phoneNum,address) values ('{sid}','{sid}', " \
              f"'{name}','{sex}','{phone}','{address}');"
        cur.execute(sql)
        conn.commit()
        sql = f"update user_info set type = '{type_info}' where user = '{sid}';"
        cur.execute(sql)
        conn.commit()
        sql = f"insert into card_info(balance,cardlock,cardId) values (0,0,'{sid}');"
        cur.execute(sql)
        conn.commit()
        QMessageBox(QMessageBox.Information, '提示', '注册提交。').exec_()
        index_window.show()
        open_card_window.hide()
        main_window.hide()
    cur.close()


def clear_open_card_window():
    open_card_window.sid_edit.clear()
    open_card_window.name_edit.clear()
    open_card_window.phone_edit.clear()
    open_card_window.address_edit.clear()


# changeCardInfo 修改饭卡信息界面
def click_change_info_btn():
    conn = connect_mysql()
    cur = conn.cursor()
    sid = change_card_info_window.sid_lab.text()
    name = change_card_info_window.name_edit.text()
    sex = change_card_info_window.sex_comb.currentText()
    type_info = change_card_info_window.type_comb.currentText()
    if type_info == '学生':
        type_info = 1
    elif type_info == '教职工':
        type_info = 2
    phone = change_card_info_window.phone_edit.text()
    address = change_card_info_window.address_edit.toPlainText()
    if len(sid) == 0 or len(name) == 0 or len(phone) == 0 or len(address) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '不能为空！').exec_()
    elif len(phone) != 11:
        QMessageBox(QMessageBox.Warning, '警告', '手机号码错误！').exec_()
    else:
        sql = f"update cardholder_info set name = '{name}',gender = '{sex}',phoneNum = '{phone}',address = '{address}'" \
              f" where sId = '{sid}';"
        cur.execute(sql)
        conn.commit()
        sql = f"update user_info set type = '{type_info}' where user = '{sid}';"
        cur.execute(sql)
        conn.commit()
        QMessageBox(QMessageBox.Information, '提示', '修改提交。').exec_()
        change_card_info_window.hide()
        main_flush(name)
    cur.close()


# loss 挂失界面
def click_up_btn():
    conn = connect_mysql()
    cur = conn.cursor()
    is_loss = False
    time = now_time()
    sid = loss_window.sid_edit.text()
    name = loss_window.username_edit.text()
    phone = loss_window.phone_edit.text()
    card_id = loss_window.cardid_edit.text()
    reason = loss_window.loss_reason.toPlainText()
    sql = f"select operation from cardhistory_info where cardId = '{card_id}';"
    cur.execute(sql)
    infos = cur.fetchall()
    for i in infos:
        if i[0] == 2:
            is_loss = True
            break
    if is_loss:
        QMessageBox(QMessageBox.Warning, '警告', '该卡已挂失！').exec_()
    else:
        if len(sid) == 0 or len(name) == 0 or len(phone) == 0 or len(card_id) == 0 or len(reason) == 0:
            QMessageBox(QMessageBox.Warning, '警告', '不能为空！').exec_()
        else:
            sql = f"select sId,name,phoneNum,cardId from cardholder_info where sId = '{sid}'"
            cur.execute(sql)
            info = cur.fetchall()
            if info[0] == (int(sid), name, phone, int(card_id)):
                sql = f"select balance from card_info where cardId = '{card_id}'"
                cur.execute(sql)
                money = cur.fetchall()[0][0]
                sql = f"update card_info set cardlock = 1.txt where cardId = '{card_id}'"
                cur.execute(sql)
                conn.commit()
                try:
                    sql = f"insert into cardhistory_info(cardId,opear_time,money,operation,info) values ({card_id},'{time}',{money},2,'{reason}')"
                    cur.execute(sql)
                    conn.commit()
                except pymysql.err.OperationalError:
                    sql = f"update card_info set cardlock = 0 where cardId = '{card_id}'"
                    cur.execute(sql)
                    conn.commit()
                    QMessageBox(QMessageBox.Warning, '警告', '挂失失败！').exec_()
                QMessageBox(QMessageBox.Information, '提示', '挂失成功！').exec_()
                loss_window.hide()
                main_window.show()
                clear_loss_window()
            else:
                QMessageBox(QMessageBox.Warning, '警告', '信息错误！').exec_()
    cur.close()


def click_cancel_btn():
    conn = connect_mysql()
    cur = conn.cursor()
    sql = f"select cardlock from card_info where cardId = '{loss_window.sid_edit.text()}'"
    cur.execute(sql)
    info_lock = cur.fetchall()[0][0]
    if info_lock != 1:
        QMessageBox(QMessageBox.Warning, '警告', '卡未挂失！').exec_()
    else:
        sql = f"update card_info set cardlock = 0 where cardId = '{loss_window.sid_edit.text()}'"
        cur.execute(sql)
        conn.commit()
        sql = f"delete from cardhistory_info where cardId = '{loss_window.sid_edit.text()}' and operation = 2"
        cur.execute(sql)
        conn.commit()
        QMessageBox(QMessageBox.Information, '提示', '解挂成功！').exec_()
        loss_window.hide()
        main_window.show()
    cur.close()


def clear_loss_window():
    loss_window.sid_edit.clear()
    loss_window.username_edit.clear()
    loss_window.phone_edit.clear()
    loss_window.cardid_edit.clear()
    loss_window.loss_reason.clear()


# selectCardInfo 查询界面
def click_flush_btn():
    flush_btn()


def flush_btn():  # 刷新信息
    conn = connect_mysql()
    cur = conn.cursor()
    sql = f"select cardId from cardholder_info where name = '{main_window.name_label.text()}'"
    cur.execute(sql)
    cardId = cur.fetchall()[0][0]
    sql = f"select opear_time, money, operation from cardhistory_info where cardId = '{cardId}'"
    cur.execute(sql)
    info = cur.fetchall()
    lists = []
    operation = ''
    for i in info:
        if i[2] == 0:
            operation = '充值'
        elif i[2] == 1:
            operation = '消费'
        elif i[2] == 2:
            operation = '挂失'
        lists.append([i[0], i[1], operation])
    select_window.info_table.setRowCount(len(lists))
    select_window.info_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    select_window.info_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
    select_window.info_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    for i in range(len(lists)):
        for j in range(3):
            select_window.info_table.setItem(i, j, QTableWidgetItem(str(lists[i][j])))
            select_window.info_table.item(i, j).setTextAlignment(Qt.AlignCenter)
    select_window.card_id_label.setText(str(cardId))
    cur.close()


# topUp 充值界面
def click_top_up_btn():
    time = now_time()
    conn = connect_mysql()
    cur = conn.cursor()
    card_id = top_up_window.card_edit.text()
    money = top_up_window.money_edit.text()
    up_type = top_up_window.type_comb.currentText()
    if len(card_id) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '请输入卡号！').exec_()
    elif len(money) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '请输入金额！').exec_()
    elif float(money) <= 0:
        QMessageBox(QMessageBox.Warning, '警告', '金额错误！').exec_()
    else:
        sql = f"select balance from card_info where cardId = '{card_id}'"
        cur.execute(sql)
        balance = cur.fetchall()[0][0]
        sql = f"update card_info set balance = {balance + float(money)} where cardId = '{card_id}'"
        cur.execute(sql)
        conn.commit()
        sql = f"insert into cardhistory_info(cardId,opear_time,money,operation,info) values ({card_id},'{time}',{money},0,'充值方式是：{up_type}')"
        cur.execute(sql)
        conn.commit()
        QMessageBox(QMessageBox.Information, '提示', '充值成功！').exec_()
        main_flush(main_window.name_label.text())
        top_up_window.hide()
    clear_top_up_window()
    cur.close()


def clear_top_up_window():
    top_up_window.card_edit.clear()
    top_up_window.money_edit.clear()


# mange 管理员界面
def click_manage_back_btn():
    manage_window.hide()
    clear_main_window()
    clear_register_window()
    index_window.show()
    close_manage_windows()


def open_select_all_window():
    select_all_window.show()
    flush_all_btn()


def open_loss_and_logout_window():
    loss_and_logout_window.show()
    click_loss_and_logout_btn()


# selectAll 查询所有信息界面
def click_flush_all_btn():
    flush_all_btn()


def flush_all_btn():
    conn = connect_mysql()
    cur = conn.cursor()
    sql = f"select cardholder_info.sId, cardholder_info.cardId, cardholder_info.name,user_info.type,card_info.cardlock " \
          f"from card_info,cardholder_info,user_info " \
          f"where card_info.cardId = cardholder_info.cardId and cardholder_info.sId = user_info.user;"
    cur.execute(sql)
    info = cur.fetchall()
    lists = []
    user_type = ''
    card_lock = ''
    for i in info:
        if i[3] == 0:
            user_type = '管理员'
        elif i[3] == 1:
            user_type = '学生'
        elif i[3] == 2:
            user_type = '教职工'
        if i[4] == 0:
            card_lock = '正常'
        elif i[4] == 1:
            card_lock = '挂失'
        lists.append([i[0], i[1], i[2], user_type, card_lock])
    select_all_window.info_table.setRowCount(len(lists))
    select_all_window.info_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    select_all_window.info_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
    select_all_window.info_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    for i in range(len(lists)):
        for j in range(5):
            select_all_window.info_table.setItem(i, j, QTableWidgetItem(str(lists[i][j])))
            select_all_window.info_table.item(i, j).setTextAlignment(Qt.AlignCenter)
    cur.close()


def click_add_user_btn():
    add_user_window.show()


# add_user 新增用户界面
def click_set_new_user_btn():
    sid = add_user_window.sid_edit.text()
    name = add_user_window.name_edit.text()
    password = '000000'
    sex = add_user_window.sex_comb.currentText()
    user_type = add_user_window.type_comb.currentText()
    if user_type == '管理员':
        user_type = 0
    elif user_type == '学生':
        user_type = 1
    elif user_type == '教职工':
        user_type = 2
    phone = add_user_window.phone_edit.text()
    address = add_user_window.address_edit.toPlainText()
    cardholder = 1
    conn = connect_mysql()
    cur = conn.cursor()
    if len(sid) == 0 or len(name) == 0 or len(phone) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '不能为空').exec_()
    elif len(phone) != 11 or phone.isdigit() == False or len(phone) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '手机号码错误！').exec_()
    elif len(sid) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '请输入学号！').exec_()
    elif len(name) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '请输入姓名！').exec_()
    else:
        sql = f"insert into user_info(user,pwd,type,cardholder) values" \
              f" ({sid},'{password}',{user_type},{cardholder})"
        cur.execute(sql)
        conn.commit()
        sql = f"insert into cardholder_info(cardId,sId,name,gender,phoneNum,address) values ('{sid}','{sid}', " \
              f"'{name}','{sex}','{phone}','{address}');"
        cur.execute(sql)
        conn.commit()
        sql = f"insert into card_info(cardId,balance,cardlock) values" \
              f" ({sid},0,0)"
        cur.execute(sql)
        conn.commit()
        QMessageBox(QMessageBox.Information, '提示', '添加成功！').exec_()
        add_user_window.hide()
        clear_add_user_window()
    cur.close()


def clear_add_user_window():
    add_user_window.sid_edit.clear()
    add_user_window.name_edit.clear()
    add_user_window.phone_edit.clear()
    add_user_window.address_edit.clear()


# userInfo 用户详细信息界面
def open_user_info():
    row = select_all_window.info_table.currentRow()
    col = select_all_window.info_table.currentColumn()
    data_list = []
    for i in range(5):
        data_list.append(select_all_window.info_table.item(row, i).text())
    user_info_window.name_label.setText(data_list[2] + '的信息')
    user_info_window.show()
    click_user_info_btn()


def click_user_info_btn():
    user_info_window.infos.setCurrentIndex(0)
    conn = connect_mysql()
    cur = conn.cursor()
    name = user_info_window.name_label.text().split('的')[0]
    sql = f"select cardId, sId, name, gender,phoneNum, address,type from cardholder_info,user_info where cardholder_info.sId = user_info.user" \
          f" and name = '{name}';"
    cur.execute(sql)
    infos = cur.fetchall()
    info = infos[0]
    user_info_window.sid_edit.setText(str(info[1]))
    user_info_window.card_id_edit.setText(str(info[0]))
    user_info_window.name_edit.setText(info[2])
    user_info_window.sex_comb.setCurrentText(info[3])
    type_info = info[6]
    if type_info == '管理员':
        type_info = 0
    elif type_info == '学生':
        type_info = 1
    elif type_info == '教职工':
        type_info = 2
    user_info_window.type_comb.setCurrentText(str(type_info))
    user_info_window.phone_edit.setText(info[4])
    user_info_window.address_edit.setText(info[5])
    cur.close()


def click_change_bth():
    conn = connect_mysql()
    cur = conn.cursor()
    name = user_info_window.name_label.text().split("的")[0]
    sql = f"select sId,cardId from cardholder_info where name = '{name}';"
    cur.execute(sql)
    infos = cur.fetchall()
    user = infos[0][0]  # 65
    old_card_id = infos[0][1]  # 65
    sid = user_info_window.sid_edit.text()
    card_id = user_info_window.card_id_edit.text()
    name = user_info_window.name_edit.text()
    sex = user_info_window.sex_comb.currentText()
    type_info = user_info_window.type_comb.currentText()
    if type_info == '管理员':
        type_info = 0
    elif type_info == '学生':
        type_info = 1
    elif type_info == '教职工':
        type_info = 2
    phone = user_info_window.phone_edit.text()
    address = user_info_window.address_edit.toPlainText()
    if len(sid) == 0 or len(name) == 0 or len(phone) == 0:
        QMessageBox(QMessageBox.Warning, '警告', '不能为空').exec_()
    elif len(phone) != 11:
        QMessageBox(QMessageBox.Warning, '警告', '手机号码错误！').exec_()
    else:
        sql = f"update user_info set user = '{sid}' where user = '{user}';"
        cur.execute(sql)
        conn.commit()
        sql = f"update cardholder_info set cardId = '{card_id}',name = '{name}',gender = '{sex}',phoneNum = '{phone}',address = '{address}'" \
              f" where cardId = '{old_card_id}';"
        cur.execute(sql)
        conn.commit()
        sql = f"update user_info set type = '{type_info}' where user = '{user}';"
        cur.execute(sql)
        conn.commit()
        select_all_window.hide()
        open_select_all_window()
        user_info_window.hide()
        QMessageBox(QMessageBox.Information, '提示', '修改成功！').exec_()

    cur.close()


def click_account_btn():
    conn = connect_mysql()
    cur = conn.cursor()
    name = user_info_window.name_label.text().split("的")[0]
    sql = f"select cardId from cardholder_info where name = '{name}';"
    cur.execute(sql)
    infos = cur.fetchall()
    card_id = infos[0][0]
    user_info_window.card_id_label.setText(str(card_id))
    user_info_window.infos.setCurrentIndex(1)
    click_account_flush_btn()


def click_account_flush_btn():
    account_flush_btn()


def account_flush_btn():  # 刷新信息
    conn = connect_mysql()
    cur = conn.cursor()
    name = user_info_window.name_label.text().split("的")[0]
    sql = f"select cardId from cardholder_info where name = '{name}'"
    cur.execute(sql)
    infos = cur.fetchall()
    cardId = infos[0][0]
    sql = f"select opear_time, money, operation from cardhistory_info where cardId = '{cardId}'"
    cur.execute(sql)
    info = cur.fetchall()
    lists = []
    operation = ''
    for i in info:
        if i[2] == 0:
            operation = '充值'
        elif i[2] == 1:
            operation = '消费'
        elif i[2] == 2:
            operation = '挂失'
        lists.append([i[0], i[1], operation])
    user_info_window.info_table.setRowCount(len(lists))
    user_info_window.info_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    user_info_window.info_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
    user_info_window.info_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    for i in range(len(lists)):
        for j in range(3):
            user_info_window.info_table.setItem(i, j, QTableWidgetItem(str(lists[i][j])))
            user_info_window.info_table.item(i, j).setTextAlignment(Qt.AlignCenter)
    user_info_window.card_id_label.setText(str(cardId))
    cur.close()


# loss_and_logout_window 界面
def click_loss_logout_flush_btn():
    index = loss_and_logout_window.infos.currentIndex()
    if index == 0:
        click_loss_and_logout_btn()
    elif index == 1:
        click_logout_btn()


def click_loss_and_logout_btn():
    loss_and_logout_window.infos.setCurrentIndex(0)
    conn = connect_mysql()
    cur = conn.cursor()
    sql = "select opear_time,type,name, cardholder_info.sId,cardholder_info.cardId,balance,info from card_info,cardholder_info,cardhistory_info,user_info " \
          "where cardholder_info.cardId = cardhistory_info.cardId and user_info.user = cardholder_info.sId and card_info.cardId = cardholder_info.cardId" \
          " and operation = 2;"
    cur.execute(sql)
    info = cur.fetchall()
    lists = []
    for i in info:
        lists.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
    loss_and_logout_window.loss_table.setRowCount(len(lists))
    loss_and_logout_window.loss_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    loss_and_logout_window.loss_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
    loss_and_logout_window.loss_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    for i in range(len(lists)):
        for j in range(7):
            loss_and_logout_window.loss_table.setItem(i, j, QTableWidgetItem(str(lists[i][j])))
            loss_and_logout_window.loss_table.item(i, j).setTextAlignment(Qt.AlignCenter)
    cur.close()


def double_click_loss_table():
    row = loss_and_logout_window.loss_table.currentRow()
    col = loss_and_logout_window.loss_table.currentColumn()
    data_list = []
    for i in range(7):
        data_list.append(loss_and_logout_window.loss_table.item(row, i).text())
    reply = QMessageBox.question(None, '取消挂失', f'确定取消挂失  {data_list[2]}  吗？',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
        conn = connect_mysql()
        cur = conn.cursor()
        sql = f"update card_info set cardlock = 0 where cardId = '{data_list[3]}'"
        cur.execute(sql)
        conn.commit()
        sql = f"delete from cardhistory_info where cardId = '{data_list[3]}' and operation = 2"
        cur.execute(sql)
        conn.commit()
        QMessageBox(QMessageBox.Information, '提示', '解挂成功！').exec_()
        cur.close()
        click_loss_and_logout_btn()
    else:
        pass


def click_logout_btn():
    loss_and_logout_window.infos.setCurrentIndex(1)
    conn = connect_mysql()
    cur = conn.cursor()
    sql = "select name, sId,cardholder_info.cardId,balance from cardholder_info,card_info where card_info.cardId = cardholder_info.cardId;"
    cur.execute(sql)
    info = cur.fetchall()
    lists = []
    for i in info:
        lists.append([i[0], i[1], i[2], i[3]])
    loss_and_logout_window.logout_table.setRowCount(len(lists))
    loss_and_logout_window.logout_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    loss_and_logout_window.logout_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
    loss_and_logout_window.logout_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    for i in range(len(lists)):
        for j in range(4):
            loss_and_logout_window.logout_table.setItem(i, j, QTableWidgetItem(str(lists[i][j])))
            loss_and_logout_window.logout_table.item(i, j).setTextAlignment(Qt.AlignCenter)

    cur.close()


def double_click_logout_table():
    row = loss_and_logout_window.logout_table.currentRow()
    col = loss_and_logout_window.logout_table.currentColumn()
    data_list = []
    for i in range(4):
        data_list.append(loss_and_logout_window.logout_table.item(row, i).text())
    reply = QMessageBox.question(None, '注销用户', f'确定注销  {data_list[0]}  用户吗？',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
        conn = connect_mysql()
        cur = conn.cursor()
        sql = f"delete from user_info where user = '{data_list[1]}'"
        cur.execute(sql)
        conn.commit()
        QMessageBox(QMessageBox.Information, '提示', '注销成功！').exec_()
        cur.close()
        click_logout_btn()


def close_main_windows():
    open_card_window.close()
    loss_window.close()
    change_card_info_window.close()
    select_window.close()
    top_up_window.close()
    change_pwd_window.close()


def close_index_windows():
    login_window.close()
    reset_window.close()
    register_window.close()
    forget_window.close()


def close_manage_windows():
    select_all_window.close()
    user_info_window.close()
    add_user_window.close()
    loss_and_logout_window.close()

# 模拟消费
def click_spend_btn():
    conn = connect_mysql()
    cur = conn.cursor()
    sql = f"select cardId from cardholder_info where name = '{main_window.name_label.text()}'"
    cur.execute(sql)
    cardId = cur.fetchone()[0]
    sql = f"select balance from card_info where cardId = '{cardId}'"
    cur.execute(sql)
    balance = cur.fetchone()[0]
    if (balance - 10) > 0:
        sql = f"update card_info set balance = balance - 10 where cardId = '{cardId}'"
        cur.execute(sql)
        conn.commit()
        sql = f"insert into cardhistory_info (cardId,opear_time,money,operation,info)values('{cardId}', '{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', -10, 1.txt, '模拟消费')"
        cur.execute(sql)
        conn.commit()
        QMessageBox(QMessageBox.Information, '提示', '消费成功！').exec_()
        main_flush(main_window.name_label.text())
    else:
        QMessageBox(QMessageBox.Information, '提示', '余额不足！').exec_()
    cur.close()

''' ------------------------------------main函数区------------------------------------'''
if __name__ == '__main__':
    app = QApplication(sys.argv)

    ''' 为两个类创建对象 '''
    index_window = index_window()
    login_window = login_window()
    main_window = main_window()
    reset_window = reset_window()
    register_window = register_window()
    forget_window = forget_window()
    manage_window = manage_window()
    open_card_window = open_card_window()
    loss_window = loss_window()
    change_card_info_window = change_card_info_window()
    select_window = select_window()
    top_up_window = top_up_window()
    change_pwd_window = change_pwd_window()
    select_all_window = select_all_window()
    user_info_window = user_info_window()
    add_user_window = add_user_window()
    loss_and_logout_window = loss_and_logout_window()

    ''' 显示窗口 '''
    index_window.show()

    ''' 为登录按钮绑定点击事件 '''
    # index 主界面
    index_window.login_button.clicked.connect(open_login_window)  # 打开登录界面
    index_window.register_button.clicked.connect(open_register_window)  # 打开激活界面

    # login 登录界面
    login_window.logging_btn.clicked.connect(click_logging_btn)  # 登录界面点击登录
    login_window.forget_btn.clicked.connect(open_forget_window)  # 登录界面点击忘记密码

    # forget 忘记密码界面
    forget_window.finding_btn.clicked.connect(click_finding_btn)  # 忘记密码界面点击找回密码

    # reset 重置密码界面
    reset_window.set_btn.clicked.connect(click_set_btn)  # 重置密码界面点击设置密码

    # register 激活界面
    register_window.register_btn.clicked.connect(click_register_btn)  # 激活界面点击激活

    # main 主界面
    main_window.back_btn.clicked.connect(click_main_back_btn)  # 主界面点击返回
    main_window.re_card_btn.clicked.connect(open_open_card_window)  # 主界面点击办卡
    main_window.loss_card_btn.clicked.connect(open_loss_window)  # 主界面点击挂失
    main_window.select_btn.clicked.connect(open_select_window)  # 主界面点击挂失
    main_window.topup_btn.clicked.connect(open_top_up_window)  # 主界面点击充值
    main_window.change_pwd_btn.clicked.connect(open_change_pwd_window)  # 主界面点击修改密码

    main_window.spend_btn.clicked.connect(click_spend_btn)  # 主界面点击模拟消费
    # change_pwd 修改密码界面
    change_pwd_window.change_pwd_btn.clicked.connect(click_change_pwd_set_btn)  # 修改密码界面点击修改密码

    # openCard 办卡界面
    open_card_window.set_btn.clicked.connect(click_open_card_set_btn)  # 办卡界面点击办卡

    # loss 挂失界面
    loss_window.up_btn.clicked.connect(click_up_btn)  # 挂失界面点击挂失
    loss_window.cancel_btn.clicked.connect(click_cancel_btn)  # 挂失界面点击撤销挂失

    # changeCardInfo 修改饭卡信息界面
    change_card_info_window.change_btn.clicked.connect(click_change_info_btn)  # 修改饭卡信息界面点击修改

    # select 查询界面
    select_window.flush_btn.clicked.connect(click_flush_btn)  # 查询界面点击刷新

    # topUp 充值界面
    top_up_window.up_btn.clicked.connect(click_top_up_btn)  # 充值界面点击充值

    # manage 管理员界面
    manage_window.back_btn.clicked.connect(click_manage_back_btn)  # 管理员界面点击返回
    manage_window.change_pwd_btn.clicked.connect(open_change_pwd_window)  # 管理员界面点击修改密码
    manage_window.infos_btn.clicked.connect(open_select_all_window)  # 管理员界面点击查询所有信息
    manage_window.loss_logout_btn.clicked.connect(open_loss_and_logout_window)  # 管理员界面点击挂失注销
    # selectAll 查询所有界面
    select_all_window.flush_btn.clicked.connect(click_flush_all_btn)  # 查询所有界面点击刷新
    select_all_window.info_table.doubleClicked.connect(open_user_info)  # 查询所有界面点击表格
    select_all_window.add_user_btn.clicked.connect(click_add_user_btn)  # 增加新用户按钮

    # userInfo 用户信息界面
    user_info_window.info_btn.clicked.connect(click_user_info_btn)  # 用户信息界面点击修改
    user_info_window.account_btn.clicked.connect(click_account_btn)  # 用户信息界面点击账户
    user_info_window.change_btn.clicked.connect(click_change_bth)  # 用户信息界面点击饭卡

    # add_user 增加用户界面
    add_user_window.set_new_user_btn.clicked.connect(click_set_new_user_btn)  # 增加用户界面点击增加

    # lossAndLogout 挂失注销界面
    loss_and_logout_window.loss_logout_flush_btn.clicked.connect(click_loss_logout_flush_btn)  # 挂失注销界面点击刷新
    loss_and_logout_window.loss_btn.clicked.connect(click_loss_and_logout_btn)  # 挂失注销界面点击挂失
    loss_and_logout_window.logout_btn.clicked.connect(click_logout_btn)  # 挂失注销界面点击注销
    loss_and_logout_window.loss_table.doubleClicked.connect(double_click_loss_table)
    loss_and_logout_window.logout_table.doubleClicked.connect(double_click_logout_table)
    ''' 关闭程序，释放资源 '''
    sys.exit(app.exec_())
