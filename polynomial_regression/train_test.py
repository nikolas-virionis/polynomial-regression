from sklearn.model_selection import train_test_split


def split(x, y, split):
    return train_test_split(x, y, test_size=0.25, random_state=0) if split else (x, x, y, y)
