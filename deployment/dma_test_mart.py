###
# Dev Server:
# DB: DMA_MART_TEST
#   1. Drop exsiting table
#   2. Sync target db
###

import os
import sys
sys.path.append(os.getcwd())

import conf.acct as acct
from tool.tool import file_name,logger,pop_db_name
import db_connect.db_operator as db_operator

target_db = "MS_HF_MART"
seed_file = ".\seed\SYNC_TARGET_DB.sql"


@logger
def clean_dma_test_mart(acct:dict):

    pop_db_name(acct)

    drop_ddl_query = "SELECT 'DROP TABLE [' + NAME + '];' FROM sysobjects WHERE xtype = 'U' AND uid = 1 ORDER BY name"
    drop_ddl_sql = ''
    drop_ddl_list = db_operator.query_db(drop_ddl_query,acct)

    for _ in drop_ddl_list:
        drop_ddl_sql += _[0]

    drop_sp_query = "SELECT 'DROP PROCEDURE [' + NAME + '];' FROM sys.all_objects a WHERE a.is_ms_shipped=0 AND a.[type] IN ('P','AF')"
    drop_sp_sql = ''
    drop_sp_list = db_operator.query_db(drop_sp_query,acct)

    drop_view_query = "SELECT 'DROP VIEW [' + NAME + '];' FROM sys.all_objects a WHERE a.is_ms_shipped=0 AND a.[type] IN ('V','AF')"
    drop_view_sql = ''
    drop_view_list = db_operator.query_db(drop_view_query,acct)

    for _ in drop_sp_list:
        drop_sp_sql += _[0]
    
    db_operator.update_db(drop_sp_sql,acct)
    db_operator.update_db(drop_ddl_sql,acct)
    
@logger
def build_target_db(acct:dict):
    buildsql = ''

    #pop_db_name(acct)

    with open(seed_file,encoding="utf") as file_object:
        lines = file_object.readlines()
    for line in lines:
        buildsql += line.replace(target_db,'DMA_MART_TEST').replace('GO\n','\n') #.replace('\n',' ').replace('\t',' ').

    db_operator.update_db(buildsql,acct)


clean_dma_test_mart(acct.DEV_DMA_MART_TEST)
#build_target_db(acct.DEV_DMA_MART_TEST)