# Smart Food Classifier

1. Train a model using [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com)
2. We had trained with images of Vegetables, Fruits, Snacks and Drinks
3. Train the Model
4. Download the Model
5. The downloaded model is placed in static/my_model directory
6. Install python on your machine
7. Run command to enable virtual environment
````
python -m venv venv
````
8. If you are using windows, run this command to activate virtual environment
````
source ./venv/Scripts/activate
````
9. If using ubuntu or mac, run this command to activate virtual environment
````
./venv/bin/activate
````
10. Install requirements
````
pip install -r requirements.txt
````
11. Create Gemini API Key from [Google AI Studio](https://aistudio.google.com)
12. Create a .env file and add this:
````
GEMINI_API_KEY=your_api_key_here
````
13.  Run the following command, to run application
````
python app.py
````

![alt](./images/food_classifier.gif)
