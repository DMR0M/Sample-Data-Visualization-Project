import os
from chart_class import Charts

csv_file_list: list = os.listdir('../csv_data')
sp = Charts(csv_file_list)
sp.combined_chart('Speed', 'Attack', bar_color_2='tomato')
sp.show_chart('Hp', bar_color='springgreen')
# sp.show_chart('Attack', bar_color='red')
# sp.show_chart('Defense', bar_color='gold')
# sp.show_chart('Sp. Attack', bar_color='navy')
# sp.show_chart('Sp. Defense', bar_color='magenta')
# sp.show_chart('Speed', bar_color='darkorange')

