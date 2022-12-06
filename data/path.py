import os


def get_data_dir():
    data_dir = "/root/laic/data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    return data_dir


def get_train_data_path():
    train_path = os.path.join(get_data_dir(), "train.txt")
    return train_path


def get_eval_data_path():
    eval_path = os.path.join(get_data_dir(), "dev.txt")
    return eval_path


def get_test_data_path():
    test_path = os.path.join(get_data_dir(), "test.txt")
    return