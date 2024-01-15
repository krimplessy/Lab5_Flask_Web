from app import app
from flask import render_template, request
from variables import vec, operation
from calculation import get_angle, sum, vec_mul


@app.route('/', methods=['GET'])
def index():

    if "show" in request.values:
        vec["dimension"] = int(request.values.get("dimension"))
        
    calculation_res = {}
    
    if "calculate" in request.values:
        points_1 = [[0]*vec["dimension"] for i in range(2)]
        points_2 = [[0]*vec["dimension"] for i in range(2)]
        
        for i in range(vec["dimension"] + 1):
            if request.values.get("vec_1_1_" + str(i)):
                points_1[0][i-1] = int(request.values.get("vec_1_1_" + str(i)))
            else:
                points_1[0][i-1] = 0

        for i in range(vec["dimension"] + 1):
            if request.values.get("vec_1_2_" + str(i)):
                points_1[1][i-1] = int(request.values.get("vec_1_2_" + str(i)))
            else:
                points_1[1][i-1] = 0

        for i in range(vec["dimension"] + 1):
            if request.values.get("vec_2_1_" + str(i)):
                points_2[0][i-1] = int(request.values.get("vec_2_1_" + str(i)))
            else:
                points_2[0][i-1] = 0

        for i in range(vec["dimension"] + 1):
            if request.values.get("vec_2_2_" + str(i)):
                points_2[1][i-1] = int(request.values.get("vec_2_2_" + str(i)))
            else:
                points_2[1][i-1] = 0

        vec["points_1"] = points_1
        vec["vec_1"] = [points_1[1][i]-points_1[0][i] for i in range(len(points_1[0]))]

        vec["points_2"] = points_2
        vec["vec_2"] = [points_2[1][i]-points_2[0][i] for i in range(len(points_2[0]))]

        if "0" in request.values.getlist("calculate"):
            calculation_res["angle"] = get_angle(vec["vec_1"], vec["vec_2"])
        if "1" in request.values.getlist("calculate"):
            calculation_res["sum"] = sum(vec["vec_1"], vec["vec_2"])
        if "2" in request.values.getlist("calculate"):
            calculation_res["vec_mul"] = vec_mul(vec["vec_1"], vec["vec_2"])

    if "clear" in request.values:
        vec["vec_1"] = []
        vec["vec_2"] = []   
        vec["points_1"] = []
        vec["points_2"] = []

    return render_template("index.html", 
                           dimension = vec["dimension"],
                           points_1 = vec["points_1"], 
                           points_2 = vec["points_2"],
                           operation = operation, 
                           calculation_res = calculation_res)