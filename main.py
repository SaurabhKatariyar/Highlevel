from pyspark.sql import SparkSession
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.ml.linalg import Vector
from pyspark.ml.feature import (Tokenizer, StopWordsRemover, CountVectorizer, IDF, HashingTF,
                                VectorAssembler, VarianceThresholdSelector, PCA)
from pyspark.ml.regression import RandomForestRegressor, GBTRegressor, LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder
from pyspark.ml import Pipeline
from typing import List
from pandas import DataFrame, read_csv
from numpy import float64
import mlflow
from time import time


def load_data(path: str) -> DataFrame:
    """
    Python Function to load data from csv
    :param path: file path
    :return: pandas DataFrame
    """
    return read_csv(path)


def text2list(txt: [str, float64]) -> List:
    """
    Function to get the extract authors or categories per book as list
    Input:
        txt: string value or NaN in case missing entry, e.g. "['a', 'b']"
    Output:
        ["a", "b"] if str
        [] in case of missing float
    Had to return blank list because spark wasn't able to load mixed type e.g. LongType and ArrayType entries
    """
    if isinstance(txt, str):
        return eval(txt)
    else:
        return []


def freq_trimmer(df: DataFrame, field: str, threshold: int) -> DataFrame:
    # Calculate frequencies
    frequency = df[field].value_counts()

    # Group rare categories into 'Other'
    df[field] = df[field].apply(lambda x: x if frequency[x] > threshold else 'Other')

    return df


def data_cleansing(df: DataFrame) -> DataFrame:
    """
    Handles all the cleansing steps identified while EDA
    :param df: Pandas DataFrame    :return:  after applying all the cleanups
    """
    df.dropna(inplace=True)  # Dropping rows with missing entries
    df['authors'] = df['authors'].apply(text2list)
    df['categories'] = df['categories'].apply(text2list)
    df['categories'] = df['categories'].apply(lambda x: x[0])
    df['num_authors'] = df['authors'].apply(lambda x: len(x) if isinstance(x, list) else 0)
    del df['Unnamed: 0']
    del df['publishedDate']
    freq_trimmer(df, 'categories', 20)
    freq_trimmer(df, 'publisher', 20)
    data_type = []
    for col_ in df.columns:
        data_type.append({'Column': col_, 'Datatype': df[col_].dtype,
                          'MissingEntries': df[col_].isnull().sum() / df.shape[0] * 100})
    print(f'Missing Value Report: \n{DataFrame(data_type)}')
    return df


def pandas_to_spark(df: DataFrame) -> SparkDataFrame:
    """
    Converts pandas to spark dataframe
    :param df: pandas dataframe
    :return: spark dataframe
    """
    return spark.createDataFrame(df)


def feature_pipeline(field: str):
    # Feature Engineering Pipeline for Title field
    if field.lower() == 'title':
        tokenizer_title = Tokenizer(inputCol="Title", outputCol="token_title")
        stopremove_title = StopWordsRemover(inputCol='token_title', outputCol='stop_tokens_title')
        count_vec_title = CountVectorizer(inputCol='stop_tokens_title', outputCol='c_vec_title')
        idf_title = IDF(inputCol="c_vec_title", outputCol="tf_idf_title")

        final_feature = VectorAssembler(
            inputCols=['tf_idf_title'],
            outputCol='title_features')

        selector = VarianceThresholdSelector(featuresCol='title_features',
                                             outputCol="selected_title_features", varianceThreshold=10)

        pipe_ = Pipeline(
            stages=[
                tokenizer_title, stopremove_title, count_vec_title, idf_title, final_feature, selector
            ])

    elif field.lower() == 'description':
        # Feature Engineering Pipeline for Description field
        tokenizer_desc = Tokenizer(inputCol="description", outputCol="token_desc")
        stopremove_desc = StopWordsRemover(inputCol='token_desc', outputCol='stop_tokens_desc')
        count_vec_desc = CountVectorizer(inputCol='stop_tokens_desc', outputCol='c_vec_desc')
        idf_desc = IDF(inputCol="c_vec_desc", outputCol="tf_idf_desc")

        final_feature = VectorAssembler(
            inputCols=['tf_idf_desc'],
            outputCol='desc_features')

        selector = VarianceThresholdSelector(featuresCol='desc_features',
                                             outputCol="selected_desc_features", varianceThreshold=10)

        pipe_ = Pipeline(
            stages=[
                tokenizer_desc, stopremove_desc, count_vec_desc, idf_desc, final_feature, selector
            ])

    elif field.lower() == 'authors':
        # Feature Engineering Pipeline for Authors field, since there are multiple authors
        count_vec_authors = CountVectorizer(inputCol='authors', outputCol='c_vec_authors')
        idf_authors = IDF(inputCol="c_vec_authors", outputCol="tf_idf_authors")

        final_feature = VectorAssembler(
            inputCols=['tf_idf_authors'],
            outputCol='authors_features')

        selector = VarianceThresholdSelector(featuresCol='authors_features',
                                             outputCol="selected_author_features", varianceThreshold=10)

        pipe_ = Pipeline(
            stages=[
                count_vec_authors, idf_authors, final_feature, selector
            ])

    elif field.lower() == 'publisher':
        # Feature Engineering Pipeline for Publisher field
        tokenizer_publisher = Tokenizer(inputCol="publisher", outputCol="token_publisher")
        encoded_publisher = HashingTF(inputCol='token_publisher', outputCol='vec_publisher')

        final_feature = VectorAssembler(
            inputCols=['vec_publisher'],
            outputCol='publisher_features')

        selector = VarianceThresholdSelector(featuresCol='publisher_features',
                                             outputCol="selected_publisher_features", varianceThreshold=10)

        pipe_ = Pipeline(
            stages=[
                tokenizer_publisher, encoded_publisher, final_feature, selector
            ])

    elif field.lower() == 'categories':

        # Feature Engineering Pipeline for categories
        tokenizer_cat = Tokenizer(inputCol="categories", outputCol="token_categories")
        encoded_categories = HashingTF(inputCol='token_categories', outputCol='vec_categories')

        final_feature = VectorAssembler(
            inputCols=['vec_categories'],
            outputCol='cat_features')

        selector = VarianceThresholdSelector(featuresCol='cat_features',
                                             outputCol="selected_cat_features", varianceThreshold=10)

        pipe_ = Pipeline(
            stages=[
                tokenizer_cat, encoded_categories, final_feature, selector
            ])

    return pipe_


def data_pipeline(df):
    # for field in ['Title', 'description', 'authors', 'categories', 'publisher']:
    for field in ['authors', 'categories', 'publisher']:
        print(field)
        pipe = feature_pipeline(field=field)
        extractor = pipe.fit(df)
        df = extractor.transform(df)

    # assembler = VectorAssembler(
    #     inputCols=['selected_title_features',  'selected_desc_features', 'selected_author_features',
    #                'selected_publisher_features', 'selected_cat_features', 'num_authors'],
    #     outputCol='features')

    assembler = VectorAssembler(
        inputCols=['selected_author_features', 'selected_publisher_features', 'selected_cat_features', 'num_authors'],
        outputCol='features')

    # pca = PCA(k=250, inputCol='features', outputCol='pca_features')

    pipe_ = Pipeline(stages=[assembler])
    feature = pipe_.fit(df)
    df = feature.transform(df)
    clean_data = df.select(['Impact', 'features'])
    clean_data = clean_data.withColumnRenamed('Impact', 'label')  #.withColumnRenamed(
    # 'pca_features', 'features')
    return clean_data


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    # Reading arguments of what training algorithm to run and number of worker nodes to log in MLFLOW
    parser.add_argument("--workers", help="Number of spark workers.")
    parser.add_argument("--algo", help="ML training algorithm")
    args = parser.parse_args()
    workers = args.workers  # #workers
    if args.algo:
        algo = args.algo  # ML algo
    else:
        algo = "NotSpecified"

    # Setting up experiments in MlFlow
    experiment_name = 'HighLevelBookTask'
    # run name specific to algo and worker node config
    run_name = f'TrainingAlgo{algo}WorkerNode{workers}'

    # csv file path, to be changed as per system
    data_path = '/home/saurabhk/Downloads/books_task.csv'
    pd_df = load_data(path=data_path)
    pd_df = data_cleansing(pd_df)
    spark = SparkSession.builder.appName("TestSpark").master("spark://192.168.1.14:7077").getOrCreate()
    data = pandas_to_spark(pd_df)

    start = time()

    data = data_pipeline(data)

    data_processing_time = time() - start

    print(data.printSchema())

    (training, testing) = data.randomSplit([0.6, 0.4], seed=12345)

    mlflow.set_experiment(experiment_name=experiment_name)

    with mlflow.start_run() as active_run:
        mlflow.set_tag('mlflow.runName', run_name)
        mlflow.log_metric('data_processing_time', data_processing_time)
        params_grid = ParamGridBuilder().build()
        reg = LinearRegression(maxIter=5, loss="squaredError", predictionCol='prediction')

        tvs = TrainValidationSplit(estimator=reg, estimatorParamMaps=params_grid,
                                   evaluator=RegressionEvaluator(metricName='mae'), trainRatio=0.7, seed=425)

        train_start = time()
        model = tvs.fit(training)
        training_time = time() - train_start

        val_scores = model.validationMetrics
        val_score = sum(val_scores) / len(val_scores)
        print(val_scores)

        print('Validation complete.')

        mlflow.log_metric('training_time', training_time)
        mlflow.log_metric('n_workers', workers)
        mlflow.log_metric("validation_metric-MAE", val_score)

        mae = RegressionEvaluator(metricName='mae')
        train_mae = mae.evaluate(training)
        test_mae = mae.evaluate(testing)

        mse = RegressionEvaluator(metricName='mse')
        train_mse = mse.evaluate(training)
        test_mse = mse.evaluate(testing)

        rmse = RegressionEvaluator(metricName='rmse')
        train_rmse = rmse.evaluate(training)
        test_rmse = rmse.evaluate(testing)

        r2 = RegressionEvaluator(metricName='r2')
        train_r2 = r2.evaluate(training)
        test_r2 = r2.evaluate(testing)

        var = RegressionEvaluator(metricName='var')
        train_var = var.evaluate(training)
        test_var = var.evaluate(testing)

        mlflow.log_metric("training_metric-MAE", train_mae)
        mlflow.log_metric("training_metric-MSE", train_mse)
        mlflow.log_metric("training_metric-RMSE", train_rmse)
        mlflow.log_metric("training_metric-R2", train_r2)
        mlflow.log_metric("training_metric-Var", train_var)

        mlflow.log_metric("testing_metric-MAE", test_mae)
        mlflow.log_metric("testing_metric-MSE", test_mse)
        mlflow.log_metric("testing_metric-RMSE", test_rmse)
        mlflow.log_metric("testing_metric-R2", test_r2)
        mlflow.log_metric("testing_metric-Var", test_var)
