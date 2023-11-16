# List of instructions

## Start virtual enviroment:

1. Create virtual enviroment:

   ```bash
   python -m venv venv
   ```

2. Activate virtual enviroment:

   ```bash
   source venv/bin/activate
   ```

3. Close it after finish:

   ```bash
   deactivate
   ```

## Create Django Project:

1. Start

   ```bash
   django-admin startproject tecnosolutb
   ```

2. Change to the project directory:

   ```bash
   cd tecnosolutb
   ```

3. Run the server:

   ```bash
   python manage.py runserver
   ```

   Ignore the warning about unapplied database migrations for now

4. Can change the port:

   ```bash
   python manage.py runserver 8080
   ```

5. Or change the ip:

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

6. Create another project in the same directory of manage.py:

   ```bash
   python manage.py startapp polls
   ```

   This directory host a new app called polls.

The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name. At this point, it’s worth reviewing what these arguments are for.

7. Database:

   After set the Database or use SQLite, migrations should be done:

   ```bash
   python manage.py migrate
   ```

   Then we should set the new app models, and:

   ```bash
   python manage.py makemigrations polls
   ```

   Te next command shows you the changes to be done in the DB:

   ```bash
   python manage.py sqlmigrate polls 0001
   ```

   Now do the changes:

   ```bash
   python manage.py migrate
   ```

   Remember the three-step guide to making model changes:

- Change your models (in models.py).
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database.

8. Python project shell:

   ```bash
   python manage.py shell
   ```

   Then explore the database API:

   ```python
   >>> from polls.models import Choice, Question  # Import the model classes we just wrote.

   # No questions are in the system yet.
   >>> Question.objects.all()
   <QuerySet []>

   # Create a new Question.
   # Support for time zones is enabled in the default settings file, so
   # Django expects a datetime with tzinfo for pub_date. Use timezone.now()
   # instead of datetime.datetime.now() and it will do the right thing.
   >>> from django.utils import timezone
   >>> q = Question(question_text="What's new?", pub_date=timezone.now())

   # Save the object into the database. You have to call save() explicitly.
   >>> q.save()

   # Now it has an ID.
   >>> q.id
   1

   # Access model field values via Python attributes.
   >>> q.question_text
   "What's new?"
   >>> q.pub_date
   datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)

   # Change values by changing the attributes, then calling save().
   >>> q.question_text = "What's up?"
   >>> q.save()

   # objects.all() displays all the questions in the database.
   >>> Question.objects.all()
   <QuerySet [<Question: Question object (1)>]>
   ```

   After formatting with `__str__()`:

   ```python
   >>> from polls.models import Choice, Question

   # Make sure our __str__() addition worked.
   >>> Question.objects.all()
   <QuerySet [<Question: What's up?>]>

   # Django provides a rich database lookup API that's entirely driven by
   # keyword arguments.
   >>> Question.objects.filter(id=1)
   <QuerySet [<Question: What's up?>]>
   >>> Question.objects.filter(question_text__startswith="What")
   <QuerySet [<Question: What's up?>]>

   # Get the question that was published this year.
   >>> from django.utils import timezone
   >>> current_year = timezone.now().year
   >>> Question.objects.get(pub_date__year=current_year)
   <Question: What's up?>

   # Request an ID that doesn't exist, this will raise an exception.
   >>> Question.objects.get(id=2)
   Traceback (most recent call last):
       ...
   DoesNotExist: Question matching query does not exist.

   # Lookup by a primary key is the most common case, so Django provides a
   # shortcut for primary-key exact lookups.
   # The following is identical to Question.objects.get(id=1).
   >>> Question.objects.get(pk=1)
   <Question: What's up?>

   # Make sure our custom method worked.
   >>> q = Question.objects.get(pk=1)
   >>> q.was_published_recently()
   True

   # Give the Question a couple of Choices. The create call constructs a new
   # Choice object, does the INSERT statement, adds the choice to the set
   # of available choices and returns the new Choice object. Django creates
   # a set to hold the "other side" of a ForeignKey relation
   # (e.g. a question's choice) which can be accessed via the API.
   >>> q = Question.objects.get(pk=1)

   # Display any choices from the related object set -- none so far.
   >>> q.choice_set.all()
   <QuerySet []>

   # Create three choices.
   >>> q.choice_set.create(choice_text="Not much", votes=0)
   <Choice: Not much>
   >>> q.choice_set.create(choice_text="The sky", votes=0)
   <Choice: The sky>
   >>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

   # Choice objects have API access to their related Question objects.
   >>> c.question
   <Question: What's up?>

   # And vice versa: Question objects get access to Choice objects.
   >>> q.choice_set.all()
   <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
   >>> q.choice_set.count()
   3

   # The API automatically follows relationships as far as you need.
   # Use double underscores to separate relationships.
   # This works as many levels deep as you want; there's no limit.
   # Find all Choices for any question whose pub_date is in this year
   # (reusing the 'current_year' variable we created above).
   >>> Choice.objects.filter(question__pub_date__year=current_year)
   <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

   # Let's delete one of the choices. Use delete() for that.
   >>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
   >>> c.delete()
   ```

9. Django admin

- Creating an admin user:

  ```bash
  python manage.py createsuperuser
  ```

  user: admin
  pass: 1234

- Start the server:

  ```bash
  python manage.py runserver
  ```

  The django admin runs at: http://127.0.0.1:8000/admin/

- Make the poll app modifiable in the admin:

  ```python
  from django.contrib import admin

  from .models import Question

  admin.site.register(Question)
  ```

  Within the templates directory you have just created, create another directory called polls, and within that create a file called index.html. In other words, your template should be at polls/templates/polls/index.html. Because of how the app_directories template loader works as described above, you can refer to this template within Django as polls/index.html.

### Style

First, make a file `.../polls/static/polls/style.css`
