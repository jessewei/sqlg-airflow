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
from airflow.operators.oracle_operator import OracleOperator

from airflow import models
from airflow.models import Variable

from acme.operators.dwh_operators import PostgresOperatorWithTemplatedParams


# DB_NAME = 'DWH'

my_taskid = "HR_DEGREEMSF"
HR_DEGREEMSF = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "HR_ETSMSF"
HR_ETSMSF = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "HR_JOBRANK"
HR_JOBRANK = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "HR_PEOMSF"
HR_PEOMSF = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "HR_PLACEMSF"
HR_PLACEMSF = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "HR_TYPMSF"
HR_TYPMSF = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "MV_HR_EMPMSF"
MV_HR_EMPMSF = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "MV_HR_EMPMSF_CN"
MV_HR_EMPMSF_CN = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "MV_HR_EMPMSF_VN"
MV_HR_EMPMSF_VN = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "HR_DEPMSF"
HR_DEPMSF = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "HR_DEPMSF_CN"
HR_DEPMSF_CN = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "HR_DEPMSF_VN"
HR_DEPMSF_VN = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "PEOMSF2"
PEOMSF2 = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "HR_BTYPMSF"
HR_BTYPMSF = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "HR_XXCONTRACT_NQJ"
HR_XXCONTRACT_NQJ = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_PERSONNEL_CATEGORY"
SDM_PERSONNEL_CATEGORY = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_SENIORITY_AT_WNC"
SDM_SENIORITY_AT_WNC = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_JOB_GRADE"
SDM_JOB_GRADE = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_JOB_FAMILY"
SDM_JOB_FAMILY = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_JOB_CATEGORY"
SDM_JOB_CATEGORY = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_WORK_PLACE"
SDM_WORK_PLACE = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_WORK_LOCATION"
SDM_WORK_LOCATION = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_CAUSE_OF_RESIGNING"
SDM_CAUSE_OF_RESIGNING = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_EDUCATION"
SDM_EDUCATION = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_DEPARTMENT"
SDM_DEPARTMENT = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_EMPLOYMENT_TYPE"
SDM_EMPLOYMENT_TYPE = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_EMPLOYEE"
SDM_EMPLOYEE = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_EMPLOYEE_H"
SDM_EMPLOYEE_H = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "SDM_HEADCOUNT_BUDGET"
SDM_HEADCOUNT_BUDGET = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')


my_taskid = "FCT_HEADCOUNT_FULFILL_RATE"
FCT_HEADCOUNT_FULFILL_RATE = OracleOperator(
    task_id=my_taskid,
    postgres_conn_id='postgres_dwh',
#    sql=DB_NAME + '/' + my_taskid + '/' + my_taskid + '.sql',
    sql=my_taskid + '/' + my_taskid + '.sql',
    parameters={"window_start_date": "{{ ds }}", "window_end_date": "{{ tomorrow_ds }}"},
    start_date=airflow.utils.dates.days_ago(1),
    pool='postgres_dwh')

