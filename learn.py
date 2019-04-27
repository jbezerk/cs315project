# Classifiers
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC 

import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import pandas as pd
import seaborn as sns
from confusion_matrix_pretty_print import pretty_plot_confusion_matrix

sns.set(rc={'figure.figsize':(10,10)})

# ----------------------- Brandon -----------------
def kNearest(X_train,y_train,X_test,y_test):
    
    kN = KNeighborsClassifier(n_neighbors=5,
                              weights='uniform',
                              algorithm='auto',
                              leaf_size=30,
                              p=2,
                              metric='minkowski',
                              metric_params=None,
                              n_jobs=None)
    
    kN.fit(X_train,y_train)
    
    y_pred = kN.predict(X_test)
    
    tn,fp,fn,tp = confusionMatValues(y_test,y_pred)
    
    confusionMatGraph(tn,fp,fn,tp,'./KNearestConfusionMatResults.png')

def KernelSVM(X_train,y_train,X_test,y_test):
    
    ksvm = SVC(C=1.0,
               kernel='rbf',
               degree=3,
               gamma='auto_deprecated',
               coef0=0.0,
               shrinking=True,
               probability=False,
               tol=0.001,
               cache_size=200,
               class_weight=None,
               verbose=False,
               max_iter=-1,
               decision_function_shape='ovr',
               random_state=None)
    
    ksvm.fit(X_train,y_train)
    
    y_pred =  ksvm.predict(X_test)
    
    tn,fp,fn,tp = confusionMatValues(y_test,y_pred)
    
    confusionMatGraph(tn,fp,fn,tp,'./KernelSVMConfusionMatResults.png')

# -------------------------------------------------


# ---------------------- Jovan --------------------
def testDecisionTree(X_train,y_train,X_test,y_test):

    # Using default hyperparameter values
    # just putting them all here to easily change them later
    dt = DecisionTreeClassifier(criterion='gini',
                                splitter='best',
                                max_depth=None,
                                min_samples_split=2,
                                min_samples_leaf=1,
                                min_weight_fraction_leaf=0.0,
                                max_features=None,
                                random_state=None,
                                max_leaf_nodes=None,
                                min_impurity_decrease=0.0,
                                min_impurity_split=None,
                                class_weight=None,
                                presort=False)

    dt.fit(X_train,y_train)

    y_pred = dt.predict(X_test)

    tn,fp,fn,tp = confusionMatValues(y_test,y_pred)

    confusionMatGraph(tn,fp,fn,tp,'./decisionTreeConfusionMatResults.png')

def testNeuralNetwork(X_train,y_train,X_test,y_test):

    # Using default hyperparameter values
    # just putting them all here to easily change them later
    nn = MLPClassifier(hidden_layer_sizes=(100, ),
                       activation='relu',
                       solver='adam',
                       alpha=0.0001,
                       batch_size='auto',
                       learning_rate='constant',
                       learning_rate_init=0.001,
                       power_t=0.5,
                       max_iter=200,
                       shuffle=True,
                       random_state=None,
                       tol=0.0001,
                       verbose=False,
                       warm_start=False,
                       momentum=0.9,
                       nesterovs_momentum=True,
                       early_stopping=False,
                       validation_fraction=0.1,
                       beta_1=0.9,
                       beta_2=0.999,
                       epsilon=1e-08,
                       n_iter_no_change=10)

    nn.fit(X_train,y_train)

    y_pred = nn.predict(y_test)

    tn,fp,fn,tp = confusionMatValues(y_test,y_pred)

    confusionMatGraph(tn,fp,fn,tp,'./neuralNetworkConfusionMatResults.png')

# -------------------------------------------------


#-------------------Utility Functions-----------------

def loadDF(filename='creditcard.csv'):
    return pd.read_csv(filename)


def makeScatterMat(data):

    attri = ['Time','V1','V2','V3',
             'V4','V5','V6','V7',
             'V8','V9','V10','V11',
             'V12','V13','V14','V15',
             'V16','V17','V18','V19',
             'V20','V21','V22','V23',
             'V24','V25','V26','V27',
             'V28','Amount','Class']

    scatter_matrix(data[attri],figsize=(30,20))

    plt.savefig('./scatter_mat.png')


def makeFeatureHistPlot(data):

    creditcard.hist(bins=50, figsize=(30,20),ylabelsize=5,xlabelsize=5,rwidth=5)

    plt.savefig('./featurehistplot.png')

    plt.show()

    return creditcard


def makeCorrelationHeatMap(data):

    cor = data.corr()

    # plot the heatmap
    htMap = sns.heatmap(cor,
        xticklabels=cor.columns,
        yticklabels=cor.columns,vmin=-1, vmax=1).set_title('Credit Card Correlation Heat Map')
    fig = htMap.get_figure()
    fig.savefig("./CorrHeatMap.png")



def confusionMatValues(y_true,y_pred):

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

    return tn,fp,fn,tp


def makePearsonCorrMat(X):

    return np.corrcoef(X)

def getImportantFeats(data):

    feats = ['Time','V1','V2','V3',
             'V4','V5','V6','V7',
             'V8','V9','V10','V11',
             'V12','V13','V14','V15',
             'V16','V17','V18','V19',
             'V20','V21','V22','V23',
             'V24','V25','V26','V27',
             'V28','Amount']

    dt = DecisionTreeClassifier()

    dt.fit(data[feats],data['Class'])

    N = 30
    ind = np.arange(N)
    width = 0.60

    plt.figure(figsize=(18, 10))
    plt.bar(ind, dt.feature_importances_, width)

    plt.ylabel('Gini Score')
    plt.title('Feature Importance')
    plt.xticks(ind,feats)

    plt.savefig('./featureImportance.png')
    plt.show()

def confusionMatGraph(tn,fp,fn,tp,filepath):

    array = np.array( [[tp, fn],
                       [fp, tn]])

    df_cm = pd.DataFrame(array, index=['fraud','non-fraud'], columns=['fraud','non-fraud'])

    cmap = 'PuRd'
    pretty_plot_confusion_matrix(df_cm, cmap=cmap,filepath=filepath)

# ------------------ Run program ------------------------------------
if __name__ == '__main__':
    creditcard = loadDF()
    # makeScatterMat(creditcard)
    # makeCorrelationHeatMap(creditcard)
    # makeFeatureHistPlot(creditcard)
    # makeCorrelationMat()
    # makeConfusionMat()
    # getImportantFeats(creditcard)
    # confusionMatGraph(50,10,5,100)