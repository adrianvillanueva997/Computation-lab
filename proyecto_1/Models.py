from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import learning_curve
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
import graphviz
import sklearn.tree as tree


class Models:
    """
    Class that will have all the Machine Learning models that the application will use
    """

    def __init__(self, x_train, y_train, x_test, y_test):
        """
        Class Constructor
        """
        self.__model = None
        self.__x_train = x_train
        self.__x_test = x_test
        self.__y_train = y_train
        self.__y_test = y_test

    def naive_bayes_multinomial(self, alpha=1.0, fit_prior=True):
        """
        Multinomial naive bayes model from sklearn
        :param alpha:
        :param fit_prior:
        :return: probability, conf_matrix
        """
        model = MultinomialNB(alpha=alpha, fit_prior=fit_prior)
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def naive_bayes_bernouilli(self, ):
        model = BernoulliNB()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def naive_bayes_gaussian(self):
        model = GaussianNB()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def tree_decision(self):
        model = DecisionTreeClassifier()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def gradient_booster(self):
        model = GradientBoostingClassifier()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def gradient_stochastic_descent(self):
        model = SGDClassifier()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def k_neighbors_classifier(self):
        model = KNeighborsClassifier()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def r_neighbors_classifier(self):
        model = RadiusNeighborsClassifier()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def svm_support_vector_classification(self, C=1.0, kernel='rbf', degree=3, gamma='auto'):
        model = SVC(C=C, kernel=kernel, degree=degree, gamma=gamma)
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def svm_support_vector_nu_classification(self):
        model = NuSVC()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def svm_support_vector_linear_classification(self):
        model = LinearSVC()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def gaussian_process_classifier(self):
        model = GaussianProcessClassifier()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def sklearn_neural_mlp(self):
        model = MLPClassifier()
        model.fit(self.__x_train, self.__y_train)
        self.__model = model
        probability, conf_matrix = self.__generate_prediction()
        return probability, conf_matrix

    def __generate_prediction(self):
        """
        Method that generates the prediction value and confussion matrix
        :return:
        """
        prediction = self.__model.predict(self.__x_test)
        probability = np.mean(prediction == self.__y_test)
        conf_matrix = confusion_matrix(self.__y_test, prediction)
        return probability, conf_matrix

    def __generate_tree_graph(self):
        dot_data = tree.export_graphviz(self.__model, out_file=None, filled=True, rounded=True, special_characters=True)
        graph = graphviz.Source(dot_data)
        return graph

    def generate_plot_learning_curve(self, title, X, y, ylim=None, cv=None, n_jobs=None,
                                     train_sizes=np.linspace(.1, 1.0, 5)):
        """
        Generate a simple plot of the test and training learning curve.

        Parameters
        ----------

        title : string
            Title for the chart.

        X : array-like, shape (n_samples, n_features)
            Training vector, where n_samples is the number of samples and
            n_features is the number of features.

        y : array-like, shape (n_samples) or (n_samples, n_features), optional
            Target relative to X for classification or regression;
            None for unsupervised learning.

        ylim : tuple, shape (ymin, ymax), optional
            Defines minimum and maximum yvalues plotted.

        cv : int, cross-validation generator or an iterable, optional
            Determines the cross-validation splitting strategy.
            Possible inputs for cv are:
              - None, to use the default 3-fold cross-validation,
              - integer, to specify the number of folds.
              - :term:`CV splitter`,
              - An iterable yielding (train, test) splits as arrays of indices.

            For integer/None inputs, if ``y`` is binary or multiclass,
            :class:`StratifiedKFold` used. If the estimator is not a classifier
            or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

            Refer :ref:`User Guide <cross_validation>` for the various
            cross-validators that can be used here.

        n_jobs : int or None, optional (default=None)
            Number of jobs to run in parallel.
            ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
            ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
            for more details.

        train_sizes : array-like, shape (n_ticks,), dtype float or int
            Relative or absolute numbers of training examples that will be used to
            generate the learning curve. If the dtype is float, it is regarded as a
            fraction of the maximum size of the training set (that is determined
            by the selected validation method), i.e. it has to be within (0, 1].
            Otherwise it is interpreted as absolute sizes of the training sets.
            Note that for classification the number of samples usually have to
            be big enough to contain at least one sample from each class.
            (default: np.linspace(0.1, 1.0, 5))
        """
        plt.figure()
        plt.title(title)
        if ylim is not None:
            plt.ylim(*ylim)
        plt.xlabel("Training examples")
        plt.ylabel("Score")
        train_sizes, train_scores, test_scores = learning_curve(
            self.__model, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
        train_scores_mean = np.mean(train_scores, axis=1)
        train_scores_std = np.std(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)
        plt.grid()

        plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1, color="g")
        plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Cross-validation score")

        plt.legend(loc="best")
        return plt
