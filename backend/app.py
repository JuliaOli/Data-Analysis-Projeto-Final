from flask import Flask, request, jsonify
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.externals import joblib

# declare constants
HOST = '0.0.0.0'
PORT = 8081

# initialize flask application
app = Flask(__name__)


@app.route('/api/train', methods=['POST'])
def train():
    # get parameters from request
    parameters = request.get_json()

    # read iris data set
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # fit model


    # fit the model to training set in order to predict classes
    knn = KNeighborsClassifier(n_neighbors=1,metric_params='C')
    knn.fit(X, y)
    #KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                    #metric_params=None, n_jobs=None, n_neighbors=1, p=2,
                    #weights='uniform')

    # svm
    clf = svm.SVC(C=float(parameters['C']),
                  probability=True,
                  random_state=1)
    clf.fit(X, y)

    # persist model
    #joblib.dump(clf, 'model.pkl')
    
    joblib.dump(knn, 'model.pkl')

    #return jsonify({'accuracy': round(clf.score(X, y) * 100, 2)})
    return jsonify({'accuracy': round(knn.score(X, y)*100, 2)})


@app.route('/api/predict', methods=['POST'])
def predict():
    # get iris object from request
    X = request.get_json()
    X = [[float(X['sepalLength']), float(X['sepalWidth']), float(X['petalLength']), float(X['petalWidth'])]]

    # read model
    #clf = joblib.load('model.pkl')
    knn = joblib.load('model.pkl')
    
    #probabilities = clf.predict_proba(X)
    probabilities = knn.predict_proba(X)

    return jsonify([{'name': 'Iris-Setosa', 'value': round(probabilities[0, 0] * 100, 2)},
                    {'name': 'Iris-Versicolour', 'value': round(probabilities[0, 1] * 100, 2)},
                    {'name': 'Iris-Virginica', 'value': round(probabilities[0, 2] * 100, 2)}])


if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)
