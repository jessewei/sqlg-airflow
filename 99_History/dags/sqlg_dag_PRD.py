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
import sqlg_jobs_PRD


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
D_ODS_PRD = airflow.DAG(    "D_ODS_PRD",
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1)

### D_STG_INITxSYS_STS_STGxD_ODS_PRD

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_PRD"
D_STG_INITxSYS_STS_STGxD_ODS_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxXXPLM_MODELxD_SDM_PRD

my_taskid = "D_ODS_PRDxXXPLM_MODELxD_SDM_PRD"
D_ODS_PRDxXXPLM_MODELxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="XXPLM_MODEL",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxMTL_SYSTEM_ITEMS_BxD_SDM_PRD

my_taskid = "D_ODS_PRDxMTL_SYSTEM_ITEMS_BxD_SDM_PRD"
D_ODS_PRDxMTL_SYSTEM_ITEMS_BxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MTL_SYSTEM_ITEMS_B",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxXXPLM_EC_CHANGE_TYPExD_SDM_PRD

my_taskid = "D_ODS_PRDxXXPLM_EC_CHANGE_TYPExD_SDM_PRD"
D_ODS_PRDxXXPLM_EC_CHANGE_TYPExD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="XXPLM_EC_CHANGE_TYPE",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxMV_XXPLM_ECxD_SDM_PRD

my_taskid = "D_ODS_PRDxMV_XXPLM_ECxD_SDM_PRD"
D_ODS_PRDxMV_XXPLM_ECxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MV_XXPLM_EC",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_XXPLM_ECxD_SDM_PRD
### D_STG_INITxSYS_STS_STGxD_SDM_PRD

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_PRD"
D_STG_INITxSYS_STS_STGxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_UPLOAD_CDOC_COUNTxD_SDM_PRD
### D_SDM_PRDxSDM_TOTAL_CDOC_COUNTxD_SDM_PRD
### D_ODS_PRDxZ_CDOCUMENT_CHECKING_RULExD_SDM_PRD

my_taskid = "D_ODS_PRDxZ_CDOCUMENT_CHECKING_RULExD_SDM_PRD"
D_ODS_PRDxZ_CDOCUMENT_CHECKING_RULExD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="Z_CDOCUMENT_CHECKING_RULE",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxMV_XXPLM_CFDMETADATAxD_SDM_PRD

my_taskid = "D_ODS_PRDxMV_XXPLM_CFDMETADATAxD_SDM_PRD"
D_ODS_PRDxMV_XXPLM_CFDMETADATAxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MV_XXPLM_CFDMETADATA",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxXXPLM_PROJECTxD_SDM_PRD

my_taskid = "D_ODS_PRDxXXPLM_PROJECTxD_SDM_PRD"
D_ODS_PRDxXXPLM_PROJECTxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="XXPLM_PROJECT",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD

my_taskid = "D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD"
D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="NSP_REQ_HEADERS",
    execution_delta=None,  # Same day as today
)
### D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD

my_taskid = "D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD"
D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_FIN",
    external_task_id="SDM_MANUFACTURING_PLANT",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_PROJECT_CODExD_SDM_PRD
### D_ODS_PRDxPCS_HEADERxD_SDM_PRD

my_taskid = "D_ODS_PRDxPCS_HEADERxD_SDM_PRD"
D_ODS_PRDxPCS_HEADERxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="PCS_HEADER",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxPCS_LINEEExD_SDM_PRD

my_taskid = "D_ODS_PRDxPCS_LINEEExD_SDM_PRD"
D_ODS_PRDxPCS_LINEEExD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="PCS_LINEEE",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxBTMS_EXPENSEPROJECTxD_SDM_PRD

my_taskid = "D_ODS_PRDxBTMS_EXPENSEPROJECTxD_SDM_PRD"
D_ODS_PRDxBTMS_EXPENSEPROJECTxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="BTMS_EXPENSEPROJECT",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CTF_EXPENSExD_SDM_PRD
### D_SDM_PRDxSDM_EQT_EXPENSExD_SDM_PRD
### D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD

my_taskid = "D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD"
D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MV_PROJECT_ACTIVITY",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_SDM_PRD
### D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_SDM_PRD
### D_SDM_PRDxSDM_PROD_DEV_MLST_DELAY_RATExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_PROD_DEV_MLST_DELAY_RATExD_DM_PRD"
D_SDM_PRDxSDM_PROD_DEV_MLST_DELAY_RATExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_PROD_DEV_MLST_DELAY_RATE",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_DM_PRD"
D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_CDOC_PLANNED_DEV_TIME",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_DM_PRD"
D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_CDOC_DELAY_TIME",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_ECN_CASE_AFTER_MPxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_ECN_CASE_AFTER_MPxD_DM_PRD"
D_SDM_PRDxSDM_ECN_CASE_AFTER_MPxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_ECN_CASE_AFTER_MP",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_DM_PRD

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_PRD"
D_STG_INITxSYS_STS_STGxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_TESTING_EXPENSExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_TESTING_EXPENSExD_DM_PRD"
D_SDM_PRDxSDM_TESTING_EXPENSExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_TESTING_EXPENSE",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_EQT_EXPENSExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_EQT_EXPENSExD_DM_PRD"
D_SDM_PRDxSDM_EQT_EXPENSExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_EQT_EXPENSE",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_EPR_MFG_SAMPLE_BUILD_EXPxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_EPR_MFG_SAMPLE_BUILD_EXPxD_DM_PRD"
D_SDM_PRDxSDM_EPR_MFG_SAMPLE_BUILD_EXPxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_EPR_MFG_SAMPLE_BUILD_EXP",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_ITEMxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_ITEMxD_DM_PRD"
D_SDM_PRDxSDM_ITEMxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_ITEM",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_PLM_CATEGORYxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_PLM_CATEGORYxD_DM_PRD"
D_SDM_PRDxSDM_PLM_CATEGORYxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_PLM_CATEGORY",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_ECN_REASONxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_ECN_REASONxD_DM_PRD"
D_SDM_PRDxSDM_ECN_REASONxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_ECN_REASON",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_PROJECT_CODExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_PROJECT_CODExD_DM_PRD"
D_SDM_PRDxSDM_PROJECT_CODExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_PROJECT_CODE",
    execution_delta=None,  # Same day as today
)
sqlg_jobs_PRD.MTL_SYSTEM_ITEMS_B.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MTL_SYSTEM_ITEMS_B)

sqlg_jobs_PRD.FND_COLUMNS.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.FND_COLUMNS)

sqlg_jobs_PRD.FND_LOOKUP_TYPES.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.FND_LOOKUP_TYPES)

sqlg_jobs_PRD.FND_LOOKUP_VALUES.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.FND_LOOKUP_VALUES)

sqlg_jobs_PRD.FND_TABLES.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.FND_TABLES)

sqlg_jobs_PRD.MTL_CATEGORIES_B.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MTL_CATEGORIES_B)

sqlg_jobs_PRD.MTL_CATEGORY_SETS_B.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MTL_CATEGORY_SETS_B)

sqlg_jobs_PRD.MTL_CUSTOMER_ITEMS.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MTL_CUSTOMER_ITEMS)

sqlg_jobs_PRD.MTL_ITEM_CATALOG_GROUPS_B.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MTL_ITEM_CATALOG_GROUPS_B)

sqlg_jobs_PRD.MTL_ITEM_CATEGORIES.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MTL_ITEM_CATEGORIES)

sqlg_jobs_PRD.MTL_ITEM_STATUS_TL.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MTL_ITEM_STATUS_TL)

sqlg_jobs_PRD.MV_PROJECT_ACTIVITY.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MV_PROJECT_ACTIVITY)

sqlg_jobs_PRD.MV_XXPLM_CFDMETADATA.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MV_XXPLM_CFDMETADATA)

sqlg_jobs_PRD.MV_XXPLM_EC.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MV_XXPLM_EC)

sqlg_jobs_PRD.PRJ_WORKTIMEDATA.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.PRJ_WORKTIMEDATA)

sqlg_jobs_PRD.XXPLM_MODEL.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.XXPLM_MODEL)

sqlg_jobs_PRD.XXPLM_PROJECT.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.XXPLM_PROJECT)

sqlg_jobs_PRD.XXPLM_TFD.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.XXPLM_TFD)

sqlg_jobs_PRD.Z_CDOCUMENT_CHECKING_RULE.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.Z_CDOCUMENT_CHECKING_RULE)

sqlg_jobs_PRD.MV_XXPLM_MODEL_CHECKRULE_V.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.MV_XXPLM_MODEL_CHECKRULE_V)

sqlg_jobs_PRD.XXPLM_EC_CHANGE_TYPE.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.XXPLM_EC_CHANGE_TYPE)

sqlg_jobs_PRD.NSP_REQ_HEADERS.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.NSP_REQ_HEADERS)

sqlg_jobs_PRD.NSP_REQ_LINES.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.NSP_REQ_LINES)

sqlg_jobs_PRD.PCS_HEADER.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.PCS_HEADER)

sqlg_jobs_PRD.PCS_LINEEE.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.PCS_LINEEE)

sqlg_jobs_PRD.BTMS_EXPENSEPROJECT.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_PRD.BTMS_EXPENSEPROJECT)

D_SDM_PRD = airflow.DAG(    "D_SDM_PRD",
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1)

### D_STG_INITxSYS_STS_STGxD_ODS_PRD

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_PRD"
D_STG_INITxSYS_STS_STGxD_ODS_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxXXPLM_MODELxD_SDM_PRD

my_taskid = "D_ODS_PRDxXXPLM_MODELxD_SDM_PRD"
D_ODS_PRDxXXPLM_MODELxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="XXPLM_MODEL",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxMTL_SYSTEM_ITEMS_BxD_SDM_PRD

my_taskid = "D_ODS_PRDxMTL_SYSTEM_ITEMS_BxD_SDM_PRD"
D_ODS_PRDxMTL_SYSTEM_ITEMS_BxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MTL_SYSTEM_ITEMS_B",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxXXPLM_EC_CHANGE_TYPExD_SDM_PRD

my_taskid = "D_ODS_PRDxXXPLM_EC_CHANGE_TYPExD_SDM_PRD"
D_ODS_PRDxXXPLM_EC_CHANGE_TYPExD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="XXPLM_EC_CHANGE_TYPE",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxMV_XXPLM_ECxD_SDM_PRD

my_taskid = "D_ODS_PRDxMV_XXPLM_ECxD_SDM_PRD"
D_ODS_PRDxMV_XXPLM_ECxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MV_XXPLM_EC",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_XXPLM_ECxD_SDM_PRD
### D_STG_INITxSYS_STS_STGxD_SDM_PRD

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_PRD"
D_STG_INITxSYS_STS_STGxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_UPLOAD_CDOC_COUNTxD_SDM_PRD
### D_SDM_PRDxSDM_TOTAL_CDOC_COUNTxD_SDM_PRD
### D_ODS_PRDxZ_CDOCUMENT_CHECKING_RULExD_SDM_PRD

my_taskid = "D_ODS_PRDxZ_CDOCUMENT_CHECKING_RULExD_SDM_PRD"
D_ODS_PRDxZ_CDOCUMENT_CHECKING_RULExD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="Z_CDOCUMENT_CHECKING_RULE",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxMV_XXPLM_CFDMETADATAxD_SDM_PRD

my_taskid = "D_ODS_PRDxMV_XXPLM_CFDMETADATAxD_SDM_PRD"
D_ODS_PRDxMV_XXPLM_CFDMETADATAxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MV_XXPLM_CFDMETADATA",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxXXPLM_PROJECTxD_SDM_PRD

my_taskid = "D_ODS_PRDxXXPLM_PROJECTxD_SDM_PRD"
D_ODS_PRDxXXPLM_PROJECTxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="XXPLM_PROJECT",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD

my_taskid = "D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD"
D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="NSP_REQ_HEADERS",
    execution_delta=None,  # Same day as today
)
### D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD

my_taskid = "D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD"
D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_FIN",
    external_task_id="SDM_MANUFACTURING_PLANT",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_PROJECT_CODExD_SDM_PRD
### D_ODS_PRDxPCS_HEADERxD_SDM_PRD

my_taskid = "D_ODS_PRDxPCS_HEADERxD_SDM_PRD"
D_ODS_PRDxPCS_HEADERxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="PCS_HEADER",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxPCS_LINEEExD_SDM_PRD

my_taskid = "D_ODS_PRDxPCS_LINEEExD_SDM_PRD"
D_ODS_PRDxPCS_LINEEExD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="PCS_LINEEE",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxBTMS_EXPENSEPROJECTxD_SDM_PRD

my_taskid = "D_ODS_PRDxBTMS_EXPENSEPROJECTxD_SDM_PRD"
D_ODS_PRDxBTMS_EXPENSEPROJECTxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="BTMS_EXPENSEPROJECT",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CTF_EXPENSExD_SDM_PRD
### D_SDM_PRDxSDM_EQT_EXPENSExD_SDM_PRD
### D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD

my_taskid = "D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD"
D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MV_PROJECT_ACTIVITY",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_SDM_PRD
### D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_SDM_PRD
### D_SDM_PRDxSDM_PROD_DEV_MLST_DELAY_RATExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_PROD_DEV_MLST_DELAY_RATExD_DM_PRD"
D_SDM_PRDxSDM_PROD_DEV_MLST_DELAY_RATExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_PROD_DEV_MLST_DELAY_RATE",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_DM_PRD"
D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_CDOC_PLANNED_DEV_TIME",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_DM_PRD"
D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_CDOC_DELAY_TIME",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_ECN_CASE_AFTER_MPxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_ECN_CASE_AFTER_MPxD_DM_PRD"
D_SDM_PRDxSDM_ECN_CASE_AFTER_MPxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_ECN_CASE_AFTER_MP",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_DM_PRD

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_PRD"
D_STG_INITxSYS_STS_STGxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_TESTING_EXPENSExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_TESTING_EXPENSExD_DM_PRD"
D_SDM_PRDxSDM_TESTING_EXPENSExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_TESTING_EXPENSE",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_EQT_EXPENSExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_EQT_EXPENSExD_DM_PRD"
D_SDM_PRDxSDM_EQT_EXPENSExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_EQT_EXPENSE",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_EPR_MFG_SAMPLE_BUILD_EXPxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_EPR_MFG_SAMPLE_BUILD_EXPxD_DM_PRD"
D_SDM_PRDxSDM_EPR_MFG_SAMPLE_BUILD_EXPxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_EPR_MFG_SAMPLE_BUILD_EXP",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_ITEMxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_ITEMxD_DM_PRD"
D_SDM_PRDxSDM_ITEMxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_ITEM",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_PLM_CATEGORYxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_PLM_CATEGORYxD_DM_PRD"
D_SDM_PRDxSDM_PLM_CATEGORYxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_PLM_CATEGORY",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_ECN_REASONxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_ECN_REASONxD_DM_PRD"
D_SDM_PRDxSDM_ECN_REASONxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_ECN_REASON",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_PROJECT_CODExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_PROJECT_CODExD_DM_PRD"
D_SDM_PRDxSDM_PROJECT_CODExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_PROJECT_CODE",
    execution_delta=None,  # Same day as today
)
sqlg_jobs_PRD.SDM_TEMPLATE_PRD.dag=D_SDM_PRD
D_ODS_PRDxXXPLM_MODELxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_TEMPLATE_PRD)

sqlg_jobs_PRD.SDM_PLM_CATEGORY.dag=D_SDM_PRD
D_ODS_PRDxXXPLM_MODELxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_PLM_CATEGORY)

sqlg_jobs_PRD.SDM_ITEM.dag=D_SDM_PRD
D_ODS_PRDxMTL_SYSTEM_ITEMS_BxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_ITEM)

sqlg_jobs_PRD.SDM_ECN_REASON.dag=D_SDM_PRD
D_ODS_PRDxXXPLM_EC_CHANGE_TYPExD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_ECN_REASON)

sqlg_jobs_PRD.SDM_XXPLM_EC.dag=D_SDM_PRD
D_ODS_PRDxMV_XXPLM_ECxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_XXPLM_EC)

sqlg_jobs_PRD.SDM_ECN_CASE_AFTER_MP.dag=D_SDM_PRD
sqlg_jobs_PRD.SDM_XXPLM_EC.set_downstream(sqlg_jobs_PRD.SDM_ECN_CASE_AFTER_MP)
D_ODS_PRDxXXPLM_MODELxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_ECN_CASE_AFTER_MP)
D_STG_INITxSYS_STS_STGxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_ECN_CASE_AFTER_MP)

sqlg_jobs_PRD.SDM_CDOC_COMPLETION_RATE.dag=D_SDM_PRD
sqlg_jobs_PRD.SDM_UPLOAD_CDOC_COUNT.set_downstream(sqlg_jobs_PRD.SDM_CDOC_COMPLETION_RATE)
sqlg_jobs_PRD.SDM_TOTAL_CDOC_COUNT.set_downstream(sqlg_jobs_PRD.SDM_CDOC_COMPLETION_RATE)

sqlg_jobs_PRD.SDM_UPLOAD_CDOC_COUNT.dag=D_SDM_PRD
D_ODS_PRDxZ_CDOCUMENT_CHECKING_RULExD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_UPLOAD_CDOC_COUNT)
D_ODS_PRDxMV_XXPLM_CFDMETADATAxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_UPLOAD_CDOC_COUNT)

sqlg_jobs_PRD.SDM_TOTAL_CDOC_COUNT.dag=D_SDM_PRD
sqlg_jobs_PRD.SDM_UPLOAD_CDOC_COUNT.set_downstream(sqlg_jobs_PRD.SDM_TOTAL_CDOC_COUNT)

sqlg_jobs_PRD.SDM_PROJECT_CODE.dag=D_SDM_PRD
D_ODS_PRDxXXPLM_PROJECTxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_PROJECT_CODE)

sqlg_jobs_PRD.SDM_TOOLING_TOTAL_EXPENSE.dag=D_SDM_PRD
D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_TOOLING_TOTAL_EXPENSE)
D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_TOOLING_TOTAL_EXPENSE)
sqlg_jobs_PRD.SDM_PROJECT_CODE.set_downstream(sqlg_jobs_PRD.SDM_TOOLING_TOTAL_EXPENSE)

sqlg_jobs_PRD.SDM_DMST_AND_INTL_TRAVEL_EXP.dag=D_SDM_PRD
D_ODS_PRDxPCS_HEADERxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_DMST_AND_INTL_TRAVEL_EXP)
D_ODS_PRDxPCS_LINEEExD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_DMST_AND_INTL_TRAVEL_EXP)
D_ODS_PRDxBTMS_EXPENSEPROJECTxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_DMST_AND_INTL_TRAVEL_EXP)

sqlg_jobs_PRD.SDM_TESTING_EXPENSE.dag=D_SDM_PRD
sqlg_jobs_PRD.SDM_CTF_EXPENSE.set_downstream(sqlg_jobs_PRD.SDM_TESTING_EXPENSE)
sqlg_jobs_PRD.SDM_EQT_EXPENSE.set_downstream(sqlg_jobs_PRD.SDM_TESTING_EXPENSE)

sqlg_jobs_PRD.SDM_CTF_EXPENSE.dag=D_SDM_PRD
D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_CTF_EXPENSE)
D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_CTF_EXPENSE)
sqlg_jobs_PRD.SDM_PROJECT_CODE.set_downstream(sqlg_jobs_PRD.SDM_CTF_EXPENSE)

sqlg_jobs_PRD.SDM_EQT_EXPENSE.dag=D_SDM_PRD
D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_EQT_EXPENSE)
D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_EQT_EXPENSE)
sqlg_jobs_PRD.SDM_PROJECT_CODE.set_downstream(sqlg_jobs_PRD.SDM_EQT_EXPENSE)

sqlg_jobs_PRD.SDM_EPR_MFG_SAMPLE_BUILD_EXP.dag=D_SDM_PRD
D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_EPR_MFG_SAMPLE_BUILD_EXP)
D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_EPR_MFG_SAMPLE_BUILD_EXP)
sqlg_jobs_PRD.SDM_PROJECT_CODE.set_downstream(sqlg_jobs_PRD.SDM_EPR_MFG_SAMPLE_BUILD_EXP)

sqlg_jobs_PRD.SDM_CDOC_PLANNED_DEV_TIME.dag=D_SDM_PRD
D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_CDOC_PLANNED_DEV_TIME)
D_ODS_PRDxXXPLM_MODELxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_CDOC_PLANNED_DEV_TIME)

sqlg_jobs_PRD.SDM_PROD_DEV_MLST_DELAY_RATE.dag=D_SDM_PRD
sqlg_jobs_PRD.SDM_CDOC_PLANNED_DEV_TIME.set_downstream(sqlg_jobs_PRD.SDM_PROD_DEV_MLST_DELAY_RATE)
sqlg_jobs_PRD.SDM_CDOC_DELAY_TIME.set_downstream(sqlg_jobs_PRD.SDM_PROD_DEV_MLST_DELAY_RATE)

sqlg_jobs_PRD.SDM_CDOC_DELAY_TIME.dag=D_SDM_PRD
D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_CDOC_DELAY_TIME)
D_ODS_PRDxXXPLM_MODELxD_SDM_PRD.set_downstream(sqlg_jobs_PRD.SDM_CDOC_DELAY_TIME)

D_DM_PRD = airflow.DAG(    "D_DM_PRD",
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1)

### D_STG_INITxSYS_STS_STGxD_ODS_PRD

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_PRD"
D_STG_INITxSYS_STS_STGxD_ODS_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxXXPLM_MODELxD_SDM_PRD

my_taskid = "D_ODS_PRDxXXPLM_MODELxD_SDM_PRD"
D_ODS_PRDxXXPLM_MODELxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="XXPLM_MODEL",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxMTL_SYSTEM_ITEMS_BxD_SDM_PRD

my_taskid = "D_ODS_PRDxMTL_SYSTEM_ITEMS_BxD_SDM_PRD"
D_ODS_PRDxMTL_SYSTEM_ITEMS_BxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MTL_SYSTEM_ITEMS_B",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxXXPLM_EC_CHANGE_TYPExD_SDM_PRD

my_taskid = "D_ODS_PRDxXXPLM_EC_CHANGE_TYPExD_SDM_PRD"
D_ODS_PRDxXXPLM_EC_CHANGE_TYPExD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="XXPLM_EC_CHANGE_TYPE",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxMV_XXPLM_ECxD_SDM_PRD

my_taskid = "D_ODS_PRDxMV_XXPLM_ECxD_SDM_PRD"
D_ODS_PRDxMV_XXPLM_ECxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MV_XXPLM_EC",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_XXPLM_ECxD_SDM_PRD
### D_STG_INITxSYS_STS_STGxD_SDM_PRD

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_PRD"
D_STG_INITxSYS_STS_STGxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_UPLOAD_CDOC_COUNTxD_SDM_PRD
### D_SDM_PRDxSDM_TOTAL_CDOC_COUNTxD_SDM_PRD
### D_ODS_PRDxZ_CDOCUMENT_CHECKING_RULExD_SDM_PRD

my_taskid = "D_ODS_PRDxZ_CDOCUMENT_CHECKING_RULExD_SDM_PRD"
D_ODS_PRDxZ_CDOCUMENT_CHECKING_RULExD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="Z_CDOCUMENT_CHECKING_RULE",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxMV_XXPLM_CFDMETADATAxD_SDM_PRD

my_taskid = "D_ODS_PRDxMV_XXPLM_CFDMETADATAxD_SDM_PRD"
D_ODS_PRDxMV_XXPLM_CFDMETADATAxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MV_XXPLM_CFDMETADATA",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxXXPLM_PROJECTxD_SDM_PRD

my_taskid = "D_ODS_PRDxXXPLM_PROJECTxD_SDM_PRD"
D_ODS_PRDxXXPLM_PROJECTxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="XXPLM_PROJECT",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD

my_taskid = "D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD"
D_ODS_PRDxNSP_REQ_HEADERSxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="NSP_REQ_HEADERS",
    execution_delta=None,  # Same day as today
)
### D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD

my_taskid = "D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD"
D_SDM_FINxSDM_MANUFACTURING_PLANTxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_FIN",
    external_task_id="SDM_MANUFACTURING_PLANT",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_PROJECT_CODExD_SDM_PRD
### D_ODS_PRDxPCS_HEADERxD_SDM_PRD

my_taskid = "D_ODS_PRDxPCS_HEADERxD_SDM_PRD"
D_ODS_PRDxPCS_HEADERxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="PCS_HEADER",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxPCS_LINEEExD_SDM_PRD

my_taskid = "D_ODS_PRDxPCS_LINEEExD_SDM_PRD"
D_ODS_PRDxPCS_LINEEExD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="PCS_LINEEE",
    execution_delta=None,  # Same day as today
)
### D_ODS_PRDxBTMS_EXPENSEPROJECTxD_SDM_PRD

my_taskid = "D_ODS_PRDxBTMS_EXPENSEPROJECTxD_SDM_PRD"
D_ODS_PRDxBTMS_EXPENSEPROJECTxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="BTMS_EXPENSEPROJECT",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CTF_EXPENSExD_SDM_PRD
### D_SDM_PRDxSDM_EQT_EXPENSExD_SDM_PRD
### D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD

my_taskid = "D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD"
D_ODS_PRDxMV_PROJECT_ACTIVITYxD_SDM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_ODS_PRD",
    external_task_id="MV_PROJECT_ACTIVITY",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_SDM_PRD
### D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_SDM_PRD
### D_SDM_PRDxSDM_PROD_DEV_MLST_DELAY_RATExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_PROD_DEV_MLST_DELAY_RATExD_DM_PRD"
D_SDM_PRDxSDM_PROD_DEV_MLST_DELAY_RATExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_PROD_DEV_MLST_DELAY_RATE",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_DM_PRD"
D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_CDOC_PLANNED_DEV_TIME",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_DM_PRD"
D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_CDOC_DELAY_TIME",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_ECN_CASE_AFTER_MPxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_ECN_CASE_AFTER_MPxD_DM_PRD"
D_SDM_PRDxSDM_ECN_CASE_AFTER_MPxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_ECN_CASE_AFTER_MP",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_DM_PRD

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_PRD"
D_STG_INITxSYS_STS_STGxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_TESTING_EXPENSExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_TESTING_EXPENSExD_DM_PRD"
D_SDM_PRDxSDM_TESTING_EXPENSExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_TESTING_EXPENSE",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_EQT_EXPENSExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_EQT_EXPENSExD_DM_PRD"
D_SDM_PRDxSDM_EQT_EXPENSExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_EQT_EXPENSE",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_EPR_MFG_SAMPLE_BUILD_EXPxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_EPR_MFG_SAMPLE_BUILD_EXPxD_DM_PRD"
D_SDM_PRDxSDM_EPR_MFG_SAMPLE_BUILD_EXPxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_EPR_MFG_SAMPLE_BUILD_EXP",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_ITEMxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_ITEMxD_DM_PRD"
D_SDM_PRDxSDM_ITEMxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_ITEM",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_PLM_CATEGORYxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_PLM_CATEGORYxD_DM_PRD"
D_SDM_PRDxSDM_PLM_CATEGORYxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_PLM_CATEGORY",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_ECN_REASONxD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_ECN_REASONxD_DM_PRD"
D_SDM_PRDxSDM_ECN_REASONxD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_ECN_REASON",
    execution_delta=None,  # Same day as today
)
### D_SDM_PRDxSDM_PROJECT_CODExD_DM_PRD

my_taskid = "D_SDM_PRDxSDM_PROJECT_CODExD_DM_PRD"
D_SDM_PRDxSDM_PROJECT_CODExD_DM_PRD= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_SDM_PRD",
    external_task_id="SDM_PROJECT_CODE",
    execution_delta=None,  # Same day as today
)
sqlg_jobs_PRD.FCT_PROD_DEV_MLST_DELAY_RATE.dag=D_DM_PRD
D_SDM_PRDxSDM_PROD_DEV_MLST_DELAY_RATExD_DM_PRD.set_downstream(sqlg_jobs_PRD.FCT_PROD_DEV_MLST_DELAY_RATE)
D_SDM_PRDxSDM_CDOC_PLANNED_DEV_TIMExD_DM_PRD.set_downstream(sqlg_jobs_PRD.FCT_PROD_DEV_MLST_DELAY_RATE)
D_SDM_PRDxSDM_CDOC_DELAY_TIMExD_DM_PRD.set_downstream(sqlg_jobs_PRD.FCT_PROD_DEV_MLST_DELAY_RATE)

sqlg_jobs_PRD.FCT_ECN_CASE_AFTER_MP.dag=D_DM_PRD
D_SDM_PRDxSDM_ECN_CASE_AFTER_MPxD_DM_PRD.set_downstream(sqlg_jobs_PRD.FCT_ECN_CASE_AFTER_MP)

sqlg_jobs_PRD.FCT_TOOLING_TOTAL_EXPENSE.dag=D_DM_PRD
D_STG_INITxSYS_STS_STGxD_DM_PRD.set_downstream(sqlg_jobs_PRD.FCT_TOOLING_TOTAL_EXPENSE)

sqlg_jobs_PRD.FCT_TESTING_EXPENSE.dag=D_DM_PRD
D_SDM_PRDxSDM_TESTING_EXPENSExD_DM_PRD.set_downstream(sqlg_jobs_PRD.FCT_TESTING_EXPENSE)
D_STG_INITxSYS_STS_STGxD_DM_PRD.set_downstream(sqlg_jobs_PRD.FCT_TESTING_EXPENSE)
D_SDM_PRDxSDM_EQT_EXPENSExD_DM_PRD.set_downstream(sqlg_jobs_PRD.FCT_TESTING_EXPENSE)
D_SDM_PRDxSDM_EPR_MFG_SAMPLE_BUILD_EXPxD_DM_PRD.set_downstream(sqlg_jobs_PRD.FCT_TESTING_EXPENSE)

sqlg_jobs_PRD.DIM_ITEM.dag=D_DM_PRD
D_SDM_PRDxSDM_ITEMxD_DM_PRD.set_downstream(sqlg_jobs_PRD.DIM_ITEM)

sqlg_jobs_PRD.DIM_PLM_CATEGORY.dag=D_DM_PRD
D_SDM_PRDxSDM_PLM_CATEGORYxD_DM_PRD.set_downstream(sqlg_jobs_PRD.DIM_PLM_CATEGORY)

sqlg_jobs_PRD.DIM_ECN_REASON.dag=D_DM_PRD
D_SDM_PRDxSDM_ECN_REASONxD_DM_PRD.set_downstream(sqlg_jobs_PRD.DIM_ECN_REASON)

sqlg_jobs_PRD.DIM_PROJECT_CODE.dag=D_DM_PRD
D_SDM_PRDxSDM_PROJECT_CODExD_DM_PRD.set_downstream(sqlg_jobs_PRD.DIM_PROJECT_CODE)
