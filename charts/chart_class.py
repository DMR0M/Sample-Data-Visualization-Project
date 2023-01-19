import matplotlib.pyplot as plt
import pandas as pd
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
            speed_sum = df[stat_key].sum()
            stats.append(speed_sum)

        # Set window title for chart window
        fig = plt.figure('Pokemon Generations Stat Comparison')
        fig.set_figwidth(15)
        fig.set_figheight(7.5)

        # Create horizontal bar chart
        plt.barh(self.gens, stats, color=bar_color, alpha=0.7)

        # Display values per generation
        for idx, val in enumerate(stats):
            plt.text(val + 1, idx + .25, f'  {str(val)}', color=line_color)

        plt.title(f'All Pokemon Generations {stat_key} Comparison')
        plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='x', alpha=0.7)
        plt.show()


def main():
    csv_file_list: list = os.listdir('../csv_data')
    sp = Charts(csv_file_list)
    print(sp)
    # sp.show_chart('Speed')


if __name__ == '__main__':
    main()
