import csv

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


class Charts:
    """Class to show all stat charts from gen 1 to gen 9 Pokemons"""
    def __init__(self, csv_files: list, *, rel_path: str = '../csv_data/'):
        self.csv_files = [*csv_files]
        self.rel_path = rel_path
        self.gens = ['Gen. 1', 'Gen. 2', 'Gen. 3', 'Gen. 4', 'Gen. 5',
                     'Gen. 6', 'Gen. 7', 'Gen. 8', 'Gen. 9']

    def __repr__(self):
        return f'File is {__file__}'

    # Show chart for a given stat
    def show_chart(self, stat_key: str,
                   *, bar_color='darkorange', line_color='darkslategrey'):
        stats: list[int] = []
        for file in self.csv_files:
            df = pd.read_csv(f'{self.rel_path}{file}')
            stat_sum = df[stat_key].sum()
            stats.append(stat_sum)

        # Set window title for chart window
        fig = plt.figure('Pokemon Generations Stat Comparison')
        fig.set_figwidth(10)
        fig.set_figheight(5)

        # Create horizontal bar chart
        plt.bar(self.gens, stats, color=bar_color, alpha=0.7, label=stat_key)

        # Display values per generation

        plt.title(f'All Pokemon Generations {stat_key} Comparison')
        plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
        plt.legend()
        plt.show()

    def combined_chart(self, stat_key_1, stat_key_2, stat_key_3, *,
                       bar_color_1='orange', bar_color_2='darkorange',
                       bar_color_3='royalblue', line_color='darkslategrey'):
        stats_1: list[int] = []
        stats_2: list[int] = []
        stats_3: list[int] = []
        for file in self.csv_files:
            df = pd.read_csv(f'{self.rel_path}{file}')
            stat_sum_1 = df[stat_key_1].sum()
            stat_sum_2 = df[stat_key_2].sum()
            stat_sum_3 = df[stat_key_3].sum()
            stats_1.append(stat_sum_1)
            stats_2.append(stat_sum_2)
            stats_3.append(stat_sum_3)

        # Set window title for chart window
        fig = plt.figure('Pokemon Generations Stat Comparison')
        fig.set_figwidth(10)
        fig.set_figheight(5)

        plt.title(f'All Pokemon Generations {stat_key_1}, {stat_key_2}'
                  f' &, {stat_key_3} Comparison')

        x_axis = np.arange(len(self.csv_files))

        plt.bar(x_axis - 0.2, stats_1, 0.2, color=bar_color_1, label=stat_key_1)
        plt.bar(x_axis, stats_2, 0.2, color=bar_color_2, label=stat_key_2)
        plt.bar(x_axis + 0.2, stats_3, 0.2, color=bar_color_3, label=stat_key_3)

        plt.xticks(x_axis, self.gens)
        plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='x', alpha=0)

        plt.legend()
        plt.show()

    @staticmethod
    def sort_stat(stat: str, csv_file: str):
        # with open(csv_file, 'r') as csv_f:
        #     csv.DictReader()
        pkmn_stat = pd.read_csv(csv_file, index_col=stat)
        sort_by_stat = pkmn_stat.sort_values(stat, ascending=False)
        return sort_by_stat.head(10)


def main():
    csv_file_list: list = os.listdir('../csv_data')
    sp = Charts(csv_file_list)
    # print(sp)
    # sp.show_chart('Speed')
    sorted_stat_df = Charts.sort_stat('Speed', '../csv_data/pkmn_gen9.csv')
    print(sorted_stat_df)


if __name__ == '__main__':
    main()
