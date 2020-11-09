
CALL SQLEXT.SP_DROP_IF_EXISTS ('DM', 'FCT_DMST_AND_INTL_TRAVEL_EXP');
CREATE TABLE DM.FCT_DMST_AND_INTL_TRAVEL_EXP (
       PROJECT_CODE                            VARCHAR2(30)
      ,DOMESTIC_AND_INTL_TRAVEL_EXPENSES       VARCHAR2(30)
      ,DATA_DATE                               VARCHAR2(8)
      ,TBL_UPD_TIME                            DATE
      ,TBL_UPD_SRC                             VARCHAR2(100)
);

ALTER TABLE DM.FCT_DMST_AND_INTL_TRAVEL_EXP nologging;



--Comments Create Script 
COMMENT ON TABLE DM.FCT_DMST_AND_INTL_TRAVEL_EXP IS '�ꤺ�~�X�t�O��';
COMMENT ON COLUMN DM.FCT_DMST_AND_INTL_TRAVEL_EXP.PROJECT_CODE IS '�M�ץN�X';
COMMENT ON COLUMN DM.FCT_DMST_AND_INTL_TRAVEL_EXP.DOMESTIC_AND_INTL_TRAVEL_EXPENSES IS '�ꤺ�~�X�t�O��';
COMMENT ON COLUMN DM.FCT_DMST_AND_INTL_TRAVEL_EXP.DATA_DATE IS 'DataDate';
COMMENT ON COLUMN DM.FCT_DMST_AND_INTL_TRAVEL_EXP.TBL_UPD_TIME IS 'Updated Time';
COMMENT ON COLUMN DM.FCT_DMST_AND_INTL_TRAVEL_EXP.TBL_UPD_SRC IS 'Updated Source';

CALL SQLEXT.SP_DROP_IF_EXISTS ('DM', 'FCT_DMST_AND_INTL_TRAVEL_EXP_TPX');
CREATE TABLE DM.FCT_DMST_AND_INTL_TRAVEL_EXP_TPX AS SELECT * FROM SQLEXT.EXCEPTIONS WHERE 1=2
;




CALL SQLEXT.SP_DROP_IF_EXISTS ('DM', 'FCT_DMST_AND_INTL_TRAVEL_EXP_TP1');
CREATE TABLE DM.FCT_DMST_AND_INTL_TRAVEL_EXP_TP1 (
       PROJECT_CODE                            VARCHAR2(30)
      ,DOMESTIC_AND_INTL_TRAVEL_EXPENSES       VARCHAR2(30)
);

ALTER TABLE DM.FCT_DMST_AND_INTL_TRAVEL_EXP_TP1 nologging;



--Comments Create Script 
COMMENT ON TABLE DM.FCT_DMST_AND_INTL_TRAVEL_EXP_TP1 IS '�ꤺ�~�X�t�O�μȦs��';
COMMENT ON COLUMN DM.FCT_DMST_AND_INTL_TRAVEL_EXP_TP1.PROJECT_CODE IS '�M�ץN�X';
COMMENT ON COLUMN DM.FCT_DMST_AND_INTL_TRAVEL_EXP_TP1.DOMESTIC_AND_INTL_TRAVEL_EXPENSES IS '�ꤺ�~�X�t�O��';


