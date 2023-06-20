
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu,pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

###################################################
# İş Problemi: Kursun Büyük Çoğunluğunu İzleyenler ile İzlemeyenlerin Puanları Birbirinden Farklı mı?
###################################################

# H0: M1 = M2 (Kursun Büyük Çoğunluğunu İzleyenler ile İzlemeyenlerin Puanlarının Ortalamaları Arasında İstatistiki Olarak Anlamlı Farklılık Yoktur.)
# H1: M1 != M2 (Kursun Büyük Çoğunluğunu İzleyenler ile İzlemeyenlerin Puanlarının Ortalamaları Arasında İstatistiki Olarak Anlamlı Farklılık Vardır.)

df = pd.read_csv("datasets/course_reviews.csv")
df.head()

df[(df["Progress"] > 75)]["Rating"].mean()

df[(df["Progress"] < 25)]["Rating"].mean()


test_stat, pvalue = shapiro(df[(df["Progress"] > 75)]["Rating"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


test_stat, pvalue = shapiro(df[(df["Progress"] < 25)]["Rating"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-değeri 0,05'ten küçük olduğu için H0 hipotezi reddedilir.
# Normallik varsayımı sağlanmamaktadır.

# Normallik varsayımı sağlanmadığı için non-parametrik test uygulanır. mannwhitneyu testi uygulanır.
# Normallik varsayımı sağlanmadığı için varyans homojenliği testini yapmamıza gerek yoktur.

test_stat, pvalue = mannwhitneyu(df[(df["Progress"] > 75)]["Rating"],
                                 df[(df["Progress"] < 25)]["Rating"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 hipotezi reddedilir.
# Dersin Çoğunluğunu Takip Edenler ile Etmeyenlerin Puan Ortalamaları Arasında İstatistiksel Olarak Anlamlı Bir Fark Vardır