﻿
# -*- coding: utf-8 -*-
# Author        : Jesse Wei
# LastUpdate    : 2020/10/04
# Impact        : Jobs generated by SQLG
# Message       : Humanity towards others, we live by sharing. Fear can hold you prisoner, only hope can set you free.

# from __future__ import print_function
import logging
import airflow
from datetime import datetime, timedelta
from airflow.operators.sensors import ExternalTaskSensor
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor


from airflow import models
from airflow.models import Variable


from acme.operators.sqlg_oracle import OracleOperatorWithTemplatedParams
from airflow.operators.oracle_operator import OracleOperator
# DB_NAME = 'DWH'

# JOB_TYPE=ODS-MAIN
my_taskid = "MV_HR_EMPMSF_H"
MV_HR_EMPMSF_H = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MV_HR_EMPMSF_CN_H"
MV_HR_EMPMSF_CN_H = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MV_HR_EMPMSF_VN_H"
MV_HR_EMPMSF_VN_H = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "HR_DEPMSF_H"
HR_DEPMSF_H = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "HR_DEPMSF_CN_H"
HR_DEPMSF_CN_H = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "HR_DEPMSF_VN_H"
HR_DEPMSF_VN_H = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MTL_SYSTEM_ITEMS_B"
MTL_SYSTEM_ITEMS_B = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FND_COLUMNS"
FND_COLUMNS = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FND_LOOKUP_TYPES"
FND_LOOKUP_TYPES = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FND_LOOKUP_VALUES"
FND_LOOKUP_VALUES = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FND_TABLES"
FND_TABLES = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MTL_CATEGORIES_B"
MTL_CATEGORIES_B = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MTL_CATEGORY_SETS_B"
MTL_CATEGORY_SETS_B = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MTL_CUSTOMER_ITEMS"
MTL_CUSTOMER_ITEMS = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MTL_ITEM_CATALOG_GROUPS_B"
MTL_ITEM_CATALOG_GROUPS_B = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MTL_ITEM_CATEGORIES"
MTL_ITEM_CATEGORIES = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MTL_ITEM_STATUS_TL"
MTL_ITEM_STATUS_TL = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "PRJ_WORKTIMEDATA"
PRJ_WORKTIMEDATA = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "XXPLM_MODEL"
XXPLM_MODEL = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "XXPLM_PROJECT"
XXPLM_PROJECT = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "XXPLM_TFD"
XXPLM_TFD = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "Z_CDOCUMENT_CHECKING_RULE"
Z_CDOCUMENT_CHECKING_RULE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MV_XXPLM_MODEL_CHECKRULE_V"
MV_XXPLM_MODEL_CHECKRULE_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "XXPLM_EC_CHANGE_TYPE"
XXPLM_EC_CHANGE_TYPE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "NSP_REQ_HEADERS"
NSP_REQ_HEADERS = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "NSP_REQ_LINES"
NSP_REQ_LINES = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "EFLOW_PCS_HEADER_TW"
EFLOW_PCS_HEADER_TW = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "EFLOW_PCS_LINEEE_TW"
EFLOW_PCS_LINEEE_TW = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "EFLOW_PCS_LINEER_TW"
EFLOW_PCS_LINEER_TW = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "EFLOW_BTMS_EXPENSEPROJECT_TW"
EFLOW_BTMS_EXPENSEPROJECT_TW = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MV_PROJECT_ACTIVITY_V"
MV_PROJECT_ACTIVITY_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MV_XXPLM_CFDMETADATA_V"
MV_XXPLM_CFDMETADATA_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_DEPARTMENT_H"
SDM_DEPARTMENT_H = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_EMPLOYEE_H"
SDM_EMPLOYEE_H = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_PLM_CATEGORY"
SDM_PLM_CATEGORY = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_ITEM"
SDM_ITEM = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_ECN_REASON"
SDM_ECN_REASON = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_XXPLM_EC"
SDM_XXPLM_EC = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_ECN_CASE_AFTER_MP"
SDM_ECN_CASE_AFTER_MP = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_CDOC_COMPLETION_RATE"
SDM_CDOC_COMPLETION_RATE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_UPLOAD_CDOC_COUNT"
SDM_UPLOAD_CDOC_COUNT = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_TOTAL_CDOC_COUNT"
SDM_TOTAL_CDOC_COUNT = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_PROJECT_CODE"
SDM_PROJECT_CODE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_TOOLING_TOTAL_EXPENSE"
SDM_TOOLING_TOTAL_EXPENSE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_DMST_AND_INTL_TRAVEL_EXP"
SDM_DMST_AND_INTL_TRAVEL_EXP = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_RD_LABOR_HOURS_EXPENSE"
SDM_RD_LABOR_HOURS_EXPENSE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_TESTING_EXPENSE"
SDM_TESTING_EXPENSE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_CTF_EXPENSE"
SDM_CTF_EXPENSE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_EQT_EXPENSE"
SDM_EQT_EXPENSE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_EPR_MFG_SAMPLE_BUILD_EXP"
SDM_EPR_MFG_SAMPLE_BUILD_EXP = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_EPR_MFG_CONVERSION_COST"
SDM_EPR_MFG_CONVERSION_COST = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_CDOC_PLANNED_DEV_TIME"
SDM_CDOC_PLANNED_DEV_TIME = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_PROD_DEV_MLST_DELAY_RATE"
SDM_PROD_DEV_MLST_DELAY_RATE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_CDOC_DELAY_TIME"
SDM_CDOC_DELAY_TIME = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_PRODUCT_ACTUAL_EXPENSE"
SDM_PRODUCT_ACTUAL_EXPENSE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_PRODUCT_EXPENSE_BUDGET"
SDM_PRODUCT_EXPENSE_BUDGET = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_PROD_DEV_MLST_DELAY_RATE"
FCT_PROD_DEV_MLST_DELAY_RATE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_ECN_CASE_AFTER_MP"
FCT_ECN_CASE_AFTER_MP = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_EPR_MFG_CONVERSION_COST"
FCT_EPR_MFG_CONVERSION_COST = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_TOOLING_TOTAL_EXPENSE"
FCT_TOOLING_TOTAL_EXPENSE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_DMST_AND_INTL_TRAVEL_EXP"
FCT_DMST_AND_INTL_TRAVEL_EXP = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_TESTING_EXPENSE"
FCT_TESTING_EXPENSE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "DIM_ITEM"
DIM_ITEM = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "DIM_PLM_CATEGORY"
DIM_PLM_CATEGORY = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "DIM_ECN_REASON"
DIM_ECN_REASON = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "DIM_PROJECT_CODE"
DIM_PROJECT_CODE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )