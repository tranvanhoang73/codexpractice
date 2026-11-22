# Python Quiz

A five-question Python multiple-choice quiz. The browser displays the questions; Flask on the server checks the selected answers and returns a score out of five.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https%3A%2F%2Fgithub.com%2Ftranvanhoang73%2Fcodexpractice)

## Run locally

```powershell
python -m pip install -r requirements-web.txt
python app.py
```

Open <http://localhost:8000>. Stop the server with Ctrl+C in its terminal.

## Deploy for free on Render

The repository includes `render.yaml` and `requirements-web.txt` for a free Render web service. Push this project to a GitHub, GitLab, or Bitbucket repository, connect that repository to Render, then create a Web Service from the repo. Render can read the Blueprint configuration and use its build and start commands. The free service sleeps after 15 minutes without traffic, so its first request after that may take about a minute to load.

For deployment details, see [Render's Flask guide](https://render.com/docs/deploy-flask) and [free instance limits](https://render.com/docs/free).
