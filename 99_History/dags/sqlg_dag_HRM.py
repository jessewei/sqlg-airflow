﻿



# -*- coding: utf-8 -*-
# Author        : Jesse Wei
# LastUpdate    : 2020/11/04
# Impact        : DAG generated by SQLG
# Message       : Humanity towards others, we live by sharing. Fear can hold you prisoner, only hope can set you free.

# from __future__ import print_function
import logging
import airflow
from datetime import datetime, timedelta
from airflow.operators.sensors import ExternalTaskSensor
from airflow.operators.python_operator import PythonOperator
from airflow import models
from airflow.models import Variable
# import sqlg_jobs 
import sqlg_jobs_HRM


#from acme.operators.dwh_operators import PostgresOperatorWithTemplatedParams

def f_SYS_STS_STG():
    logging.info('Control flow: STAGE status ')

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),
    'provide_context': True
}

tmpl_search_path = Variable.get("sql_path")

my_taskid = 'SYS_STS_STG'
D_STG_INIT = airflow.DAG(
    'D_STG_INIT',
    schedule_interval=timedelta(1),
    default_args=args,
    template_searchpath=tmpl_search_path,    
    max_active_runs=1)

SYS_STS_STG = PythonOperator(task_id=my_taskid,
                    python_callable=f_SYS_STS_STG,
                    provide_context=False,
                    dag=D_STG_INIT)

my_taskid = 'D_STG_INITxSYS_STS_STG'                    
D_STG_INITxSYS_STS_STG = ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id='D_STG_INIT',
    external_task_id='SYS_STS_STG',
    execution_delta=None,  # Same day as today
    )

# Flow dag    
# DB_NAME = 'DWH'    
D_ODS_HRM = airflow.DAG(    "D_ODS_HRM",
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1)

### D_STG_INITxSYS_STS_STGxD_ODS_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_HRM"
D_STG_INITxSYS_STS_STGxD_ODS_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_SDM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_HRM"
D_STG_INITxSYS_STS_STGxD_SDM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxM_SDM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxM_SDM_HRM"
D_STG_INITxSYS_STS_STGxM_SDM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### M_SDM_HRMxSDM_EMPLOYEExM_SDM_HRM
### D_STG_INITxSYS_STS_STGxD_DM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_HRM"
D_STG_INITxSYS_STS_STGxD_DM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
sqlg_jobs_HRM.HR_DEGREEMSF.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_DEGREEMSF)

sqlg_jobs_HRM.HR_ETSMSF.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_ETSMSF)

sqlg_jobs_HRM.HR_JOBRANK.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_JOBRANK)

sqlg_jobs_HRM.HR_PEOMSF.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_PEOMSF)

sqlg_jobs_HRM.HR_PLACEMSF.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_PLACEMSF)

sqlg_jobs_HRM.HR_TYPMSF.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_TYPMSF)

sqlg_jobs_HRM.MV_HR_EMPMSF.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.MV_HR_EMPMSF)

sqlg_jobs_HRM.MV_HR_EMPMSF_CN.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.MV_HR_EMPMSF_CN)

sqlg_jobs_HRM.MV_HR_EMPMSF_VN.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.MV_HR_EMPMSF_VN)

sqlg_jobs_HRM.HR_DEPMSF.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_DEPMSF)

sqlg_jobs_HRM.HR_DEPMSF_CN.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_DEPMSF_CN)

sqlg_jobs_HRM.HR_DEPMSF_VN.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_DEPMSF_VN)

sqlg_jobs_HRM.PEOMSF2.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.PEOMSF2)

sqlg_jobs_HRM.HR_BTYPMSF.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_BTYPMSF)

sqlg_jobs_HRM.HR_XXCONTRACT_NQJ.dag=D_ODS_HRM
D_STG_INITxSYS_STS_STGxD_ODS_HRM.set_downstream(sqlg_jobs_HRM.HR_XXCONTRACT_NQJ)

D_SDM_HRM = airflow.DAG(    "D_SDM_HRM",
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1)

### D_STG_INITxSYS_STS_STGxD_ODS_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_HRM"
D_STG_INITxSYS_STS_STGxD_ODS_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_SDM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_HRM"
D_STG_INITxSYS_STS_STGxD_SDM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxM_SDM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxM_SDM_HRM"
D_STG_INITxSYS_STS_STGxM_SDM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### M_SDM_HRMxSDM_EMPLOYEExM_SDM_HRM
### D_STG_INITxSYS_STS_STGxD_DM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_HRM"
D_STG_INITxSYS_STS_STGxD_DM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
sqlg_jobs_HRM.SDM_PERSONNEL_CATEGORY.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_PERSONNEL_CATEGORY)

sqlg_jobs_HRM.SDM_SENIORITY_AT_WNC.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_SENIORITY_AT_WNC)

sqlg_jobs_HRM.SDM_JOB_GRADE.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_JOB_GRADE)

sqlg_jobs_HRM.SDM_JOB_FAMILY.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_JOB_FAMILY)

sqlg_jobs_HRM.SDM_JOB_CATEGORY.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_JOB_CATEGORY)

sqlg_jobs_HRM.SDM_WORK_PLACE.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_WORK_PLACE)

sqlg_jobs_HRM.SDM_WORK_LOCATION.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_WORK_LOCATION)

sqlg_jobs_HRM.SDM_CAUSE_OF_RESIGNING.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_CAUSE_OF_RESIGNING)

sqlg_jobs_HRM.SDM_EDUCATION.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_EDUCATION)

sqlg_jobs_HRM.SDM_DEPARTMENT.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_DEPARTMENT)

sqlg_jobs_HRM.SDM_EMPLOYMENT_TYPE.dag=D_SDM_HRM
D_STG_INITxSYS_STS_STGxD_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_EMPLOYMENT_TYPE)

M_SDM_HRM = airflow.DAG(    "M_SDM_HRM",
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1)

### D_STG_INITxSYS_STS_STGxD_ODS_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_HRM"
D_STG_INITxSYS_STS_STGxD_ODS_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_SDM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_HRM"
D_STG_INITxSYS_STS_STGxD_SDM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxM_SDM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxM_SDM_HRM"
D_STG_INITxSYS_STS_STGxM_SDM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### M_SDM_HRMxSDM_EMPLOYEExM_SDM_HRM
### D_STG_INITxSYS_STS_STGxD_DM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_HRM"
D_STG_INITxSYS_STS_STGxD_DM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
sqlg_jobs_HRM.SDM_EMPLOYEE.dag=M_SDM_HRM
D_STG_INITxSYS_STS_STGxM_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_EMPLOYEE)

sqlg_jobs_HRM.SDM_EMPLOYEE_H.dag=M_SDM_HRM
sqlg_jobs_HRM.SDM_EMPLOYEE.set_downstream(sqlg_jobs_HRM.SDM_EMPLOYEE_H)

sqlg_jobs_HRM.SDM_HEADCOUNT_BUDGET.dag=M_SDM_HRM
D_STG_INITxSYS_STS_STGxM_SDM_HRM.set_downstream(sqlg_jobs_HRM.SDM_HEADCOUNT_BUDGET)

D_DM_HRM = airflow.DAG(    "D_DM_HRM",
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1)

### D_STG_INITxSYS_STS_STGxD_ODS_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_HRM"
D_STG_INITxSYS_STS_STGxD_ODS_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_SDM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_HRM"
D_STG_INITxSYS_STS_STGxD_SDM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxM_SDM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxM_SDM_HRM"
D_STG_INITxSYS_STS_STGxM_SDM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### M_SDM_HRMxSDM_EMPLOYEExM_SDM_HRM
### D_STG_INITxSYS_STS_STGxD_DM_HRM

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_HRM"
D_STG_INITxSYS_STS_STGxD_DM_HRM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
sqlg_jobs_HRM.FCT_HEADCOUNT_FULFILL_RATE.dag=D_DM_HRM
D_STG_INITxSYS_STS_STGxD_DM_HRM.set_downstream(sqlg_jobs_HRM.FCT_HEADCOUNT_FULFILL_RATE)

