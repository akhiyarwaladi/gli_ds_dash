        ### #END FORM
        # if not os.path.exists(modul_path):
        #     engine = create_engine(engine_stmt)
        #     q = '''
        #     SELECT AVG(ACTUAL_DAILY) AS AVG_DAILY
        #     FROM(
        #         SELECT 
        #             ACTUAL / ((END_DATE - START_DATE) + 1) AS ACTUAL_DAILY
        #         FROM GLI_REPORT_FAKTUR_SALES_ONLINE
        #         WHERE PLU = {}
        #     )


        #     '''.format(pred_plu)
        #     con = engine.connect()
        #     try:
        #         res_avg = pd.read_sql_query(q,con)
        #     except Exception as e:
        #         if is_debug:
        #             print(e)
        #         pass
        #     con.close()
        #     engine.dispose()
        #     return (
        #         rupiah_format(res_avg['avg_daily'][0] * pred_df['duration'][0], with_prefix=True),
        #         {'display': 'block'}, 
        #         {'display': 'block'},
        #         'duration',
        #         ''
        #     )
        # ####