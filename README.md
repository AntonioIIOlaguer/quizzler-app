# Quizzler – True/False Quiz Game

Quizzler is a lightweight, GUI‑based quiz game built with Python and Tkinter. It pulls trivia questions in real time from the public Open Trivia Database, presents them to the user one at a time, and keeps track of your score. It’s a fun project for learning about REST APIs, basic game logic and building simple desktop apps in Python.

## 🎯 Features
- Simple graphical interface using the built‑in tkinter module.
- Retrieves a set of true/false questions from OpenTDB on startup via HTTP.
- Displays each question on a canvas and updates the text as you progress.
- Shows a running score and increments it when you answer correctly.
- Two buttons with custom icons for True and False selections.
- Ends the quiz gracefully when no questions remain, showing your final score and disabling input.
- Modular design with separate files for data fetching, quiz logic, question model and UI.

## 🚀 Getting started
1.	Clone the repository
```bash
git clone https://github.com/AntonioIIOlaguer/quizzler-app.git
cd quizzler-app
```

2. Install dependencies
```bash
pip install requests
```

3. Run the application
``` bash
python main.py
```

A window titled “Quizzler” will open and begin asking you true/false questions pulled from the Open Trivia Database. Make sure you have an internet connection so the questions can be downloaded.

## ⚙️ Customising the quiz
- Number and type of questions: In data.py there is a parameters dictionary passed to the API. The default fetches 10 boolean questions. You can change the amount key to request a different number, and set the type to 'multiple' for multiple‑choice questions. OpenTDB also supports categories via a category parameter – see their API docs for options.
- Theme colours: The background and canvas colours are defined at the top of ui.py via THEME_COLOR and CANVAS_COLOR. Adjust these hex values to customise the look.
- Images: The images/ folder includes default true.png and false.png icons. Feel free to replace them with your own assets (keeping the filenames) to change the button graphics.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the project and submit a pull request if you have improvements, such as adding multiple‑choice support, persisting high scores, or enhancing the UI.
	1.	Fork this repository.
	2.	Create a feature branch: git checkout -b my-feature.
	3.	Commit your changes and push the branch.
	4.	Open a pull request on GitHub.

## 🪪 License

This project is released under the MIT License – see the LICENSE file for details.
