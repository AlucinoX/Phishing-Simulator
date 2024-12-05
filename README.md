Phishing Simulator in Python
This is a basic phishing simulator developed in Python using Flask. The project's purpose is to demonstrate how phishing attacks can be conducted through fake login pages. The code was created for educational purposes and serves as an example of how these attacks can be simulated in a controlled environment for learning.

Important Note: This project is intended for educational use only. It should not be used to carry out real attacks. Use it to understand phishing concepts and how to protect your information.

🚀 Features
Simulated Login Page: A page that mimics a legitimate login site.
Data Capture: When a user submits their credentials, the information (email and password) is captured and displayed in the console.
Simple Interface: The basic interface is built with HTML and rendered using Flask.
💡 How It Works
The user accesses the site locally and sees a page asking for their email and password.
After submitting credentials, the information is captured and displayed in the console.
A confirmation page is shown to the user, simulating that their data has been successfully collected.
🛠️ Requirements
Ensure you have Python installed. You will need to install the Flask library to run the simulator:

bash
Copiar código
pip install flask
🏁 How to Run the Project
Clone this repository or download the phishing_simulator.py file.

Open a terminal and navigate to the directory where the file is saved.

Run the Python script:

bash
Copiar código
python phishing_simulator.py
Open a browser and go to the address http://127.0.0.1:5000/.

Interact with the page and observe the credentials being captured in the console.

🌱 How to Contribute
Fork this repository.
Create a branch for your changes (git checkout -b my-branch).
Make your changes and commit them (git commit -am 'Add new features').
Push your changes to the repository (git push origin my-branch).
Create a pull request.
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📚 Learning Objectives
This project aims to demonstrate how phishing attacks work and how social engineering can be used to capture personal information. By studying it, you will learn about:

How to create simulated login pages.
How to capture data submitted via forms in a web environment.
The importance of being cautious when accessing websites and providing credentials.
Important: This project should only be used in a controlled learning environment and with due care. Misuse of this code may be illegal and harmful.
