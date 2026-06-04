def total_production(df):

    return df["Production"].sum()


def total_area(df):

    return df["Area"].sum()


def average_yield(df):

    return df["Yield"].mean()


def total_states(df):

    return df["State"].nunique()


def total_crops(df):

    return df["Crop"].nunique()
