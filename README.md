# Criptovis

## 📜 **Description**

This project is an educational Django application demonstrating cryptocurrency price visualization and prediction using machine learning. It integrates yfinance for data retrieval, scikit-learn for linear regression modeling, and Docker for containerized deployment. The app serves as a practical example of combining web development with data science concepts.

---

## 🚀 *How to Run the Project*

1. Install dependencies:

   ```bash
   pip install -r Requirments.txt
   ```

2. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

3. Create a superuser for admin access:
   Follow the prompts to set up your admin user.
   ```bash
   python manage.py createsuperuser
   ```
   
4. Run the server:

   ```bash
   python manage.py runserver
   ```

5. Open the web page in your browser:
   ```bash
   http://localhost:8000/
   ```
---




## 🚀 *How to Run the Project in docker*

1. Build the image:

   ```bash
   docker build -t bunkfer/criptovis . 
   ```

2. Run the container:

   ```bash
   docker run -d -p8080:8080 --name criptovis bunkfer/criptovis
   ```

3. Execute the container bash:

   ```bash
   docker exec -it criptovis bash
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   Follow the prompts to set up your admin user.
   ```bash
   python manage.py createsuperuser
   ```

6. Open the web page in your browser:
   ```bash
   http://localhost:8080/
   ```

7. Stop the running container:
   ```bash
   docker kill criptovis
   ```   
---

## 🖼️ **Appendix**

We created a Docker image that is use as the base for this web page project.

Django = 5.2.1
django-crispy-forms = 2.4
scikit-learn = 1.6.1
scipy = 1.15.3
yfinance = 0.2.61

[Base Image](https://hub.docker.com/r/bunkfer/django)

---

## 📚 **References**

- [Django Documentation](https://docs.djangoproject.com/en/5.2/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Docker Documentation](https://docs.docker.com/guides/)
---