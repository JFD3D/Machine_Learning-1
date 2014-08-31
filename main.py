"""lol"""
import datasets
import utils
import models


def main(distribution, count):
    """dnolul"""
    past_days, past_values, fieldnames = datasets.btc_csv_data()

    model = models.linear_regression(past_days, past_values)

    future_days = [[x*distribution+past_days[-1][0]] for x in xrange(count)]
    future_values = model.predict(future_days)

    total_days = past_days + future_days
    total_values = past_values + future_values

    utils.make_graph(total_days, total_values, fieldnames[0], fieldnames[1])

main(1, 200)
