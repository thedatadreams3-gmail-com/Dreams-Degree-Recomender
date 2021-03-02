# Project title: Dreams Degree Recommender

### **Description:**

	• Our model uses the descriptions of the study programs from the UDE. Using those data, our model can recommend 
	study programs based on a user input text. Gensim, TF-IDF sum up, and SVM are the three methods we use to make the predictions. 
	• Since those methods have different emphases, the user can choose from the recommendations (of the method) that fit him best.
	
# Project Architecture
### Components:

### Frontend:

The tool was created by using HTML/CSS/JS with the vue.js framework.

	├── index.html
	├── main.js
	├── degrees_info.json
	├── App.vue
	├── components
	│   ├── About.vue
	│   ├── BarChart.vue   *To generate a bar chart
	│   ├── Documentation.vue
	│   ├── Home.vue       *Sends requests to the backend side and wait for response, after that it shows the recommended degrees
	│   ├── PieChart.vue   *To generate a pie chart
	│   ├── RecomenderCourseList.vue
	│   └── Start.vue
	└── README.md

* The charts were generated using chart.js and vue-chartjs libraries.
* All data that we used in the project comes from the file degrees_info.json that is bundled with the website.

### Backend:

The tool was created using Python with Flask framework.

The used libraries: click, dill, Flask, Flask-Cors, gensim, itsdangerous, Jinja2, joblib, MarkupSafe, nltk, numpy, pandas, python-dateutil, pytz, regex, scikit-learn
scipy, six, smart-open, threadpoolctl, tqdm, Werkzeug

# The visualizations

### Bar Chart Top 10/Top 5: shows the recommended study programs (used for Gensim, and TF-IDF sum up)

![Barchart Top 5](https://user-images.githubusercontent.com/50524579/109694156-c5d97c00-7b8a-11eb-8d64-ad3ee22e8b3f.png)

![Barchart Top 10](https://user-images.githubusercontent.com/50524579/109694192-d25dd480-7b8a-11eb-9aa9-3397f2896979.png)

![Gensim Bar Chart Top 5](https://user-images.githubusercontent.com/50524579/109694215-db4ea600-7b8a-11eb-9cfd-9f46d3c62b3e.png)

![Gensim Bar Chart Top 9](https://user-images.githubusercontent.com/50524579/109694227-dee22d00-7b8a-11eb-9313-a967a570ca31.png)

### Pie Chart: shows the amount of hours for one chosen study program (used for all methods)

![Pie Chart ](https://user-images.githubusercontent.com/50524579/109694268-e7d2fe80-7b8a-11eb-864a-2d85d46d9b4c.png)

### List for Pie Chart: To choose from the study programs that shall be visualized (used for all methods)

![List for Pie Chart](https://user-images.githubusercontent.com/50524579/109694298-f02b3980-7b8a-11eb-9a46-b23970ffb73b.png)

# Steps on running the project

### Frontend:

* Download and install YARN and Node.js
* Clone or download and extract the frontend repository.
* Install the needed libraries by running this command 
```yarn``` 
* To run the project locally for development, run this command
```yarn serve```
* To build the project for deployment, run this command
```yarn build```
* After building the project you will get the website in "dist" folder
* You can upload the files into static filehosting service


### Backend:

* Download and install Python 3
* Clone or download and extract the backend repository.
* Install the needed libraries by running this command 
```pip install -r requirements.txt``` 
* To run the project locally for development, run this command
```python basics.py```

### In order to run the project properly you have to run both Frontend and Backend sides

# Supervised by

* Professor Dr. Mohamed Amine Chatti
* Mouadh Guesmi

# Group Members

* Furkan Erbil
* Ilia Nassif
* Nikul Goyani
* Salman Adjie Wiratama
* Yustinus Aquila Adrian
