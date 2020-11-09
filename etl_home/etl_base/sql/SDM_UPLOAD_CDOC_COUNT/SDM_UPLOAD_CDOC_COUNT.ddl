
CALL SQLEXT.SP_DROP_IF_EXISTS ('SDM', 'SDM_UPLOAD_CDOC_COUNT');
CREATE TABLE SDM.SDM_UPLOAD_CDOC_COUNT (
       PROJECT_CODE                            VARCHAR2(30)
      ,BUSINESS_GROUP                          VARCHAR2(30)
      ,MODEL                                   VARCHAR2(30)
      ,MANUFACTURING_PLANT                     VARCHAR2(30)
      ,DOC_CODE                                VARCHAR2(30)
      ,STAGE                                   VARCHAR2(30)
      ,UPLOAD_CDOC_COUNT                       NUMBER
      ,DATA_DATE                               VARCHAR2(8)
      ,TBL_UPD_TIME                            DATE
      ,TBL_UPD_SRC                             VARCHAR2(100)
);

ALTER TABLE SDM.SDM_UPLOAD_CDOC_COUNT nologging;



--Comments Create Script 
COMMENT ON TABLE SDM.SDM_UPLOAD_CDOC_COUNT IS 'C �帹�����ƶq_';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT.PROJECT_CODE IS '�M�ץN�X';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT.BUSINESS_GROUP IS '�з�-�Ʒ~�s';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT.MODEL IS 'Model';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT.MANUFACTURING_PLANT IS '�з�-�s�y�t';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT.DOC_CODE IS 'DOC_CODE';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT.STAGE IS 'STAGE';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT.UPLOAD_CDOC_COUNT IS 'C �帹�����ƶq_';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT.DATA_DATE IS 'DataDate';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT.TBL_UPD_TIME IS 'Updated Time';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT.TBL_UPD_SRC IS 'Updated Source';

CALL SQLEXT.SP_DROP_IF_EXISTS ('SDM', 'SDM_UPLOAD_CDOC_COUNT_TPX');
CREATE TABLE SDM.SDM_UPLOAD_CDOC_COUNT_TPX AS SELECT * FROM SQLEXT.EXCEPTIONS WHERE 1=2
;




CALL SQLEXT.SP_DROP_IF_EXISTS ('SDM', 'SDM_UPLOAD_CDOC_COUNT_TP1');
CREATE TABLE SDM.SDM_UPLOAD_CDOC_COUNT_TP1 (
       PROJECT_CODE                            VARCHAR2(30)
      ,BUSINESS_GROUP                          VARCHAR2(30)
      ,MODEL                                   VARCHAR2(30)
      ,MANUFACTURING_PLANT                     VARCHAR2(30)
      ,DOC_CODE                                VARCHAR2(30)
      ,STAGE                                   VARCHAR2(30)
      ,UPLOAD_CDOC_COUNT                       NUMBER
);

ALTER TABLE SDM.SDM_UPLOAD_CDOC_COUNT_TP1 nologging;



--Comments Create Script 
COMMENT ON TABLE SDM.SDM_UPLOAD_CDOC_COUNT_TP1 IS 'C �帹�����ƶq_�Ȧs��';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT_TP1.PROJECT_CODE IS '�M�ץN�X';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT_TP1.BUSINESS_GROUP IS '�з�-�Ʒ~�s';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT_TP1.MODEL IS 'Model';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT_TP1.MANUFACTURING_PLANT IS '�з�-�s�y�t';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT_TP1.DOC_CODE IS 'DOC_CODE';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT_TP1.STAGE IS 'STAGE';
COMMENT ON COLUMN SDM.SDM_UPLOAD_CDOC_COUNT_TP1.UPLOAD_CDOC_COUNT IS 'C �帹�����ƶq_';


