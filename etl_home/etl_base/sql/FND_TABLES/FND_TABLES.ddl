
CALL SQLEXT.SP_DROP_IF_EXISTS ('ODS', 'FND_TABLES');
CREATE TABLE ODS.FND_TABLES (
       APPLICATION_ID                          NUMBER(15, 0)
      ,TABLE_ID                                NUMBER(15, 0)
      ,TABLE_NAME                              VARCHAR2(30)
      ,USER_TABLE_NAME                         VARCHAR2(80)
      ,LAST_UPDATE_DATE                        DATE
      ,LAST_UPDATED_BY                         NUMBER(15, 0)
      ,CREATION_DATE                           DATE
      ,CREATED_BY                              NUMBER(15, 0)
      ,LAST_UPDATE_LOGIN                       NUMBER(15, 0)
      ,AUTO_SIZE                               VARCHAR2(1)
      ,TABLE_TYPE                              VARCHAR2(1)
      ,INITIAL_EXTENT                          NUMBER(15, 0)
      ,NEXT_EXTENT                             NUMBER(15, 0)
      ,MIN_EXTENTS                             NUMBER(15, 0)
      ,MAX_EXTENTS                             NUMBER(15, 0)
      ,PCT_INCREASE                            NUMBER(15, 0)
      ,INI_TRANS                               NUMBER(15, 0)
      ,MAX_TRANS                               NUMBER(15, 0)
      ,PCT_FREE                                NUMBER(15, 0)
      ,PCT_USED                                NUMBER(15, 0)
      ,DESCRIPTION                             VARCHAR2(240)
      ,HOSTED_SUPPORT_STYLE                    VARCHAR2(30)
      ,IREP_COMMENTS                           VARCHAR2(4000)
      ,IREP_ANNOTATIONS                        VARCHAR2(4000)
      ,DATA_DATE                               VARCHAR2(8)
      ,TBL_UPD_TIME                            DATE
      ,TBL_UPD_SRC                             VARCHAR2(100)
);

ALTER TABLE ODS.FND_TABLES nologging;



--Comments Create Script 
COMMENT ON TABLE ODS.FND_TABLES IS 'FND_TABLES';
COMMENT ON COLUMN ODS.FND_TABLES.APPLICATION_ID IS 'APPLICATION_ID';
COMMENT ON COLUMN ODS.FND_TABLES.TABLE_ID IS 'TABLE_ID';
COMMENT ON COLUMN ODS.FND_TABLES.TABLE_NAME IS 'TABLE_NAME';
COMMENT ON COLUMN ODS.FND_TABLES.USER_TABLE_NAME IS 'USER_TABLE_NAME';
COMMENT ON COLUMN ODS.FND_TABLES.LAST_UPDATE_DATE IS 'LAST_UPDATE_DATE';
COMMENT ON COLUMN ODS.FND_TABLES.LAST_UPDATED_BY IS 'LAST_UPDATED_BY';
COMMENT ON COLUMN ODS.FND_TABLES.CREATION_DATE IS 'CREATION_DATE';
COMMENT ON COLUMN ODS.FND_TABLES.CREATED_BY IS 'CREATED_BY';
COMMENT ON COLUMN ODS.FND_TABLES.LAST_UPDATE_LOGIN IS 'LAST_UPDATE_LOGIN';
COMMENT ON COLUMN ODS.FND_TABLES.AUTO_SIZE IS 'AUTO_SIZE';
COMMENT ON COLUMN ODS.FND_TABLES.TABLE_TYPE IS 'TABLE_TYPE';
COMMENT ON COLUMN ODS.FND_TABLES.INITIAL_EXTENT IS 'INITIAL_EXTENT';
COMMENT ON COLUMN ODS.FND_TABLES.NEXT_EXTENT IS 'NEXT_EXTENT';
COMMENT ON COLUMN ODS.FND_TABLES.MIN_EXTENTS IS 'MIN_EXTENTS';
COMMENT ON COLUMN ODS.FND_TABLES.MAX_EXTENTS IS 'MAX_EXTENTS';
COMMENT ON COLUMN ODS.FND_TABLES.PCT_INCREASE IS 'PCT_INCREASE';
COMMENT ON COLUMN ODS.FND_TABLES.INI_TRANS IS 'INI_TRANS';
COMMENT ON COLUMN ODS.FND_TABLES.MAX_TRANS IS 'MAX_TRANS';
COMMENT ON COLUMN ODS.FND_TABLES.PCT_FREE IS 'PCT_FREE';
COMMENT ON COLUMN ODS.FND_TABLES.PCT_USED IS 'PCT_USED';
COMMENT ON COLUMN ODS.FND_TABLES.DESCRIPTION IS 'DESCRIPTION';
COMMENT ON COLUMN ODS.FND_TABLES.HOSTED_SUPPORT_STYLE IS 'HOSTED_SUPPORT_STYLE';
COMMENT ON COLUMN ODS.FND_TABLES.IREP_COMMENTS IS 'IREP_COMMENTS';
COMMENT ON COLUMN ODS.FND_TABLES.IREP_ANNOTATIONS IS 'IREP_ANNOTATIONS';
COMMENT ON COLUMN ODS.FND_TABLES.DATA_DATE IS 'DataDate';
COMMENT ON COLUMN ODS.FND_TABLES.TBL_UPD_TIME IS 'Updated Time';
COMMENT ON COLUMN ODS.FND_TABLES.TBL_UPD_SRC IS 'Updated Source';

CALL SQLEXT.SP_DROP_IF_EXISTS ('ODS', 'FND_TABLES_TPX');
CREATE TABLE ODS.FND_TABLES_TPX AS SELECT * FROM SQLEXT.EXCEPTIONS WHERE 1=2
;




CALL SQLEXT.SP_DROP_IF_EXISTS ('ODS', 'FND_TABLES_TP1');
CREATE TABLE ODS.FND_TABLES_TP1 (
       APPLICATION_ID                          NUMBER(15, 0)
      ,TABLE_ID                                NUMBER(15, 0)
      ,TABLE_NAME                              VARCHAR2(30)
      ,USER_TABLE_NAME                         VARCHAR2(80)
      ,LAST_UPDATE_DATE                        DATE
      ,LAST_UPDATED_BY                         NUMBER(15, 0)
      ,CREATION_DATE                           DATE
      ,CREATED_BY                              NUMBER(15, 0)
      ,LAST_UPDATE_LOGIN                       NUMBER(15, 0)
      ,AUTO_SIZE                               VARCHAR2(1)
      ,TABLE_TYPE                              VARCHAR2(1)
      ,INITIAL_EXTENT                          NUMBER(15, 0)
      ,NEXT_EXTENT                             NUMBER(15, 0)
      ,MIN_EXTENTS                             NUMBER(15, 0)
      ,MAX_EXTENTS                             NUMBER(15, 0)
      ,PCT_INCREASE                            NUMBER(15, 0)
      ,INI_TRANS                               NUMBER(15, 0)
      ,MAX_TRANS                               NUMBER(15, 0)
      ,PCT_FREE                                NUMBER(15, 0)
      ,PCT_USED                                NUMBER(15, 0)
      ,DESCRIPTION                             VARCHAR2(240)
      ,HOSTED_SUPPORT_STYLE                    VARCHAR2(30)
      ,IREP_COMMENTS                           VARCHAR2(4000)
      ,IREP_ANNOTATIONS                        VARCHAR2(4000)
);

ALTER TABLE ODS.FND_TABLES_TP1 nologging;



--Comments Create Script 
COMMENT ON TABLE ODS.FND_TABLES_TP1 IS 'FND_TABLES�Ȧs��';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.APPLICATION_ID IS 'APPLICATION_ID';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.TABLE_ID IS 'TABLE_ID';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.TABLE_NAME IS 'TABLE_NAME';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.USER_TABLE_NAME IS 'USER_TABLE_NAME';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.LAST_UPDATE_DATE IS 'LAST_UPDATE_DATE';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.LAST_UPDATED_BY IS 'LAST_UPDATED_BY';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.CREATION_DATE IS 'CREATION_DATE';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.CREATED_BY IS 'CREATED_BY';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.LAST_UPDATE_LOGIN IS 'LAST_UPDATE_LOGIN';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.AUTO_SIZE IS 'AUTO_SIZE';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.TABLE_TYPE IS 'TABLE_TYPE';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.INITIAL_EXTENT IS 'INITIAL_EXTENT';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.NEXT_EXTENT IS 'NEXT_EXTENT';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.MIN_EXTENTS IS 'MIN_EXTENTS';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.MAX_EXTENTS IS 'MAX_EXTENTS';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.PCT_INCREASE IS 'PCT_INCREASE';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.INI_TRANS IS 'INI_TRANS';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.MAX_TRANS IS 'MAX_TRANS';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.PCT_FREE IS 'PCT_FREE';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.PCT_USED IS 'PCT_USED';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.DESCRIPTION IS 'DESCRIPTION';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.HOSTED_SUPPORT_STYLE IS 'HOSTED_SUPPORT_STYLE';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.IREP_COMMENTS IS 'IREP_COMMENTS';
COMMENT ON COLUMN ODS.FND_TABLES_TP1.IREP_ANNOTATIONS IS 'IREP_ANNOTATIONS';


