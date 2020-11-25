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
my_taskid = "DIM_CONTINENT_V"
DIM_CONTINENT_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "DIM_ERPODP_TO_FODP_V"
DIM_ERPODP_TO_FODP_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "DIM_PLANT"
DIM_PLANT = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "DIM_FIG"
DIM_FIG = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "HR_OPERATING_UNITS_V"
HR_OPERATING_UNITS_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "IS_ELEMENT_DEF_T"
IS_ELEMENT_DEF_T = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "MFG_REVENUE_V"
MFG_REVENUE_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "POWERBI_SM_CON_DETAIL_V"
POWERBI_SM_CON_DETAIL_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SM_PURE_DETAIL_V"
SM_PURE_DETAIL_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SM_REVENUE_V"
SM_REVENUE_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "GL_DAILY_RATES_V"
GL_DAILY_RATES_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SCD_FODP"
SCD_FODP = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "IS_ELEMENT_ADJUST"
IS_ELEMENT_ADJUST = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "TB_DETAIL"
TB_DETAIL = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "IS_OPEX_FINAL_V"
IS_OPEX_FINAL_V = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FND_COLUMNS_H"
FND_COLUMNS_H = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ":END_DT_CHAR"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_LEGAL_ENTITY"
SDM_LEGAL_ENTITY = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_BASE_BUSINESS_UNIT"
SDM_BASE_BUSINESS_UNIT = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_BUSINESS_UNIT"
SDM_BUSINESS_UNIT = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_BASE_BUSINESS_GROUP"
SDM_BASE_BUSINESS_GROUP = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_BUSINESS_GROUP"
SDM_BUSINESS_GROUP = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_COUNTRY"
SDM_COUNTRY = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_MANUFACTURING_PLANT"
SDM_MANUFACTURING_PLANT = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_REVENUE_CATEGORY"
SDM_REVENUE_CATEGORY = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_CONVERSION_RATE"
SDM_CONVERSION_RATE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_BUDGET"
SDM_BUDGET = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_REALIZED_REVENUE"
SDM_REALIZED_REVENUE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_MANUFACTURING_REVENUE"
SDM_MANUFACTURING_REVENUE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_ADDED_VALUE_RATE"
SDM_ADDED_VALUE_RATE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_GROSS_MARGIN"
SDM_GROSS_MARGIN = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_PLANT_MFG_CONVERSION_COST"
SDM_PLANT_MFG_CONVERSION_COST = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "SDM_EMPLOYEE_H"
SDM_EMPLOYEE_H = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "DIM_REPORT_CURRENCY"
DIM_REPORT_CURRENCY = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_BUDGET_HIT_RATE"
FCT_BUDGET_HIT_RATE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_REALIZED_REVENUE"
FCT_REALIZED_REVENUE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_MANUFACTURING_REVENUE"
FCT_MANUFACTURING_REVENUE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_ADDED_VALUE_RATE"
FCT_ADDED_VALUE_RATE = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_GROSS_MARGIN"
FCT_GROSS_MARGIN = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )

# JOB_TYPE=ODS-MAIN
my_taskid = "FCT_PLANT_MFG_CONVERSION_COST"
FCT_PLANT_MFG_CONVERSION_COST = OracleOperatorWithTemplatedParams(
    task_id=my_taskid,
    parameters=({":END_DT_CHAR":"{{ ds_nodash }}"}),
    sql= "Begin SQLEXT." + my_taskid + "_SP("+  
        ",${END_DT_CHAR}"+
        "); End;"
    )
