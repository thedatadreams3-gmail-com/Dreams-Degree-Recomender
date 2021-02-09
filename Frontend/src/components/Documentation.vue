<template>
    <div class="allPad">
        <h2  class="heading_1">Introduction About The Dream Degree Recomender</h2>
        <h3>
            <ul>
                <li>
                    <p> 
                        More often than not, students that are about to <span>graduate highschool are still undecided about which university degree </span> want to enroll in. 
                        Most will ask their <span>senior peers for advice, gathering information about </span> what their peers are studying and skills that are required for the degree. 
                        Some might even follow their <span> 'parents' footsteps for their career </span> others will look for degrees that have <span>a high employability rate</span>.
                    </p>
                </li>

                <li>
                    <p> 
                        Through the information they gathered, <span>students will be more likely to find out what they want to study</span> but are yet <span>still undecided to choose a degree</span>. 
                        This is probably due to some subjects may overlap in several degrees and are <span> quite difficult to distinguish without any other information about</span>.
                    </p>
                </li>   

                <li>
                    <p> 
                        <span>Our goal is to actually provide aspiring students, a recommendation of several degrees that they might want to check out further</span>. 
                        This is also backed by insights that allows them to <span>better understand the degree being recommended, further establishing the difference between similar degrees</span>.
                    </p>
                </li>
            </ul>   
        </h3>

        <h2 class="heading_1"> Task Description  </h2>
        <h3>
            <ul>
                <li>
                    <p>
                    <span>Recommend degree by analysing description</span> that is given by user. The user, a person interested in pursuing a degree, provides a description of their interest and their positive experience.
                    </p>
                </li>
            </ul>
        </h3>

        <h2 class="heading_1"> Natural Language Processing Basics  </h2>
            <h3>
                <ul>
                    <li>
                        <p>
                        Natural Language Processing tries to bridge the interaction-gap between the <span>human language and computers</span>. 
                        It is a field that covers a little <span>bit of linguistics, computer science and artificial intelligence</span>. 
                        <span>To put it bluntly:</span> it helps computers understand us and interact with us by <span>communicating whether verbally or written</span> in the language that we know.
                        </p>
                    </li>

                    <li>
                        <p>
                        <span>Consider the situation:</span> You are trying to send a message to your love-interest. 
                        You are horrible at <span>writing and you do not trust your friend </span>because they are hopeless as well. 
                        Let us say you want to know if your <span>letter is cheesy or not</span>. 
                        Maybe you want to make it more elegant. Perhaps you just want to know if the letter you <span>wrote will note be considered sexual harassment</span>.
                        </p>
                    </li>

                    <li>
                        <p>
                        With the help of the <span>NLP system</span>, the system will let you know whether your <span>letter is cheesy, elegant or a potential evidence for the police</span>. 
                        They do this by learning our language. It learns what makes a <span>sentence cheesy and finds out what words</span> that make it so. 
                        It comprehends the <span>body of texts and predicts the sentiment of the text (negative or positive)</span>. 
                        It can also help <span>recommend synonyms that make your letter just better</span>.
                        </p>
                    </li>

                    <li>
                        <p>
                        So <span>how do they do it?</span> It all starts with a <span>body of text</span>. 
                        This body of text is then <span>processed to be something more manageable for the computer</span>. 
                        Of course, something more <span>manageable are numbers for the computer</span>. 
                        Interestingly, what makes <span> NLP different from other ML projects is this quantification of texts</span>. 
                        With this representation, <span>Machine Learning methods</span> or <span>even special NLP method</span> can then be applied to create a <span>model for the NLP systems</span>.
                        
                        </p>
                    </li>
                </ul>
            </h3>
        <h2 class="heading_1"> Our Data  </h2>
        <h3>
            <ul>
                <li>
                    <p>
                    For this task, we created our <span>own data by scraping the University of Duisburg-Essen’s website</span>. It provides a description of each course within each degree.
                    </p>
                </li>
                <span>
                    <img style="width: 60%; margin-left: 20%" src="../assets/images/ourData.jpg" alt="We_Create_own_DataFromUniDue" />
                </span>

                <li>
                    <p>
                    The raw data contains 3 columns: <span>Study Program, Courses and Description</span>. 
                    For the entirety of this project, we will be using <span>this data i.e. manipulating it, cleaning it and even training our model it</span>.
                    </p>
                </li>
            </ul>
        </h3>

        <h2 class="heading_1"> Data Cleaning  </h2>
        <h3>
            <ul>
                <li>
                    <p>
                    As in <span>NLP methodology</span>, we have acquired the corpus that we want to use. The said corpus is the description we have.
                    </p>
                </li>
                <li>
                    <p>
                    Before being fed to the algorithms <span>we worked on preprocessing the data</span>.
                    </p>
                </li>
                <li>
                    <p>
                    First we change some of the values in the column <span>‘Study Program’ </span> contains the degrees. 
                    In the raw data, we found out that there is some<span> old syllabus that is scrapped by our script</span>. 
                    In order to have a <span> better description of the degree </span> we replaced the values that contains the old syllabus.
                    </p>
                </li>
                <li>
                    <p>
                        The <span>second part of the preprocessing is cleaning the data</span>. We cleaned the <span>corpus by removing punctuations</span>, <span>changing all letters to small letters</span>, <span>removing special symbols</span> and <span>lastly removing any stop words</span>. 
                        The cleaning phase uses a mixture of <span>the re library and nltk library</span>. 
                        <span>The re library provides functions for regular expressions and the nltk library provides tokenizing functions and gives us the list of stop words</span>.
                    </p>
                    
                </li>
                <li>
                    <p>
                        Although tokenizing is used in the cleaning, the output of <span>the process gives us back a ‘clean’ corpus</span>.
                    </p>
                    
                </li>
                <li>
                    <p>
                        To have cleaner data <span>(i.e. better machine learning model)</span>, we extended the <span>list of stop words</span>. 
                        Extending the stop words means that we have to <span>select words that we think that are not important for all the available degrees</span>. 
                        <span>The selection is done manually by picking words that might not contribute to the Recommendation</span>.
                    </p>
                </li>
                <li> 
                    <p>
                        The words that are used to extend the <span>list of stop words are the words</span> that come up frequently but having <span>no meaning towards the degree</span>. 
                    Those words are selected manually and are discussed by the team. This process (hopefully) ensures that we have <span>all the words that are important for each degree</span>.
                    </p>
                </li>
                <li>
                    <p>
                        After all of this is done, the output is <span>two csv files</span> that are ready to be fed into our <span>machine learning processes</span>.
                    </p>
                </li>

                <li>
                    <p>
                <ul> <span>The two output are</span> :-
                    <ol>
                        <li>
                            <span>Cleaned_data.csv: </span> this contains the same amount of rows as the original data but <span>renamed and cleaned</span>.
                        </li>
                        <li>
                            <span>Cleaned_data_grouped.csv: </span> this contains original data but renamed, cleaned and grouped according to their degree. 
                            The number of <span>rows correspond to the amount of the (latest) degree</span> that the <span>University of Duisburg-Essen</span> is providing.  
                            In this part, <span>we also deleted the column ‘Courses’</span> to make the column <span>‘Study Program’</span> the only label that we will be working with, as <span> would like to recommend degrees and not courses</span>.
                        </li>
                    </ol> 
                </ul>
                </p>
                <span>
                    <img style="width: 60%; margin-left:20%" src="../assets/images/DataCleaning.jpg" alt="Data_Cleaning_Process"  />
                </span>
                </li>

            </ul>
        </h3>


        <h2 class="heading_1">Data Distribution and Analysis</h2>
        <h3>
            <ul>
                <li>
                    <p>
                    Below are graph that shows the <span>distribution of the unique 24 degrees</span>.
                    </p>
                </li>
                <span>
                    <a href="https://prnt.sc/yotzb8" target="_blank" >
                        <img style="width: 120%; margin-right:10%" src="../assets/images/Data Distribution.png" alt="Data Distribution and Analysis"  />
                    </a> 
                </span>


                <li>
                    <p>
                    As you can see from the distribution, there are degrees that <span>hold more description than others</span>. 
                    <span>Pay attention to the mechanical engineering degrees and the specializations</span>. 
                    It has more descriptions than other degrees. 
                    As for the <span> Applied Cognitive and Media Science</span>, it has the least <span>amount of description</span>.
                    </p>
                </li>

                <li>
                    <p>
                    <span>In the context of our project and the nature of how we use our data, this could lead to biases</span>. 
                    <span>Degrees with more description could hold a higher amount of keywords compared to degrees that have less description</span>. 
                    Those keywords are crucial for our <span>methods in order to recommend degrees</span>.
                    </p>
                </li>

                <li>
                    <p>
                    For anyone interested in picking up a project similar as this, <span>we recommend having an evenly distributed description for each degree</span>.
                    </p>
                </li>
            </ul>
        </h3>


        <h2 class="heading_1"> Method Used</h2>
        <h3>
            <ul>
                <li>
                    <p>
                    The methods used in our project are methods that are <span>very familiar in other NLP projects</span>.
                    </p>
                </li>
            </ul>
        </h3>

        <h2 class="heading_1"> Summed TF-IDF scores</h2>
        <h3>
            <ul>
                <li>
                    <p>
                    In this method, make use of the <span>TF-IDF approach</span>. 
                    For each course, we generated the <span>TF-IDF scores</span> for each meaningful from <span>our bag of words (all course descriptions)</span>.
                    From the user text, we <span>filter out meaningful words (keywords) and though</span>, we collect for each course only these <span>TF-IDF values of the keywords that match the keywords from the user text</span>.
                    </p>
                </li>

                <li>
                    <p><span>The idea behind the recommendation:- </span></p>
                    <p>
                    We <span>sum up all TF-IDF values (sum up results) for each course</span>. This way, we can determine <span>significant courses regarding the user text</span>.
                    </p>
                </li>

                <li>
                    <p>
                    A study program includes a <span>variety of courses</span>. 
                    That is why we collect for <span>each study program the sum up results of each course it contains</span>, and these are <span>summed up again (final results)</span>.
                    The study program with the highest final result is <span>recommended since it contains (most of) the significant courses</span>.
                    </p>
                </li>
            </ul>
        </h3>

        <h2 class="heading_1"> TF-IDF and SVM</h2>
        <h3>
            <ul>
                <li>
                    <p>
                    This method uses completely <span>Machine Learning Technique</span> that is well known. With the <span>TF-IDF that is generated</span>, each course is represented by a vector. 
                    The length of the <span>vector is the length of the bag of words</span>.
                    The value of the vector of each course will be determined by <span>the TF-IDF scores</span>.
                    </p>
                </li>

                <li>
                    <p>
                    Since we are dealing with vectors and our task description can be understood as <span>a classification problem</span>, the generated vectors are then <span>fed to a SVM (Support Vector Machine) to train</span>.
                    The label for each course will be the <span>Degrees</span>.
                    </p>
                </li>

                <li>
                    <p>
                    When an input corpus is provided it will be <span>cleaned and fed to the trained SVM</span>. The SVM will then <span>classify the input and output a single degree</span>. 
                    The degree that the input is classified as will be the <span>recommendation for the user</span>.
                    </p>
                </li>

                <li>
                    <p>
                    However, to recommend several similar other degrees, we use the <span>very same TF-IDF vectors</span> and <span>fed it to a K-mean cluster</span>. 
                    The model will then <span>cluster the degrees</span> that are found to have <span>similarities depending on the importance of a word for each degree</span>.
                    </p>
                </li>

                <li>
                    <p>
                    To sum up, this method combines <span>classification and clustering techniques</span>. 
                    The input corpus will be <span>classified by the model and based</span> on the <span>classification, recommends other degrees</span> that is based on the <span>cluster of the classified degree</span>.
                    </p>
                </li>
                
            </ul>
        </h3>

        <h2 class="heading_1"> TF-IDF Intermediate Explanation </h2>
        <h3>
            <ul>
                <li>
                <span>
                    <img style="width: 60%; margin-left: 20%;" src="../assets/images/TF-IDF_Approach_Intermediate_Explanation.png" alt="TF-IDF_Approach_Intermediate_Explanation" />
                </span>
                </li>

                
            </ul>
        </h3>


        <h2 class="heading_1"> Word Embedding </h2>
        <h3>
            <ul>
                <li>
                    <p>
                        The <span>word embedding method</span> is trying to map the <span>words or phrases</span> into <span>multi dimensional vector</span>. 
                        The <span>dimension of vectors</span> that are being used in <span>SVM and K-Means Clustering is the features(bag of words)</span> while <span>word embedding use multidimensional vectors </span>as assigned area space. 
                    </p>
                </li>


                <li>
                    <p> 
                        This also implies that word embedding has an advantage that it can <span>preserve the semantics</span>, and can search the <span>word or phrases that are similar or different with each other</span>. 
                        This happens because similar words will point into similar areas in the <span>multi dimensional vector space</span>.
                    </p>
                </li>
                <span>
                    <img style="width: 60%; margin-left: 20%;" src="../assets/images/worldVectors.jpg"  alt="WordEmbedding_World_Vectors"/>
                    <h5><span>Picture source:</span> <a href="https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors" target="_blank">WordEmbedding_World_Vectors</a></h5>
                </span>
                
            </ul>
        </h3>
        <h2 class="heading_1">Example</h2>
                <h3>
                    <ul>
                        <li>
                            <p>
                                For the sake of example our course description has a word of:<br>
                                <span> [physic, mathematics, logic , thermodynamics, optics, programming, circuit] </span>
                            </p>
                        </li>

                        <li>
                            <p>
                                It depends on the each <span>document of courses</span> but it might look like this
                            </p>
                        </li>

                        <li>
                            <p>
                                tfidf vectorizer: <span>[0.69, 1.25 , 0.34, 0, 0, 0, 0]</span>
                            </p>
                        </li>

                        <li>
                            <p>
                                Word embedding vector with <span>150 multidimensional space:</span>
                            </p>
                        </li>
                        <span>
                            <img style="width: 60%; margin-left: 20%;" src="../assets/images/tfidf_arrayVlaue.jpg"  alt="tfidf_array_Vlaue."/>
                        </span>
                        
                        <li>
                            <p>
                                We can see that there is <span>zero value (sparse matrix) on the tf-idf vector</span>. 
                                That is because sometimes documents do not have <span>particular words</span>. 
                                Notice that in <span>word embedding it has minus value and positive values?</span> <span>Positive values implies that the phrase or words is heading toward that specific vector space area</span>. 
                                On the other hand, <span>minus values means that phrase or words is evading that specific vector space area</span>.
                            </p>
                        </li>

                    </ul>
                </h3>



        <h2 class="aboutAs">About us:</h2>
        <h3 class="">We are:
            <ol>
                <li> Ilia Nassif  (Degree:- M.Sc. Computer Engineering (Interactive Systems and Visualization PO 15) Student)</li>
                <li> Nikulkumar Goyani (Degree:- M.Sc. Computer Engineering (Intelligent Networked Systems PO 15) Student)</li>
                <li> Furkan Erbil (Degree:- M.Sc. Angewandte Informatik (Medieninformatik PO 19) Student )</li>
                <li> Salman Adjie Wiratama (Degree:- M.Sc. Computer Engineering (Intelligent Networked Systems PO 19) Student)</li>
                <li> Yustinus Aquila Adrian (Degree:- M.Sc. Computer Engineering (Intelligent Networked Systems PO 19) Student)</li>
            </ol> 
            We created this tool as a part of the Learning Analytics (LA) under the guidance of:
            <p class=""> 
                <ol>
                    <li><a href="https://www.uni-due.de/soco/people/mohamed-chatti.php" target="_blank"> Prof. Dr. Mohamed Amine Chatti </a></li>   
                    <li><a href="https://www.uni-due.de/soco/people/mouadh-guesmi.php" target="_blank"> Mr.Mouadh Guesmi </a></li>
                </ol>
            </p>
        </h3>
        <br>
        <h2 class="heading_1"><a href="https://www.uni-due.de/soco/teaching/courses/lecture-la-ws21.php" target="_blank">About Learning Analytics (LA):</a></h2>
        <h3 style="text-align:center">
        <p style="margin: auto; width: 50%; border: 3px solid green; padding: 10px;"> 
        Learning Analytics (LA) has attracted a great deal of attention as practitioners, institutions, and researchers are increasingly seeing the potential that LA has to shape the future technology-enhanced learning landscape. LA is an emerging data science field that represents the application of big data and analytics in education. It deals with the development of methods that harness educational data sets to support the learning process. LA is an interdisciplinary field involving competences from computer science, cognitive psychology, and pedagogy.
        </p>
        </h3>
    </div>
</template>

<script>
</script>
