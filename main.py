# main file for students marks analysis project
from src.utils import load_data, calculate_average
from src.report import plot_scores

def main()
  filepath = "data/marks.csv"

  #load data 
  df = calculate_average(df)
  print("student data with averages : \n", df)

  # plot scores
  plot_scores(df)

  if__name__=="__main__":
    main()