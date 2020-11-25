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
#from acme.operators.dwh_operators import PostgresOperatorWithTemplatedParams
import sqlg_jobs_QAM


args = {
    "owner": "JESSEWEI",
    'start_date': airflow.utils.dates.days_ago(1),
    'provide_context': True
}

ExternalTaskSensor.ui_color = 'white'
ExternalTaskSensor.ui_fgcolor = 'blue'

tmpl_search_path = Variable.get("sql_path")

# Flow dag    
# DB_NAME = 'DWH' 
D_ODS_QAM = airflow.DAG(
    "D_ODS_QAM",
    tags=["QAM"],
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1
	)


my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_QAM"
D_STG_INITxSYS_STS_STGxD_ODS_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_ODS_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_QAM"
D_STG_INITxSYS_STS_STGxD_SDM_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_SDM_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_QAM"
D_STG_INITxSYS_STS_STGxD_DM_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_DM_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_PRD"
D_STG_INITxSYS_STS_STGxD_ODS_PRD= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_ODS_PRD,
#    execution_delta=None,  # Same day as today
)
sqlg_jobs_QAM.HISTORYCARD.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.HISTORYCARD)

sqlg_jobs_QAM.PN_SPC.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.PN_SPC)

sqlg_jobs_QAM.SUB_SPC.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.SUB_SPC)

sqlg_jobs_QAM.RWK_GLOBAL_LOT_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.RWK_GLOBAL_LOT_WS1)

sqlg_jobs_QAM.RWK_GLOBAL_LOT_DETAIL_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.RWK_GLOBAL_LOT_DETAIL_WS1)

sqlg_jobs_QAM.INSTRUMENT_CORRECT_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.INSTRUMENT_CORRECT_NQJ)

sqlg_jobs_QAM.INSTRUMENT_INFO_CORRECT_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.INSTRUMENT_INFO_CORRECT_NQJ)

sqlg_jobs_QAM.MV_MTL_CROSS_REFERENCES_V.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MV_MTL_CROSS_REFERENCES_V)

sqlg_jobs_QAM.XX_ERP_ITEM.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.XX_ERP_ITEM)

sqlg_jobs_QAM.ERPIQC.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.ERPIQC)

sqlg_jobs_QAM.ERFORM_DOC_MSG_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.ERFORM_DOC_MSG_WS1)

sqlg_jobs_QAM.EF_QCEXCEPTION_MST_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.EF_QCEXCEPTION_MST_WS1)

sqlg_jobs_QAM.PN_MODULE.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.PN_MODULE)

sqlg_jobs_QAM.PN_MODULE_MAINTAIN.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.PN_MODULE_MAINTAIN)

sqlg_jobs_QAM.SPC_ABNORMAL.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.SPC_ABNORMAL)

sqlg_jobs_QAM.COPQ_FCTACTUALCOST.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.COPQ_FCTACTUALCOST)

sqlg_jobs_QAM.MTL_MATERIAL_TRANSACTIONS.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MTL_MATERIAL_TRANSACTIONS)

sqlg_jobs_QAM.COPQ_DIMCATEGORY.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.COPQ_DIMCATEGORY)

sqlg_jobs_QAM.BI_DIMMULTIORG.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.BI_DIMMULTIORG)

sqlg_jobs_QAM.MV_ORG_ORGANIZATION_DEF.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MV_ORG_ORGANIZATION_DEF)

sqlg_jobs_QAM.ERDRLRR_INSPECTION_HEADER_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.ERDRLRR_INSPECTION_HEADER_WS1)

sqlg_jobs_QAM.MV_GL_SETS_OF_BOOKS.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MV_GL_SETS_OF_BOOKS)

sqlg_jobs_QAM.MV_WSH_DELIVERABLES_V.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MV_WSH_DELIVERABLES_V)

sqlg_jobs_QAM.QKB_ITEM.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.QKB_ITEM)

sqlg_jobs_QAM.ERDRLRR_INSPECTION_STATUS_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.ERDRLRR_INSPECTION_STATUS_WS1)

sqlg_jobs_QAM.ERDRLRR_INSPECTION_DETAIL_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.ERDRLRR_INSPECTION_DETAIL_WS1)

sqlg_jobs_QAM.ERDRLRR_INSPECTION_RESULT_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.ERDRLRR_INSPECTION_RESULT_WS1)

sqlg_jobs_QAM.PLANT.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.PLANT)

sqlg_jobs_QAM.SAP_MATERIALMASTER.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.SAP_MATERIALMASTER)

sqlg_jobs_QAM.MATERIALGROUP.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MATERIALGROUP)

sqlg_jobs_QAM.CONTROLTABLE.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.CONTROLTABLE)

sqlg_jobs_QAM.EMS_LOOKUPVALUE_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.EMS_LOOKUPVALUE_NQJ)

sqlg_jobs_QAM.WO_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.WO_NQJ)

sqlg_jobs_QAM.SPN_TABL_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.SPN_TABL_NQJ)

sqlg_jobs_QAM.RESULTTYPE.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.RESULTTYPE)

sqlg_jobs_QAM.MV_PDE_EXCEPTION_HEADER_V_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MV_PDE_EXCEPTION_HEADER_V_WS1)

sqlg_jobs_QAM.MV_PDE_EXCEPTION_EQUIP_V_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MV_PDE_EXCEPTION_EQUIP_V_WS1)

sqlg_jobs_QAM.MV_PDE_EXCEPTION_DETAIL_V_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MV_PDE_EXCEPTION_DETAIL_V_WS1)

sqlg_jobs_QAM.PDE_USER_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.PDE_USER_WS1)

sqlg_jobs_QAM.QCE_REASON_CODE_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.QCE_REASON_CODE_WS1)

sqlg_jobs_QAM.EMS_MANUFACTURER_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.EMS_MANUFACTURER_WS1)

sqlg_jobs_QAM.MODELTYPE.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MODELTYPE)

sqlg_jobs_QAM.EFLOW_ATLO_SCAR_CN.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.EFLOW_ATLO_SCAR_CN)

sqlg_jobs_QAM.ATLO_QUESTION_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.ATLO_QUESTION_NQJ)

sqlg_jobs_QAM.EF_QCEXCEPTION_MST_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.EF_QCEXCEPTION_MST_NQJ)

sqlg_jobs_QAM.ATLO_SCAR_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.ATLO_SCAR_NQJ)

sqlg_jobs_QAM.MV_XXCS_INCIDENTS_SFCS.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MV_XXCS_INCIDENTS_SFCS)

sqlg_jobs_QAM.CLOUD_WO_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.CLOUD_WO_NQJ)

sqlg_jobs_QAM.MATERIALGROUP_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MATERIALGROUP_NQJ)

sqlg_jobs_QAM.INSPECTIONLOT_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.INSPECTIONLOT_NQJ)

sqlg_jobs_QAM.MSD_CS_DATA.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.MSD_CS_DATA)

sqlg_jobs_QAM.SAP_MATERIALMASTER_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.SAP_MATERIALMASTER_NQJ)

sqlg_jobs_QAM.ERPIQC_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs_QAM.ERPIQC_NQJ)

D_SDM_QAM = airflow.DAG(
    "D_SDM_QAM",
    tags=["QAM"],
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1
	)


my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_QAM"
D_STG_INITxSYS_STS_STGxD_ODS_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_ODS_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_QAM"
D_STG_INITxSYS_STS_STGxD_SDM_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_SDM_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_QAM"
D_STG_INITxSYS_STS_STGxD_DM_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_DM_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_PRD"
D_STG_INITxSYS_STS_STGxD_ODS_PRD= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_ODS_PRD,
#    execution_delta=None,  # Same day as today
)
sqlg_jobs_QAM.SDM_MATERIAL_CATEGORY_QA.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_MATERIAL_CATEGORY_QA)

sqlg_jobs_QAM.SDM_PRODUCT_TYPE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_PRODUCT_TYPE)

sqlg_jobs_QAM.SDM_MODULE_TYPE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_MODULE_TYPE)

sqlg_jobs_QAM.SDM_PRODUCT_DEVELOPMENT_TYPE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_PRODUCT_DEVELOPMENT_TYPE)

sqlg_jobs_QAM.SDM_MATERIAL_DEFECT_MODE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_MATERIAL_DEFECT_MODE)

sqlg_jobs_QAM.SDM_ABNORMAL_DESCRIPTION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_ABNORMAL_DESCRIPTION)

sqlg_jobs_QAM.SDM_CATEGORY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CATEGORY)

sqlg_jobs_QAM.SDM_QA_RESULT.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_QA_RESULT)

sqlg_jobs_QAM.SDM_CONTROL_STATION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CONTROL_STATION)

sqlg_jobs_QAM.SDM_CONTROL_THE_PROJECT.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CONTROL_THE_PROJECT)

sqlg_jobs_QAM.SDM_TURN_AROUND_TIME.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_TURN_AROUND_TIME)

sqlg_jobs_QAM.SDM_RMA_CASE_STATUS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_RMA_CASE_STATUS)

sqlg_jobs_QAM.SDM_PERSON_IN_CHARGE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_PERSON_IN_CHARGE)

sqlg_jobs_QAM.SDM_CLOSED_DAY_8D.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CLOSED_DAY_8D)

sqlg_jobs_QAM.SDM_TIER1.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_TIER1)

sqlg_jobs_QAM.SDM_SHIPPING_DATE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_SHIPPING_DATE)

sqlg_jobs_QAM.SDM_RETURN_SOURCE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_RETURN_SOURCE)

sqlg_jobs_QAM.SDM_SHIPPING_PERIOD.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_SHIPPING_PERIOD)

sqlg_jobs_QAM.SDM_WARRANTY_STATUS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_WARRANTY_STATUS)

sqlg_jobs_QAM.SDM_INVENTORY_OWNER.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_INVENTORY_OWNER)

sqlg_jobs_QAM.SDM_MANUFACTURER.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_MANUFACTURER)

sqlg_jobs_QAM.SDM_CAVITY_NO.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CAVITY_NO)

sqlg_jobs_QAM.SDM_CASE_CLOSE_STATUS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CASE_CLOSE_STATUS)

sqlg_jobs_QAM.SDM_STATION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_STATION)

sqlg_jobs_QAM.SDM_C_FLOW_DEVELOPMENT_STAGE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_C_FLOW_DEVELOPMENT_STAGE)

sqlg_jobs_QAM.SDM_C_FLOW_DEVELOPMENT_DERI.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_C_FLOW_DEVELOPMENT_DERI)

sqlg_jobs_QAM.SDM_ATLO_FOR_MP.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_ATLO_FOR_MP)

sqlg_jobs_QAM.SDM_MP_FLAG.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_MP_FLAG)

sqlg_jobs_QAM.SDM_PM.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_PM)

sqlg_jobs_QAM.SDM_EPR_UPPER_LIMIT_OF_MOD.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_EPR_UPPER_LIMIT_OF_MOD)

sqlg_jobs_QAM.SDM_MO_NO.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_MO_NO)

sqlg_jobs_QAM.SDM_MO_START_MONTH.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_MO_START_MONTH)

sqlg_jobs_QAM.SDM_MO_PART_TYPE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_MO_PART_TYPE)

sqlg_jobs_QAM.SDM_EPR_UPPER_LIMIT_OF_SIN.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_EPR_UPPER_LIMIT_OF_SIN)

sqlg_jobs_QAM.SDM_MP_APPROVE_DATE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_MP_APPROVE_DATE)

sqlg_jobs_QAM.SDM_SR_NUMBER.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_SR_NUMBER)

sqlg_jobs_QAM.SDM_CSD_REASON_PAY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CSD_REASON_PAY)

sqlg_jobs_QAM.SDM_CSD_MATERIAL_SCRAP_COS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CSD_MATERIAL_SCRAP_COS)

sqlg_jobs_QAM.SDM_CSD_CUSTOMER_PAID_SERV.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CSD_CUSTOMER_PAID_SERV)

sqlg_jobs_QAM.SDM_IQC_DAILY_INPUT_MANP_A.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_IQC_DAILY_INPUT_MANP_A)

sqlg_jobs_QAM.SDM_IQC_DAILY_INPUT_MANP.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_IQC_DAILY_INPUT_MANP)

sqlg_jobs_QAM.SDM_IQC_DAILY_TOTAL_INSP.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_IQC_DAILY_TOTAL_INSP)

sqlg_jobs_QAM.SDM_IQC_AVERAGE_INSPECTION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_IQC_AVERAGE_INSPECTION)

sqlg_jobs_QAM.SDM_INCOMING_MATERIAL_REJEC.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_INCOMING_MATERIAL_REJEC)

sqlg_jobs_QAM.SDM_SUPPLIER_MATERIAL_PRODUC.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_SUPPLIER_MATERIAL_PRODUC)

sqlg_jobs_QAM.SDM_CUSTOMER_INSPECTION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CUSTOMER_INSPECTION)

sqlg_jobs_QAM.SDM_CUSTOMER_COMPLAIN_CASES.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CUSTOMER_COMPLAIN_CASES)

sqlg_jobs_QAM.SDM_IN_PROCESS_QUALITY_CONTROL.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_IN_PROCESS_QUALITY_CONTROL)

sqlg_jobs_QAM.SDM_QUALITY_ALERT_CASES.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_QUALITY_ALERT_CASES)

sqlg_jobs_QAM.SDM_EQUIPMENT_ANOMALY_CASE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_EQUIPMENT_ANOMALY_CASE)

sqlg_jobs_QAM.SDM_FIXTURE_ANOMALY_CASES.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_FIXTURE_ANOMALY_CASES)

sqlg_jobs_QAM.SDM_EQUIPMENT_FIXTURE_ANOM.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_EQUIPMENT_FIXTURE_ANOM)

sqlg_jobs_QAM.SDM_FAULT_INJECTION_DR.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_FAULT_INJECTION_DR)

sqlg_jobs_QAM.SDM_Q_SCAN_DEFECT_RATE_DR.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_Q_SCAN_DEFECT_RATE_DR)

sqlg_jobs_QAM.SDM_FINAL_QUALITY_INSPECTI.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_FINAL_QUALITY_INSPECTI)

sqlg_jobs_QAM.SDM_FQC_LRR.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_FQC_LRR)

sqlg_jobs_QAM.SDM_QUALITY_HOLD_CASES.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_QUALITY_HOLD_CASES)

sqlg_jobs_QAM.SDM_CLOSE_WITHIN_SIPULATED.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CLOSE_WITHIN_SIPULATED)

sqlg_jobs_QAM.SDM_CUSTOMER_COMPLAIN_FOR.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CUSTOMER_COMPLAIN_FOR)

sqlg_jobs_QAM.SDM_ON_TIME_CLOSE_RATIO_FOR_WN.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_ON_TIME_CLOSE_RATIO_FOR_WN)

sqlg_jobs_QAM.SDM_CLOSE_WITHIN_14_DAYS_FO.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CLOSE_WITHIN_14_DAYS_FO)

sqlg_jobs_QAM.SDM_CUSTOMER_COMPLAIN_FOR_S.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CUSTOMER_COMPLAIN_FOR_S)

sqlg_jobs_QAM.SDM_CLOSE_WITHIN_14_DAYS_RATIO.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CLOSE_WITHIN_14_DAYS_RATIO)

sqlg_jobs_QAM.SDM_FIELD_DEFECT_QUANTITY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_FIELD_DEFECT_QUANTITY)

sqlg_jobs_QAM.SDM_SHIPPING_QUANTITY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_SHIPPING_QUANTITY)

sqlg_jobs_QAM.SDM_AUTOMOTIVE_PRODUCT_FIELD_D.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_AUTOMOTIVE_PRODUCT_FIELD_D)

sqlg_jobs_QAM.SDM_ON_SITE_REWORK_QUANTITY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_ON_SITE_REWORK_QUANTITY)

sqlg_jobs_QAM.SDM_IN_WARRANTY_RETURN_QUANTITY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_IN_WARRANTY_RETURN_QUANTITY)

sqlg_jobs_QAM.SDM_QUALITY_REJECT_QUANTITY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_QUALITY_REJECT_QUANTITY)

sqlg_jobs_QAM.SDM_MODELS_WITH_MO_RECORDS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_MODELS_WITH_MO_RECORDS)

sqlg_jobs_QAM.SDM_CSD_PLANNED_SHIPPING.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CSD_PLANNED_SHIPPING)

sqlg_jobs_QAM.SDM_ACTUAL_CALIBRATION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_ACTUAL_CALIBRATION)

sqlg_jobs_QAM.SDM_PLANNED_CALIBRATION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_PLANNED_CALIBRATION)

sqlg_jobs_QAM.SDM_CALIBRATION_COMPLETED_RATE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_CALIBRATION_COMPLETED_RATE)

sqlg_jobs_QAM.SDM_TICKET_TYPE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_TICKET_TYPE)

sqlg_jobs_QAM.SDM_FINAL_QUALITY_INSPECT.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs_QAM.SDM_FINAL_QUALITY_INSPECT)

D_DM_QAM = airflow.DAG(
    "D_DM_QAM",
    tags=["QAM"],
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1
	)


my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_QAM"
D_STG_INITxSYS_STS_STGxD_ODS_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_ODS_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_QAM"
D_STG_INITxSYS_STS_STGxD_SDM_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_SDM_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_QAM"
D_STG_INITxSYS_STS_STGxD_DM_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_DM_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_PRD"
D_STG_INITxSYS_STS_STGxD_ODS_PRD= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_ODS_PRD,
#    execution_delta=None,  # Same day as today
)
sqlg_jobs_QAM.DIM_MATERIAL_CATEGORY_QA.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_MATERIAL_CATEGORY_QA)

sqlg_jobs_QAM.DIM_PRODUCT_TYPE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_PRODUCT_TYPE)

sqlg_jobs_QAM.DIM_MODULE_TYPE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_MODULE_TYPE)

sqlg_jobs_QAM.DIM_PRODUCT_DEVELOPMENT_TYPE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_PRODUCT_DEVELOPMENT_TYPE)

sqlg_jobs_QAM.DIM_MATERIAL_DEFECT_MODE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_MATERIAL_DEFECT_MODE)

sqlg_jobs_QAM.DIM_ABNORMAL_DESCRIPTION.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_ABNORMAL_DESCRIPTION)

sqlg_jobs_QAM.DIM_CATEGORY.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_CATEGORY)

sqlg_jobs_QAM.DIM_QA_RESULT.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_QA_RESULT)

sqlg_jobs_QAM.DIM_CONTROL_STATION.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_CONTROL_STATION)

sqlg_jobs_QAM.DIM_CONTROL_THE_PROJECT.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_CONTROL_THE_PROJECT)

sqlg_jobs_QAM.DIM_TURN_AROUND_TIME.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_TURN_AROUND_TIME)

sqlg_jobs_QAM.DIM_RMA_CASE_STATUS.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_RMA_CASE_STATUS)

sqlg_jobs_QAM.DIM_PERSON_IN_CHARGE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_PERSON_IN_CHARGE)

sqlg_jobs_QAM.DIM_CLOSED_DAY_8D.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_CLOSED_DAY_8D)

sqlg_jobs_QAM.DIM_TIER1.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_TIER1)

sqlg_jobs_QAM.DIM_SHIPPING_DATE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_SHIPPING_DATE)

sqlg_jobs_QAM.DIM_RETURN_SOURCE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_RETURN_SOURCE)

sqlg_jobs_QAM.DIM_SHIPPING_PERIOD.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_SHIPPING_PERIOD)

sqlg_jobs_QAM.DIM_WARRANTY_STATUS.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_WARRANTY_STATUS)

sqlg_jobs_QAM.DIM_INVENTORY_OWNER.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_INVENTORY_OWNER)

sqlg_jobs_QAM.DIM_MANUFACTURER.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_MANUFACTURER)

sqlg_jobs_QAM.DIM_CAVITY_NO.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_CAVITY_NO)

sqlg_jobs_QAM.DIM_CASE_CLOSE_STATUS.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_CASE_CLOSE_STATUS)

sqlg_jobs_QAM.DIM_STATION.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_STATION)

sqlg_jobs_QAM.DIM_C_FLOW_DEVELOPMENT_STAGE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_C_FLOW_DEVELOPMENT_STAGE)

sqlg_jobs_QAM.DIM_C_FLOW_DEVELOPMENT_DERI.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_C_FLOW_DEVELOPMENT_DERI)

sqlg_jobs_QAM.DIM_ATLO_FOR_MP.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_ATLO_FOR_MP)

sqlg_jobs_QAM.DIM_MP_FLAG.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_MP_FLAG)

sqlg_jobs_QAM.DIM_PM.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_PM)

sqlg_jobs_QAM.DIM_EPR_UPPER_LIMIT_OF_MOD.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_EPR_UPPER_LIMIT_OF_MOD)

sqlg_jobs_QAM.DIM_MO_NO.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_MO_NO)

sqlg_jobs_QAM.DIM_MO_START_MONTH.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_MO_START_MONTH)

sqlg_jobs_QAM.DIM_MO_PART_TYPE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_MO_PART_TYPE)

sqlg_jobs_QAM.DIM_EPR_UPPER_LIMIT_OF_SIN.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_EPR_UPPER_LIMIT_OF_SIN)

sqlg_jobs_QAM.DIM_MP_APPROVE_DATE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_MP_APPROVE_DATE)

sqlg_jobs_QAM.DIM_SR_NUMBER.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.DIM_SR_NUMBER)

sqlg_jobs_QAM.FCT_CSD_MATERIAL_SCRAP_COS.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_CSD_MATERIAL_SCRAP_COS)

sqlg_jobs_QAM.FCT_CSD_CUSTOMER_PAID_SERV.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_CSD_CUSTOMER_PAID_SERV)

sqlg_jobs_QAM.FCT_IQC_DAILY_INPUT_MANP.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_IQC_DAILY_INPUT_MANP)

sqlg_jobs_QAM.FCT_IQC_DAILY_TOTAL_INSP.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_IQC_DAILY_TOTAL_INSP)

sqlg_jobs_QAM.FCT_IQC_AVERAGE_INSPECTION.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_IQC_AVERAGE_INSPECTION)

sqlg_jobs_QAM.FCT_SUPPLIER_MATERIAL_PRODUC.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_SUPPLIER_MATERIAL_PRODUC)

sqlg_jobs_QAM.FCT_CUSTOMER_INSPECTION.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_CUSTOMER_INSPECTION)

sqlg_jobs_QAM.FCT_CUSTOMER_COMPLAIN_CASES.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_CUSTOMER_COMPLAIN_CASES)

sqlg_jobs_QAM.FCT_FAULT_INJECTION_DR.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_FAULT_INJECTION_DR)

sqlg_jobs_QAM.FCT_Q_SCAN_DEFECT_RATE_DR.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_Q_SCAN_DEFECT_RATE_DR)

sqlg_jobs_QAM.FCT_QUALITY_HOLD_CASES.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_QUALITY_HOLD_CASES)

sqlg_jobs_QAM.FCT_CLOSE_WITHIN_SIPULATED.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_CLOSE_WITHIN_SIPULATED)

sqlg_jobs_QAM.FCT_CUSTOMER_COMPLAIN_FOR.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_CUSTOMER_COMPLAIN_FOR)

sqlg_jobs_QAM.FCT_ON_TIME_CLOSE_RATIO_FOR_WN.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_ON_TIME_CLOSE_RATIO_FOR_WN)

sqlg_jobs_QAM.FCT_CLOSE_WITHIN_14_DAYS_FO.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_CLOSE_WITHIN_14_DAYS_FO)

sqlg_jobs_QAM.FCT_CUSTOMER_COMPLAIN_FOR_S.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_CUSTOMER_COMPLAIN_FOR_S)

sqlg_jobs_QAM.FCT_CLOSE_WITHIN_14_DAYS_RATIO.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_CLOSE_WITHIN_14_DAYS_RATIO)

sqlg_jobs_QAM.FCT_FIELD_DEFECT_QUANTITY.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_FIELD_DEFECT_QUANTITY)

sqlg_jobs_QAM.FCT_SHIPPING_QUANTITY.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_SHIPPING_QUANTITY)

sqlg_jobs_QAM.FCT_AUTOMOTIVE_PRODUCT_FIELD_D.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs_QAM.FCT_AUTOMOTIVE_PRODUCT_FIELD_D)

D_ODS_PRD = airflow.DAG(
    "D_ODS_PRD",
    tags=["QAM"],
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1
	)


my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_QAM"
D_STG_INITxSYS_STS_STGxD_ODS_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_ODS_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_QAM"
D_STG_INITxSYS_STS_STGxD_SDM_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_SDM_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_QAM"
D_STG_INITxSYS_STS_STGxD_DM_QAM= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_DM_QAM,
#    execution_delta=None,  # Same day as today
)

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_PRD"
D_STG_INITxSYS_STS_STGxD_ODS_PRD= ExternalTaskSensor(
#    schedule_interval=None,
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
#    dag=D_ODS_PRD,
#    execution_delta=None,  # Same day as today
)
sqlg_jobs_QAM.ODS_UP_consign_vendor_Prod_map_WH.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_QAM.ODS_UP_consign_vendor_Prod_map_WH)

sqlg_jobs_QAM.ODS_UP_consign_vendor_Prod_map_CPD.dag=D_ODS_PRD
sqlg_jobs_QAM.ODS_UP_consign_vendor_Prod_map_WH.set_downstream(sqlg_jobs_QAM.ODS_UP_consign_vendor_Prod_map_CPD)

sqlg_jobs_QAM.UP_consign_vendor_Prod_map_STG.dag=D_ODS_PRD
sqlg_jobs_QAM.ODS_UP_consign_vendor_Prod_map_CPD.set_downstream(sqlg_jobs_QAM.UP_consign_vendor_Prod_map_STG)

sqlg_jobs_QAM.ODS_UP_consign_vendor_Prod_map_LD.dag=D_ODS_PRD
sqlg_jobs_QAM.UP_consign_vendor_Prod_map_STG.set_downstream(sqlg_jobs_QAM.ODS_UP_consign_vendor_Prod_map_LD)

sqlg_jobs_QAM.UP_consign_vendor_Prod_map.dag=D_ODS_PRD
sqlg_jobs_QAM.ODS_UP_consign_vendor_Prod_map_LD.set_downstream(sqlg_jobs_QAM.UP_consign_vendor_Prod_map)

sqlg_jobs_QAM.ODS_UP_Expense_Budget_Prod_map_WH.dag=D_ODS_PRD
D_STG_INITxSYS_STS_STGxD_ODS_PRD.set_downstream(sqlg_jobs_QAM.ODS_UP_Expense_Budget_Prod_map_WH)

sqlg_jobs_QAM.ODS_UP_Expense_Budget_Prod_map_CPD.dag=D_ODS_PRD
sqlg_jobs_QAM.ODS_UP_Expense_Budget_Prod_map_WH.set_downstream(sqlg_jobs_QAM.ODS_UP_Expense_Budget_Prod_map_CPD)

sqlg_jobs_QAM.UP_Expense_Budget_Prod_map_STG.dag=D_ODS_PRD
sqlg_jobs_QAM.ODS_UP_Expense_Budget_Prod_map_CPD.set_downstream(sqlg_jobs_QAM.UP_Expense_Budget_Prod_map_STG)

sqlg_jobs_QAM.ODS_UP_Expense_Budget_Prod_map_LD.dag=D_ODS_PRD
sqlg_jobs_QAM.UP_Expense_Budget_Prod_map_STG.set_downstream(sqlg_jobs_QAM.ODS_UP_Expense_Budget_Prod_map_LD)

sqlg_jobs_QAM.UP_Expense_Budget_Prod_map.dag=D_ODS_PRD
sqlg_jobs_QAM.ODS_UP_Expense_Budget_Prod_map_LD.set_downstream(sqlg_jobs_QAM.UP_Expense_Budget_Prod_map)

