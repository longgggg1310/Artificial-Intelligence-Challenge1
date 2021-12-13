Flask Drawing Recognition Application based on CNN model

![preview](preview.jpg)

<br />


This is source code uses to draw and recognize what picture is. 
## Introduction :
Author       | Email
------------ | -------------
Vu Dang Long | long.vu190404@vnuk.edu.vn
<br />

## Flow Chart of this processing:

![flow](flow.jpg)

<br />

## Making model
In this project, I use data from 'Quick, draw' dataset which is a very popular game where users draw object rely on machine's questions. You can find dataset in [here](https://github.com/googlecreativelab/quickdraw-dataset).
I focus my use case on 3 fruits: grape, pineapple, banana and 1 object is umbrella. Here is a sample of data: 
![classes](classes.png)
<br />


Once everything is ready, let’s build our model using Keras ! This model will have the following structure : <br />
Convolutional Layer : 30 filters, (3 * 3) kernel size <br />
Max Pooling Layer : (2 * 2) pool size <br />
Convolutional Layer : 15 filters, (3 * 3) kernel size <br />
Max Pooling Layer : (2 * 2) pool size <br />
DropOut Layer : Dropping 20% of neurons. <br />
Flatten Layer <br />
Dense/Fully Connected Layer : 128 Neurons, Relu activation function <br />
Dense/Fully Connected Layer : 50 Neurons, Softmax activation function <br />


## Using Flask to complete the Web-App Drawing
### Flask 
Flask is a web micro-framework written in Python. It allows you to design a solid and professional web application.
How does it work ?
Although it doesn’t require a specific architecture, there are some good practice to follow :

app.py : Is the main code that will run our Flask application. It will contain the different routes for our application, respond to HTTP requests and decide what to display in the templates. In our case, it will also call our CNN classifier, operate pre-processing steps for our input data and make prediction.
Templates folder : A template is an HTML file which can receive Python objects and is linked to the Flask application. Hence, our html pages will be stored in this folder.
Saved pictues folder : Image that drawed by users will be saved in this folder to get more data about hand drawing 

## Run the app
The last step is to launch our app! You can go into Darwing App Folder(you can find app.py in there) and use flask run or python app.py
![flask](flask.jpg)

Your app will be running on your local server. By default is 127.0.0.1:5000
![final](final.png)


## Conclusion
That’s it ! In this article, we have seen how to develop a Flask Drawing app that uses a previously built CNN model to classify drawings made by the user.
This is one over many possible uses of Flask to deploy machine learning models. In fact, an infinity of use cases can be found, and I hope this specific project will help you build other ML web-apps to make your code more accessible to others !

<br />

## License
[MIT](https://choosealicense.com/licenses/mit/) <br />
## Author 
VU DANG LONG [@VU DANG LONG](long.vu190404@vnuk.edu.vn).<br />
