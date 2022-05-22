from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Loading trained ML model and Scaling object from pickle 

model_timeSeries=pickle.load(open('model_arima_fit.pkl','rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')


@app.route("/predict", methods=['POST'])
def predict():
    # Taking input from front end page 
    if request.method == 'POST':
        n_timesteps=int(request.form['n_timesteps'])		
        
        forecasted_data=model_timeSeries.forecast(n_timesteps)[0]     
        forecasted_data_s=[]
        for i in range(0,n_timesteps):
            forecasted_data_s.append(str(round(forecasted_data[i])))
            
        forecasted_data_str=','.join(forecasted_data_s)
			
		
		 
       
        #X=np.array([Company,TypeName,Inches,Ram_GB,OpSys,Weight_kg,Memory1_size_GB,Memory1_type,Memory2_size_GB,Memory2_type,Cpu_Company,Cpu_Type,Cpu_Type_intensity,Cpu_Ghz,Gpu_company,Gpu_type,ScreenType,SRPxlH,SRPxlV]).reshape(1,-1)
        # Predicting target 
          		
        
        return render_template('home.html',prediction_text="Number of ticket may be created next {} time stamps are [{}] respectively".format(n_timesteps,forecasted_data_str))
        
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)