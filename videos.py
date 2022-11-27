import pandas as pd

pd.set_option('display.max_columns', None)  # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据
pd.set_option('display.max_colwidth', 100)

videos = pd.read_csv('static/videos.csv')

kedou_wutai = videos[(videos['pages'] == 'kedou') & (videos['class_name'] == '舞台')][
    ['links', 'ids', 'images', 'titles']]

kedou_mcm = videos[(videos['pages'] == 'kedou') & (videos['class_name'] == '经典名场面')][
    ['links', 'ids', 'images', 'titles']].reset_index()

kedou_wutai_n = len(kedou_wutai)
kedou_mcm_n = len(kedou_mcm)

