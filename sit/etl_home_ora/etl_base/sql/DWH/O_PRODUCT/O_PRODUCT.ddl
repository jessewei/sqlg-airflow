
DROP TABLE IF EXISTS DWH.O_PRODUCT;
CREATE TABLE DWH.O_PRODUCT (
       PRODUCT_ID                              INT
      ,PRODUCT_NAME                            VARCHAR(50)
      ,SUPPLIER_ID                             INT
      ,PRODUCTTYPE_ID                          INT
      ,UPDATED_DTM                             TIMESTAMP
);



--Comments Create Script 
COMMENT ON TABLE DWH.O_PRODUCT IS 'PRODUCT';
COMMENT ON COLUMN DWH.O_PRODUCT.PRODUCT_ID IS 'PRODUCT_ID';
COMMENT ON COLUMN DWH.O_PRODUCT.PRODUCT_NAME IS 'PRODUCT_NAME';
COMMENT ON COLUMN DWH.O_PRODUCT.SUPPLIER_ID IS 'SUPPLIER_ID';
COMMENT ON COLUMN DWH.O_PRODUCT.PRODUCTTYPE_ID IS 'PRODUCTTYPE_ID';
COMMENT ON COLUMN DWH.O_PRODUCT.UPDATED_DTM IS 'UPDATED_DTM';

DROP TABLE IF EXISTS DWH.O_PRODUCT_TPX;
CREATE TABLE DWH.O_PRODUCT_TPX (
       PRODUCT_ID                              INT
      ,PRODUCT_NAME                            VARCHAR(50)
      ,SUPPLIER_ID                             INT
      ,PRODUCTTYPE_ID                          INT
      ,UPDATED_DTM                             TIMESTAMP
);





DROP TABLE IF EXISTS DWH.O_PRODUCT_TP1;
CREATE TABLE DWH.O_PRODUCT_TP1 (
       PRODUCT_ID                              INT
      ,PRODUCT_NAME                            VARCHAR(50)
      ,SUPPLIER_ID                             INT
      ,PRODUCTTYPE_ID                          INT
      ,UPDATED_DTM                             TIMESTAMP
);



--Comments Create Script 
COMMENT ON TABLE DWH.O_PRODUCT_TP1 IS 'PRODUCT_Process Temp Table';
COMMENT ON COLUMN DWH.O_PRODUCT_TP1.PRODUCT_ID IS 'PRODUCT_ID';
COMMENT ON COLUMN DWH.O_PRODUCT_TP1.PRODUCT_NAME IS 'PRODUCT_NAME';
COMMENT ON COLUMN DWH.O_PRODUCT_TP1.SUPPLIER_ID IS 'SUPPLIER_ID';
COMMENT ON COLUMN DWH.O_PRODUCT_TP1.PRODUCTTYPE_ID IS 'PRODUCTTYPE_ID';
COMMENT ON COLUMN DWH.O_PRODUCT_TP1.UPDATED_DTM IS 'UPDATED_DTM';


