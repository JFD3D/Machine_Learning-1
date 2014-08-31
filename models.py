"""models for sklearn"""
import sklearn.svm
import sklearn.linear_model


class ModelWrapper(object):
    """generic predictor wrapper"""
    def __init__(self, model):
        self.model = model

    def predict(self, future_days):
        """predicintg"""
        future_values = []
        print "--==Predicting==--"
        for day in future_days:
            future_values.append(self.model.predict(day))
            print "Day: %s Value: %s" % (day, future_values[-1])
        return future_values


def svc(source, target):
    """gets svc model"""
    model = sklearn.svm.SVC()
    model.fit(source, target)
    model_wrapper = ModelWrapper(model)
    return model_wrapper


def linear_regression(source, target):
    """gets linear regression model"""
    model = sklearn.linear_model.LinearRegression()
    model.fit(source, target)
    model_wrapper = ModelWrapper(model)
    return model_wrapper
