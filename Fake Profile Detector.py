#Used the gender-guesser library to identify gender from the given name
import gender_guesser.detector as gender
from sklearn.externals import joblib
import numpy as np
model = joblib.load('model.obj')
#Added languages with codes with the usual representation of the languages
l_list = list([(0, 'de'),(1, 'en'),(2, 'es'),(3, 'fr'),(4, 'gl'),(5, 'it'),(6, 'nl'),(7, 'tr')])
def return_gender(name):
    predictor = gender.Detector(case_sensitive=False)
    sex = predictor.get_gender(name)
    sex_dict={'female': -2, 'mostly_female': -1,'andy':0,'unknown':0,'mostly_male':1, 'male': 2}
    sex_code = sex_dict.get(sex)
    return sex_code
lang_list = l_list   
lang_dict = { name : i for i, name in lang_list }
def return_lang(lang):
    return lang_dict.get(lang)
#Use the below function to predict
#'name','statuses_count','followers_count','friends_count','favourites_count','listed_count',lang_code'
def predict_new(name,s,f,fr,fav,lis,lang):
    se = return_gender(name)
    lc = return_lang(lang)
    pred = model.predict([[s,f,fr,fav,lis,se,lc]])
    if pred == 1:
        print("fake")
    else:
        print("genuine")

