# Project title: Dreams Degree Recommender

**Description**

	• Our model uses the descriptions of the study programs from the UDE. Using those data, our model can recommend 
	study programs based on a user input text. Gensim, TF-IDF sum up, and SVM are the three methods we use to make the predictions. 
	• Since those methods have different emphases, the user can choose from the recommendations (of the method) that fit him best.
	
# Project Architecture
### Components:
The tool was created by using HTML/CSS/JS with the vue.js framework.

	├── index.html
	├── main.js
	├── AllData.json
	├── App.vue
	├── components
	│   ├── About.vue
	│   ├── AddCourse.vue
	│   ├── Conflicts.vue   *To get the conflicts in course time
	│   ├── HomePage.vue
	│   ├── HorizontalBarChart.vue   *To generate a bar chart
	│   ├── PieChart.vue   *To generate a pie chart
	│   ├── SemesterCourses.vue
	│   ├── StackedBarChart.vue   *To generate a stacked bar chart
	│   └── TimeTable.vue   *To generate the final timetable
	└── README.md

* The charts were generated using chart.js and vue-chartjs libraries.
* To generate the final table, we have used vue-cal library, this library provides calendar table.
* It is a web application that was built using javascript without a backend.
* All data that we used in the project comes from the file AllData.json that is bundled with the website.

# The visualizations

### Bar Chart Top 10/Top 5: shows the recommended study programs (used for Gensim, and TF-IDF sum up)

### Pie Chart: shows the amount of hours for one chosen study program (used for all methods)

### List for Pie Chart: To choose from the study programs that shall be visualized (used for all methods)

### List for Pie Chart: To choose from the study programs that shall be visualized (used for all methods)


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

# Supervised by

* Professor Dr. Mohamed Amine Chatti
* Mouadh Guesmi

# Group Members

* Furkan Erbil
* Ilia Nassif
* Nikul Goyani
* Salman Adjie Wiratama
* Yustinus Aquila Adrian
