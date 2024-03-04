I had already learnt some htmx and had been using it to good effect, but this is a mini-project to improve my
understanding and use of the it.

I'm working to the chapters as set out in the excellent https://hypermedia.systems/ and plan to structured this code
into branches that correspond with the chapters there. At times I've not found it so straight forward to work in
this way so my branches may not correspond entirely with the chapters.

In the helpers.py file there is a create_random_contacts function to speed up getting contacts into the db at the start,
which can be run directly from the terminal via `python helpers.py`

Completed branches:
- web_1.0_application. This is the application in it pre-htmx state. (Chapters 1-3)
- extending_htmx. (Chapters 4-5)
    - Spent ages messing around with the htmx instillation (kept getting a 405 error). The actual bug was not updating
      the server side methods in the app routes.
    - created a new html template called contact_values to make code more DRY.
    - In line validation. I found the app.py code for the inline validation for email values needed re-factoring because
      the contact email was overwritten with the value from the request's query string, without persisting the change to
      the database.
    - Infinite scroll. 
    - I found the search button functionality v hard. There's an incomplete explanation of how to implement it at the
      beginning of chapter 4. I got it working in this branch by using hx-get not hx-post (otherwise 'q' was a None
      value) and the used of `hx-select="tbody > tr"` on button to ensure the tbody was being replaced properly. (You
      learn hx-select in the infinite scroll.) However, as you'll see the search functionality if covered in detail in
      the next chapter.
- more htmx patterns. (Chapter 6)
    - Implementing active search via HTTP request headers. The book explains this in the best approach.
    - Lazy loading. 
    - Inline deleting with css transition. 
    - Bulk deleting. 
- archive ui. (Chapter 7)
    - Data download progress bar with one bit of hyperscript at the end. 
- tricks of masters (Chapters 8 - ) wip
  - options button with vanilla JS and Reasonable System for JavaScript Structure (RSJS). 
  - upto Alpine.js section. 

Other things I am enjoying learning along the way:
- Flask (this is the first time I've used it)
- The css at https://missing.style/
- What raw html can do for you anyway! Going beyond this - learning a deeper appreciation of how html works and it's
  tags. This goes hand in hand with how htmx works.
- The flask flash functionality to flash a new message to the next request. 
- event handlers, especially for hxtm events. 
- reasonable system for javascript structure (RSJS)
- `dunking on JavaScript is not the aim of the htmx project. The goal of htmx is not less JavaScript, but less code, more readable and hypermedia-friendly code.`
- `simply listing “best practices” is rarely convincing or edifying. To be honest, it’s boring.`
- `No code is faster than no code.` Merb. 