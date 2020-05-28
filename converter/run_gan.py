import GAN_171103
import importlib
import pandas as pd
import sklearn.cluster as cluster
# importlib.reload(GAN_171103) # For reloading after making changes
from GAN_171103 import *

rand_dim = 17 # 32 # needs to be ~data_dim
base_n_count = 16 # 128

nb_steps = 5 + 1 # 50000 # Add one for logging of the last interval
batch_size = 32 # 64

k_d = 1  # number of critic network updates per adversarial training step
k_g = 1  # number of generator network updates per adversarial training step
critic_pre_train_steps = 10 # 100  # number of steps to pre-train the critic before starting adversarial training
log_interval = 10 # 100  # interval (in steps) at which to log loss summaries and save plots of image samples to disc
learning_rate = 5e-4 # 5e-5
data_dir = 'cache/'
generator_model_path, discriminator_model_path, loss_pickle_path = None, None, None

# show = False
show = True

# Reading data block
# Load engineered dataset from EDA section
# data = pickle.load(open('creditcard.csv','rb'))
data = pd.read_csv('train/training_data.csv')

# data columns will be all other columns except class
data_cols = list(data.columns[ data.columns != 'Class' ])
print("Data cols: ", data_cols)
label_cols = ['Class']

sorted_cols = ["html", "div", "meta", "title", "link", "script", "style", "h1", "h2", "ul", "a", "class", "br", "button", "img", "interaction", "aesthetic", "Class"]
# sorted_cols = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

data = data[ sorted_cols ].copy()
train = data.loc[ data['Class']==1 ].copy()

algorithm = cluster.KMeans
args, kwds = (), {'n_clusters':2, 'random_state':0}
labels = algorithm(*args, **kwds).fit_predict(train[ data_cols ])

fraud_w_classes = train.copy()
fraud_w_classes['Class'] = labels

# train = create_toy_spiral_df(1000)
# train = create_toy_df(n=1000,n_dim=2,n_classes=4,seed=0)
train = fraud_w_classes.copy().reset_index(drop=True) # fraud only with labels from classification

# train = pd.get_dummies(train, columns=['Class'], prefix='Class', drop_first=True)
label_cols = [ i for i in train.columns if 'Class' in i ]
data_cols = [ i for i in train.columns if i not in label_cols ]
train[ data_cols ] = train[ data_cols ] / 10 # scale to random noise size, one less thing to learn
train_no_label = train[ data_cols ]


# Training the vanilla GAN and CGAN architectures

k_d = 1  # number of critic network updates per adversarial training step
learning_rate = 5e-4 # 5e-5
arguments = [rand_dim, nb_steps, batch_size,
             k_d, k_g, critic_pre_train_steps, log_interval, learning_rate, base_n_count,
            data_dir, generator_model_path, discriminator_model_path, loss_pickle_path, show ]

adversarial_training_GAN(arguments, train_no_label, data_cols ) # GAN
adversarial_training_GAN(arguments, train, data_cols=data_cols, label_cols=label_cols ) # CGAN
