# coding: UTF-8

import mysql.connector
import sys
import os


def main():
    """
    引数で指定したホストのmysqlレプリケーションのステータスを取得する
    Slave_IO_Running
    Slave_SQL_Running
    Seconds_Behind_Master
    """

    try:
        argv = sys.argv
        argv_len = len(argv)
        # print(argv_len)

        if argv_len < 2:
            print("ホスト名を引数で1つ以上指定してください")
            sys.exit()

        # リスト内並び替え 実行ファイル名削除するから不要になった
        # argv.reverse()
        # print(argv)

        # 1個目の引数を削除(実行ファイル名)
        argv.pop(0)
        # print(argv)

        for host in argv:
            conn = mysql.connector.connect(
                host=host,
                port=3306,
                user=os.environ['MONITORING_DB_USER'],
                passwd=os.environ['MONITORING_DB_PASS']
            )
            c = conn.cursor()

            sql = 'SHOW SLAVE STATUS'
            c.execute(sql)

            for row in c.fetchall():
                print("%s\nSlave_IO_Running: %s, Slave_SQL_Running: %s, Seconds_Behind_Master: %d " % (host, row[10], row[11], row[32]))
            c.close
            conn.close

    except Exception as e:
        emsg = sys._getframe().f_code.co_name + str(e) + "\ntype:" + str(type(e)) + "\nargs:" + str(e.args)
        sys.exit(emsg)


if __name__ == '__main__':
    main()
