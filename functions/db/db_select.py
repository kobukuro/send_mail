import cx_Oracle
import pandas as pd

def getOracleData(ip,
                  port,
                  DBname,
                  userName,
                  password,
                  statement):
    dsn_tns = cx_Oracle.makedsn(ip, port, DBname)
    conn = cx_Oracle.connect(userName, password, dsn_tns,encoding='UTF-8')
    df_ora = pd.read_sql(statement, con=conn)
    conn.close()
    return df_ora

def selectOracleSeq(ip,
                  port,
                  DBname,
                  userName,
                  password,
                  seqName):

    dsn_tns = cx_Oracle.makedsn(ip, port, DBname)
    conn = cx_Oracle.connect(userName, password, dsn_tns,encoding='UTF-8')

    sql = 'SELECT '+ seqName +'.NEXTVAL COL FROM DUAL'
    df_ora = int(pd.read_sql(sql, con=conn).loc[0, 'COL'])
    conn.close()
    return df_ora