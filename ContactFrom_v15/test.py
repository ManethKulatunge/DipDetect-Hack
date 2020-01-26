import code_nlp as mf

pm = mf.process_message('I am sad and depressed')
print(mf.sc_tf_idf.classify(pm))
