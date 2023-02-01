CREATE TABLE public.CDC_CONN (
    CONN_TYPE VARCHAR(128),
    CONN_NAME VARCHAR(128)
);

ALTER TABLE public.CDC_CONN ADD CONSTRAINT PK_CDC_CONN PRIMARY KEY(CONN_NAME);

CREATE TABLE public.CDC_TABLES (
    TABLE_ID         VARCHAR(128),
    SOURCE_DB        VARCHAR(128),
    SOURCE_SCHEMA    VARCHAR(128),
    SOURCE_TABLE     VARCHAR(128),
    TARGET_SCHEMA    VARCHAR(128),
    TARGET_TABLE     VARCHAR(128),
    UPPERCASE_FIELDS DECIMAL(18,0),
    FILTER           VARCHAR(128),
    FORCE_INIT       VARCHAR(128),
    CNTRL_FLD        VARCHAR(128)
);

ALTER TABLE public.CDC_TABLES ADD CONSTRAINT PK_CDC_TABLES PRIMARY KEY(TABLE_ID);

CREATE TABLE public.CDC_STATUS (
    TABLE_ID      VARCHAR(128),
    LAST_READ_SEQ VARCHAR(35),
    INIT_READ_SEQ VARCHAR(35)
);

ALTER TABLE public.CDC_STATUS ADD CONSTRAINT PK_CDC_STATUS PRIMARY KEY(TABLE_ID);

CREATE TABLE public.CDC_FIELDS (
    TABLE_ID          VARCHAR(128),
    SOURCE_FIELD_NAME VARCHAR(128),
    TARGET_FIELD_NAME VARCHAR(128),
    FIELD_INDEX       DECIMAL(6,0),
    FIELD_TYPE        VARCHAR(40),
    MODIFIED_TIME     TIMESTAMP,
    PK                DECIMAL(10,0),
    REQUIRED          DECIMAL(10,0)
);

ALTER TABLE public.CDC_FIELDS ADD CONSTRAINT PK_CDC_FIELDS PRIMARY KEY(TABLE_ID, SOURCE_FIELD_NAME);


