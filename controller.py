from flask_restful import Resource, reqparse
from flask import request 
from text_analize import *
class Controller(Resource):
    def get(self):
        return {"data":"Hello World"}
    def post(self):
        data = str(request.form.get("text"))
        analyze = AnalyzeGrammar()
        err, num_err = analyze.start(data)

        return {
            "data":{
                "num_err": num_err,
                "data": err
                }
            }
        
        # return {
        #     "data":{
        #         "num_error":num_err,
        #         "errors":err
        #         }
        #     }
        


