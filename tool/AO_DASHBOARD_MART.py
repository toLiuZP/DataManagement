from Aspira import kitmaker

kitmaker.Release(
    r'KS_DASHBOARD_MART.sql',
    kitmaker.Plan(
        dict(
            DBNAME='KS_DASHBOARD_MART',
            TABLEFG='KS_DASHBOARD_MART_DATA',
            INDEXFG='KS_DASHBOARD_MART_IDX'
        ),
        r'..\..\SourceCode\Databases\ASPIRAONE_DASHBOARD_MART\Schemas',
		r'..\..\SourceCode\Databases\ASPIRAONE_DASHBOARD_MART\Tables',
		r'..\..\SourceCode\Databases\ASPIRAONE_DASHBOARD_MART\UserFunctions',
		r'..\..\SourceCode\Databases\ASPIRAONE_DASHBOARD_MART\StoredProcedures'

    )
).generate()
