I have already learnt some htmx and am using it to good effect.

This is a mini-project to improve my knowledge of learning on how to use it.

I'm working to the chapters as set out in the excellent https://hypermedia.systems/ and plan to structured this code
into
branches that correspond well with the chapters there.

In the helpers.py file there is a create_random_contacts function to speed up getting contacts into the db at the start.
Run this in the flask shell.

Completed branches:

- web_1.0_application. This is the application in it pre-htmx state.
- extending_htmx.
    - Spent ages messing around with the htmx instillation (kept getting a 405 error) - the actual bug was not updating
      the server side methods in the app routes.
    - I found the app.py code for the inline validation for email values needed re-factoring because the contact email
      was overwritten with the value from the request's query string, without persisting the change to the database.
    - I found the search button functionality v hard. not very well explained in the book. things I did to make it work:
      used hx-get not hx-post otherwise 'q' was a None value. used of `hx-select="tbody > tr"` on button to ensure the
      tbody was being replaced properly. (You learn hx-select in the infinite scroll.)
- more htmx patterns (coming next!)

I have been / am enjoying learning a few other things along the
way, including:

- Flask (this is the first time I've used it)
- The css at https://missing.style/
- What raw html can do for you anyway!
- The flash functionality to flash a new message to the next request. 