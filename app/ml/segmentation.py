from sklearn.cluster import KMeans
import pandas as pd


def segment_customers(customers):

    data = pd.DataFrame(customers)

    model = KMeans(
        n_clusters=3,
        random_state=42
    )

    data["cluster"] = model.fit_predict(
        data[["age"]]
    )

    return data.to_dict(orient="records")