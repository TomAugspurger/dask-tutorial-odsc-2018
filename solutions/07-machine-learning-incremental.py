sgd = sklearn.linear_model.SGDClassifier(random_state=0)
inc = dask_ml.wrappers.Incremental(sgd)
inc.fit(X_train, y_train, classes=[0, 1])
