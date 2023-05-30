**How to Use:**

- Clone this repo:

  ```bash
  git clone git@github.com:navneet-28/Truefoundry_MLE.git
  ```

- Install the requirements:

  ```bash
  pip install -r requirements.txt
  ```

- Run the FastAPI server using uvicorn:

  ```bash
  uvicorn main:app --host 0.0.0.0 --port 8000
  ```

- The app is now live at http://localhost:8000/
- Run the test cases:

  ```bash
  python test_all.py http://0.0.0.0:8000/predict
  ```
