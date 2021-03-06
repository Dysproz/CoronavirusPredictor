from callbacks.callbacks import CovidEstimator
if __name__ == '__main__':
    c = CovidEstimator()
    c.load_data("https://raw.githubusercontent.com/dtandev/coronavirus/master/data/CoronavirusPL%20-%20General.csv", web=True)
    from datetime import datetime
    hmin = datetime(2020, 5, 20)
    hmax = datetime(2020, 6, 20)
    c.set_predict_horizon(hmin, hmax)
    c.train_AR()
    c.predict()
    c.plt()